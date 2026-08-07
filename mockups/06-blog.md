# MOCKUP — Blog

> High-fidelity, token-referenced. The article index view.

---

# Base

- Paper background, ink text. Cards carry hairlines, not shadows — the system is
  flat (D-008).

---

# Typography

| Element | Token |
| --- | --- |
| Page title | `font.size.h1`, `font.weight.medium` |
| Card titles | `font.size.h3`, `font.weight.medium`, `font.tracking.heading` |
| Card summaries | `font.size.body`, muted |
| Meta | `font.size.small`, `color.base.muted` |
| Type chips | `font.size.caption`, `font.tracking.uppercase` |

---

# Region treatment

## Hero

- Left-aligned; overline `font.tracking.uppercase`, muted

## Filter

- Chips on paper, `radius.sm`, `space.2` apart, wrapping
- Selected: `font.weight.semibold` + check marker + `color.base.border` fill —
  selection shown beyond color
  (`../design-system/ACCESSIBILITY.md`)

## Post list

- Single-column Cards: title → summary → meta (date · read time · author)
- `radius.md`, `color.base.border` hairline, `space.4` internal padding
- `space.6` between Cards
- Type chip top-left, `color.base.surface` fill, muted text

## Paging

- Numbered List, current page `font.weight.semibold` + accent text; prev/next
  ghost Buttons

## CTA

- Centered; one primary Button

---

# Components in use

- **Chips:** filter variant, removable only where the filter set demands it
- **Card:** plain (whole card not a link); title and "read" link navigate
- **List:** paging and related links

---

# Spacing rhythm

- Hero `space.12` bottom; filter `space.8` below hero, `space.6` above list
- Cards `space.6` apart; meta `space.2` below summary
- Paging `space.12` above; CTA `space.16`

---

# Dark theme

Standard inversion; chips `#17171A` surface; card hairlines `#2A2A2E`.

---

# Reduced motion

No entrance animations; chips update instantly with announced filter result.
