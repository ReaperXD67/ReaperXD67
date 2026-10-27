"""Reject malformed SVGs, executable embeds, or inconsistent calendar exports."""
import json
import hashlib
import math
from datetime import date
from pathlib import Path
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
assets = root / 'assets'
data = json.loads((assets / 'contribution-data.json').read_text())
cells = data['cells']
assert 365 <= len(cells) <= 371, 'Expected a rolling year including week alignment'
assert sum(day['count'] for day in cells) == data['total'], 'Calendar total diverged'
dates = [date.fromisoformat(day['date']) for day in cells]
assert len(set(dates)) == len(dates), 'Duplicate calendar days'
assert all((b-a).days == 1 for a,b in zip(dates,dates[1:])), 'Nonconsecutive calendar'
assert all(isinstance(day['count'],int) and day['count'] >= 0 for day in cells)

names = ['contribution-snake.svg','contribution-calendar.svg','contribution-skyline.svg','contribution-skyline-still.svg',
         'contribution-loom.svg','contribution-loom-still.svg','contribution-loom-mobile.svg','contribution-loom-mobile-still.svg']
expected_cells = {(day['date'], str(day['count']), str(day['y']), str(day['x'])) for day in cells}
digest = hashlib.sha256(json.dumps(cells, separators=(',', ':'), ensure_ascii=False).encode()).hexdigest()
for name in names:
    text = (assets / name).read_text()
    tree = ET.fromstring(text)
    assert tree.tag.endswith('svg'), f'Not an SVG: {name}'
    for element in tree.iter():
        tag = element.tag.rsplit('}',1)[-1]
        assert tag not in ['script','foreignObject','iframe'], f'Executable element: {name}'
        assert not any(attr.lower().startswith('on') for attr in element.attrib), f'Event handler: {name}'
        for attr,value in element.attrib.items():
            if attr.endswith('href') or attr == 'src':
                assert not value.startswith(('http:','https:','//')), f'Remote runtime asset: {name}'
    if name.startswith('contribution-loom'):
        facets = [element for element in tree.iter() if element.attrib.get('data-cell') == 'true']
        actual_cells = {(el.attrib['data-date'], el.attrib['data-count'], el.attrib['data-lane'], el.attrib['data-week']) for el in facets}
        assert len(facets) == len(cells) and actual_cells == expected_cells, f'Loom invented, omitted or changed a day: {name}'
        maximum = max(1, max(day['count'] for day in cells))
        assert all(abs(float(el.attrib['data-height']) - (0.045 + 0.92 * math.log1p(int(el.attrib['data-count'])) / math.log1p(maximum))) <= 0.0051 for el in facets), f'Loom height no longer encodes actual count: {name}'
        meta = json.loads(next(el.text for el in tree.iter() if el.tag.endswith('metadata')))
        assert meta['sha256'] == digest and meta['total'] == data['total'], f'Loom snapshot diverged: {name}'
        assert meta['first'] == data['first'] and meta['last'] == data['last'], f'Loom dates diverged: {name}'
        assert meta['generated'] == data['generated'], f'Loom snapshot date stale: {name}'
        if not name.endswith('-still.svg'):
            moving = [el for el in tree.iter() if el.tag.endswith('animateMotion')]
            assert len(moving) == 7, f'Expected seven decorative weekday sweeps: {name}'
            assert all(not any(child.tag.rsplit('}',1)[-1].startswith('animate') for child in facet.iter()) for facet in facets), f'Actual cell data animates: {name}'
    if name.endswith('-still.svg') or name == 'contribution-calendar.svg':
        assert '<animate' not in text and '@keyframes' not in text, f'Still contains motion: {name}'
    elif name == 'contribution-snake.svg':
        assert '@keyframes' in text and 'Platane/snk' in text
    elif name.startswith('contribution-skyline'):
        assert '<animateTransform' in text and 'repeatCount="indefinite"' in text
print(f'PASS: actual-data total {data["total"]}; {len(cells)} unique days; eight self-contained SVGs; all four loom variants preserve every date/count; static fallbacks contain no motion.')
