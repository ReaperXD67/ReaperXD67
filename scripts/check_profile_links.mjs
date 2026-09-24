/** Read-only, bounded audit of README destinations. Requires authenticated gh.
 * No cookies, browser sessions, mutations, or requests to authenticated social pages.
 * Run: node scripts/check_profile_links.mjs
 */
import { execFile } from 'node:child_process';
import { readFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import path from 'node:path';
import { promisify } from 'node:util';
const exec = promisify(execFile);
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const readme = await readFile(path.join(root, 'README.md'), 'utf8');
const urls = [...new Set(readme.match(/https:\/\/[^\s"'<>)]*/g))];
const apiCache = new Map();
async function api(endpoint) {
  if (!apiCache.has(endpoint)) apiCache.set(endpoint, exec('gh', ['api', endpoint], { timeout: 20000, maxBuffer: 5_000_000 }).then(({ stdout }) => JSON.parse(stdout)));
  return apiCache.get(endpoint);
}
const headings = (markdown) => [...markdown.matchAll(/^#{1,6}\s+(.+)$/gm)].map((m) => m[1].toLowerCase().replace(/[^\p{L}\p{N}_\-\s]/gu, '').trim().replace(/\s/g, '-'));
async function check(raw) {
  const url = new URL(raw.replaceAll('&amp;', '&'));
  if (['www.linkedin.com', 'linkedin.com', 'x.com'].includes(url.hostname)) return { url: raw, result: 'manual', note: 'Social profile: verify in the signed-in UI; no automated session access.' };
  try {
    if (url.hostname === 'github.com') {
      const [, owner, repo, kind, ...rest] = url.pathname.split('/');
      const base = `repos/${owner}/${repo}`;
      if (kind === 'blob') {
        const [ref, ...file] = rest;
        const data = await api(`${base}/contents/${file.join('/')}?ref=${ref}`);
        return { url: raw, result: 'ok', note: `Source exists: ${data.path}` };
      }
      if (kind === 'actions' && rest[0] === 'workflows' && !rest.includes('badge.svg')) {
        const data = await api(`${base}/actions/workflows/${rest[1]}`);
        return { url: raw, result: 'ok', note: `Workflow: ${data.name} (${data.state})` };
      }
      if (!kind) {
        await api(base);
        if (url.hash) {
          const data = await api(`${base}/readme`);
          const body = Buffer.from(data.content, 'base64').toString('utf8');
          if (!headings(body).includes(decodeURIComponent(url.hash.slice(1)))) return { url: raw, result: 'review', note: 'Repository exists, but README heading anchor was not found.' };
        }
        return { url: raw, result: 'ok', note: url.hash ? 'Repository and README heading exist.' : 'Repository exists.' };
      }
    }
    const response = await fetch(url, { signal: AbortSignal.timeout(15000), headers: { 'User-Agent': 'AmanProfileLinkCheck/1.0' } });
    const note = `HTTP ${response.status}${response.redirected ? ` → ${response.url}` : ''}`;
    await response.body?.cancel();
    return { url: raw, result: response.ok ? 'ok' : 'review', note };
  } catch (error) {
    return { url: raw, result: 'review', note: String(error.message).split('\n')[0] };
  }
}
const results = new Array(urls.length);
let cursor = 0;
await Promise.all(Array.from({ length: 5 }, async () => {
  while (cursor < urls.length) {
    const index = cursor++;
    results[index] = await check(urls[index]);
  }
}));
console.log(JSON.stringify({ checkedAt: new Date().toISOString(), total: results.length, summary: results.reduce((acc, item) => ({ ...acc, [item.result]: (acc[item.result] || 0) + 1 }), {}), results }, null, 2));
if (results.some((result) => result.result === 'review')) process.exitCode = 1;
