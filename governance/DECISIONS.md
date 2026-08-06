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

# Document-the-Decision Rule

If a change significantly affects the design system, document it here before implementing — describe what changed, why, the alternatives, trade-offs, and the intended benefit.

Do not make silent architectural decisions.

---

# Final Principle

A system that records why it exists is a system that can outlast its founders.

If a decision cannot be explained, it should be reconsidered.