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

## v1.6 — Agent Manual Rewrite

- **Added** `.ai/AGENT_MANUAL.md` — 12-section operating procedure for AI coding agents (D-022).
- **Added** `bin/build_docx.py` — python-docx generator with canonical monochrome styling; generates `DOC/AGENT_MANUAL.docx`.
- **Added** `DOC/AGENT_MANUAL.docx` — generated Word copy from markdown source.
- **Updated** `governance/DECISIONS.md` — added D-022 (Agent Manual Rewrite with Verified STITCH Integration).
- **Content:** mission, token lock, component contract, Pagla Sans typeface, STITCH MCP integration, CSS architecture, workflow, quality gates, anti-patterns, governance, quick reference.

## v1.5 — Pagla Sans Font Integration

- **Added** `fonts/` — Pagla Sans typeface files (TTF + WOFF2) for all weights (Light, Regular, Medium, SemiBold, Bold) plus variable font.
- **Added** `design-system/PAGLA_SANS.md` — complete typeface specification: anatomy, weights, metrics, CSS implementation, usage rules, accessibility.
- **Updated** `css/tokens.css` — added `@font-face` declarations for all Pagla Sans weights with `font-display: swap`.
- **Updated** `design-system/DESIGN_TOKENS.md` — added typeface specification section referencing PAGLA_SANS.md.
- **Font files:** copied from `PaglaAI.space/pagla-sans/fonts/` with SIL OFL license.

## v1.4 — Font Naming and Surface Effects

- **Fixed** `brand/BRAND.md` — normalized "PaglaAI Sans" to "Pagla Sans" (lines 131, 174, 176).
- **Added** `design-system/DESIGN_TOKENS.md` — surface effect tokens (`surface.glass.*`, `surface.clear.*`) and `layout.reading` (`42rem`).
- **Added** `css/tokens.css` — surface effect CSS custom properties and `--layout-reading`.
- **Recorded** the decision as D-021.

## v1.3 — Agent Manual Relocated

- **Added** `.ai/agent-manual/` — the agent operating procedure (D-020).
- **Rewritten** `AGENT_MANUAL.md` — v2.0.0 inherits tokens, components,
  templates, and MCP tools from the authority; removed invented palette,
  fonts, components, and tools.
- **Added** `.ai/agent-manual/build_docx.py` — regenerates a canonical,
  monochrome-styled Word copy; duplicate DOCX artifacts removed.
- **Updated** `.ai/README.md` — registers the agent-manual.
- **Updated** `.gitignore` — excludes generated `.ai/agent-manual/DOC/`.
- **Recorded** the decision as D-020.

## v1.2 — Maturation Pass

- **Added** `design-system/UX_PATTERNS.md` — interaction layer: transitions, scroll rhythm, hover, loading/empty/error, 404, search, theme switching (D-015).
- **Added** `templates/hero.md`, `landing.md`, `product.md`, `docs.md`, `blog.md`, `case-study.md`, `sections.md` — reusable page-level compositions (D-017).
- **Registered** `Breadcrumbs`, `Code Block`, `Terminal` in `COMPONENT_LIBRARY.md`; extended every registry entry with Structure and Behavior (D-016).
- **Added** `wireframes/01-home.md` … `08-404.md` — structural layouts (D-018).
- **Added** `mockups/01-home.md` … `08-404.md` — token-referenced visual specs (D-018).
- **Updated** `design-system/README.md` — lists `UX_PATTERNS.md`.
- **Updated** `components/COMPONENTS.md` — component language extended with the three new components.
- **Recorded** the decisions as D-015, D-016, D-017, D-018, D-019.

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