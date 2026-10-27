/** Real GitHub calendar -> Platane/snk animation + yoshi389111 3D skyline.
 * Dependencies and upstream bundle are pinned. No synthetic contribution days.
 * Run with GITHUB_TOKEN in CI, or an already authenticated local GitHub CLI.
 */
import { execFileSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import { mkdir, readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { generateSnakeAnimation, getUserContribution } from 'generate-snake-animation';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const assets = path.join(root, 'assets');
const login = process.env.GH_LOGIN || 'ReaperXD67';
if (!/^[a-z\d](?:[a-z\d-]{0,37}[a-z\d])?$/i.test(login)) throw new Error('Invalid GitHub login.');
const token = process.env.GITHUB_TOKEN || execFileSync('gh', ['auth', 'token'], { encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] }).trim();
const source = { platform: 'github', username: login, githubToken: token };
const cells = await getUserContribution(source);
const total = cells.reduce((sum, cell) => sum + cell.count, 0);
const date = new Date().toISOString().slice(0, 10);
const colors = ['#161b22', '#0e4429', '#006d32', '#26a641', '#39d353'];
const width = 1000, height = 300;
const frame = (body, subtitle) => `<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}" viewBox="0 0 ${width} ${height}" role="img" aria-label="${total} real GitHub contributions, ${cells[0].date} to ${cells.at(-1).date}"><rect width="1000" height="300" fill="#0b0d0e"/><rect x=".5" y=".5" width="999" height="299" fill="none" stroke="#303934"/><text x="30" y="37" fill="#d8ff4f" font-family="monospace" font-size="12" letter-spacing="2">A YEAR OF BUILDING / ${subtitle}</text><text x="30" y="72" fill="#f5f5f1" font-family="Arial,sans-serif" font-size="26">${total} contributions. One living field.</text>${body}<text x="30" y="278" fill="#9aa69a" font-family="monospace" font-size="11">${cells[0].date} — ${cells.at(-1).date} / refreshed ${date} / actual GitHub calendar</text></svg>`;
await mkdir(assets, { recursive: true });
const [snake] = await generateSnakeAnimation(source, [{
  format: 'svg',
  drawOptions: { colorDots: {1:colors[1],2:colors[2],3:colors[3],4:colors[4]}, colorEmpty:colors[0], colorDotBorder:'#0b0d0e', colorSnake:'#d8ff4f', sizeCell:16, sizeDot:12, sizeDotBorderRadius:2 },
  animationOptions: { stepDurationMs:85, frameByStep:1 },
}]);
const animated = String(snake).replace(/<svg\b([^>]*)>/, (_, attributes) => `<svg x="28" y="86" width="944" height="162" preserveAspectRatio="xMidYMid meet" ${attributes.replace(/\b(?:width|height)="[^"]*"/g,'')}>`);
await writeFile(path.join(assets, 'contribution-snake.svg'), frame(animated, 'SNAKE / PLATANE'));
const calendar = cells.map(cell => `<rect x="${45+cell.x*17.3}" y="${104+cell.y*17}" width="13" height="13" rx="2" fill="${colors[cell.level]}"><title>${cell.date}: ${cell.count} contributions</title></rect>`).join('');
await writeFile(path.join(assets, 'contribution-calendar.svg'), frame(calendar, 'STATIC CALENDAR'));
await writeFile(path.join(assets, 'contribution-data.json'), JSON.stringify({login, generated:date, total, first:cells[0].date, last:cells.at(-1).date, cells, generators:{snake:'generate-snake-animation@3.5.0',skyline:'yoshi389111/github-profile-3d-contrib@e235d118909be71eb7edb05482a3de4e76156df3'}}, null, 2)+'\n');

// Official MIT generator, fetched by immutable revision and content digest.
// Only the generated SVG is published; the downloaded software stays ignored.
const revision = 'e235d118909be71eb7edb05482a3de4e76156df3';
const base = `https://raw.githubusercontent.com/yoshi389111/github-profile-3d-contrib/${revision}/`;
const vendor = path.join(root, 'output', 'vendor-3d');
await mkdir(vendor, { recursive:true });
const downloads = [
  ['dist/index.js','index.cjs','981a9fd309b504c6d93770d798a1adf3243644d37b343290d70227fe061cd882'],
  ['dist/xhr-sync-worker.js','xhr-sync-worker.js','a0498e247544e66795565a474d50a6b1566acacafc1339bcc43587ca1f9a9a50'],
  ['LICENSE','LICENSE','caa1ef089455b8d6bc7c03eded3b513868a530e04930f57f2e9cd93f3edef1c6'],
];
for (const [remote, local, expected] of downloads) {
  let bytes;
  try { bytes = await readFile(path.join(vendor,local)); } catch {}
  if (!bytes || createHash('sha256').update(bytes).digest('hex') !== expected) {
    const response = await fetch(base+remote);
    if (!response.ok) throw new Error(`Unable to fetch pinned skyline generator (${response.status}).`);
    bytes = Buffer.from(await response.arrayBuffer());
  }
  if (createHash('sha256').update(bytes).digest('hex') !== expected) throw new Error('Pinned skyline generator digest mismatch.');
  await writeFile(path.join(vendor,local),bytes);
}
await mkdir(path.join(assets,'licenses'),{recursive:true});
await writeFile(path.join(assets,'licenses','github-profile-3d-contrib-MIT.txt'),await readFile(path.join(vendor,'LICENSE')));
const settings = [{type:'normal',fileName:'aman-skyline.svg',backgroundColor:'#0b0d0e',foregroundColor:'#f5f5f1',strongColor:'#d8ff4f',weakColor:'#9aa69a',radarColor:'#39d353',growingAnimation:true,contribColors:colors}];
await writeFile(path.join(vendor,'settings.json'),JSON.stringify(settings));
try {
  execFileSync(process.execPath,[path.join(vendor,'index.cjs'),login],{cwd:vendor,env:{...process.env,GITHUB_TOKEN:token,MAX_REPOS:'100',SETTING_JSON:path.join(vendor,'settings.json')},stdio:['ignore','pipe','pipe'],timeout:90000,maxBuffer:10_000_000});
} catch {
  // Axios diagnostic objects may contain request headers; never print them.
  throw new Error('Pinned 3D generator failed; its diagnostic payload was withheld to protect credentials.');
}
const fullSkyline = await readFile(path.join(vendor,'profile-3d-contrib','aman-skyline.svg'),'utf8');
// Keep the upstream calendar geometry, without repeating its language/radar/
// popularity panels. A balanced-group extraction preserves the SVG tree.
const groupStart=fullSkyline.search(/<g(?:\s|>)/);
if(groupStart<0) throw new Error('Pinned skyline calendar group missing.');
const groups=/<g\b[^>]*>|<\/g>/g;groups.lastIndex=groupStart;
let depth=0,groupEnd=-1,match;
while((match=groups.exec(fullSkyline))) { depth+=match[0].startsWith('</')?-1:1; if(depth===0){groupEnd=groups.lastIndex;break;} }
if(groupEnd<0) throw new Error('Pinned skyline calendar group malformed.');
const prefix=fullSkyline.slice(0,groupStart).replace('height="850"','height="900"').replace('viewBox="0 0 1280 850"','viewBox="0 0 1280 900"');
const focusedSkyline=prefix+`<rect width="1280" height="900" fill="#0b0d0e"/><text x="40" y="48" fill="#d8ff4f" font-family="monospace" font-size="17" letter-spacing="2">ACTUAL CONTRIBUTION SKYLINE / ${total} CONTRIBUTIONS</text><text x="40" y="80" fill="#9aa69a" font-family="monospace" font-size="14">${cells[0].date} — ${cells.at(-1).date} / refreshed ${date}</text>`+fullSkyline.slice(groupStart,groupEnd)+`<text x="40" y="878" fill="#9aa69a" font-family="monospace" font-size="14">Real calendar. Source-generated architecture. Activity is not a skill score.</text></svg>`;
const skyline = focusedSkyline.replace(/<animate(?:Transform)?\b[^>]*>/g, tag => {
  let result=tag.replace(/repeatCount="1"/g,'repeatCount="indefinite"').replace(/dur="3s"/g,'dur="8s"');
  const values=result.match(/values="([^"]+)"/);
  if(values && values[1].split(';').length===2 && !result.includes('keyTimes=')) {
    const end=values[1].split(';')[1];
    result=result.replace(values[0],`values="${values[1]};${end}" keyTimes="0;0.4;1"`);
  }
  return result;
});
if (/<script|<foreignObject|(?:href|src)=["']https?:/i.test(skyline)) throw new Error('Unexpected executable or remote asset in skyline output.');
await writeFile(path.join(assets,'contribution-skyline.svg'),skyline);
await writeFile(path.join(assets,'contribution-skyline-still.svg'),skyline.replace(/<animate(?:Transform)?\b[^>]*(?:\/>|>[\s\S]*?<\/animate(?:Transform)?>)/g,''));
console.log(`Generated actual calendar: ${total} contributions, ${cells.length} days. Snake, static calendar and 3D skyline written.`);
