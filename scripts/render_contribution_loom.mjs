/** Original Contribution Loom. Node stdlib only; no network or executable SVG.
 * Seven weekday strands carry the actual daily calendar through a projected helix.
 * Geometry/color are fixed by counts. Only an explicitly decorative light travels.
 */
import { createHash } from 'node:crypto';
import { readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const TAU = Math.PI * 2;
const weekdays = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'];
const f = n => Number(n.toFixed(2));
const esc = value => String(value).replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;');
const rgb = hex => [1, 3, 5].map(i => parseInt(hex.slice(i, i + 2), 16));
const mix = (a, b, t) => `#${rgb(a).map((c, i) => Math.round(c + (rgb(b)[i] - c) * t).toString(16).padStart(2, '0')).join('')}`;

function validate(data) {
  if (!Array.isArray(data.cells) || data.cells.length < 365 || data.cells.length > 371) throw new Error('Expected the actual rolling calendar.');
  let total = 0, previous = -Infinity;
  const days = new Set();
  for (const cell of data.cells) {
    const stamp = Date.parse(`${cell.date}T00:00:00Z`);
    if (!Number.isFinite(stamp) || !Number.isInteger(cell.count) || cell.count < 0 || !Number.isInteger(cell.x) || !Number.isInteger(cell.y) || cell.y < 0 || cell.y > 6 || days.has(cell.date)) throw new Error('Invalid real-calendar cell.');
    if (previous !== -Infinity && stamp - previous !== 86400000) throw new Error('Calendar dates must be consecutive.');
    if (new Date(stamp).getUTCDay() !== cell.y) throw new Error('Weekday lane does not match date.');
    days.add(cell.date); previous = stamp; total += cell.count;
  }
  if (total !== data.total || data.first !== data.cells[0].date || data.last !== data.cells.at(-1).date) throw new Error('Calendar summary mismatch.');
}

function render(data, mobile, animated) {
  const width = mobile ? 700 : 1200, height = mobile ? 1080 : 650;
  const maxWeek = Math.max(...data.cells.map(cell => cell.x));
  const maxCount = Math.max(1, ...data.cells.map(cell => cell.count));
  const digest = createHash('sha256').update(JSON.stringify(data.cells)).digest('hex');
  const center = mobile ? [350, 603] : [664, 343];
  const unit = mobile ? 42 : 55;
  // Fixed camera: a real depth projection with a separate portrait composition.
  const project = p => {
    const [x, y, z] = p;
    const a = x * Math.cos(0.3) + z * Math.sin(0.3);
    const b = -x * Math.sin(0.3) + z * Math.cos(0.3);
    const up = y * Math.cos(0.38) - b * Math.sin(0.38);
    const depth = y * Math.sin(0.38) + b * Math.cos(0.38);
    const perspective = 25 / (25 - depth);
    return mobile
      ? [center[0] + up * unit * perspective * 1.8, center[1] + a * unit * perspective, depth]
      : [center[0] + a * unit * perspective, center[1] - up * unit * perspective - a * 2.3, depth];
  };
  const point = (week, lane) => {
    const t = week / Math.max(1, maxWeek);
    const phase = t * TAU * 1.34 + lane / 7 * TAU;
    return [(t - 0.5) * 15.6, Math.sin(phase) * 1.48, Math.cos(phase) * 1.7];
  };
  const poly = points => points.map(p => `${f(p[0])},${f(p[1])}`).join(' ');
  const visible = [];

  // Each small segment is depth-sorted with the real daily facets to preserve braiding.
  for (let lane = 0; lane < 7; lane++) {
    const dates = data.cells.filter(cell => cell.y === lane);
    const first = dates[0].x, last = dates.at(-1).x;
    for (let sample = first * 4; sample < last * 4; sample++) {
      const p = project(point(sample / 4, lane)), q = project(point((sample + 1) / 4, lane));
      const light = Math.max(0.15, Math.min(0.8, (p[2] + 5) / 10));
      visible.push({ depth: (p[2] + q[2]) / 2 - 0.05,
        svg: `<path d="M${f(p[0])} ${f(p[1])}L${f(q[0])} ${f(q[1])}" fill="none" stroke="${mix('#273a3b', '#81978b', light)}" stroke-width="${mobile ? 2.2 : 1.5}" stroke-linecap="round"/>` });
    }
  }

  for (const cell of data.cells) {
    const p = point(cell.x, cell.y);
    const strength = Math.log1p(cell.count) / Math.log1p(maxCount);
    const rise = 0.045 + strength * 0.92;
    const halfX = 0.093, halfZ = 0.105;
    const corners = (y) => [
      project([p[0] - halfX, y, p[2] - halfZ]), project([p[0] + halfX, y, p[2] - halfZ]),
      project([p[0] + halfX, y, p[2] + halfZ]), project([p[0] - halfX, y, p[2] + halfZ]),
    ];
    const bottom = corners(p[1]), top = corners(p[1] + rise);
    const color = cell.count ? mix('#40713f', '#d8ff4f', 0.18 + strength * 0.82) : '#233435';
    const faces = [
      `<polygon points="${poly([bottom[0], bottom[1], top[1], top[0]])}" fill="${mix('#080e0d', color, 0.48)}"/>`,
      `<polygon points="${poly([bottom[1], bottom[2], top[2], top[1]])}" fill="${mix('#0b1511', color, 0.7)}"/>`,
      `<polygon points="${poly([bottom[2], bottom[3], top[3], top[2]])}" fill="${mix('#07120e', color, 0.55)}"/>`,
      `<polygon points="${poly([bottom[3], bottom[0], top[0], top[3]])}" fill="${mix('#09130f', color, 0.4)}"/>`,
      `<polygon points="${poly(top)}" fill="${color}" stroke="${cell.count ? '#d1ef8a' : '#49605b'}" stroke-opacity="${cell.count ? 0.55 : 0.3}" stroke-width="${mobile ? 0.75 : 0.5}"/>`,
    ];
    // SVG image viewers do not expose every title, so equivalent semantics remain in Markdown.
    const svg = `<g data-cell="true" data-date="${cell.date}" data-count="${cell.count}" data-lane="${cell.y}" data-week="${cell.x}" data-height="${f(rise)}"><title>${cell.date} · ${weekdays[cell.y]} · ${cell.count} contributions</title>${faces.join('')}</g>`;
    visible.push({ depth: project(p)[2] + rise * 0.2, svg });
  }
  visible.sort((a, b) => a.depth - b.depth);
  const energy = [];
  if (animated) for (let lane = 0; lane < 7; lane++) {
    const dates = data.cells.filter(cell => cell.y === lane);
    const start = dates[0].x, end = dates.at(-1).x, origin = project(point(start, lane));
    const samples = [];
    for (let t = start * 4; t <= end * 4; t++) samples.push(project(point(t / 4, lane)));
    const route = samples.map((p, i) => `${i ? 'L' : 'M'}${f(p[0] - origin[0])} ${f(p[1] - origin[1])}`).join('');
    energy.push(`<circle cx="${f(origin[0])}" cy="${f(origin[1])}" r="${mobile ? 3.7 : 2.5}" fill="#e3ffc5" opacity=".78"><animateMotion path="${route}" dur="14s" begin="-${lane * 1.8}s" repeatCount="indefinite" calcMode="paced"/></circle>`);
  }
  const text = (x, y, size, fill, value, extra = '') => `<text x="${x}" y="${y}" font-family="Arial,Helvetica,sans-serif" font-size="${size}" fill="${fill}" ${extra}>${esc(value)}</text>`;
  const mono = (x, y, size, fill, value, extra = '') => `<text x="${x}" y="${y}" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="${size}" fill="${fill}" ${extra}>${esc(value)}</text>`;
  const header = mobile ? [
    text(38, 70, 46, '#f1f4e9', 'Contribution Loom', 'letter-spacing="-1.4"'),
    text(38, 115, 24, '#a4b6aa', 'Seven weekday strands. One real calendar.'),
    text(38, 190, 60, '#d8ff4f', String(data.total), 'font-weight="600"'),
    mono(190, 183, 23, '#b8c7bb', 'contributions'),
    `<path d="M38 220H662" stroke="#34453d"/>`,
  ].join('') : [
    text(42, 66, 42, '#f1f4e9', 'Contribution Loom', 'letter-spacing="-1.1"'),
    text(43, 100, 17, '#a4b6aa', 'Seven weekday strands. One real calendar.'),
    text(1156, 65, 48, '#d8ff4f', String(data.total), 'font-weight="600" text-anchor="end"'),
    mono(1155, 95, 13, '#b8c7bb', 'ACTUAL CONTRIBUTIONS', 'text-anchor="end"'),
    `<path d="M42 123H1158" stroke="#34453d"/>`,
  ].join('');
  let previousLabel = 175;
  const laneLabels = weekdays.map((day, lane) => ({ day, p: project(point(data.cells.find(cell => cell.y === lane).x, lane)) }))
    .sort((a, b) => a.p[1] - b.p[1]).map(({ day, p }) => {
      const y = Math.max(previousLabel + 23, Math.min(505, p[1] + 4)); previousLabel = y;
      return mono(76, f(y), 12, '#a7bcae', day, 'text-anchor="end"') + `<path d="M86 ${f(y - 4)}H118L${f(p[0] - 8)} ${f(p[1])}" fill="none" stroke="#40554a" stroke-width=".7"/>`;
    });
  const legend = mobile ? [
    `<path d="M38 927H662" stroke="#34453d"/>`,
    text(38, 965, 22, '#d2dccd', 'Each facet = one day · height / light = log(1 + count)'),
    mono(38, 1002, 21, '#93a995', `${data.first} → ${data.last}`),
    text(38, 1040, 20, '#93a995', `Snapshot ${data.generated} · light sweep is decorative`),
  ].join('') : [
    ...laneLabels,
    `<path d="M42 536H1158" stroke="#34453d"/>`,
    text(43, 570, 15, '#d2dccd', 'One facet per actual day. Height and light use log(1 + count).'),
    mono(43, 605, 13, '#93a995', `${data.first} → ${data.last}  /  snapshot ${data.generated}`),
    mono(1156, 570, 12, '#93a995', 'LIGHT SWEEP = DECORATIVE', 'text-anchor="end"'),
    mono(1156, 605, 12, '#93a995', `${maxWeek + 1} WEEKS / ${data.cells.length} REAL DAYS`, 'text-anchor="end"'),
  ].join('');
  const metadata = { generator: 'original-contribution-loom@1', source: 'assets/contribution-data.json', sha256: digest,
    total: data.total, first: data.first, last: data.last, generated: data.generated, days: data.cells.length,
    scale: 'height = 0.045 + 0.92 * log1p(count) / log1p(maxCount); intensity uses the same normalized count',
    motion: animated ? 'decorative lane sweep only; all contribution cells remain fixed' : 'none' };
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}" viewBox="0 0 ${width} ${height}" role="img" aria-labelledby="title desc"><title id="title">Contribution Loom · ${data.total} actual GitHub contributions</title><desc id="desc">${data.cells.length} real consecutive dates, ${data.first} to ${data.last}, woven into seven weekday strands. Each faceted cell represents one actual day. Logarithmic height and light encode its count. ${animated ? 'Only decorative energy travels; cells and counts never change.' : 'Complete still composition without motion.'} Activity is not a skill score.</desc><metadata>${esc(JSON.stringify(metadata))}</metadata><defs><radialGradient id="stage"><stop stop-color="#15251c"/><stop offset="1" stop-color="#080c0b"/></radialGradient></defs><rect width="${width}" height="${height}" fill="#080c0b"/><ellipse cx="${center[0]}" cy="${center[1]}" rx="${mobile ? 310 : 520}" ry="${mobile ? 365 : 210}" fill="url(#stage)"/><rect x=".5" y=".5" width="${width - 1}" height="${height - 1}" fill="none" stroke="#34453d"/>${header}<g data-field="contribution-loom">${visible.map(item => item.svg).join('')}</g>${energy.join('')}${legend}</svg>\n`;
}

export async function renderContributionLoom(data, assets = path.join(root, 'assets')) {
  validate(data);
  const variants = [[false, true, ''], [false, false, '-still'], [true, true, '-mobile'], [true, false, '-mobile-still']];
  for (const [mobile, animated, suffix] of variants) await writeFile(path.join(assets, `contribution-loom${suffix}.svg`), render(data, mobile, animated));
  console.log(`Original Contribution Loom: ${data.cells.length} real days / ${data.total} contributions / four self-contained variants.`);
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  await renderContributionLoom(JSON.parse(await readFile(path.join(root, 'assets/contribution-data.json'), 'utf8')));
}
