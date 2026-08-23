# Plan: PaglaDESIGN v2.0 — Audience Renderer Initiative

## Problem

`PaglaAI.space` and future consumer surfaces render the same PaglaDESIGN Markdown inconsistently — each inventing its own layout, component mapping, and audience targeting. There is no canonical metadata contract telling a consumer *how* to render a given page.

## Scope (this PR only)

- 5 new documentation files defining the Audience Renderer architecture
- 2 modified files updating the constitution
- CI/CD event pipeline is **out of scope** — separate follow-on initiative

## Decisions

| Decision | Rationale |
|---|---|
| Three canonical renderers: **FERN** (Human), **MACHINE**, **ARCHITECT** | Maps directly to the three consumer types that need different output: web surfers, programmatic consumers/agents, and governance/engineering stakeholders |
| `audience` is an array frontmatter key in `RENDERER_API.md` | A doc page can target multiple audiences; `["human"]`, `["human","machine"]`, `["architect"]` |
| Constitutional spec lives in `governance/AUDIENCE_RENDERER_SPEC.md` | Follows D-001 pattern: principle/specification in governance, implementation guidance in design-system |
| Renderer guides live in `design-system/` | They are implementation guidance for the design system (parallels `CSS_ARCHITECTURE.md`, `COMPONENTS.md`) |
| Principle 06 added to `PRINCIPLES.md` | `PRINCIPLES.md` is the constitutional document; current count is 13 + Final Principle |
| CI/CD event pipeline is separate | Renderer specs must ship and be validated by `PaglaAI.space` build first; combining risks oversized PR touching docs, CSS, CI, and cross-repo automation |

## Files to Create

| File | Purpose |
|---|---|
| `governance/AUDIENCE_RENDERER_SPEC.md` | Constitutional specification: why three renderers exist, the `audience` frontmatter contract, and the relationship between renderers and consumer surfaces |
| `design-system/RENDERER_API.md` | Metadata contract for every PaglaAI doc page: required/optional frontmatter keys, schema, version, renderer routing rules |
| `design-system/FERN_RENDERER.md` | Human renderer implementation guide: HTML output, component mapping, typography token references (`css/tokens.css`), navigation, theme resolution |
| `design-system/MACHINE_RENDERER.md` | Machine renderer: JSON schema output, OpenAPI generation, MCP tool bundle, prompt bundle format |
| `design-system/ARCHITECT_RENDERER.md` | Architect renderer: RFC/ADR templates, governance doc UI, audit trail rendering, decision-record structure |

## Files to Modify

| File | Change |
|---|---|
| `README.md` | Add PaglaDESIGN v2 architecture section and Audience Renderer overview in the Repository Structure / Ecosystem section |
| `PRINCIPLES.md` | Insert Principle 06 — Audience Rendering between current Principle 05 and Principle 06 (renumbering subsequent principles) |

## What Each New Document Must Contain

**`governance/AUDIENCE_RENDERER_SPEC.md`**
- Problem statement (inconsistent rendering across consumer surfaces)
- The three renderer model and when each applies
- The `audience` frontmatter key contract (delegates schema to `RENDERER_API.md`)
- Relationship to existing documents (`DESIGN_TOKENS.md`, `CSS_ARCHITECTURE.md`, `COMPONENTS.md`, `templates/`)
- Migration path: how existing docs adopt the frontmatter

**`design-system/RENDERER_API.md`**
- Required frontmatter: `title`, `audience` (array), `renderer` (string or derived from `audience`)
- Optional frontmatter: `version`, `status` (draft/active/deprecated), `dependencies` (array of doc paths), `schema` (JSON Schema ref for Machine renderer)
- Routing rules: how a consumer maps `audience` values to the three renderers
- Validation rules: what makes a frontmatter block valid/invalid
- Examples for each audience combination

**`design-system/FERN_RENDERER.md`**
- Output format: HTML, structured with semantic class names referencing `css/tokens.css` custom properties
- Component mapping: which Markdown elements map to which `COMPONENT_LIBRARY.md` components
- Typography: token-referenced type scale (`--font-size-h1` through `--font-size-caption`)
- Layout: reading measure (`--font-max-width-body: 65ch`), spacing rhythm
- Theme: inherits light/dark via `[data-theme="dark"]` (D-010)
- Navigation: breadcrumb, TOC, related-pages pattern
- Accessibility gates: focus states, reduced motion, semantic HTML

**`design-system/MACHINE_RENDERER.md`**
- Output formats: JSON document, OpenAPI 3.x fragment, MCP tool bundle, prompt bundle
- Schema: JSON Schema for the document structure (references `RENDERER_API.md` schema key)
- OpenAPI: how doc sections map to OpenAPI paths/operations/schemas
- MCP: tool definitions that expose doc content to agents (complements `.ai/mcp/`)
- Prompt bundle: Markdown optimized for LLM consumption (headings + code blocks + tables)
- Idempotency: same input → same output

**`design-system/ARCHITECT_RENDERER.md`**
- Output formats: RFC template, ADR template, governance/audit document
- Structure: context → decision → alternatives → trade-offs → result (mirrors `DECISIONS.md` format)
- Audit UI: rendered view showing version history, decision lineage, deprecation status
- Relationship to `governance/DECISIONS.md`: when a doc is an ADR vs. when it is general architecture

## Conventions to Follow

- Markdown style: follow `governance/DOCUMENTATION_STYLE.md`
- Token references: use `css/tokens.css` custom property names, never invent new values
- Component references: use names from `components/COMPONENT_LIBRARY.md`
- Folder structure: stable per D-012; no new top-level folders
- Naming: kebab-case filenames matching existing convention

## Validation

- All 5 new files follow `DOCUMENTATION_STYLE.md` structure
- All token references in FERN_RENDERER.md match `css/tokens.css` exactly
- `PRINCIPLES.md` renumbering is consistent (old 06–13 become 07–14)
- `README.md` links resolve correctly
- No invented spacing, color, or motion values anywhere in the new docs

## Out of Scope (this PR)

- CI/CD event pipeline (design.updated event, schema validation workflow, downstream repo triggering)
- Implementation in `PaglaAI.space`
- Changes to `css/tokens.css`, `COMPONENT_LIBRARY.md`, or `COMPONENTS.md`
- MCP server changes in `.ai/mcp/`

## Open Question for Implementation Agent

**What does "FERN" stand for?**

The user specified the filename `FERN_RENDERER.md` but did not define the acronym. Options:
1. **Front-end Experience Renderer** (descriptive, matches the Human-facing role)
2. **Keep as "FERN"** as a proper name (consistent with Pagla Face branding)
3. Ask the user for the intended expansion

**Recommendation:** Use option 2 — treat FERN as a proper name aligned with the PaglaAI brand (Pagla Face). If the user wants an expansion, they will specify it during review.
