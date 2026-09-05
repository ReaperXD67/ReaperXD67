/** Local visual QA using GitHub's real Markdown renderer; never publishes profile changes. */
import { execFileSync } from 'node:child_process';
import { readFile } from 'node:fs/promises';
import { createServer } from 'node:http';
import { fileURLToPath } from 'node:url';
import path from 'node:path';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const markdown = execFileSync('gh', ['api', 'markdown', '--method', 'POST', '-F', 'text=@README.md', '-f', 'mode=gfm'], { cwd: root, encoding: 'utf8', maxBuffer: 5_000_000 });
const html = `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Aman — GitHub profile preview</title><style>
*{box-sizing:border-box}html{color-scheme:dark}body{background:#0d1117;color:#f0f6fc;font:16px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;margin:0;padding:32px}main{max-width:1012px;margin:auto;border:1px solid #3d444d;padding:32px;border-radius:6px}a{color:#4493f8;text-decoration:none}a:hover{text-decoration:underline}p{margin:0 0 16px}h2{font-size:24px;border-bottom:1px solid #3d444d;padding-bottom:8px;margin:32px 0 16px}h3{font-size:20px;margin:28px 0 16px}img{max-width:100%;height:auto;vertical-align:middle}picture{display:block}sub{font-size:12px}summary{cursor:pointer}details{margin:0 0 16px}details[open]>summary{margin-bottom:16px}li{margin:8px 0}code{background:#ffffff12;border-radius:6px;padding:2px 6px}hr{border:0;background:#3d444d;height:4px;margin:24px 0}a:focus-visible,summary:focus-visible{outline:2px solid #4493f8;outline-offset:4px}@media(max-width:640px){body{padding:12px}main{padding:16px}h2{font-size:23px}h3{font-size:19px}}@media(prefers-color-scheme:light){html{color-scheme:light}body{background:white;color:#1f2328}main{border-color:#d1d9e0}a{color:#0969da}h2,hr{border-color:#d1d9e0}code{background:#818b981f}}
</style></head><body><main>${markdown}</main></body></html>`;
const types = { '.svg': 'image/svg+xml', '.png': 'image/png', '.gif': 'image/gif', '.jpg': 'image/jpeg' };
createServer(async (req, res) => {
  const url = new URL(req.url, 'http://127.0.0.1');
  if (url.pathname === '/favicon.ico') { res.writeHead(204); res.end(); return; }
  if (url.pathname === '/') { res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' }); res.end(html); return; }
  if (!/^\/(?:assets\/[a-z0-9-]+\.(?:svg|png|gif|jpg)|metrics\.svg)$/.test(url.pathname)) { res.writeHead(404); res.end(); return; }
  try { const file = path.join(root, url.pathname); const bytes = await readFile(file); res.writeHead(200, { 'Content-Type': types[path.extname(file)] }); res.end(bytes); }
  catch { res.writeHead(404); res.end(); }
}).listen(4287, '127.0.0.1', () => console.log('GitHub-rendered local preview: http://127.0.0.1:4287'));
