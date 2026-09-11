# PaglaDESIGN

> The canonical design system, BrandKit, and UX foundation for the entire PaglaAI ecosystem.

**Single source of truth.** Every product inherits visual language, tokens, components, and documentation standards from this repository.

---

## What this is

PaglaDESIGN is the design authority for PaglaAI — not a website project, not a component library alone.

It defines:

- Brand identity and BrandKit
- Design tokens (locked values)
- Typography (Pagla Sans)
- Color system, motion, accessibility, icons
- CSS architecture (tokens → base → utilities)
- Component language and registry
- Documentation and renderer contracts (FERN / MACHINE / ARCHITECT)
- Governance (decisions, roadmap, changelog)

Everything visual begins here. Implementation is last.

---

## Design principles

- Editorial over decorative
- Typography over ornamentation
- Consistency over novelty
- Accessibility by default
- Timeless over trendy
- Performance over visual excess

Whitespace is content. Accent is meaning only — never a fill.

---

## Repository skeleton

```
PaglaDESIGN/
├── README.md                 # this file
├── LICENSE                   # MIT
├── VISION.md                 # why PaglaAI exists
├── DESIGN.md                 # design philosophy
├── PRINCIPLES.md             # standing principles
├── ecosystem.json            # machine-readable product registry
├── ecosystem.schema.json
│
├── brand/                    # identity, mark, BrandKit
├── design-system/            # locked tokens, type, color, motion, a11y, renderers
├── components/               # component language + registry
├── css/                      # reference implementation (tokens, base, utilities)
├── fonts/                    # Pagla Sans (woff2, ttf, variable)
│
├── governance/               # DECISIONS, ROADMAP, CHANGELOG, docs style
├── site/                     # IA, journeys, content strategy
├── templates/                # page-level compositions
├── wireframes/               # low-fidelity layouts
├── mockups/                  # high-fidelity visuals
├── references/               # research library (non-canonical)
│
├── .ai/                      # agent infrastructure (MCP + RAG, AGENT_MANUAL)
├── bin/                      # build / utility scripts
└── DOC/                      # generated documents
```

Structure is **stable**. New work fits these folders; the layout is not reorganized casually.

---

## Quick start for consumers

### CSS (reference implementation)

```css
@import url("./css/tokens.css");   /* locked design tokens */
@import url("./css/base.css");     /* reset + element defaults */
@import url("./css/utilities.css");
```

Canonical typeface: **Pagla Sans** (family name exact). Files live in `fonts/`.

### Tokens authority

All concrete values live in [`design-system/DESIGN_TOKENS.md`](./design-system/DESIGN_TOKENS.md).  
CSS custom properties in `css/tokens.css` are the port of those values.  
Change only through the decision workflow (see `governance/DECISIONS.md`).

### Agents

See [`.ai/AGENT_MANUAL.md`](./.ai/AGENT_MANUAL.md). The design authority is exposed via MCP for deterministic retrieval.

---

## Ecosystem registry

PaglaDESIGN is the authority for the PaglaAI ecosystem.

| Product | Repo | Role | Status |
|---------|------|------|--------|
| **PaglaDESIGN** | `paglaai/PaglaDESIGN` | authority | active |
| **PaglaAI.space** | `paglaai/paglaai.space` | surface | active |
| **paglaai-docs** | `paglaai/paglaai-docs` | surface | active |
| **PaglaMLX** | `paglaai/PaglaMLX` | product | active |
| **PaglaROUTER** | `paglaai/PaglaROUTER` | product | active |
| **PaglaSHELL** | `paglaai/PaglaSHELL` | product | active |
| **B3K4R** | `paglaai/B3K4R` | product | active |
| **PaglaCHAT** | `paglaai/PaglaCHAT` | product | active |
| **PaglaOS** | `paglaai/KolponaOS` | product | active |
| SANCTUM, PaglaAPI, PaglaCPP, PaglaMTP, PaglaUI, PaglaBRAND, PaglaGPT | — | planned | — |

Full machine-readable registry: [`ecosystem.json`](./ecosystem.json).

`PaglaAI.space` is the first consumer surface — it inherits `css/tokens.css` and renders via the FERN (human) renderer.

---

## Workflow (design-first)

```
Vision → Research → Documentation → Design → Review → Prototype → Implementation
```

Implementation is intentionally last. Before code we define why it exists, what problem it solves, how it fits the ecosystem, and whether it is reusable.

---

## Key documents

| Document | Purpose |
|----------|---------|
| [`design-system/DESIGN_TOKENS.md`](./design-system/DESIGN_TOKENS.md) | Locked values |
| [`design-system/CSS_ARCHITECTURE.md`](./design-system/CSS_ARCHITECTURE.md) | CSS layers |
| [`design-system/PAGLA_SANS.md`](./design-system/PAGLA_SANS.md) | Typeface spec |
| [`brand/BRAND.md`](./brand/BRAND.md) / [`brand/BRANDKIT.md`](./brand/BRANDKIT.md) | Identity |
| [`governance/DECISIONS.md`](./governance/DECISIONS.md) | Decision record |
| [`governance/CHANGELOG.md`](./governance/CHANGELOG.md) | History |
| [`.ai/AGENT_MANUAL.md`](./.ai/AGENT_MANUAL.md) | Agent operating procedure |

---

## License

MIT — see [LICENSE](./LICENSE).

---

*PaglaDESIGN is the design operating system for the PaglaAI ecosystem. Every future surface inherits from here.*
