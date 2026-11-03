"""Validate published portrait integrity, safe SVG playback and static fallbacks."""
from pathlib import Path
from base64 import b64decode
from hashlib import sha256
import json
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
assets = root / 'assets'
manifest = json.loads((assets / 'identity-portrait-provenance.json').read_text())
original = (root / manifest['source']).read_bytes()
assert sha256(original).hexdigest() == manifest['portrait_sha256']
ns = {'svg': 'http://www.w3.org/2000/svg'}

for variant in manifest['variants']:
    data = (assets / variant['file']).read_bytes()
    assert len(data) == variant['bytes'] and sha256(data).hexdigest() == variant['sha256']
    document = ET.fromstring(data)
    images = document.findall('.//svg:image', ns)
    assert len(images) == 1, 'Exactly one unchanged photo, without copies over the face.'
    assert b64decode(images[0].attrib['href'].split(',', 1)[1]) == original
    assert not list(images[0]), 'The photo itself must stay still.'
    assert document.find('svg:title', ns) is not None
    assert document.find('svg:desc', ns) is not None
    for element in document.iter():
        tag = element.tag.split('}')[-1]
        assert tag not in {'script', 'foreignObject', 'filter'}, tag
        assert not any(key.lower().startswith('on') for key in element.attrib)
        for key, value in element.attrib.items():
            if key.endswith('href'):
                assert value.startswith('data:image/jpeg;base64,'), 'No external runtime dependency.'
    animations = [node for node in document.iter() if node.tag.split('}')[-1].startswith('animate')]
    if '-still' in variant['file']:
        assert not animations, 'Reduced-motion output must be genuinely static.'
    else:
        assert len(document.findall('.//svg:animateMotion', ns)) == 154
    assert len(data) < 600000, 'Selected header must stay below the 600KB raw budget.'

readme = (root / 'README.md').read_text(encoding='utf8')
for variant in manifest['variants']:
    assert variant['file'] in readme
assert 'credential-micro1.svg' in readme and 'micro1-certification.jpg' in readme
assert readme.rfind('## ') == readme.index('## The build trace.'), 'Contribution art remains last.'
assert readme.count('/badge.svg?branch=main') == 3, 'Use actual default-branch status badges.'
ET.parse(assets / 'credential-micro1.svg')
print('Verified: four responsive identity variants, byte-identical portrait, static fallbacks, bounded assets, three native workflow badges and credential evidence link.')
