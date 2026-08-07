# INSPIRATION

> *Research distills into principles. Principles shape the system. The system
> serves the product.*

---

# Purpose

INSPIRATION records the **extracted principles** from the visual and
communication research captured under `references/`. It is the bridge between
non-canonical research and the canonical design documents.

The screenshots and captures in the per-source folders are not authority.

The principles distilled here are authority only when they restate or extend
the canonical documents (`../DESIGN.md`, `../PRINCIPLES.md`, `brand/`,
`design-system/`). Where this document disagrees with a canonical document,
the canonical document wins.

---

# Sources Studied

| Source | Studied in | Folder |
| --- | --- | --- |
| OpenAI | Communication and editorial style | `openai/` |
| Apple | Whitespace and hierarchy | `apple/` |
| Anthropic | Calm technical surfaces and docs | `anthropic/` |
| Stripe | Documentation and developer empathy | `stripe/` |
| Linear | Interaction and focus discipline | `linear/` |
| Vercel | Typography-led developer branding | `vercel/` |
| Cloudflare | Plain-language technical communication | `cloudflare/` |
| Fern | API reference structure | `fern/` |
| PaglaMLX | In-ecosystem product communication | `pagla-mlx/` |

---

# Distilled Principles

These principles confirm and sharpen the existing canonical direction. They are
organized by the document they reinforce.

## Communication

- Explain the *why* before the *what*.
- One primary question per page; one clear next step per page.
- Terminal and code captures are honest illustration — show the real output.
- Plain language outranks impressive language.

Reinforces: `../site/CONTENT_STRATEGY.md`, `../brand/BRAND.md`.

## Structure

- Teach progressively: purpose, then value, then details.
- Documentation is a first-class deliverable, not an afterthought.
- API references follow one predictable anatomy everywhere.
- The navigation map and the content structure should agree.

Reinforces: `../site/SITEMAP.md`, `../governance/DOCUMENTATION_STYLE.md`.

## Visual language

- Typography and whitespace carry hierarchy before color.
- Monochrome first; a single functional accent, never a background fill.
- Generous spacing; the reading column never fights the content.
- Motion is fast, purposeful, and reduced-motion safe.

Reinforces: `../design-system/TYPOGRAPHY.md`, `../design-system/COLOR_SYSTEM.md`,
`../design-system/MOTION.md`, `../design-system/DESIGN_TOKENS.md`.

## Interaction

- Focus is explicit and never sacrificed for polish.
- Color is never the only carrier of state.
- Every state change is confirmed, never ambiguous.

Reinforces: `../design-system/ACCESSIBILITY.md`, `../components/COMPONENTS.md`.

---

# Boundary

Research is captured, not copied.

- We extract principles, never visual assets from other brands.
- Reference material never enters `brand/` or `design-system/` as authority.
- When a source idea survives distillation, it survives as a principle that
  any PaglaAI product can own.

---

# Relationship to Documents

- Canonical direction — `../DESIGN.md`, `../PRINCIPLES.md`
- Brand and voice — `../brand/BRAND.md`
- Visual system — `../design-system/`
- Site structure — `../site/`
- Decision history — `../governance/DECISIONS.md`

---

# Final Principle

> *Inspiration is input. Principles are output. The system is the result.*
