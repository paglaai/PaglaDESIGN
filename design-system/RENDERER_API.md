# RENDERER_API

> *Every doc page tells the renderer how to present itself.*

---

# Purpose

RENDERER_API defines the metadata contract for every PaglaAI documentation
page.

It specifies the frontmatter keys, their schema, validation rules, and routing
logic that the three canonical renderers — FERN, MACHINE, and ARCHITECT —
consume.

Consumer surfaces (`PaglaAI.space`, CI pipelines, MCP servers) use this
contract to determine how to render a doc page without inventing their own
logic.

---

# The `audience` Key

`audience` is an array of one or more renderer names.

```yaml
---
title: "Design Tokens"
audience:
  - human
  - machine
  - architect
---
```

Valid values:

| Value | Renderer | Consumer |
|---|---|---|
| `human` | FERN | `PaglaAI.space` (HTML/CSS) |
| `machine` | MACHINE | CI pipelines, static site generators, MCP servers |
| `architect` | ARCHITECT | Governance UI, audit tools, RFC/ADR workflows |

A page may target multiple audiences. A page with no `audience` key is not
rendered by any consumer.

---

# Required Frontmatter Keys

| Key | Type | Required | Description |
|---|---|---|---|
| `title` | string | Yes | The page title. Used in `<title>`, breadcrumbs, and document headers. |
| `audience` | array | Yes | One or more of: `human`, `machine`, `architect`. |

---

# Optional Frontmatter Keys

| Key | Type | Default | Description |
|---|---|---|---|
| `version` | string | none | Semantic version of the document. Consumers use this for cache invalidation. |
| `status` | string | `active` | Document lifecycle: `draft`, `active`, `deprecated`. |
| `dependencies` | array | `[]` | Paths to other PaglaAI docs this page depends on. Used by MACHINE for schema linking. |
| `schema` | string | none | JSON Schema `$ref` for structured output. Used by MACHINE renderer. |
| `renderer` | string | derived from `audience` | Override the renderer routing. Normally derived from `audience`; set explicitly only for edge cases. |

---

# Routing Rules

A consumer maps `audience` values to renderers as follows:

**Rule 1 — Single audience.**

```yaml
audience: [human]
```

Routed to FERN only. MACHINE and ARCHITECT skip this page.

**Rule 2 — Multiple audiences.**

```yaml
audience:
  - human
  - machine
```

Routed to both FERN and MACHINE. ARCHITECT skips this page.

**Rule 3 — All audiences.**

```yaml
audience:
  - human
  - machine
  - architect
```

Routed to all three renderers.

**Rule 4 — `renderer` override.**

```yaml
audience:
  - human
renderer: fern
```

Explicit `renderer` takes precedence over derived routing. Use only when the
audience array does not map cleanly to a single renderer.

**Rule 5 — Missing `audience`.**

Pages without an `audience` key are invisible to the renderer layer. Consumers
must not render them. This is an explicit opt-in model.

---

# Validation Rules

A frontmatter block is **valid** when:

1. `title` is a non-empty string.
2. `audience` is a non-empty array.
3. Every value in `audience` is one of: `human`, `machine`, `architect`.
4. If `status` is present, it is one of: `draft`, `active`, `deprecated`.
5. If `version` is present, it is a valid semver string (e.g. `1.0.0`).
6. If `schema` is present, it is a valid JSON Schema reference string.
7. If `dependencies` is present, it is a non-empty array of strings.
8. If `renderer` is present, it is one of: `fern`, `machine`, `architect`.

A frontmatter block is **invalid** when any of the above conditions fail.

Consumers must log a validation error and skip the page rather than render it
with fallback defaults.

---

# Frontmatter Examples

**Human-only page (tutorial):**

```yaml
---
title: "Getting Started with PaglaROUTER"
audience:
  - human
version: "1.2.0"
status: active
---
```

**Machine-only page (API schema):**

```yaml
---
title: "PaglaROUTER OpenAPI Schema"
audience:
  - machine
version: "2.0.0"
schema: "schemas/paglarouter.json"
dependencies:
  - ../design-system/DESIGN_TOKENS.md
---
```

**Architect-only page (RFC):**

```yaml
---
title: "RFC-0042: Event Pipeline Architecture"
audience:
  - architect
version: "0.1.0"
status: draft
---
```

**All audiences (core design doc):**

```yaml
---
title: "PaglaAI Design Tokens"
audience:
  - human
  - machine
  - architect
version: "1.0.0"
status: active
---
```

---

# Rendering Contract Summary

| Condition | FERN | MACHINE | ARCHITECT |
|---|---|---|---|
| `audience: [human]` | renders | skips | skips |
| `audience: [machine]` | skips | renders | skips |
| `audience: [architect]` | skips | skips | renders |
| `audience: [human, machine]` | renders | renders | skips |
| `audience: [human, architect]` | renders | skips | renders |
| `audience: [machine, architect]` | skips | renders | renders |
| `audience: [human, machine, architect]` | renders | renders | renders |
| missing `audience` | skips | skips | skips |
| invalid frontmatter | error | error | error |

---

# Idempotency Requirement

Given the same source Markdown, the same frontmatter, and the same renderer
configuration, the output must be byte-identical across runs.

This requirement exists because:

- CI pipelines cache rendered output.
- `PaglaAI.space` serves static assets from a CDN.
- MCP tools return deterministic results for agent reasoning.

Non-deterministic output breaks caching, invalidates CDN edges, and produces
inconsistent agent responses.

---

# Relationship to Documents

- Constitutional spec — `governance/AUDIENCE_RENDERER_SPEC.md`
- Human renderer guide — `design-system/FERN_RENDERER.md`
- Machine renderer guide — `design-system/MACHINE_RENDERER.md`
- Architect renderer guide — `design-system/ARCHITECT_RENDERER.md`
- Token values — `design-system/DESIGN_TOKENS.md`
- Token CSS — `css/tokens.css`
- Component registry — `components/COMPONENT_LIBRARY.md`
- Documentation standards — `governance/DOCUMENTATION_STYLE.md`

---

# Final Principle

> **Explicit opt-in.**
>
> **Explicit contract.**
>
> **Explicit output.**
