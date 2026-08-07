# MOCKUP — BrandKit

> High-fidelity, token-referenced. The consumer surface of `../brand/BRAND.md`.

---

# Base

- Paper background, ink text. Values on this page are displayed, never
  invented — they render `../design-system/DESIGN_TOKENS.md` verbatim.

---

# Typography

| Element | Token |
| --- | --- |
| Page title | `font.size.h1`, `font.weight.medium` |
| Tabs | `font.size.body`, selected `font.weight.semibold` |
| Token names | `font.size.code`, `font.weight.semibold` |
| Specimen | PaglaAI Sans — `font.size.display` specimen in light weight |
| Descriptions | `font.size.body`, muted where secondary |

---

# Tab panels

## Brand

- Story prose at 65ch; `color.base.muted` for secondary context

## Logo

- Pagla Face specimen on paper, inside a `color.base.border` clearspace frame
  drawn to the clearspace rule in `../brand/BRAND.md`
- Usage List: do/don't items with text markers

## Typography

- Type specimen: PaglaAI Sans wordmark at `font.size.display`,
  `font.weight.light`
- Token Table: token → value → role (rendered from `DESIGN_TOKENS.md`)

## Colors

- Swatch Table: token → swatch (rendered color chip, border hairline) → value →
  usage
- Accent row notes "meaning only, never a fill" (D-004)

## Icons

- Icon grid at `icon.md`; semantics List below

## Downloads

- List of assets: name → format → ghost Button (Download)

---

# Components in use

- **Tabs:** card variant or underline; six panels
- **Table:** hairline borders, header `font.weight.semibold`
- **Button:** ghost for downloads, primary only for the closing CTA

---

# Spacing rhythm

- Tab bar `space.4` below hero; panel content `space.8` padding
- Tables `space.6` above/below; specimen `space.12` around
- Downloads rows `space.2` apart

---

# Dark theme

Swatches keep their literal values (they are brand colors); surrounding chrome
inverts. Contrast of the swatch labels holds to baseline.

---

# Reduced motion

Tab switches instant under reduced motion; announced selection.
