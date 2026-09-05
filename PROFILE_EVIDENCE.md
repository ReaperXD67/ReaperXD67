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

- `assets/identity-scan.gif`: the approved photograph, unchanged, introduced with a finite top-to-bottom pixel reveal. It settles after 2.25 seconds instead of looping. `prefers-reduced-motion` selects `identity-still.png`.
- `assets/architecture-atlas.svg`: original static vector geometry at 1000 × 684. It distinguishes approval, retrieval-fusion, and signed-event boundaries.
- `assets/architecture-atlas-mobile.svg`: deliberately recomposed 460 × 1052 version, not a shrinking desktop screenshot. The README's picture source selects it below 640px.
- `assets/aman-kumar-avatar.jpg`: the approved square portrait exported for an account-avatar upload. Presence in this repository does not mean the account avatar has been changed.

Regenerate the architecture assets with:

```sh
node scripts/render_atlas.mjs
```

All essential facts and links remain ordinary Markdown. The images contain accessible descriptions and no scripts, embedded fonts, tracking, external assets, or claims of interactivity.
