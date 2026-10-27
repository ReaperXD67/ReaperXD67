"""Reject malformed SVGs, executable embeds, or inconsistent calendar exports."""
import json
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

for name in ['contribution-snake.svg','contribution-calendar.svg','contribution-skyline.svg','contribution-skyline-still.svg']:
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
    if name.endswith('-still.svg') or name == 'contribution-calendar.svg':
        assert '<animate' not in text and '@keyframes' not in text, f'Still contains motion: {name}'
    elif name == 'contribution-snake.svg':
        assert '@keyframes' in text and 'Platane/snk' in text
    else:
        assert '<animateTransform' in text and 'repeatCount="indefinite"' in text
print(f'PASS: actual-data total {data["total"]}; {len(cells)} unique days; four valid, self-contained SVGs; static fallbacks contain no motion.')
