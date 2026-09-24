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

- `assets/identity-scan.gif`: Aman's approved September 24, 2026 portrait, composed without further retouching into a quiet 1280 × 480 editorial header. A finite top-to-bottom pixel reveal settles after 1.7 seconds instead of looping. `prefers-reduced-motion` selects `identity-still.png`.
- `assets/identity-mobile-scan.gif`: a separately composed 700 × 890 portrait-first header. The source order gives small screens a legible vertical layout, and small screens with reduced motion get `identity-mobile-still.png` instead of a GIF. Both variants have the same complete text available in the ordinary Markdown and image description.
- `assets/architecture-atlas.svg`: original static vector geometry at 1000 × 684. It distinguishes approval, retrieval-fusion, and signed-event boundaries.
- `assets/architecture-atlas-mobile.svg`: deliberately recomposed 460 × 1052 version, not a shrinking desktop screenshot. The README's picture source selects it below 640px.
- `assets/aman-kumar-avatar.jpg`: the approved square portrait exported for an account-avatar upload. Presence in this repository does not mean the account avatar has been changed.
- `assets/fonts/space-grotesk-latin-wght-normal.woff2`: the open-source Space Grotesk face used to render the header. Its SIL Open Font License is included alongside it; the finished image has no external font dependency.

Regenerate both identity compositions with Pillow and fontTools/Brotli installed:

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
