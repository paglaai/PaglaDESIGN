# ROADMAP

> *The system is never finished. It is cared for.*

---

# Purpose

ROADMAP describes the direction of PaglaDESIGN — where the design system stands today and where it is heading.

It is a living document.

It is updated as the ecosystem grows, not frozen.

---

# Principles of the Roadmap

- One meaningful, versionable artifact per step.
- Philosophy before values. Values before code.
- Every step strengthens the system, not just a single page.
- Accessibility and documentation are never deferred.
- The system is built for decades, not releases.

---

# Audit v2.0 — Canonical Roadmap

> Source: [`paglaai/pagladesign#3`](https://github.com/paglaai/pagladesign/issues/3) — PaglaAI Ecosystem Audit v2.0  
> Registry: [`ecosystem.json`](../ecosystem.json) · Schema: [`ecosystem.schema.json`](../ecosystem.schema.json)  
> Authority: **PaglaDESIGN** is the single source of truth. All ecosystem products inherit from it.

Objectives (P0):

- Establish PaglaDESIGN as the single source of truth.
- Create ecosystem registry (`ecosystem.json`).
- Unify documentation across PaglaDESIGN, PaglaAI.space and paglaai-docs via the Audience Renderer contract.
- Design GitHub → Cloudflare CI/CD pipeline (`design.updated` event).
- Prepare SANCTUM Runtime public architecture repository.

Renderer contract: `design-system/RENDERER_API.md` · Spec: `governance/AUDIENCE_RENDERER_SPEC.md`  
Renderers: `FERN_RENDERER.md` (human) · `MACHINE_RENDERER.md` (machine) · `ARCHITECT_RENDERER.md` (architect)

---

# Phase 1 — PaglaDESIGN v2.0 Foundation (Active)

Status: **Active** · Decision: D-023

- PaglaDESIGN v2.0 documentation — `RENDERER_API.md`, `AUDIENCE_RENDERER_SPEC.md`, `FERN/MACHINE/ARCHITECT_RENDERER.md`.
- Human / Machine / Architect modes — every doc page declares `audience: [human|machine|architect]` (RENDERER_API.md#validation-rules); frontmatter `title` + `audience` required, `version`/`status`/`dependencies`/`schema` optional; consumers route by audience and skip pages with missing/invalid frontmatter.
- Ecosystem registry — `ecosystem.json` (16 entries, 9 active · 7 planned) + `ecosystem.schema.json` — authority `paglaai/pagladesign`, first consumer `paglaai.space` (Cloudflare Pages), unified-docs target `paglaai-docs`, planned `sanctum` runtime.

Foundation already in place:

- Constitutional layer — `VISION.md`, `DESIGN.md`, `PRINCIPLES.md`, `DECISIONS.md`
- Semantics layer — `TYPOGRAPHY.md`, `COLOR_SYSTEM.md`, `BRAND.md`, `DESIGN_TOKENS.md`
- Experience layer — `SITEMAP.md`, `USER_JOURNEYS.md`, `CONTENT_STRATEGY.md`, `NAVIGATION.md`
- Foundation layer — `COMPONENTS.md`, `MOTION.md`, `ACCESSIBILITY.md`, `UX_PATTERNS.md`
- Implementation reference — `CSS_ARCHITECTURE.md`, `ICONS.md`, `DOCUMENTATION_STYLE.md`, `COMPONENT_LIBRARY.md`
- Composition layer — `templates/` (hero, landing, product, docs, blog, case-study, sections)
- Artifacts — `wireframes/` and `mockups/` (8 pages, token-referenced)
- Research — `references/` captures + `INSPIRATION.md`
- Agent infrastructure — `.ai/mcp/` (MCP server + BM25 RAG), `.ai/AGENT_MANUAL.md` (D-022), `css/tokens.css` locked (D-010, D-013)

---

# Phase 2 — SANCTUM + Shell + B3K4R (Planned)

Status: **Planned** — triggers after Phase 1 `ecosystem.json` lands and frontmatter adoption begins.

- SANCTUM Runtime repository — public architecture repo at `paglaai/sanctum`, consumes `ARCHITECT` renderer (RFC/ADR, governance, audit UI). Registry entry `planned` → `active` on repo creation.
- PaglaSHELL CLI roadmap — `PaglaSHELL` (`paglaai/PaglaSHELL`) as the AI-native execution kernel; inherits `css/tokens.css`, documents CLI interaction patterns in `design-system/UX_PATTERNS.md`.
- B3K4R MVP documentation — `B3K4R` (`paglaai/B3K4R`) as first application consumer; docs rendered via `FERN` (human) with `MACHINE` prompt bundles for agent tooling.

---

# Phase 3 — Automation & Release (Planned)

Status: **Planned** — depends on Phase 1 pipelines spec in `ecosystem.json`.

- GitHub Actions automation — `validate-design-system` (build-tokens) + `validate-ecosystem` (ecosystem.json against schema) + `validate-frontmatter` (RENDERER_API contract) on `push: main` and `pull_request`.
- Cloudflare Pages deployment — PaglaDESIGN preview (mirrors `paglaai.space` `deploy.yml`), `paglaai-docs` unified docs via `FERN`; Pages project per registry `pipelines.githubToCloudflare`.
- Release workflow for PaglaOS ecosystem — `release.yml` publishes `pagladesign-assets.tar.gz` + `ecosystem.json` + `css/tokens.css` via `softprops/action-gh-release@v2` on `release: published` / `workflow_dispatch`.
- `design.updated` event pipeline — `repository_dispatch` from PaglaDESIGN to `paglaai.space`, `paglaai-docs`, `sanctum` to trigger downstream rebuilds; idempotent renderer output required (`RENDERER_API.md#idempotency-requirement`).

---

# Now / Next / Later (Legacy — superseded by phases above)

Now = Phase 1 active. Next = Phase 2. Later = Phase 3 + maturing governance for every ecosystem product.

---

# Design System Core

These documents form the stable foundation this repo rests on:

| Document | Role |
| --- | --- |
| `VISION.md` | Why PaglaAI exists |
| `DESIGN.md` | Design philosophy and pillars |
| `PRINCIPLES.md` | Standing principles of the system |
| `DECISIONS.md` | Architectural history |
| `TYPOGRAPHY.md` | Typography philosophy and hierarchy |
| `COLOR_SYSTEM.md` | Color semantics |
| `BRAND.md` | Identity, mark, brand usage |
| `DESIGN_TOKENS.md` | Concrete implementation values |

---

# Governance

Nothing in this roadmap is executed alone.

Every change follows the workflow:

Understand → Research → Document → Design → Review → Implement → Refine → Document.

---

# Final Principle

The roadmap is a compass, not a contract.

What matters is the direction — toward a single, lasting, and unifying design system for every PaglaAI product.