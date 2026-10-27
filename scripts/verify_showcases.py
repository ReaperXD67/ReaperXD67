"""Bounded asset safety and real-capture verification for authored SVG films."""
from pathlib import Path
from base64 import b64decode
from hashlib import sha256
from io import BytesIO
import json, xml.etree.ElementTree as ET
from PIL import Image

root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'assets/showcase-provenance.json').read_text())
allowed={entry['embedded_sha256'] for entry in manifest['captures']}
files=sorted((root/'assets').glob('showcase-*.svg'))
assert len(files)==20, f'Expected twenty desktop/mobile/motion/static SVGs, found {len(files)}'
for file in files:
    tree=ET.fromstring(file.read_text(encoding='utf8'))
    assert tree.find('{http://www.w3.org/2000/svg}title') is not None
    assert tree.find('{http://www.w3.org/2000/svg}desc') is not None
    animations=0; images=0
    for element in tree.iter():
        tag=element.tag.rsplit('}',1)[-1]
        assert tag not in {'script','foreignObject','iframe','style'}, f'Executable/runtime content in {file.name}'
        animations+=tag in {'animate','animateMotion','animateTransform'}
        for key,value in element.attrib.items():
            assert not key.lower().startswith('on'), f'Event attribute in {file.name}'
            if key.rsplit('}',1)[-1] in {'href','src'}:
                assert tag=='image' and value.startswith('data:image/jpeg;base64,'), f'External reference in {file.name}'
                data=b64decode(value.split(',',1)[1],validate=True)
                assert sha256(data).hexdigest() in allowed, f'Unproven image in {file.name}'
                Image.open(BytesIO(data)).verify(); images+=1
    if '-still' in file.stem:
        assert animations==0, f'Static variant contains motion: {file.name}'
        assert not any(e.attrib.get('data-motion') for e in tree.iter()), f'Static variant retains a moving packet or sweep: {file.name}'
    elif 'capabilities' not in file.stem: assert animations>0, f'Expected motion: {file.name}'
    if 'atlaslm' in file.stem or 'karixmc' in file.stem: assert images==1, f'Real capture missing: {file.name}'
for entry in manifest['captures']:
    source=root/entry['committed_input']
    assert source.exists(), f'Committed capture input missing: {source}'
    assert sha256(source.read_bytes()).hexdigest()==entry['source_sha256']
print('PASS:20 valid self-contained SVGs; static variants have zero animation;8 embedded captures match recorded JPEG digests; original source digests verified when available.')
