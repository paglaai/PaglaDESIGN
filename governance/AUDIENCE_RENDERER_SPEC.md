# AUDIENCE_RENDERER_SPEC

> *The same source, many readers, one contract.*

---

# Purpose

AUDIENCE_RENDERER_SPEC is the constitutional specification for the Audience
Renderer architecture in PaglaDESIGN v2.

It defines why three canonical renderers exist, how they relate to the design
system, and how every PaglaAI doc page declares its intended audience through a
standard metadata contract.

This document governs the renderer layer. It does not implement it.

---

# Problem

`PaglaAI.space` and future consumer surfaces render the same PaglaDESIGN
Markdown inconsistently.

Each product invents its own:

- layout structure
- component mapping
- typography treatment
- audience targeting

The result is the same source producing different experiences depending on
where it is consumed. That drift undermines the design system's core promise:
shared identity across the ecosystem.

---

# The Three Renderers

The PaglaAI ecosystem has three canonical audiences for its documentation.

A single doc page may target one or more of them.

| Renderer | Audience | Output |
|---|---|---|
| **FERN** | Human — web surfers, readers, learners | Rich HTML, navigable, themed |
| **MACHINE** | Machine — agents, CI pipelines, static site generators, API consumers | JSON, OpenAPI, MCP tool bundle, prompt bundle |
| **ARCHITECT** | Architect — engineers, decision-makers, auditors | RFC, ADR, governance document, audit UI |

No renderer is primary. No renderer is optional.

All three share the same source Markdown. The difference is in how the source
is routed and structured for output.

---

# The `audience` Frontmatter Key

Every PaglaAI doc page declares its audience in YAML frontmatter:

```yaml
---
title: "Design Tokens"
audience:
  - human
  - machine
  - architect
---
```

The `audience` key is an array of one or more renderer names.

Valid values: `human`, `machine`, `architect`.

If a doc page omits `audience`, the consumer MUST NOT render it. This is an
explicit opt-in model.

The schema for frontmatter keys, validation rules, and routing logic is defined
in `RENDERER_API.md`.

---

# Relationship to Existing Documents

The Audience Renderer architecture is a layer above the existing design system.
It does not replace any existing document.

| Existing Document | Role in the Renderer Layer |
|---|---|
| `design-system/DESIGN_TOKENS.md` | Locked values. FERN references these tokens; it never redefines them. |
| `css/tokens.css` | Canonical CSS custom property translation. FERN renders with these classes. |
| `design-system/COMPONENTS.md` | Component language. FERN maps Markdown elements to these components. |
| `components/COMPONENT_LIBRARY.md` | Registered components. FERN uses only Active components from this registry. |
| `design-system/CSS_ARCHITECTURE.md` | Implementation guidance. FERN follows the naming conventions defined here. |
| `design-system/ACCESSIBILITY.md` | Baseline requirements. All renderers must meet the accessibility gates defined here. |
| `design-system/MOTION.md` | Motion principles. FERN applies motion only where MOTION.md permits it. |
| `governance/DECISIONS.md` | Decision record format. ARCHITECT renders RFC/ADR in this structure. |
| `governance/DOCUMENTATION_STYLE.md` | Writing and markup standards. All renderers consume docs written in this style. |

The renderer layer sits between the source Markdown and the consumer surface.

```
Source Markdown (with frontmatter)
    ↓
RENDERER_API.md routing rules
    ↓
┌─────────────┬─────────────┬─────────────┐
│    FERN     │   MACHINE   │  ARCHITECT  │
│ (Human)     │ (Machine)   │ (Architect)  │
└─────────────┴─────────────┴─────────────┘
    ↓               ↓               ↓
 PaglaAI.space   CI / MCP /      Governance /
 (HTML/CSS)       OpenAPI         Audit UI
```

---

# Rendering Principles

All three renderers share these principles:

**Source of truth is the Markdown.**

The frontmatter declares intent. The body provides content. No renderer adds
information that is not in the source.

**No invented values.**

FERN references `css/tokens.css` custom properties. It never invents spacing,
color, or motion values.

**Component fidelity.**

FERN maps Markdown elements to components registered in
`components/COMPONENT_LIBRARY.md`. If a component is not registered, it is not
used.

**Accessibility is non-negotiable.**

Every renderer output must pass the accessibility baseline defined in
`design-system/ACCESSIBILITY.md`.

**Idempotent output.**

The same source, the same renderer, the same configuration must always produce
the same output. This is essential for CI pipelines and cached consumers.

---

# Migration Path

Existing PaglaDESIGN doc pages do not yet have `audience` frontmatter.

Migration proceeds in three phases:

**Phase 1 — Adopt the contract.**

Add `RENDERER_API.md`. No frontmatter changes yet. Consumers continue rendering
as before.

**Phase 2 — Opt in.**

Authors add `audience` arrays to doc pages they want to render. Pages without
`audience` remain invisible to the renderer layer until they are updated.

**Phase 3 — Enforce.**

The renderer contract becomes a requirement. Pages without `audience` fail
validation.

This staged approach prevents breaking existing documentation while the consumer
surfaces (`PaglaAI.space`) are updated to consume the new architecture.

---

# What This Document Does Not Cover

This specification defines the renderer contract. It does not cover:

- The CI/CD event pipeline that detects PaglaDESIGN changes and triggers
  downstream repositories. That is a separate initiative.
- Implementation in `PaglaAI.space`. That is the responsibility of the consumer.
- Changes to locked token values. Those go through the decision workflow
  defined in `governance/DECISIONS.md`.

---

# Relationship to Documents

- Token values — `design-system/DESIGN_TOKENS.md`
- Token CSS — `css/tokens.css`
- Component language — `design-system/COMPONENTS.md`
- Component registry — `components/COMPONENT_LIBRARY.md`
- CSS implementation — `design-system/CSS_ARCHITECTURE.md`
- Accessibility baseline — `design-system/ACCESSIBILITY.md`
- Motion principles — `design-system/MOTION.md`
- Decision record format — `governance/DECISIONS.md`
- Documentation standards — `governance/DOCUMENTATION_STYLE.md`
- Renderer API contract — `design-system/RENDERER_API.md`
- Human renderer guide — `design-system/FERN_RENDERER.md`
- Machine renderer guide — `design-system/MACHINE_RENDERER.md`
- Architect renderer guide — `design-system/ARCHITECT_RENDERER.md`

---

# Final Principle

> **The source is the authority.**
>
> **The renderer is the servant.**
>
> **The reader is the beneficiary.**
