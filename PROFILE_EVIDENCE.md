# Profile evidence and implementation

This profile is a curated reading path, not a dashboard or a claim of production scale. The diagrams are intentionally simplified; implementation links in the README are the source of truth.

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

The green native contribution grid belongs to GitHub and cannot be restyled from a profile README. The README adds real-calendar visualizations above the flagship reading path:

- **Contribution snake:** generated by [Platane/snk](https://github.com/Platane/snk), using the exact `generate-snake-animation@3.5.0` npm package. An authored frame identifies the actual rolling period and snapshot date. A native disclosure hides the moving field; reduced motion selects a static calendar.
- **3D contribution skyline:** generated by [yoshi389111/github-profile-3d-contrib](https://github.com/yoshi389111/github-profile-3d-contrib) at revision `e235d118909be71eb7edb05482a3de4e76156df3`, customized to the portfolio palette. The output retains its calendar geometry and omits repeated radar, language and popularity panels. Its generated growth animation repeats every eight seconds, holding the full skyline after the rise so it still animates when a visitor opens its disclosure later. Its executable is downloaded from that immutable official revision and checked against a committed SHA-256 before running. The MIT notice is preserved in `assets/licenses/github-profile-3d-contrib-MIT.txt`. A separate static SVG removes animation elements for reduced motion.
- **Provenance:** `assets/contribution-data.json` records the actual day counts, dates, total, generation date, and generator versions. There are no synthetic contribution cells, artificial commits, or skill/quality scores. At the first generation, GitHub returned 536 contributions and zero restricted contributions. The calendar can change after new genuine activity.

Install and regenerate with an authenticated local GitHub CLI, or provide `GITHUB_TOKEN` through the environment:

```sh
npm ci --ignore-scripts
npm run activity
```

`scripts/generate_activity.mjs` reads credentials into process memory and never prints them. Upstream failure diagnostics are withheld because HTTP diagnostic objects can contain request headers. Software downloads stay in ignored `output/`; only SVGs, data provenance, notices, and authored scripts are published.

The existing daily refresh workflow now regenerates metrics and contribution instruments together. Checkout and Node setup actions are pinned to reviewed revisions; npm dependencies are locked; the job uses GitHub's repository-scoped token with `contents: write` only where publication is required. No personal token or new account secret is created. The snk upstream/npm package did not declare an explicit license in the inspected metadata; it is consumed through its documented generator API, attributed, and no upstream source is vendored or relabeled as MIT.

Run the local GitHub Markdown preview with `npm run preview`; set `PORT` when a different local port is needed. The preview uses GitHub's renderer and does not publish changes.

## Badge provenance — checked September 24, 2026

Four small badges appear beside the work or credential they describe, rather than as a wall of unrelated logos:

- **Autonomous Personal Agent CI:** GitHub's native workflow badge for `actions/workflows/ci.yml?branch=main`. At review, [run 35873161678](https://github.com/ReaperXD67/autonomous-personal-agent/actions/runs/35873161678) passed on September 23, 2026. The badge remains live and can change.
- **AtlasLM RAG quality gates:** GitHub's native badge for `actions/workflows/quality.yml?branch=main`. At review, [run 31781510995](https://github.com/ReaperXD67/notebooklm-rag/actions/runs/31781510995) passed on August 14, 2026. This is the latest run, not a claim that checks ran today.
- **Agent MIT license:** a dynamic Shields badge linked to that repository's actual `LICENSE` file. It describes that project only, not every repository on the profile.
- **micro1 credential:** an informational badge linked to Aman's supplied certificate, issued March 11, 2026 for Freelance AI / Machine Learning Developer. Shields is only the image renderer; it does not independently verify credentials.

GitHub's sidebar **Achievements** are platform-awarded events. README badges cannot award them. No artificial pull requests, stars, co-author records, or self-created awards were used in this refinement. See [GitHub's profile reference](https://docs.github.com/en/account-and-profile/reference/profile-reference) and [native workflow badge documentation](https://docs.github.com/en/actions/how-tos/monitor-workflows/add-a-status-badge).

The three flagship repositories' current READMEs were checked again for lifecycle, retrieval, and plugin-boundary claims on September 24. None of these badges asserts customer scale, commercial outcomes, independent security certification, or universal ATS compatibility.

## Reading path & link maintenance

The first screen names the work Aman can do, the actual internship context, and the primary portfolio, recruiter, résumé, and contact routes. The canonical résumé link is labeled **One-page ATS résumé · PDF**; it is a photo-free, single-column document, not an alternate visual résumé. No claim of universal ATS acceptance is made.

The flagship section starts with direct actions for the agent source, AtlasLM workspace, and KarixMC site. The architecture comparison remains available in a native disclosure after the three project explanations, so a large illustration no longer separates visitors from the first project links. Project-specific disclosure labels distinguish the three scope notes. Technical skills remain ordinary visible text instead of being hidden behind another click.

Run the bounded, read-only destination audit with Node.js and an authenticated GitHub CLI:

```sh
node scripts/check_profile_links.mjs
```

On September 24, 2026, the README contained **35 unique HTTPS destinations**: 33 returned a successful HTTP response or resolved through GitHub's documented repository, content, or workflow APIs. LinkedIn and X were explicitly reserved for manual signed-in verification rather than treated as broken links or accessed through session extraction. No stale source or live-site URL was found. The checker also verifies the two linked README heading anchors.

This checks destination availability, not full application behavior, uptime guarantees, current CI success, or the integrity of an external credential. It does not submit forms, edit remote accounts, or run against authenticated social pages. Results are a dated maintenance check, not a permanent uptime claim.

## October 27, 2026 refinement

The profile now opens with a continuously rotating Decision Loom, the recognizable supplied portrait and canonical recruiter actions, then the actual contribution snake. Optional skyline motion follows before the failure-led project evidence: stale worker completion, unsupported generated answers, and lost game-delivery acknowledgement. Repeated role and introduction paragraphs were compacted so the contribution field follows the hero immediately.

The portrait master is Aman's supplied yellow-kurta photograph edited for a restrained charcoal background and professional lighting. Facial identity, hair, expression, and clothing are preserved. The current header compositor resizes the approved square export and adds only layout and procedural signal geometry. Desktop APNG is 2,599,367 bytes; mobile APNG is 2,635,361 bytes. Both retain full RGB color and loop every 4.68 seconds, with 52 timed frames and a complete default PNG image. Static versions and ordinary Markdown preserve the core information. The earlier finite entrance assets remain available as previous versions. Neither GitHub nor LinkedIn's account avatar is changed.

The Agent scope disclosure now reflects the current implementation: Career Play can authorize bounded automatic applications within an explicit expiring scope; manually prepared actions retain exact-action review. External application proof and Gmail OAuth proof are still pending. This supersedes the old blanket statement that every external submission needs an individual approval.

The bounded destination audit resolved **36 of 38 unique HTTPS destinations** on October 27; LinkedIn and X remain manual signed-in checks. Repository content paths, active workflow definitions, and README anchors resolved. This is availability evidence, not a whole-application test. An authenticated read-only GitHub query confirmed the six approved pins already appear in the required order.

The original signal geometry and header were authored for this profile. Reusable contribution systems were inspected and the actual snake and skyline generators were integrated. The research matrix compares twelve primary sources, including Platane/snk, github-profile-3d-contrib, Arcade Contribution Graph Games, lowlighter/metrics, readme-typing-svg and capsule-render. Full dated references and integration decisions live in the companion portfolio's `docs/github-animation-research-2026-10-27.md`.

The current GitHub-rendered local README preview was inspected at desktop, 768 px, 390 px and 320 px. At 390 and 320 px, document width equals viewport width, all images load and the mobile hero is selected. Keyboard Space toggles the native hero disclosure; the snake also collapses. The focused skyline renders its actual calendar geometry. The four contribution SVGs parse successfully, contain no executable content or external runtime assets, and their static versions contain no animation elements. The integrity check verifies 367 consecutive unique dates summing to the actual 536-contribution snapshot. Pillow confirms looping APNGs and single-frame static PNGs. Reduced-motion source declarations are present; this current iteration did not emulate an OS preference. The preview uses GitHub's Markdown renderer with a local stylesheet and does not certify every possible GitHub theme or device.

Published as commit `61f96c59fd5f17915bbef92e8f198f86be1969ce`. A manual [refresh run](https://github.com/ReaperXD67/ReaperXD67/actions/runs/40532370338) succeeded on October 27: clean dependency installation, actual snake and skyline generation, SVG/data verification, public metrics generation and bot publication all passed. The generated refresh commit is `4a225fa`. The public GitHub profile was then checked for the new hero and contribution images, loaded assets and native disclosures. This confirms the shipped generation path rather than only a future scheduled promise.
