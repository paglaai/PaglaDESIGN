# PaglaDESIGN

> The canonical design system, BrandKit, and user experience foundation for the entire PaglaAI ecosystem.

---

## What is PaglaDESIGN?

PaglaDESIGN is the central design authority for every product developed under the **PaglaAI** ecosystem.

It is not simply a website project.

It is the single source of truth for the visual language, user experience, interaction patterns, documentation standards, branding, and design philosophy shared across all current and future PaglaAI products.

PaglaDESIGN v2 introduces the Audience Renderer architecture: every doc page declares its intended audience through a standard metadata contract, and three canonical renderers — FERN (human), MACHINE (machine), and ARCHITECT (governance) — produce consistent output for every consumer surface.

Everything visual begins here.

---

## Purpose

The purpose of this repository is to ensure every PaglaAI product shares a consistent identity.

Rather than designing each project independently, PaglaDESIGN defines a reusable system that every application can inherit.

This repository governs:

- Brand Identity
- Website Design
- User Experience (UX)
- User Interface (UI)
- Design System
- CSS Architecture
- Typography
- Icons
- Motion
- Accessibility
- Documentation Style
- Component Library
- Product Layouts

---

## Ecosystem

PaglaDESIGN is the **single source of truth** for the PaglaAI ecosystem (Audit v2.0 — [`paglaai/pagladesign#3`](https://github.com/paglaai/pagladesign/issues/3)).

The machine-readable registry is [`ecosystem.json`](./ecosystem.json) (schema [`ecosystem.schema.json`](./ecosystem.schema.json)) — 16 entries, 9 active · 7 planned.

| Product | Repo | Role | Status | Audience |
|---|---|---|---|---|
| **PaglaDESIGN** | `paglaai/pagladesign` | authority | active | human · machine · architect |
| **PaglaAI.space** | `paglaai/paglaai.space` | surface | active | human |
| **paglaai-docs** | `paglaai/paglaai-docs` | surface | active | human · machine · architect |
| **SANCTUM Runtime** | `paglaai/sanctum` | runtime | planned | architect |
| **PaglaSHELL** | `paglaai/PaglaSHELL` | product | active | human · machine |
| **B3K4R** | `paglaai/B3K4R` | product | active | human |
| **PaglaMLX** | `paglaai/PaglaMLX` | product | active | human · machine |
| **PaglaROUTER** | `paglaai/PaglaROUTER` | product | active | human · machine |
| **PaglaCHAT** | `paglaai/PaglaCHAT` | product | active | human |
| **PaglaOS** | `paglaai/KolponaOS` | product | active | human · architect |
| **PaglaAPI** | `paglaai/paglaapi` | product | planned | machine |
| **PaglaCPP** | `paglaai/paglacpp` | product | planned | machine · architect |
| **PaglaMTP** | `paglaai/paglamtp` | product | planned | machine |
| **PaglaUI** | `paglaai/paglaui` | product | planned | human · machine |
| **PaglaBRAND** | `paglaai/paglabrand` | product | planned | human |
| **PaglaGPT** | `paglaai/paglagpt` | product | planned | human · machine |

> `PaglaAI.space` is the first consumer surface — it inherits `css/tokens.css` (D-013) and renders via the `FERN` (human) renderer. `paglaai-docs` is the unified-docs target and `SANCTUM` is the public architecture repo (Phase 2). Every doc page declares its audience via `design-system/RENDERER_API.md`.

Future products should inherit the same visual language and interaction principles defined here.

---

## Design Philosophy

The design language of PaglaAI follows a few simple principles:

- Editorial over decorative
- Simplicity over complexity
- Typography over ornamentation
- Consistency over novelty
- Performance over visual excess
- Accessibility by default
- Timeless over trendy

The goal is not to create a fashionable interface.

The goal is to build a design language that remains useful and recognizable for years.

---

## Repository Structure

```
PaglaDESIGN/

README.md          — repository purpose and structure (index)
VISION.md          — why PaglaAI exists
DESIGN.md          — design philosophy and pillars
PRINCIPLES.md      — standing principles of the system
AGENTS.md          — contribution workflow and repository facts
LICENSE            — MIT license

ecosystem.json     — canonical registry of the PaglaAI ecosystem (Audit v2.0, D-023)
ecosystem.schema.json — JSON Schema for the registry

brand/             — identity, mark, and brand usage
  BRAND.md         — identity, mark, and brand usage
  BRANDKIT.md      — portable identity pack

components/        — component language and registry
  COMPONENTS.md    — component language and rules
  COMPONENT_LIBRARY.md — component registry

design-system/     — implementation-ready design values
  DESIGN_TOKENS.md — concrete implementation values (locked)
  COLOR_SYSTEM.md  — color semantics
  TYPOGRAPHY.md    — typography philosophy and hierarchy
  PAGLA_SANS.md    — Pagla Sans typeface specification
  MOTION.md        — motion principles
  ACCESSIBILITY.md — accessibility requirements
  ICONS.md         — icon language
  CSS_ARCHITECTURE.md — CSS implementation guidance
  RENDERER_API.md  — metadata contract for every documentation page
  FERN_RENDERER.md — human-facing HTML renderer specification
  MACHINE_RENDERER.md — JSON, OpenAPI, MCP, and prompt bundle renderer
  ARCHITECT_RENDERER.md — RFC, ADR, governance, and audit UI renderer

governance/        — project governance of the design system
  DECISIONS.md     — architectural history and decision record
  ROADMAP.md       — direction and phases
  CHANGELOG.md     — historical log of changes
  DOCUMENTATION_STYLE.md — writing and documentation standards

site/              — the website the design system serves
  SITEMAP.md       — information architecture
  USER_JOURNEYS.md — experience layer
  CONTENT_STRATEGY.md — content and writing direction

templates/         — reusable page-level compositions
references/        — visual research library (non-canonical)
css/               — stylesheet assets (tokens, base, utilities)
mockups/           — high-fidelity visual mockups
wireframes/        — low-fidelity layout sketches
fonts/             — Pagla Sans typeface files (TTF, WOFF2, variable)
DOC/               — generated documents (Word copies)

bin/               — build and utility scripts
  build_docx.py    — generates DOC/AGENT_MANUAL.docx from markdown

.ai/               — agent infrastructure (MCP + RAG server, D-014)
  mcp/             — PaglaDESIGN MCP server exposing the authority to agents
  AGENT_MANUAL.md  — canonical agent operating procedure (D-022)
```

The repository structure is declared **stable**. New work fits into these folders; the layout is no longer reorganized.

---

## Workflow

Every design decision follows the same process.

```
Vision
    ↓
Research
    ↓
Documentation
    ↓
Design
    ↓
Review
    ↓
Prototype
    ↓
Implementation
```

Implementation is intentionally the final step.

---

## Design First

This repository intentionally prioritizes design over implementation.

Before writing code, we define:

- Why something exists.
- What problem it solves.
- How it fits within the ecosystem.
- Whether it can become reusable.

Only then is it implemented.

---

## Long-Term Vision

PaglaDESIGN is intended to become the design operating system for the entire PaglaAI ecosystem.

Every future website, desktop application, mobile application, documentation portal, and product should inherit its visual identity from this repository.

---

## License

This repository is released under the MIT License unless otherwise specified.
