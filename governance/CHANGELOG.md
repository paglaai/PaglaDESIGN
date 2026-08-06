# CHANGELOG

> *The record of how the design authority came to be.*

---

# Purpose

CHANGELOG is the historical log of meaningful changes to PaglaDESIGN.

It complements `DECISIONS.md`.

- `DECISIONS.md` records the reasoning behind architectural choices.
- `CHANGELOG.md` records when things happened.

---

# Format

Each entry notes the change and its location.

Entries are grouped by phase and ordered newest first within a phase.

---

## v1.1 — Agent Tooling (MCP + RAG)

- **Added** `.ai/` — agent infrastructure (re-added after v0.9 removal, D-014).
- **Added** `.ai/mcp/server.py` — MCP server exposing the design authority to coding agents: `search`, `get_doc`, `list_docs`, `lookup_token`, `search_tokens`, `get_context`.
- **Added** `.ai/mcp/rag.py` — heading-chunked BM25 retrieval over the canonical Markdown + `css/tokens.css`; deterministic, pure-stdlib, no API key.
- **Added** `.ai/mcp/run.cmd` — Windows launcher resolving the shared PaglaAI venv.
- **Added** `.opencode/opencode.json` — registers `pagladesign` as a local MCP server.
- **Recorded** the decision as D-014 (agent tooling returns `.ai/`).

## v1.0 — Reference CSS Implementation

- **Added** `css/tokens.css` — canonical token layer; every locked value from `DESIGN_TOKENS.md` as CSS custom properties on `:root` (light) and `[data-theme="dark"]`.
- **Added** `css/base.css` — reset, element defaults, typography, focus states, reduced motion, responsive type scaling.
- **Added** `css/utilities.css` — single-purpose, token-driven helpers.
- **Updated** `css/README.md` — states these are reference implementation; consumers import or graft from here.
- **Recorded** the decision as D-013 (design authority owns canonical tokens; frameworks live in consumer repos).

## v0.9 — Repository Structure Refinement

- **Renamed** `docs/` → `governance/` — decisions, roadmap, changelog, documentation style (project governance, not documentation).
- **Renamed** `website/` → `site/`.
- **Moved** `SITEMAP.md`, `USER_JOURNEYS.md`, `CONTENT_STRATEGY.md` from `governance/` to `site/`.
- **Added** `templates/` — reusable page-level compositions.
- **Added** `references/` — visual research library (non-canonical).
- **Removed** `.ai/` — no agent-specific content yet.
- **Declared** the repository structure stable (D-012).

## v0.8 — Repository Reorganization

- **Reorganized** the repository into a canonical folder structure per `VISION.md`: `brand/`, `design-system/`, `components/`, `docs/`, `css/`, `mockups/`, `wireframes/`, `website/`, `.ai/`.
- **Moved** brand docs (`BRAND.md`, `BRANDKIT.md`) into `brand/`.
- **Moved** design values (`DESIGN_TOKENS.md`, `COLOR_SYSTEM.md`, `TYPOGRAPHY.md`, `MOTION.md`, `ACCESSIBILITY.md`, `ICONS.md`, `CSS_ARCHITECTURE.md`) into `design-system/`.
- **Moved** component docs (`COMPONENTS.md`, `COMPONENT_LIBRARY.md`) into `components/`.
- **Moved** structural docs (`DECISIONS.md`, `ROADMAP.md`, `CHANGELOG.md`, `SITEMAP.md`, `USER_JOURNEYS.md`, `CONTENT_STRATEGY.md`, `DOCUMENTATION_STYLE.md`) into `docs/`.
- **Added** index READMEs to each folder.
- **Updated** internal references to resolve relative to each file's location.
- **Recorded** the decision as D-011.

## v0.7 — Brand & Identity Pack

- **Added** `BRANDKIT.md` — the canonical brand identity pack sourcing from `BRAND.md` and `DESIGN_TOKENS.md`.
- **Added** `brand/` — registered canonical assets: Pagla Face (black/white), wordmark, mark, display picture.
- **Updated** `BRAND.md` — added the Brand Assets registry.

## v0.6 — Token Lock

- **Updated** `DESIGN_TOKENS.md` — all literal values locked: spacing, typography, color (light + dark), accent, state, UI, motion, breakpoints, layout.

## v0.5 — Component Registry

- **Added** `COMPONENT_LIBRARY.md` — registry of shared components, lifecycle, ownership, and quality gate.

## v0.4 — Implementation Reference

- **Added** `CSS_ARCHITECTURE.md` — layer model, tokens-as-properties, theming, and class naming.
- **Added** `ICONS.md` — icon language, grid, naming, and usage rules.
- **Added** `DOCUMENTATION_STYLE.md` — documentation structure, code, and navigation.

## v0.3 — Cognitive Layer

- **Added** `COMPONENTS.md` — component language, anatomy, shared states, and registry rules.
- **Added** `MOTION.md` — motion philosophy, gates, durations, and reduced motion.
- **Added** `ACCESSIBILITY.md` — mandatory baseline, foundations, and testing gates.

## v0.2 — Design System Core

- **Added** `DECISIONS.md` — architectural history (D-001 → D-009) and governing decision format.
- **Added** `DESIGN_TOKENS.md` — value layer; naming convention, spacing, typography, color, UI, and theme tokens.
- **Added** `ROADMAP.md` — Now / Next / Later phases and the Design System Core index.
- **Updated** `TYPOGRAPHY.md` — primary typeface set to PaglaAI Sans.
- **Added** `BRAND.md` — consolidated identity, mark, brand voice, usage, and AYNAGHOR back-matter.

## Phase 0 — Foundation

- **Added** `README.md` — repository purpose and structure.
- **Added** `VISION.md` — why PaglaAI exists.
- **Added** `DESIGN.md` — design philosophy and pillars.
- **Added** `PRINCIPLES.md` — standing principles of the system.
- **Added** `AGENTS.md` — contribution workflow and repository facts.
- **Added** `SITEMAP.md` — information architecture.
- **Added** `USER_JOURNEYS.md` — experience layer.
- **Added** `CONTENT_STRATEGY.md` — content and writing direction.
- **Added** `COLOR_SYSTEM.md` — color semantics.

---

## Working Notes (not yet versioned)

- `LICENSE` — MIT, © 2026 AYNAGHOR.
- `.gitattributes` — LF normalization kept.