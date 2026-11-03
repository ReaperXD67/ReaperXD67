"""Author the portrait-led GitHub identity, with no playback dependencies.

The approved JPEG is embedded byte-for-byte. Only original vector particles and
type animate; the face remains fixed. Regenerate with npm run identity.
"""
from base64 import b64encode
from hashlib import sha256
from html import escape
from math import sin, pi
from pathlib import Path
from random import Random
import json, sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'output/python-deps'))
from PIL import Image
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen

ASSETS = ROOT / 'assets'
FONT = instantiateVariableFont(TTFont(ASSETS / 'fonts/SpaceGrotesk.ttf'), {'wght': 600}, inplace=False)
GLYPHS = FONT.getGlyphSet()
CMAP = FONT.getBestCmap()
EM = FONT['head'].unitsPerEm
PHOTO = ASSETS / 'aman-kumar-avatar.jpg'
PHOTO_BYTES = PHOTO.read_bytes()
PHOTO_URI = 'data:image/jpeg;base64,' + b64encode(PHOTO_BYTES).decode()
PHOTO_IMAGE = Image.open(PHOTO).convert('RGB')
FG, MUTED, ACID = '#f3f3eb', '#b7bdb6', '#d8ff4f'


def text(x, y, value, size=24, color=FG, align='start', opacity=1):
    scale = size / EM
    run, advance = [], 0
    for char in value:
        glyph = GLYPHS[CMAP.get(ord(char), CMAP[ord('?')])]
        pen = SVGPathPen(GLYPHS)
        glyph.draw(pen)
        run.append((advance, pen.getCommands()))
        advance += glyph.width
    shift = advance * scale * (.5 if align == 'middle' else 1 if align == 'end' else 0)
    return f'<g fill="{color}" opacity="{opacity}" aria-label="{escape(value, quote=True)}" transform="translate({x-shift:.2f} {y}) scale({scale:.5f} {-scale:.5f})">' + ''.join(f'<path transform="translate({a} 0)" d="{d}"/>' for a, d in run if d) + '</g>'


def colour(v):
    rgb = PHOTO_IMAGE.getpixel((round(PHOTO_IMAGE.width * .97), round(PHOTO_IMAGE.height * v)))
    gain = max(1, 205 / max(max(rgb), 1))
    return '#' + ''.join(f'{min(255, round(c * gain)):02x}' for c in rgb)


def ribbon(mobile, still):
    rng = Random(67)
    body = ''
    for i in range(22):
        t = i / 21
        v = .52 + t * .36
        if mobile:
            path = f'M580 {250+520*v:.2f} C{619+t*8:.2f} {700+t*20:.2f} 610 {803+t*16:.2f} {465+t*10:.2f} {807+t*9:.2f} S{210+t*30:.2f} {795-t*10:.2f} {78+t*10:.2f} {826-t*2:.2f}'
        else:
            path = f'M1210 {80+500*v:.2f} C{1258+t*7:.2f} {500+t*30:.2f} 1270 {643+t*15:.2f} {1050-t*30:.2f} {638+t*12:.2f} S{620+t*20:.2f} {614-t*8:.2f} {465+t*8:.2f} {642-t*18:.2f}'
        tint = colour(v)
        body += f'<path d="{path}" fill="none" stroke="{tint}" stroke-width="{.6+t*.8:.2f}" opacity="{.14+t*.12:.2f}"/>'
        if still:
            continue
        for j in range(7):
            duration = 6.6 + rng.random() * 3
            begin = -rng.random() * duration
            radius = 1 + rng.random() * 1.55
            body += f'<circle r="{radius:.2f}" fill="{tint}" opacity="0"><animateMotion path="{path}" dur="{duration:.2f}s" begin="{begin:.2f}s" repeatCount="indefinite" calcMode="paced"/><animate attributeName="opacity" values="0;.95;.95;0" keyTimes="0;.07;.87;1" dur="{duration:.2f}s" begin="{begin:.2f}s" repeatCount="indefinite"/></circle>'
    return body


def header(mobile=False, still=False):
    w, h = (640, 1030) if mobile else (1280, 720)
    s = '<rect width="100%" height="100%" fill="#080a09"/>'
    s += text(34, 40, 'A.K. / REAPERXD67', 16, ACID)
    if mobile:
        s += text(606, 40, 'BENGALURU, INDIA', 14, MUTED, 'end')
        s += text(28, 132, 'AMAN', 105)
        s += text(28, 227, 'KUMAR', 105)
        s += f'<image x="60" y="250" width="520" height="520" href="{PHOTO_URI}"/>'
        s += ribbon(True, still)
        s += text(34, 885, 'AI ENGINEER &', 34)
        s += text(34, 931, 'FULL-STACK DEVELOPER', 34)
        s += '<path d="M34 958H606" stroke="#374136"/>'
        s += text(34, 991, 'BUILDING AT SIP', 17, ACID)
        s += text(606, 991, 'PREVIOUSLY micro1', 17, MUTED, 'end')
    else:
        s += text(1246, 40, 'BENGALURU, INDIA / OPEN TO OPPORTUNITIES', 16, MUTED, 'end')
        s += text(34, 190, 'AMAN', 145)
        s += text(34, 327, 'KUMAR', 145)
        s += text(40, 399, 'AI ENGINEER &', 36)
        s += text(40, 447, 'FULL-STACK DEVELOPER', 36)
        s += text(40, 526, 'Systems that explain themselves.', 26, MUTED)
        s += text(40, 570, 'Agents. Retrieval. Reliable interfaces.', 23, MUTED)
        s += f'<image x="710" y="80" width="500" height="500" href="{PHOTO_URI}"/>'
        s += ribbon(False, still)
        s += '<path d="M40 677H1240" stroke="#374136"/>'
        s += text(40, 706, 'BUILDING AT SIP', 16, ACID)
        s += text(1240, 706, 'PREVIOUSLY AI ENGINEER INTERN / micro1', 16, MUTED, 'end')
    title = 'Aman Kumar — AI Engineer and Full-Stack Developer'
    description = 'The approved, unchanged yellow-kurta portrait leads an original editorial identity. A bright current sampled from the photograph travels from its right edge. Bengaluru; building at SIP; previous AI Engineer Intern at micro1. The particle animation is decorative, not telemetry.'
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{title}</title><desc id="desc">{description}</desc>{s}</svg>'


def credential():
    body = '<rect width="392" height="32" rx="4" fill="#171d16" stroke="#52623b"/>'
    body += '<path d="M13 16l4 4 8-9" fill="none" stroke="#d8ff4f" stroke-width="2"/>'
    body += text(35, 22, 'micro1 · AI / ML credential · view certificate', 14, FG)
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="392" height="32" viewBox="0 0 392 32" role="img"><title>micro1 supplied AI / Machine Learning credential; open certificate</title>{body}</svg>'


if __name__ == '__main__':
    outputs = []
    for mobile in (False, True):
        for still in (False, True):
            name = 'identity-portrait' + ('-mobile' if mobile else '') + ('-still' if still else '') + '.svg'
            data = header(mobile, still).encode()
            (ASSETS / name).write_bytes(data)
            outputs.append({'file': name, 'bytes': len(data), 'sha256': sha256(data).hexdigest()})
    (ASSETS / 'credential-micro1.svg').write_text(credential(), encoding='utf8')
    manifest = {'source': 'assets/aman-kumar-avatar.jpg', 'portrait_sha256': sha256(PHOTO_BYTES).hexdigest(), 'portrait_encoding': 'Original JPEG bytes embedded unchanged', 'font': 'Space Grotesk, SIL OFL; assets/fonts/SPACE-GROTESK-LICENSE.txt', 'animation': 'Original self-contained SVG SMIL; 154 decorative grains; no runtime or external resource', 'variants': outputs}
    (ASSETS / 'identity-portrait-provenance.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf8')
    print(json.dumps(outputs, indent=2))
