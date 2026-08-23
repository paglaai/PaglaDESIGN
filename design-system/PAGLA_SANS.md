# PAGLA_SANS

> *The typeface is the primary interface.*

---

# Purpose

PAGLA_SANS is the design specification for the PaglaAI ecosystem's primary typeface.

It defines the visual characteristics, technical requirements, and usage rules for Pagla Sans.

Concrete implementation values live in `DESIGN_TOKENS.md`.

---

# Design Philosophy

Pagla Sans begins with Open Sans.

It is lighter, more open, more premium-minimal.

Same DNA, different attitude.

Type is the primary interface. The typeface must carry hierarchy without decoration, feel calm at body sizes, and authoritative at display sizes.

---

# Anatomy

## Base

Pagla Sans is derived from Open Sans (variable `wdth` 75–100, `wght` 300–800), designed by Steve Matteson, licensed under SIL Open Font License 1.1 / Apache License 2.0.

## Modifications

### Perfect-Circle O & P

The `O` (outer outline and counterhole) and the `P` counterhole are mathematically perfect circles.

Every contour point is projected radially onto an exact circle. Extrema deviate less than 1 unit at 2048 UPM.

This creates a geometric precision that distinguishes Pagla Sans from its humanist ancestor.

### Lighter Weight Distribution

Pagla Sans maintains legibility at lighter weights than typical humanist sans-serifs.

- Light (300) is usable at display sizes
- Regular (400) is the body workhorse
- Bold (700) provides emphasis without heaviness

### Open Apertures

Letterforms maintain generous open apertures for excellent legibility at small sizes and on screens.

### Monolinear Stroke

Stroke contrast is minimal, creating a clean, modern appearance that works across all weights.

---

# Weights

| Weight | OS/2 | CSS | Use |
|---|---|---|---|
| Light | 300 | `font-weight: 300` | Display text, large headings |
| Regular | 400 | `font-weight: 400` | Body text, default |
| Medium | 500 | `font-weight: 500` | Nav labels, emphasis |
| SemiBold | 600 | `font-weight: 600` | Headings, card titles |
| Bold | 700 | `font-weight: 700` | Strong emphasis, CTAs |

## Variable Font

Pagla Sans is also available as a variable font with axes:
- `wght`: 300–700
- `wdth`: 75–100

Use the variable font when dynamic weight/width interpolation is needed.

---

# Technical Specifications

## Units Per Em

2048 UPM

## Ascender / Descender

- Ascender: 2189
- Descender: -600
- Line gap: 0

## Metrics

| Metric | Value |
|---|---|
| x-height | 1500 (approx. 73% of cap height) |
| Cap height | 2050 |
| Ascender | 2189 |
| Descender | -600 |
| Average glyph width | 550 |

## Character Set

- Latin Extended (European languages)
- Cyrillic (planned)
- Greek (planned)
- IPA extensions

---

# File Formats

| Format | Use | Files |
|---|---|---|
| TrueType (.ttf) | Desktop, print | `PaglaSans-*.ttf` |
| WOFF2 (.woff2) | Web | `PaglaSans-*.woff2` |
| Variable TrueType | Advanced web, apps | `PaglaSans-VF.ttf` |
| Variable WOFF2 | Modern web | `PaglaSans-VF.woff2` |

## Naming Convention

```
PaglaSans-{Weight}.ttf
PaglaSans-{Weight}.woff2
PaglaSans-VF.ttf
PaglaSans-VF.woff2
```

Where `{Weight}` is: `Light`, `Regular`, `Medium`, `SemiBold`, `Bold`

---

# CSS Implementation

## @font-face Declarations

```css
@font-face {
  font-family: "Pagla Sans";
  src: url("../fonts/PaglaSans-Light.woff2") format("woff2");
  font-weight: 300;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Pagla Sans";
  src: url("../fonts/PaglaSans-Regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Pagla Sans";
  src: url("../fonts/PaglaSans-Medium.woff2") format("woff2");
  font-weight: 500;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Pagla Sans";
  src: url("../fonts/PaglaSans-SemiBold.woff2") format("woff2");
  font-weight: 600;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Pagla Sans";
  src: url("../fonts/PaglaSans-Bold.woff2") format("woff2");
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}
```

## Font Stack

```css
font-family: "Pagla Sans", system-ui, -apple-system, "Segoe UI", Roboto,
  Helvetica, Arial, sans-serif;
```

## Code Font Stack

```css
font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono",
  monospace;
```

---

# Usage Rules

## Do

- Use Pagla Sans as the primary typeface for all PaglaAI products
- Respect the weight hierarchy (Light for display, Regular for body, Bold for emphasis)
- Use generous line height (1.5 for body, 1.2 for headings)
- Apply negative tracking at display sizes (-0.02em)
- Test legibility at all sizes and weights

## Don't

- Use Light or Thin weights at small sizes (below 14px)
- Stretch or distort the typeface
- Apply faux bold or faux italic
- Mix Pagla Sans with other sans-serif families in the same context
- Use decorative or script fonts alongside Pagla Sans

---

# Accessibility

## Legibility

- Minimum body size: 16px (1rem)
- Minimum caption size: 12px (0.75rem)
- Prefer Regular or Medium weights for body text
- Avoid Light weights at small sizes

## Contrast

- Body text on paper: `color.base.ink` on `color.base.paper`
- Muted text: `color.base.muted` (ensure 4.5:1 contrast ratio)

## Dynamic Type / User Scaling

Pagla Sans uses `rem` units, so it scales with the user's root font size setting.

---

# Relationship to Documents

- Concrete values — `DESIGN_TOKENS.md`
- Color semantics — `COLOR_SYSTEM.md`
- Brand usage — `../brand/BRAND.md`
- CSS architecture — `CSS_ARCHITECTURE.md`
- License — `../fonts/LICENSE.txt`

---

# Final Principle

The typeface should feel calm, precise, and unmistakably human.

It whispers "Intelligence, Unhinged."

And it does not need to say the rest.
