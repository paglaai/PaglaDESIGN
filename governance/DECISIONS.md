# DECISIONS

> *Every decision in this document is a binding architectural decision. It records what was changed, why, and what it cost.*

---

# Purpose

DECISIONS is the long-term architectural record of the PaglaAI design system.

It exists so that future contributors never rediscover a decision by accident, never silently reverse a direction, and always understand the reasoning behind the system they are working within.

This document is intended to last as long as the ecosystem.

Read it as history, not as instruction.

---

# Format

Each entry records:

- **Context** — the problem being solved
- **Decision** — what was chosen
- **Alternatives** — what was considered and rejected
- **Trade-offs** — what was gained and what was given up
- **Result** — the impact on the system

---

# D-001 · Design First, Documentation Second, Implementation Last

**Status:** Adopted

**Context**

The repository was created with the risk of becoming a collection of pages rather than a system. Code, if begun too early, would define the design instead of the other way around.

**Decision**

Never begin by writing code.

Begin by understanding the problem, then research, then document, then design, then review, then implement.

Documentation is part of every deliverable.

**Alternatives considered**

- Prototype-first, where interaction precedes documentation.
- Document-only, with no implementation lifecycle.

**Trade-offs**

Rejected rapid prototyping as a starting point to protect consistency. Accepted a slower initial velocity in exchange for a design system that can scale.

**Result**

The repository is structured as an authority, not a website.

---

# D-002 · Typography as the Primary Interface

**Context:** The visual language needed a single foundation that could carry hierarchy without decoration.

**Decision**

Typography is the primary interface of the PaglaAI ecosystem.

Hierarchy is communicated through scale, weight, and spacing before color or ornamentation.

**Alternatives**

- Color-led hierarchy.
- Decorative, illustration-led identity.

**Trade-offs**

Typography-led design requires rigorous type discipline and generous whitespace. The payoff is calm, readable, timeless interfaces.

**Note:** Philosophy and values are documented in `TYPOGRAPHY.md`. Concrete scales live in `DESIGN_TOKENS.md`.

---

# D-003 · PaglaAI Sans as the Primary Typeface

**Context:** The identity needed a typeface that was readable, neutral, and unpretentious. It also needed to feel unmistakably PaglaAI, not like another product's font.

**Decision**

The primary typeface is PaglaAI Sans, an open, light, neutral family built for clarity.

**Alternatives considered**

- A system default.
- A heavy, characterful display face (explicitly rejected for being bold, chunky, and playful).

**Trade-offs**

A neutral sans is less visually distinctive on its own, so the mark and voice must carry the personality.

**Outcome**

Typography stays calm; the Pagla Face carries the brand.

---

# D-004 · Monochrome First

**Context:** Modern systems often lean on color for identity.

**Decision**

The primary visual identity is monochrome.

Most interfaces should communicate in neutrals alone.

Color is reserved for meaning, state, and focus, never decoration.

**Alternatives:** a bright limited palette as the identity; a gradient-led identity.

**Trade-off made:** A monochrome system is quieter and more timeless, but relies on strong type and spacing to function.

**Outcome:** Monochrome is the default wherever meaning does not demand color.

---

# D-005 · Philosophy Independent from Implementation Values

**Context:** Setting concrete pixel and hex values prematurely fixes the system before its philosophy is fully defined.

**Decision**

Philosophy and semantics live in documents like `TYPOGRAPHY.md`, `COLOR_SYSTEM.md`, and `BRAND.md`.

Concrete implementation values live only in `DESIGN_TOKENS.md`.

Philosophy first. Values later.

**Alternatives:** a bright default ramp of neutral values (Gray-50–Gray-900) and a full scale, defined up front.

**Trade-off:** deferred implementation detail slows early prototyping but avoids rewriting the philosophy for each palette change.

**Benefit:** the design language evolves without invalidating its documents.

---

# D-006 · The Pagla Face as the Primary Mark

**Context:** The system needed a mark that was unmistakably human and unmistakably PaglaAI, not a derivative of another brand's symbol.

**Decision:** The Pagla Face — a single-weight, black-ink-only mark with messy genius hair, calm sunglasses, and a precise goatee.

**Alternatives:** a blossom/flower symbol (rejected as derivative); a geometric abstract mark (rejected for lacking humanity).

**Trade-offs:** a face mark carries more personality and less decorative neutrality. It demands careful, clearspace discipline.

**Result:** a mark that is quiet, precise, and slightly off — by design.

---

# D-007 | The Name Speaks for Itself

**Context:** There was pressure to define what "Pagla" means in the documentation.

**Decision:** Define nothing. Let the work itself teach the meaning.

**Trade-off:** some onboarding ambiguity in exchange for honesty of the lived experience.

---

# D-008 | Editorial Restraint over Decoration

**Context:** The instinct in most design systems is to decorate.

**Decision:** Whitespace is intentional. Content before decoration. Every element must earn its place. No trend-driven UI, no unnecessary animation.

**Documented in:** `DESIGN.md`, `PRINCIPLES.md`, `BRAND.md`.

---

# D-009 | Single Canonical Identity (Aggregated)

**Decision**

The brand authority is a single document.

Do not maintain multiple brandkit, brand-system, and brand-guideline copies scattered across the ecosystem.

Consolidate the strongest ideas once, in `BRAND.md`, and remove duplicates.

**Alternatives:** keep separate brandkit files per product.

**Outcome:** Locally scattered brand attempts (at least one pair byte-identical) are no longer part of the repository. The canonical identity lives once, in `BRAND.md`.

---

# D-010 · Locking the Token Values

**Context:** The philosophy and semantics layers were complete. Until now, literal values were deliberately deferred (`D-005`) so the design language could settle before implementation numbers were fixed.

**Decision**

Lock the token values in `DESIGN_TOKENS.md`:

- `rem`-based sizing so the system respects user zoom.
- Monochrome-first neutrals (`#0A0A0B` ink / `#FFFFFF` paper) as the identity requires.
- A single accent family led by `#6B7EFF` — reserved for meaning, never a background fill.
- Light and dark themes share one semantic structure; only values change between them.
- Spacing on the `0.25rem` base unit.

**Alternatives considered**

- Keeping values deferred indefinitely.
- Defining a broader, brighter palette before the identity was final.

**Trade-offs**

Locking commits the system to these numbers. It also lets every product implement from one source without inventing values.

**Result**

`DESIGN_TOKENS.md` is now the binding source of values. Future changes go through the documented decision workflow.

---

# D-011 · Canonical Repository Layout

**Context:** The vision recommended a nested, discoverable layout, but content had accreted as flat files at the repository root. Several documents crossed the whole ecosystem (`BRAND.md`, `DESIGN_TOKENS.md`, `COMPONENTS.md`, `DECISIONS.md`) and were hard for contributors and automation to locate.

**Decision**

Reorganize the repository into a canonical folder structure without changing file contents:

- `brand/` — identity, mark, brand usage, brandkit, assets
- `design-system/` — tokens, color, typography, motion, accessibility, icons, css architecture
- `components/` — component language and registry
- `governance/` — decisions, roadmap, changelog, documentation style
- `site/` — sitemap, user journeys, content strategy (the website the system serves)
- `templates/` — reusable page-level compositions
- `references/` — visual research library (non-canonical)
- `css/`, `mockups/`, `wireframes/` — supporting artifact folders with index READMEs
- Constitution files (`README.md`, `VISION.md`, `DESIGN.md`, `PRINCIPLES.md`, `AGENTS.md`, `LICENSE`) stay at the root

Internal references were updated to relative paths; no content was altered.

**Alternatives considered**

- Keeping the flat layout to avoid churn.
- Moving the constitution files into `governance/` as well.

**Trade-offs**

Rewriting commit paths causes one coordinated migration. It is done once and improves discoverability and automation. Keeping the constitution at the root preserves on-boarding clarity.

**Result**

The repository now matches the vision's intended structure. Cross-document references resolve relative to each file's location, and each directory carries an index README. The layout was refined by D-012 and is now declared stable.

---

# D-012 · Repository Structure Declared Stable

**Context:** The reorganization (D-011) settled the folder layout. The repository is the canonical design authority, and continued structural churn would erode contributor trust and automation stability.

**Decision**

Declare the repository structure stable:

- No further moving or renaming of top-level folders.
- `docs/` was renamed to `governance/`, and `website/` to `site/`; `templates/` and `references/` were added; `.ai/` was removed until there is real agent-specific content.
- All future contributions fit into the existing structure: `brand/`, `components/`, `design-system/`, `governance/`, `site/`, `templates/`, `references/`, `css/`, `mockups/`, `wireframes/`.

**Alternatives considered**

- Continuing to refine the hierarchy for marginal naming improvements.
- Keeping `.ai/` as an empty placeholder.

**Trade-offs**

Stability outranks perfection. The cost of restructuring now outweighs its benefit; the system matures through real use rather than further reorganization.

**Result**

The structure is the contract. New content lands in an existing folder, or a documented decision creates a new one.

---

# D-013 · The Design Authority Owns Canonical Tokens; Frameworks Live in Consumers

**Context:** With `DESIGN_TOKENS.md` locked (D-010) and the ecosystem about to
produce real surfaces (`PaglaAI.space`, product front-ends), the system had to
decide how implementation is shared. Re-typing token values in every consumer
risks drift; shipping a whole UI framework here risks a second, competing
implementation and maintenance burden.

**Decision**

PaglaDESIGN ships the **token + base + utilities** CSS layers as a reference
implementation in `css/`:

- `css/tokens.css` — the canonical translation of `DESIGN_TOKENS.md` into CSS
  custom properties (`:root` + `[data-theme="dark"]`).
- `css/base.css` — element defaults, typography, focus, reduced motion.
- `css/utilities.css` — single-purpose, token-driven helpers.

These are marked **reference**, not a shipped UI kit. No UI framework, component
package, or rendered HTML surface (including a `brandkit.html`) lives in this
repository. Frameworks and rendered surfaces belong to their consumer repos
(e.g. `PaglaAI.space`, PaglaROUTER portal), which inherit from these tokens.

**Alternatives considered**

- Docs-only: keep `css/` empty and let each consumer re-type values. Rejected —
  removes the single source of truth for actual values.
- Ship a full component framework (React/Vue, build, tests). Rejected — creates
  a second, competing implementation and a maintenance burden.
- Publish the reference as a reusable package. Deferred — the ecosystem has no
  package registry need yet.

**Trade-offs:** the system gains one authoritative `tokens.css`, at the cost of
maintaining base/utilities here as living reference. Frameworks stay in
products, preserving the design-first authority relationship.

**Result:** `PaglaAI.space` and future products consume `css/tokens.css` instead
of re-inventing token values. The authority relationship is enforced by
construction.

---

# D-014 · Agent Tooling (MCP + RAG) Returns `.ai/`

**Context:** D-012 removed `.ai/` because it held no real content, reasoning it
would return "when there is real agent-specific content." The ecosystem now
needs coding agents (opencode, Claude Code, Cursor, PaglaAI launcher CLIs) to
ground UI work in the canonical design system instead of guessing token values
or re-reading the whole repository.

**Decision**

Re-introduce `.ai/` as **agent infrastructure**, specifically a Model Context
Protocol (MCP) server with dependency-free RAG retrieval:

- `.ai/mcp/server.py` — MCP server (`MCPServer`, MCP SDK 2.x) over stdio,
  registering `search`, `get_doc`, `list_docs`, `lookup_token`,
  `search_tokens`, and `get_context` tools.
- `.ai/mcp/rag.py` — heading-chunked BM25 retrieval over `**/*.md` and
  `css/tokens.css`. Deterministic, pure-stdlib, no model, no network, no API
  key — matching the zero-cost, open-source ethos.
- Registered as a local MCP server in `.opencode/opencode.json`.

`.ai/` is excluded from the RAG index so agent tooling never retrieves itself.

**Alternatives considered**

- Keep `.ai/` removed and rely on coding agents reading files manually.
  Rejected — agents cannot afford to load the whole authority in context, and
  guessing token values drifts from the truth.
- Ship a hosted/embedding RAG pipeline. Deferred — adds cost and a network and
  API-key dependency for no retrieval-quality win at this scale (a design
  authority is lexical by nature).
- Build agent tooling outside this repo. Rejected — it is intrinsic to the
  authority; the design system and its tooling belong together.

**Trade-offs:** retrieval is lexical (BM25) and deterministic, so it may miss
paraphrased queries that an embedding model would catch; the system is
embeddings-ready if a future decision wants semantic retrieval. A maintenance
surface (the MCP server + indexer) is added to the repo.

**Result:** coding agents can ground UI work in the canonical design authority,
values are looked up exactly from `css/tokens.css`, and `.ai/` has real,
versioned content.

---

# D-015 · Interaction Patterns Added

**Status:** Adopted

**Context:** `MOTION.md` and `ACCESSIBILITY.md` set principles, but the system
had no document for *reusable interaction behaviors* — transitions, scroll
rhythm, hover, loading, empty, error, not-found, search, and theme switching.
Without it, each consumer (starting with `PaglaAI.space`) would invent
behaviors per product.

**Decision**

Add `design-system/UX_PATTERNS.md` as the interaction layer of the system.

Patterns are token-referenced, pass the gates of `MOTION.md`, and meet the
baseline of `ACCESSIBILITY.md`. Theme switching defaults to the OS preference,
persists an explicit choice, and resolves both themes through one semantic
structure (D-010).

**Alternatives considered**

- Leave behavior to each product. Rejected — recreates the drift the system
  exists to prevent.
- Fold behaviors into `COMPONENTS.md`. Rejected — that document is the grammar
  of parts, not the behavior of states.

**Trade-offs:** one more document to maintain, in exchange for interaction
that is defined once and inherited everywhere.

**Result:** interaction is a first-class layer of the design system, and the
site build has a behavior contract to implement.

---

# D-016 · Component Library Deepened and Extended

**Context:** The registry listed eleven components with terse entries. The site
build needs three shared parts not yet registered — code presentation, CLI
output, and navigation context — and the existing entries lacked the anatomy
and behavior needed to build them consistently.

**Decision**

Register **Breadcrumbs**, **Code Block**, and **Terminal** as library
components, and extend every registry entry with **Structure** and
**Behavior**. The language is documented in `COMPONENTS.md`; the registry in
`COMPONENT_LIBRARY.md`.

- Code Block — readable, copyable code presentation at `font.size.code`
- Terminal — faithful CLI output; real output, never implied capability
- Breadcrumbs — a trail ending in the current page as text, never a link

**Alternatives considered**

- Model Terminal as a Code Block variant. Rejected — Terminal presents
  *execution*, Code Block presents *source*; distinct roles, distinct states.
- Keep the registry terse. Rejected — depth is what the build consumes.

**Trade-offs:** a longer registry, in exchange for contracts clear enough to
implement from.

**Result:** fourteen registered components, each with anatomy and behavior.

---

# D-017 · Template Compositions Matured

**Context:** `templates/` existed as a concept (a README) with no content. The
wireframes referenced compositions that did not exist yet.

**Decision**

Author the reusable page-level compositions in `templates/`:

- `hero.md` — opening composition with variants
- `landing.md` — the progressive home arc
- `product.md` — the consistent product spine
- `docs.md` — the learning-path layout
- `blog.md` — index and article
- `case-study.md` — problem → decision → outcome
- `sections.md` — Feature Grid, CTA, Timeline, Footer

Templates compose components; they are not components themselves.

**Alternatives considered**

- Leave templates conceptual until a product exists. Rejected — the build needs
  the contract now.
- Duplicate page recipes inside consumer repos. Rejected — that recreates
  per-product divergence.

**Trade-offs:** a maintenance surface, in exchange for page-level consistency
across every product surface.

**Result:** the composition layer is documented before the first site is built.

---

# D-018 · Wireframes and Mockups as Token-Referenced Markdown

**Context:** `wireframes/` and `mockups/` each held only a README. The
ecosystem has no image tooling, and static exports (Figma images, PNGs) would
drift from the locked tokens the moment a value changes.

**Decision**

Produce the maturation artifacts as maintainable Markdown:

- **Wireframes** — structural: regions, order, and component placement, in
  ASCII layout plus a region table.
- **Mockups** — high-fidelity in words: surface maps, typography tokens,
  spacing rhythm, and dark-theme treatment, every value token-referenced.

Eight pages are covered: Home, Product, Docs, API Reference, BrandKit, Blog,
About, 404.

**Alternatives considered**

- Static image mockups. Rejected — they rot the instant a token changes.
- Code-only mockups. Rejected — that begins implementation before design
  (D-001).

**Trade-offs:** Markdown mockups are not pixel-perfect; they track tokens
exactly and never drift.

**Result:** the site build has an exact, reviewable visual contract, and the
folders are no longer placeholders.

---

# D-019 · PaglaAI.space as the First Consumer Surface

**Context:** D-013 declared that frameworks and rendered surfaces belong to
consumer repos, which inherit `css/tokens.css`. The ecosystem's first consumer
surface is `PaglaAI.space`, and its stack and theming had to be decided.

**Decision**

Build `PaglaAI.space` as a plain HTML/CSS/JS site:

- Imports `css/tokens.css`, `css/base.css`, and `css/utilities.css` from
  PaglaDESIGN (D-013).
- White theme is the default; a dark theme re-resolves the same semantics
  through `[data-theme="dark"]`.
- Theme choice defaults to `prefers-color-scheme`, persists an explicit toggle
  to `localStorage`, and honors reduced motion.
- Minimal vanilla JavaScript — shared header/footer include, theme toggle,
  mobile menu, tabs, copy buttons. No framework, no build step.

**Alternatives considered**

- A static site generator. Deferred — adds a build step for no current need.
- A framework (React/Vue). Rejected — contradicts the D-013 authority
  relationship and adds weight.
- Docs-only page. Rejected — the ecosystem needs a real, designed surface.

**Trade-offs:** a small manual-include pattern for shared chrome, in exchange
for a zero-dependency site grounded in the canonical tokens.

**Result:** the first consumer surface inherits the authority by construction;
wireframes and mockups (D-018) are its build reference.

---

# D-020 · Agent Manual Relocated into the Authority as Operating Procedure

**Status:** Adopted

**Context:** A previously authored "PaglaOS × Stitch × PaglaDESIGN Agent
Operating Manual" (v1.0.0) lived in `PaglaAI.space/Agent-Manual/` and
**defined** the system rather than inheriting it — it carried its own palette
(`#FF3E00`, `#0A0A0A`, gradients), its own fonts (Inter, JetBrains Mono, Plus
Jakarta Sans), invented components (Badge, Avatar, Dropdown, Tooltip), a
fabricated lint CLI, and fabricated MCP tools. These conflicted with the
canonical tokens (D-010), components, and tooling (D-014). Its DOCX build
script pointed at paths that did not exist and used non-canonical styling.

**Decision**

- Relocate the manual into the authority: `.ai/agent-manual/`.
- Rewrite it as **operating procedure only**: token/component/layout/tool
  facts are inherited from canonical sources, never redefined here.
- Keep the genuine value-add: the prompt formula, lint severity model, build
  playbook, and anti-patterns.
- Document STITCH as an **external, optional** generator — never an authority.
- Fix `build_docx.py` (correct paths, canonical monochrome styling, UTF-8
  output) and regenerate the Word copy; remove duplicate DOCX artifacts.

**Alternatives considered**

- Keep the manual in `PaglaAI.space`. Rejected — it would continue to drift
  from the authority it claims to implement.
- Patch v1.0.0 in place. Rejected — its defining sections (tokens,
  components, grid, tools) were structurally wrong; replacement, not patching,
  was required.

**Trade-offs:** the manual shrinks from ~11,000 words of duplicated definition
to ~19,000 characters of procedure. It can no longer drift because it no
longer carries values.

**Result:** the manual and its authority live in one repository. `.ai/`
now holds real, versioned agent content beyond the MCP server, and the
previous competing definition is gone.

---

# Document-the-Decision Rule

If a change significantly affects the design system, document it here before implementing — describe what changed, why, the alternatives, trade-offs, and the intended benefit.

Do not make silent architectural decisions.

---

# Final Principle

A system that records why it exists is a system that can outlast its founders.

If a decision cannot be explained, it should be reconsidered.