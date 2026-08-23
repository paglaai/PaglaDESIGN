# MACHINE_RENDERER

> *The programmatic renderer. What a system sees when it reads a PaglaAI doc page.*

---

# Purpose

MACHINE_RENDERER defines how PaglaDESIGN Markdown is transformed into
structured, machine-readable output for programmatic consumers.

It specifies four output formats: JSON document, OpenAPI 3.x fragment, MCP
tool bundle, and prompt bundle. All formats are derived from the same source and
frontmatter.

MACHINE does not render HTML. It produces data structures, schemas, and
prompts that downstream tools consume directly.

---

# Output Formats

| Format | Use Case | Consumer |
|---|---|---|
| **JSON document** | Structured doc representation | CI pipelines, static site generators, internal tools |
| **OpenAPI 3.x fragment** | API documentation surface | Developer portals, API reference sites |
| **MCP tool bundle** | Agent-readable doc content | `.ai/mcp/` server, external MCP clients |
| **Prompt bundle** | LLM-optimized content | RAG pipelines, prompt injection, agent context |

---

# JSON Document Format

The JSON document is the canonical structured representation of a PaglaAI doc
page.

```json
{
  "meta": {
    "title": "Design Tokens",
    "audience": ["human", "machine", "architect"],
    "version": "1.0.0",
    "status": "active",
    "dependencies": [],
    "schema": null
  },
  "content": {
    "sections": [
      {
        "type": "heading",
        "level": 1,
        "text": "Design Tokens"
      },
      {
        "type": "paragraph",
        "text": "Design tokens are the visual design primitives..."
      },
      {
        "type": "code",
        "language": "css",
        "text": ":root {\n  --color-base-ink: #0a0a0b;\n}"
      }
    ]
  },
  "links": {
    "internal": ["../design-system/DESIGN_TOKENS.md"],
    "external": []
  }
}
```

**Rules:**

- `meta` is derived from the page's YAML frontmatter.
- `content.sections` is an ordered array of block-level elements.
- Section types: `heading`, `paragraph`, `code`, `list`, `table`, `blockquote`,
  `image`.
- `links.internal` contains relative paths found in the Markdown body.
- `links.external` contains absolute URLs.
- The output is deterministic. Same input produces identical JSON.

---

# OpenAPI 3.x Fragment

When a doc page is API documentation, MACHINE produces an OpenAPI 3.x
fragment.

```yaml
# Frontmatter
---
title: "PaglaROUTER API"
audience:
  - machine
  - human
schema: "schemas/paglarouter.json"
---
```

```json
{
  "openapi": "3.0.3",
  "info": {
    "title": "PaglaROUTER API",
    "version": "1.0.0"
  },
  "paths": {
    "/v1/route": {
      "post": {
        "summary": "Create a route",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": { "$ref": "#/components/schemas/RouteRequest" }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Route created",
            "content": {
              "application/json": {
                "schema": { "$ref": "#/components/schemas/RouteResponse" }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "RouteRequest": {
        "type": "object",
        "properties": {
          "target": { "type": "string" },
          "ttl": { "type": "integer" }
        },
        "required": ["target"]
      },
      "RouteResponse": {
        "type": "object",
        "properties": {
          "id": { "type": "string" },
          "status": { "type": "string" }
        }
      }
    }
  }
}
```

**Rules:**

- The fragment is a valid OpenAPI 3.x document on its own.
- It may be merged with other fragments to form a full API spec.
- `schema` in frontmatter references a JSON Schema file path relative to the
  doc.
- The consumer is responsible for resolving `$ref` pointers.

---

# MCP Tool Bundle

MACHINE produces a Model Context Protocol tool bundle that exposes doc content
to agents.

```json
{
  "tool": "get_doc",
  "description": "Retrieve a PaglaAI documentation page by path.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "path": {
        "type": "string",
        "description": "Relative path to the Markdown file."
      }
    },
    "required": ["path"]
  },
  "output": {
    "meta": { "title": "Design Tokens", "version": "1.0.0" },
    "content": { "sections": [...] }
  }
}
```

**Rules:**

- The bundle is a JSON object with one or more tool definitions.
- Each tool definition follows the MCP 2.x specification.
- Tool names are snake_case.
- Output is the same JSON document structure used by the JSON document format.
- The bundle complements the existing `.ai/mcp/` server (D-014). It does not
  replace it.
- `.ai/mcp/` handles search and retrieval over the file index; MACHINE
  provides the structured output format for a single doc page.

---

# Prompt Bundle

MACHINE produces a prompt bundle optimized for LLM consumption.

```markdown
# Design Tokens

**Version:** 1.0.0
**Status:** active
**Audience:** human, machine, architect

## Overview

Design tokens are the visual design primitives...

## CSS Custom Properties

```css
:root {
  --color-base-ink: #0a0a0b;
  --color-base-paper: #ffffff;
}
```

## Related

- DESIGN_TOKENS.md
- CSS_ARCHITECTURE.md
```

**Rules:**

- Frontmatter is converted to a concise header block.
- Code blocks retain their language tags.
- Internal links are converted to plain text references.
- Tables are converted to pipe-delimited lists.
- No images are included; image descriptions are retained as alt text.
- The bundle is stripped of HTML, comments, and navigation markup.
- Maximum token efficiency: headings are preserved for structure; prose is
  preserved for context; code is preserved for accuracy.

---

# Schema Reference

The `schema` frontmatter key references a JSON Schema file.

```yaml
---
title: "PaglaROUTER Request Schema"
audience:
  - machine
schema: "schemas/route-request.json"
---
```

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "target": {
      "type": "string",
      "format": "uri"
    },
    "ttl": {
      "type": "integer",
      "minimum": 0
    }
  },
  "required": ["target"]
}
```

**Rules:**

- Schema references are relative to the doc file.
- The consumer resolves the reference before validating output.
- If `schema` is absent, the JSON document output omits the `schema` field.

---

# Idempotency

MACHINE output is idempotent.

Given the same source Markdown, the same frontmatter, and the same renderer
version, the output is byte-identical across runs.

No timestamps, random values, or environment-dependent values are included in
the output.

---

# Validation

MACHINE validates frontmatter against the rules in `RENDERER_API.md` before
rendering.

Invalid frontmatter produces a structured error in the JSON document format:

```json
{
  "error": {
    "code": "INVALID_FRONTMATTER",
    "message": "audience array is empty",
    "field": "audience"
  }
}
```

No partial output is produced for invalid input.

---

# Relationship to Documents

- Renderer API — `design-system/RENDERER_API.md`
- Constitutional spec — `governance/AUDIENCE_RENDERER_SPEC.md`
- Token values — `design-system/DESIGN_TOKENS.md`
- Component registry — `components/COMPONENT_LIBRARY.md`
- Documentation standards — `governance/DOCUMENTATION_STYLE.md`
- Agent tooling — `.ai/mcp/` (complement, not replacement)

---

# Final Principle

> **Structured over decorative.**
>
> **Deterministic over dynamic.**
>
> **Machine-readable over human-pretty.**
