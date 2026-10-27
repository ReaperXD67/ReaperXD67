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

The new profile reading path begins with three concrete failures and direct inspection routes: stale worker completion, unsupported generated answers, and lost game-delivery acknowledgement. The compact index is followed by the actual decisions, linked implementation, and native scope disclosures.

The portrait master is Aman's supplied yellow-kurta photograph edited for a restrained charcoal background and professional lighting. Facial identity, hair, expression, and clothing are preserved. The header compositor resizes the approved square export and adds only layout and the finite entrance. Primary desktop APNG is 1,460,221 bytes; mobile APNG is 973,595 bytes. Both retain full RGB color and play once. The larger lossless format was chosen after inspecting GIF palette artifacts on facial shading; static and animated views now preserve the same photograph. All core information also exists in ordinary Markdown.

The Agent scope disclosure now reflects the current implementation: Career Play can authorize bounded automatic applications within an explicit expiring scope; manually prepared actions retain exact-action review. External application proof and Gmail OAuth proof are still pending. This supersedes the old blanket statement that every external submission needs an individual approval.

The bounded destination audit resolved **34 of 36 unique HTTPS destinations** on October 27; LinkedIn and X remain manual signed-in checks. Repository content paths, active workflow definitions, and three README anchors resolved. This is availability evidence, not a new CI execution or whole-application test. An authenticated read-only GitHub query confirmed the six approved pins already appear in the required order.

The original signal geometry and header were authored for this profile. Research compared Anurag Hazra, DenverCoder1, lowlighter, Sindre Sorhus, innng, and common profile component repositories. The visual direction uses their lessons in hierarchy, authored identity, disclosures, and proof routes; no third-party header illustration or code was copied. Full dated references live in the companion portfolio's `docs/github-research-2026-10-27.md`.

The GitHub-rendered local README preview was visually inspected at 1280 px and 390 px. A 320 px check confirmed the final page width equals the viewport and all images load; the failure index uses ordinary flowing Markdown to stay readable at narrow widths. Reduced-motion emulation selected the mobile static PNG, and the checked preview reported zero console errors or warnings. Both APNGs have one animation cycle and a complete static default image. This preview uses GitHub's Markdown renderer with a local stylesheet and does not certify every possible GitHub theme or device. The published GitHub profile was also checked for the new heading, updated Agent disclosure, loaded responsive assets, and reduced-motion source selection.
