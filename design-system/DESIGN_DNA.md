# DESIGN_DNA

> *Fixed enough that UI work stops being invented. Evolving enough that the system stays alive.*

**Status:** Locked (D-024)  
**Authority:** PaglaDESIGN  
**Consumers:** every PaglaAI surface — website, products, docs, storefronts

---

## Why this exists

You should not spend time redesigning UI for each product.

DesignDNA is the permanent visual and interaction contract for the entire PaglaAI ecosystem. It is **fixed** at the doctrine layer and **evolving** only through the decision workflow in `governance/DECISIONS.md`.

If a product needs a one-off pattern, the pattern is wrong — or DesignDNA is incomplete. Fix the DNA, not the product.

---

## The fixed core (do not invent past this)

### 1. Typeface

| Rule | Value |
|------|--------|
| Family | **Pagla Sans** (exact CSS name: `"Pagla Sans"`) |
| Weights | 300 Light · 400 Regular · 500 Medium · 600 SemiBold · 700 Bold |
| Display / wordmark | Light 300, tracking `font.tracking.display` |
| Body | Regular 400, measure ≤ 65ch |
| Never | invent a second brand face; never outline the wordmark |

### 2. Color

| Rule | Value |
|------|--------|
| Identity | **Monochrome first** — ink + paper |
| Light ink / paper | `#0A0A0B` / `#FFFFFF` |
| Dark ink / paper | `#F5F5F3` / `#0A0A0B` |
| Accent | `#6B7EFF` — **meaning only** (dot, underline, focus). Never a fill. |
| Surfaces | surface / border / muted from `DESIGN_TOKENS.md` only |

### 3. Space & rhythm

| Rule | Value |
|------|--------|
| Base unit | `0.25rem` |
| Scale | space.0 → space.24 only |
| Doctrine | Whitespace is content. When in doubt, add one step. |
| Reading column | `layout.reading` = 42rem; body max 65ch |

### 4. Layout (OpenAI-class editorial)

| Rule | Value |
|------|--------|
| Density | Editorial, not dashboard |
| Hero | Large type, short line, one primary action |
| Nav | Minimal primary links; utility secondary |
| Sections | Generous vertical rhythm (`space.12`–`space.24` between major bands) |
| Max content | `layout.maxWidth` = 75rem |
| Cards / grids | Token radii only; hairline borders; no heavy shadows |

### 5. Motion & a11y

| Rule | Value |
|------|--------|
| Duration | fast 100ms · base 200ms · slow 400ms |
| Reduced motion | honor `prefers-reduced-motion` → 0ms |
| Focus | visible, accent-colored ring |
| Targets | ≥ `interactive.minTarget` (2.75rem) |

### 6. Mark & brand

| Rule | Value |
|------|--------|
| Mark | Pagla Face — black or white only, flat |
| Wordmark | Pagla Sans Light; never with Face in the same lockup |
| Clearspace | height of the sunglasses |
| Voice | Precise first, playful second |

---

## What is allowed to evolve

Evolution is allowed **only** via a numbered decision in `governance/DECISIONS.md` and a CHANGELOG entry:

- Token value adjustments (with migration note for consumers)
- New registered components (not one-offs)
- New templates / page compositions
- New ecosystem products in `ecosystem.json`
- Automation pipelines that **reflect** DNA, never override it

Evolution is **not** allowed as:

- Inline hex / px in product CSS
- A second typeface “just for marketing”
- Accent used as a page background
- Per-product redesign sprints that ignore this document

---

## Source of numbers

All concrete values live in [`DESIGN_TOKENS.md`](./DESIGN_TOKENS.md).  
CSS port: `css/tokens.css` in this repo; consumers inherit, they do not retype.

---

## Surfaces that must obey DesignDNA

| Surface | Role |
|---------|------|
| **paglaai.space** | Public website (FERN) |
| **apphole.store** | Package / app storefront |
| **paglaai-docs** | Unified docs |
| Product UIs (PaglaMLX, PaglaROUTER, …) | Product chrome |
| PaglaGPT / agent UIs | Model-facing surfaces |

---

## Automation rule

When GitHub changes (commit, release, public repo, package publish):

1. **Tokens / brand / DNA** change → validate → dispatch `design.updated` → rebuild consumers.
2. **Product / release** change → regenerate ecosystem-facing pages (products list, changelog, storefront catalog) from `ecosystem.json` + GitHub API — **never** by hand-editing marketing copy that will drift.

The website is a **reflection** of the repos, not a parallel design project.

---

## Quick compliance checklist

- [ ] Font family is exactly `"Pagla Sans"`
- [ ] No colors outside the token table
- [ ] Accent never used as a fill
- [ ] Spacing only from the space scale
- [ ] Body measure ≤ 65ch
- [ ] No second brand mark or typeface
- [ ] Theme follows semantic tokens (light/dark)
- [ ] Reduced motion respected

If any box fails, the change does not ship.

---

*DesignDNA is the design operating system. Products inherit. They do not negotiate.*
