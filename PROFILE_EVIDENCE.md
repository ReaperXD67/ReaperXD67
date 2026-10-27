# Profile evidence and implementation

This profile is a visual reading path with real project captures and authored system films. Motion explains implementation boundaries; it does not report a running test, live production telemetry or measured commercial outcomes. Source links and scope notes remain ordinary Markdown.

## Project showcase films

The October 27 body redesign replaces long default-visible project paragraphs with five full-width visual compositions. The header and genuine contribution artwork remain intact. At Aman's subsequent request, the complete contribution section now appears **last**, after the recruiter close and static/evidence footer, under **The build trace.** The snake, optional skyline, native motion controls, static sources, daily data and provenance links are preserved. The first reading path now runs directly from personal introduction and professional actions into flagship work.

- **Autonomous Personal Agent:** orange owned-execution timeline and stale-completion boundary. It is explicitly labeled **Local alpha / architecture study**, not a real interface capture. Ordinary Markdown links to the actual lifecycle and action-store implementation. External application proof remains pending; the stale blanket clause about pending Gmail proof was removed after current source review, without introducing a broader email-delivery claim.
- **AtlasLM:** a real landing-page capture beside an original dense/BM25 candidate convergence study. The simplified path retains RRF, reranking and a sufficiency gate before generation and citation audit; the source architecture describes full ingestion and MMR behavior.
- **MinePulse / KarixMC:** the real colorful site capture owns the visual stage, followed by a signed-event / server-side ledger / recorded-receipt bridge. Snapshot values in the capture belong to the recorded interface and are not presented as current telemetry or verified customer outcomes.
- **Build index:** ROLLFORWARD, Revive and AtlasForge AI use a compact animated editorial index; direct live/source routes and honest prototype boundaries remain in Markdown.
- **Capabilities:** a static typographic composition groups actual working tools without a score, popularity ranking or animated proficiency meters. Complete stack text remains in a disclosure; career roles and dates remain visible and unchanged.

The choreography moves emphasis across complete mechanism states: Agent transaction → lease → receipt/refusal boundary; AtlasLM candidate bands → fusion → sufficiency/citation gate; KarixMC HMAC/nonce → ledger → recorded-receipt return. Framed optical sweeps cross the real captures without replacing their content. Project names and stage labels remain visible throughout the twelve-second sequence. Each moving film sits in an open native disclosure with an explicit collapse action. Every composition has a separately laid-out narrow-screen version and zero-animation static version, selected with `picture` sources. Static exports omit complete moving-packet and optical-sweep elements, rather than leaving circles at the origin. Static project files: [Agent](./assets/showcase-agent-still.svg), [AtlasLM](./assets/showcase-atlaslm-still.svg), [KarixMC](./assets/showcase-karixmc-still.svg), [build index](./assets/showcase-build-index-still.svg), [capabilities](./assets/showcase-capabilities-still.svg). Their `-mobile-still.svg` companions are composed for phones rather than shrinking a desktop diagram.

`scripts/render_project_showcases.py` uses Pillow only to resize/re-encode supplied project captures, and fontTools to outline the existing OFL Space Grotesk font. SVG playback needs neither fonts nor JavaScript, remote image servers, `foreignObject`, CSS injection or an installed animation runtime. The capture JPEGs are embedded as data URIs. `assets/showcase-provenance.json` records original file dimensions and SHA-256, embedded dimensions/encoding and SHA-256, font provenance and the distinction between a real capture and illustrative motion. The source assets are `public/assets/atlaslm-landing.png` and `public/assets/karixmc-live.png` in the companion portfolio. No project screenshot is synthesized or passed off as a new run.

The two original owned capture inputs are committed under `assets/captures/`, so a standalone profile clone can regenerate the same output. Their original companion-portfolio paths and matching digests remain in the manifest. Regenerate from this repository:

```sh
python -m pip install -r requirements-showcases.txt
npm run showcases
npm run verify:showcases
npm run preview
```

`scripts/compose_profile_body.py` is the source for this authored body composition; it retains the current hero, writes the body and places the preserved complete contribution block last, idempotently. Ordinary content edits can also be made directly in `README.md`; synchronize the compositor if the body is regenerated. Committed outputs remain fully usable without Pillow/fontTools. No third-party playback runtime is installed in the published profile.

The bounded validator parses all twenty SVGs, rejects executable and external runtime references, checks every embedded capture against its recorded digest and verifies that static variants contain no animation or moving-packet/sweep remnants. An isolated standalone-input test, without the companion `public/` directory, reproduced all twenty SVGs byte-for-byte. Local full-page desktop and 390 px inspection confirmed all five selected assets load, mobile uses all five recomposed variants, and native Space collapse works; a 320 px check found no page overflow or missing images. Selected desktop graphics total 1,119,408 bytes; mobile graphics total 1,054,417 bytes. All twenty variants total 4,337,812 bytes, with 821,208 bytes of original capture inputs. Live GitHub verification of embedded captures is a separate publication step, not implied by the local preview.

The body shipped in [commit 955935e](https://github.com/ReaperXD67/ReaperXD67/commit/955935e56e7d3947ca21033810277fbc50c48d94). The actual [public GitHub profile](https://github.com/ReaperXD67) was then checked: all five new selected SVG assets loaded, and both embedded AtlasLM and KarixMC captures visibly rendered inside the image context. Two live AtlasLM frames at the same scroll position and dimensions showed different large candidate/gate emphasis and optical-sweep positions, confirming the authored sequence plays on GitHub. Live screenshots also captured the complete KarixMC product and signed receipt-return band. This body refinement does not modify the already-verified contribution refresh workflow.

### Primary body-animation references

- [Wenoxxxx/svg-readme](https://github.com/Wenoxxxx/svg-readme): inspected the actual Project Showcase template and export architecture. Its template principle supports a visual body; this profile authors its own compositions and does not run or vendor that editor.
- [ryanpolasky/ryme.md](https://github.com/ryanpolasky/ryme.md): inspected source documentation for per-section, self-contained SVG/CSS and deterministic raster export. No source or biography copied.
- [ratacat/github-marquee](https://github.com/ratacat/github-marquee): inspected its examples and self-contained timeline guidance. The current project labels stay visible while only packets and short strokes move.
- [charmbracelet/bubbletea](https://github.com/charmbracelet/bubbletea): actual README leads with a full-width product demonstration before tutorial prose. Applied the artifact-first hierarchy, without borrowing its branded media.
- [charmbracelet/vhs](https://github.com/charmbracelet/vhs): inspected reproducible terminal demonstrations and their source tapes. This profile has no fabricated terminal output; the Agent plate is labeled an architecture study instead.
- [nbedos/termtosvg](https://github.com/nbedos/termtosvg), [marionebl/svg-term-cli](https://github.com/marionebl/svg-term-cli): inspected script-free SVG recording approaches. termtosvg is archived; neither generator is installed or used here.
- [GitHub diagram documentation](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams) and [AtlasLM's actual retrieval diagram](https://github.com/ReaperXD67/notebooklm-rag/blob/main/docs/assets/readme/atlaslm-retrieval-flow.svg): checked native diagram constraints and source-faithful retrieval ordering.

The deliverable is native repository SVG inside GitHub Markdown. HyperFrames' entry guidance was reviewed; its HTML/video runtime does not execute in this surface, so the implementation uses authored, self-contained SVG SMIL and explicit static outputs.

## Content checked on 2026-09-05

| Profile claim | Primary source |
| --- | --- |
| Transactional outbox, worker ownership, heartbeat, stale-completion refusal | [Agent lifecycle ADR](https://github.com/ReaperXD67/autonomous-personal-agent/blob/main/docs/decisions/ADR-0007-durable-execution-lifecycle.md), [worker implementation](https://github.com/ReaperXD67/autonomous-personal-agent/blob/main/services/control-api/app/worker.py) |
| Exact-action digest, durable receipts, limited local-alpha scope | [Action-store implementation](https://github.com/ReaperXD67/autonomous-personal-agent/blob/main/services/control-api/app/action_store.py), [exact-action ADR](https://github.com/ReaperXD67/autonomous-personal-agent/blob/main/docs/decisions/ADR-0010-exact-external-actions.md) |
| Dense + BM25, RRF, reranking/MMR, sufficiency gate, citation audit | [AtlasLM checklist and architecture](https://github.com/ReaperXD67/notebooklm-rag#production-checklist) |
| Single-source workspace and instance-local cache | [AtlasLM honest scope](https://github.com/ReaperXD67/notebooklm-rag#honest-scope) |
| HMAC events, expiring delivery claims, plugin-side receipt journal | [MinePulse plugin API](https://github.com/ReaperXD67/MinePulse#plugin-api) |
| Two replicas, VPS, backup/runbook, manually confirmed campaign credits | [MinePulse deployment and currencies](https://github.com/ReaperXD67/MinePulse#production-deployment) |
| Optimistic projection, IndexedDB outbox, same-key retries and 412 conflicts | [ROLLFORWARD](https://github.com/ReaperXD67/rollforward-optimistic-engine) |
| Live recovery prototype, immutable audit, fictional payment outcomes | [Revive implementation and scope](https://github.com/ReaperXD67/revive-ai#what-is-actually-implemented) |
| SQLite/filesystem runtime, checkpoints, bounded cloud spend | [AtlasForge actual runtime and rationale](https://github.com/ReaperXD67/atlasforge-ai#why-this-architecture) |

Employment, education, and dates follow Aman's supplied résumé. No customer counts, revenue gains, awards, or third-party endorsements are inferred from source code. Test totals are deliberately not duplicated here; linked CI evidence can evolve with the repositories.

## Authored assets

The current hero is `assets/identity-signal.png`, with a separately composed mobile image and explicit static variants. An original, perspective-projected Decision Loom rotates continuously through a 4.68-second full-RGB APNG loop. The supplied portrait is placed mechanically and remains clear throughout; neither account avatar is replaced. A native disclosure can hide the moving hero without hiding the ordinary Markdown role, context, links and evidence. Regenerate with:

```sh
python scripts/render_signal_identity.py --portrait /path/to/approved-square-portrait.png
```

The older finite-assembly headers below are retained as previous artifacts, not the primary README entrance.

- `assets/identity-assembly.png`: Aman's approved October 27, 2026 yellow-kurta portrait, composed without further retouching into an authored 1280 × 520 editorial header. Full-RGB APNG preserves natural facial shading. The single signal route and finite top-to-bottom pixel reveal settle after 1.7 seconds; `loop=1` plays once. A complete static default PNG frame serves clients without APNG support, and `prefers-reduced-motion` selects `identity-still.png`.
- `assets/identity-mobile-assembly.png`: a separately composed 700 × 890 portrait-first header with the same finite, full-RGB animation and complete static default image. Small screens with reduced motion get `identity-mobile-still.png`. Both variants have the same complete text available in ordinary Markdown and image descriptions. Prior GIF exports are retained for compatibility, but are no longer the primary README images.
- `assets/architecture-atlas.svg`: original static vector geometry at 1000 × 684. It distinguishes approval, retrieval-fusion, and signed-event boundaries.
- `assets/architecture-atlas-mobile.svg`: deliberately recomposed 460 × 1052 version, not a shrinking desktop screenshot. The README's picture source selects it below 640px.
- `assets/aman-kumar-avatar.jpg`: the approved square portrait exported for an account-avatar upload. Presence in this repository does not mean the account avatar has been changed.
- `assets/fonts/SpaceGrotesk.ttf`: the open-source variable Space Grotesk face used to render the header directly with Pillow. Its SIL Open Font License is included alongside it; the finished image has no external font dependency. The prior WOFF2 source is retained.

Regenerate both identity compositions with Pillow installed:

```sh
python scripts/render_identity.py --portrait /path/to/approved-square-portrait.png
```

The compositor preserves the supplied square framing. It does not synthesize, retouch, or reconstruct Aman's face.

Regenerate the architecture assets with:

```sh
node scripts/render_atlas.mjs
```

All essential facts and links remain ordinary Markdown. The images contain accessible descriptions and no scripts, embedded fonts, tracking, external assets, or claims of interactivity.

## Contribution instruments

The green native contribution grid belongs to GitHub and cannot be restyled from a profile README. The README adds real-calendar visualizations in its final **The build trace.** section:

- **Original Contribution Loom, primary:** `scripts/render_contribution_loom.mjs` projects seven weekday helices into an authored 3D weave. Every actual date gets one fixed faceted cell, including empty days. Cell rise is `0.045 + 0.92 × log(1 + count) / log(1 + maximum daily count)`; light intensity uses the same normalized count. This logarithmic scale keeps low-activity days visible alongside unusually large counts. All daily geometry and colors stay fixed. Seven light sweeps are explicitly decorative, not new contributions, live traffic or measured work quality. The renderer uses Node's standard library only, makes no network request, and embeds neither external resources nor executable content. Complete first frames, separate desktop/mobile compositions and explicit static SVGs are generated from the same snapshot. SVG metadata records the source-cell SHA-256, total, dates, snapshot date and encoding semantics. No third-party artwork or geometry was copied.
- **Contribution snake, optional closed disclosure:** generated by [Platane/snk](https://github.com/Platane/snk), using the exact `generate-snake-animation@3.5.0` npm package. An authored frame identifies the actual rolling period and snapshot date. Reduced motion selects a static calendar.
- **3D contribution skyline, optional closed disclosure:** generated by [yoshi389111/github-profile-3d-contrib](https://github.com/yoshi389111/github-profile-3d-contrib) at revision `e235d118909be71eb7edb05482a3de4e76156df3`, customized to the portfolio palette. The output retains its calendar geometry and omits repeated radar, language and popularity panels. Its generated growth animation repeats every eight seconds, holding the full skyline after the rise so it still animates when a visitor opens its disclosure later. Its executable is downloaded from that immutable official revision and checked against a committed SHA-256 before running. The MIT notice is preserved in `assets/licenses/github-profile-3d-contrib-MIT.txt`. A separate static SVG removes animation elements for reduced motion.
- **Provenance:** `assets/contribution-data.json` records the actual day counts, dates, total, generation date, and generator versions. There are no synthetic contribution cells, artificial commits, or skill/quality scores. At the first generation, GitHub returned 536 contributions and zero restricted contributions. The calendar can change after new genuine activity.

Install and regenerate with an authenticated local GitHub CLI, or provide `GITHUB_TOKEN` through the environment:

```sh
npm ci --ignore-scripts
npm run activity
```

Regenerate only the original loom from the existing checked-in snapshot, without credentials, a data refresh or dependencies:

```sh
node scripts/render_contribution_loom.mjs
python scripts/verify_activity.py
```

The integrity verifier checks all eight contribution SVGs, the exact date/count/lane/week set in every loom variant, the logarithmic height mapping, snapshot digests/dates/totals and the absence of motion in static files. No contribution cell contains animation. Animated variants have exactly seven decorative route sweeps. The daily `activity` command invokes the original renderer immediately after writing the real JSON snapshot; the existing scoped `assets/contribution-*.svg` publication glob includes every loom variant. Existing token permissions and dependencies are unchanged.

`scripts/generate_activity.mjs` reads credentials into process memory and never prints them. Upstream failure diagnostics are withheld because HTTP diagnostic objects can contain request headers. Software downloads stay in ignored `output/`; only SVGs, data provenance, notices, and authored scripts are published.

The existing daily refresh workflow now regenerates metrics and contribution instruments together. Checkout and Node setup actions are pinned to reviewed revisions; npm dependencies are locked; the job uses GitHub's repository-scoped token with `contents: write` only where publication is required. No personal token or new account secret is created. The snk upstream/npm package did not declare an explicit license in the inspected metadata; it is consumed through its documented generator API, attributed, and no upstream source is vendored or relabeled as MIT.

Run the local GitHub Markdown preview with `npm run preview`; set `PORT` when a different local port is needed. The preview uses GitHub's renderer and does not publish changes.

## Source evidence, workflows & credentials

The current body uses direct CI/quality-gate, source, license and supplied-certificate links instead of repeating badge images. A link to a workflow does not claim it ran today or independently certifies the project. The Agent MIT license describes that repository only. The micro1 certificate is the supplied Freelance AI / Machine Learning Developer credential issued March 11, 2026.

GitHub's sidebar **Achievements** are platform-awarded events. README artwork cannot award them. No artificial pull requests, stars, co-author records or self-created awards were used. See [GitHub's profile reference](https://docs.github.com/en/account-and-profile/reference/profile-reference).

## Reading path & link maintenance

The first screen names the work Aman can do, the actual internship context, and the primary portfolio, recruiter, résumé, and contact routes. The canonical résumé link is labeled **One-page ATS résumé · PDF**; it is a photo-free, single-column document, not an alternate visual résumé. No claim of universal ATS acceptance is made.

Each flagship film is followed immediately by the ordinary Markdown project name, honest status, one sentence and direct actions for live/source/decisions. Deep engineering and scope notes sit in clearly named native disclosures. The architecture comparison remains optional. Working-tool categories are visible in the static capability composition, with complete plain-text stack details in a disclosure. Employment roles and dates remain visible in ordinary Markdown.

Run the bounded, read-only destination audit with Node.js and an authenticated GitHub CLI:

```sh
node scripts/check_profile_links.mjs
```

The current body audit on October 27, 2026 checked **34 unique HTTPS destinations**: 32 returned a successful HTTP response or resolved through GitHub's documented repository, content or workflow APIs. LinkedIn and X remain manual signed-in checks rather than being treated as broken links or accessed through session extraction. No stale source or live-site URL was found. Repository heading anchors are checked against their actual READMEs.

This checks destination availability, not full application behavior, uptime guarantees, current CI success, or the integrity of an external credential. It does not submit forms, edit remote accounts, or run against authenticated social pages. Results are a dated maintenance check, not a permanent uptime claim.

## October 27, 2026 refinement

The profile opens with a continuously rotating Decision Loom, the recognizable supplied portrait and canonical recruiter actions, followed directly by the source-linked project films described above. The complete genuine-calendar contribution field and optional skyline now close the README after all recruiter and footer content, at Aman's explicit request.

The portrait master is Aman's supplied yellow-kurta photograph edited for a restrained charcoal background and professional lighting. Facial identity, hair, expression, and clothing are preserved. The current header compositor resizes the approved square export and adds only layout and procedural signal geometry. Desktop APNG is 2,599,367 bytes; mobile APNG is 2,635,361 bytes. Both retain full RGB color and loop every 4.68 seconds, with 52 timed frames and a complete default PNG image. Static versions and ordinary Markdown preserve the core information. The earlier finite entrance assets remain available as previous versions. Neither GitHub nor LinkedIn's account avatar is changed.

The Agent scope disclosure reflects the current implementation: Career Play can authorize bounded automatic applications within an explicit expiring scope; manually prepared actions retain exact-action review. External application proof remains pending. This supersedes the old blanket statement that every external submission needs an individual approval; the profile does not generalize the source's bounded owned-inbox email proof into a claim about creator-inbox placement.

The current bounded destination audit resolved **32 of 34 unique HTTPS destinations** on October 27; LinkedIn and X remain manual signed-in checks. This is availability evidence, not a whole-application test. An earlier authenticated read-only GitHub query confirmed the six approved pins already appear in the required order; this body redesign does not change them.

The original signal geometry and header were authored for this profile. Reusable contribution systems were inspected and the actual snake and skyline generators were integrated. The research matrix compares twelve primary sources, including Platane/snk, github-profile-3d-contrib, Arcade Contribution Graph Games, lowlighter/metrics, readme-typing-svg and capsule-render. Full dated references and integration decisions live in the companion portfolio's `docs/github-animation-research-2026-10-27.md`.

The earlier hero/body GitHub-rendered local README preview was inspected at desktop, 768 px, 390 px and 320 px. That pass checked mobile image selection, native disclosures and the original four contribution SVGs. Pillow confirmed looping APNGs and single-frame static PNGs. The newer Contribution Loom adds four self-contained SVGs; its current integrity check verifies every one of 367 consecutive unique dates summing to the actual 536-contribution snapshot, with identical source digests across all variants. The original desktop and vertical mobile loom and the actual GitHub-rendered local README were inspected in Chrome. At 390 px the mobile SVG is selected and loads successfully, with no horizontal page overflow. Static versions are complete and contain no animation elements; reduced-motion picture sources are declared. This pass did not emulate an OS motion preference. A local preview uses GitHub's Markdown renderer with a local stylesheet and does not certify every possible GitHub theme, device or live image-cache behavior.

The hero/contribution iteration published as commit `61f96c59fd5f17915bbef92e8f198f86be1969ce`. Its manual [refresh run](https://github.com/ReaperXD67/ReaperXD67/actions/runs/40532370338) succeeded on October 27: clean dependency installation, actual snake and skyline generation, SVG/data verification, public metrics generation and bot publication all passed. The generated refresh commit is `4a225fa`. The public GitHub profile was checked for those new assets and disclosures. The later body redesign has its own review/publication verification and does not reuse that earlier run as evidence for its new graphics.
