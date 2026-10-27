"""Apply the authored visual reading path while retaining the existing header/calendar."""
from pathlib import Path
root=Path(__file__).resolve().parents[1]
path=root/'README.md'
original=path.read_text(encoding='utf8')
boundary="GitHub's native contribution grid remains GitHub-controlled.</sub>"
assert boundary in original, 'Expected genuine-calendar prefix boundary is missing.'
heading='## The build trace.' if '## The build trace.' in original else '## A year, in motion.'
start=original.index(heading)
contributions=original[start:original.index(boundary,start)+len(boundary)].replace('## A year, in motion.','## The build trace.')
prefix=original[:original.index('</div>')+len('</div>')]+'\n'

def picture(name,alt):
    return f'''<picture>
  <source media="(max-width: 640px) and (prefers-reduced-motion: reduce)" srcset="./assets/{name}-mobile-still.svg">
  <source media="(max-width: 640px)" srcset="./assets/{name}-mobile.svg">
  <source media="(prefers-reduced-motion: reduce)" srcset="./assets/{name}-still.svg">
  <img src="./assets/{name}.svg" width="1000" alt="{alt}">
</picture>'''

body='''
[LinkedIn](https://www.linkedin.com/in/aman-kumar-494601329) · [Email](mailto:amankumr3254u@gmail.com) · [X / Twitter](https://x.com/Aman1181)

## Systems you can inspect.

Three flagship builds. Real interfaces, visible boundaries, source behind every decision.

<details open>
<summary><strong>Autonomous Personal Agent · architecture film · collapse to hide motion</strong></summary>

'''+picture('showcase-agent','Autonomous Personal Agent, local alpha. Original orange architecture study: task and outbox share a transaction, execution holds an owned lease, durable receipts record effects, and stale completion is rejected. This is an illustrative source explanation, not a live interface or test run.')+'''

</details>

**[Autonomous Personal Agent](https://github.com/ReaperXD67/autonomous-personal-agent) · Local alpha.** Owned leases, bounded retries and durable receipts make interrupted work recoverable.

[Source](https://github.com/ReaperXD67/autonomous-personal-agent) · [Why stale workers stop](https://github.com/ReaperXD67/autonomous-personal-agent/blob/main/docs/decisions/ADR-0007-durable-execution-lifecycle.md) · [Approval + receipt implementation](https://github.com/ReaperXD67/autonomous-personal-agent/blob/main/services/control-api/app/action_store.py) · [CI](https://github.com/ReaperXD67/autonomous-personal-agent/actions/workflows/ci.yml)

<details>
<summary>Agent engineering, stack & honest scope</summary>

Python / FastAPI / PostgreSQL / Redis / Docker. Task, outbox and audit state share a transaction. Owned leases, heartbeats, bounded retries and dead letters recover interrupted work. Exact-action digests bind reviewed content to execution; receipts protect recorded side effects from replay.

Private single-operator dashboard, career workflows and isolated adapters. Career Play can authorize bounded applications within an explicit, expiring scope; manually prepared actions retain exact-action review. External application proof remains pending. The isolated ATS adapter is verified against a local fixture. [Current capability status](https://github.com/ReaperXD67/autonomous-personal-agent#implemented-now) · [Exact-action design](https://github.com/ReaperXD67/autonomous-personal-agent/blob/main/docs/decisions/ADR-0010-exact-external-actions.md) · [MIT license](https://github.com/ReaperXD67/autonomous-personal-agent/blob/main/LICENSE).

</details>

<details open>
<summary><strong>AtlasLM · product + retrieval film · collapse to hide motion</strong></summary>

'''+picture('showcase-atlaslm','AtlasLM, live document intelligence. Its real landing-page capture sits beside authored blue streams of dense and BM25 candidates converging through RRF and reranking. The sufficiency gate precedes generation and citation audit. The illustration explains source behavior; it is not live telemetry.')+'''

</details>

**[AtlasLM](https://github.com/ReaperXD67/notebooklm-rag) · Live.** Hybrid retrieval and evidence gates keep generated answers inspectable; weak evidence can stop an answer.

[Open workspace](https://notebooklm-rag-five.vercel.app/workspace) · [Source](https://github.com/ReaperXD67/notebooklm-rag) · [Retrieval architecture](https://github.com/ReaperXD67/notebooklm-rag/blob/main/docs/RAG_ARCHITECTURE.md) · [Quality gates](https://github.com/ReaperXD67/notebooklm-rag/actions/workflows/quality.yml)

<details>
<summary>AtlasLM engineering, stack & honest scope</summary>

Next.js / TypeScript / Qdrant / Upstash Vector / OpenRouter. Deterministic ingestion, dense + BM25 retrieval, reciprocal-rank fusion, reranking and MMR diversity. Answers expose source passages, citation checks, confidence signals and timed execution traces.

One source workspace at a time. The semantic cache is instance-local; multiple instances would need shared cache state. Qdrant serves the local path and Upstash Vector the serverless deployment. [Architecture and honest scope](https://github.com/ReaperXD67/notebooklm-rag#honest-scope).

</details>

<details open>
<summary><strong>MinePulse / KarixMC · product + trust-boundary film · collapse to hide motion</strong></summary>

'''+picture('showcase-karixmc','MinePulse / KarixMC, live on VPS. A real existing KarixMC interface capture leads a green signed-event bridge from the Paper plugin through API and server-side ledger to the delivery receipt journal. The motion is an illustrative source explanation, not live network telemetry; capture values are part of the recorded image.')+'''

</details>

**[MinePulse / KarixMC](https://github.com/ReaperXD67/MinePulse) · Live on VPS.** Signed game events, server-side rewards and recorded delivery receipts connect play to the web.

[Explore KarixMC](https://karixmc.pl) · [Source](https://github.com/ReaperXD67/MinePulse) · [Paper plugin](https://karixmc.pl/plugin) · [Security boundary](https://github.com/ReaperXD67/MinePulse/blob/main/SECURITY.md) · [Production runbook](https://github.com/ReaperXD67/MinePulse/blob/main/PRODUCTION_RUNBOOK.md)

<details>
<summary>KarixMC engineering, stack & honest scope</summary>

Next.js / Java / Paper / PostgreSQL / Redis / Nginx. Verified playtime, reward ledgers, server stores and a Paper plugin. HMAC-signed events cross the game/API boundary; expiring purchase claims and a plugin-side receipt journal handle acknowledgements. Remembering delivered commands makes recovery safer when an acknowledgement is lost.

Two application replicas behind Nginx, PostgreSQL, Redis and recurring encrypted backups. Campaign-credit purchases are manually confirmed; automated payment checkout is not connected. Deployment is not a claim of customer scale. [Current implementation](https://github.com/ReaperXD67/MinePulse#plugin-api).

</details>

<details>
<summary>Compare the three architectures</summary>

<picture>
  <source media="(max-width: 640px)" srcset="./assets/architecture-atlas-mobile.svg">
  <img src="./assets/architecture-atlas.svg" width="1000" alt="Static comparison of owned agent execution, retrieval fusion and signed game events. These simplified diagrams are explanations; linked implementation is the source of truth.">
</picture>

</details>

## More engineering, different constraints.

<details open>
<summary><strong>Explore the build index · collapse to hide motion</strong></summary>

'''+picture('showcase-build-index','More systems, other constraints: ROLLFORWARD preserves optimistic intent across network failure; Revive explains payment recovery; AtlasForge AI bounds video-production spend. Original animated lines illustrate their different constraints, without live measurements.')+'''

</details>

[**ROLLFORWARD → live**](https://rollforward-engine.onrender.com) · [decisions](https://github.com/ReaperXD67/rollforward-optimistic-engine/blob/main/DECISIONS.md)<br>
[**Revive → live**](https://revive-revenue.vercel.app) · [source](https://github.com/ReaperXD67/revive-ai)<br>
[**AtlasForge AI → source**](https://github.com/ReaperXD67/atlasforge-ai) · [architecture](https://github.com/ReaperXD67/atlasforge-ai/blob/main/ARCHITECTURE.md)

<details>
<summary>Secondary systems, constraints & lower-level explorations</summary>

- **ROLLFORWARD:** separate projected state from confirmed truth; preserve intent in IndexedDB, retry with the same idempotency key and expose `412` conflicts.
- **Revive:** live payment-recovery prototype with deterministic policies, HMAC-verified webhooks and immutable audit records. Its challenge exercises the hosted backend; payment outcomes are demo data, not real charges or measured merchant uplift.
- **AtlasForge AI:** checkpointed video production with provider fallbacks, editorial gates and bounded cloud spend. SQLite and filesystem artifacts deliberately serve one workstation.
- [GPT Prototype](https://github.com/ReaperXD67/GPT-Prototype): a decoder-only transformer built from first principles with RoPE, RMSNorm, QK-Norm and Muon + AdamW.
- [Distributed Search Typeahead](https://github.com/ReaperXD67/distributed-search-typeahead): FastAPI, PostgreSQL, Redis Streams, consistent hashing, batched writes and failure handling.

</details>

## From models to shipped interfaces.

'''+picture('showcase-capabilities','Working stack: AI systems with agents, RAG, evaluation, PyTorch and OpenRouter; applications with Python, TypeScript, Java, FastAPI, Next.js and React; data and delivery with PostgreSQL, Redis, Qdrant, Docker, Linux and Vercel. These are working tools, not ranked proficiency scores.')+'''

<details>
<summary>Full working stack</summary>

**AI:** LLM applications, agent workflows, RAG, hybrid retrieval, evaluation, citations, PyTorch, OpenRouter.<br>
**Application:** Python, TypeScript, FastAPI, Next.js, React, Java, REST APIs, OAuth, signed webhooks.<br>
**Data + delivery:** PostgreSQL, pgvector, Redis, Qdrant, Upstash Vector, Prisma, Docker, Linux, Nginx, GitHub Actions, Vercel, VPS.

</details>

**SIP Organization** · Project Lead Developer Intern · Jul 2026–Present<br>
**micro1** · AI Engineer Intern · Aug 2025–Jul 2026<br>
**Independent AI / ML Developer** · 2025–Present

<details>
<summary>Experience, education & supplied credential</summary>

- **SIP Organization:** AI-powered WhatsApp onboarding, conversational workflows, backend integrations and service delivery.
- **micro1:** worker orchestration and modular cell components for a self-adaptive AI architecture.
- **Independent development:** applied LLM products, automation, APIs and training/inference workflows.

**B.Sc. Computer Science**, Scaler School of Technology with BITS Pilani · Aug 2024–Sep 2028.

Certified Freelance AI / Machine Learning Developer · micro1 · March 11, 2026. [View the supplied certificate](https://aman-kumar-ai-portfolio.vercel.app/assets/micro1-certification.jpg).

</details>

<details>
<summary>Public build activity</summary>

![Aman's rolling public GitHub activity, generated in this repository](./metrics.svg)

Generated daily from public GitHub data. Activity is context, not a substitute for implementation and decisions.

</details>

---

**Have a role or a hard engineering problem?** [Email Aman →](mailto:amankumr3254u@gmail.com)<br>
Open to AI engineering, full-stack roles, internships and contract builds. Bengaluru · any work mode.

[**Portfolio**](https://aman-kumar-ai-portfolio.vercel.app) · [**One-page ATS résumé · PDF**](https://aman-kumar-ai-portfolio.vercel.app/profile/aman-kumar-resume.pdf) · [**LinkedIn**](https://www.linkedin.com/in/aman-kumar-494601329)

<sub>[Static header](./assets/identity-signal-still.png) · [Static mobile header](./assets/identity-signal-mobile-still.png) · [Static project films](./PROFILE_EVIDENCE.md#project-showcase-films) · [Evidence & provenance](./PROFILE_EVIDENCE.md). All project films are illustrative source explanations. Account avatars are unchanged.</sub>
'''
path.write_text((prefix+body+'\n\n'+contributions+'\n').replace('  \n','<br>\n'),encoding='utf8')
print('Composed the complete visual-first profile body.')
