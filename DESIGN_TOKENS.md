# DESIGN_TOKENS

> *Values belong here. Philosophy belongs in the documents that name them.*

---

# Purpose

DESIGN_TOKENS is the single source of concrete implementation values for the PaglaAI design system.

`TYPOGRAPHY.md`, `COLOR_SYSTEM.md`, `BRAND.md`, and `DESIGN.md` define why and how.

This document defines the numbers.

Every value in the system derives from this file. No value is invented inline in a product.

---

# Token Naming

Language is part of the discipline.

Tokens follow a flat, semantic naming convention:

`category.role[.modifier]`

Examples:

- `font.size.body`
- `font.weight.medium`
- `space.3`
- `color.base.ink`
- `radius.tile`

Names describe a role, never a pixel value. The role remains stable even when a value changes.

---

# Spacing

Spacing follows a modular scale so rhythm stays consistent across every product — web, API output, and native.

The base unit is `space.base`.

All spacing distances are multiples of the base unit.

- `space.0` — none
- `space.1` — base
- `space.2` — 2 × base
- `space.3` — 3 × base
- `space.4` — 4 × base
- `space.5` — 5 × base
- `space.6` — 6 × base
- `space.8` — 8 × base
- `space.12` — 12 × base
- `space.16` — 16 × base
- `space.24` — 24 × base

Reserve `space.0` for alignment-only resets. Do not use odd units inline.

---

# Spacing doctrine

Spacing is generous.

Whitespace is content, not emptiness.

When in doubt, add one step of space between related groups rather than squeezing content together (see `PRINCIPLES.md`, #5).

---

# Typography

## Size scale

The type scale is modular and ratio-based. Sizes are named by role, not by multiple, so the same tokens work across surfaces.

- `font.size.display` — brand and marketing display
- `font.size.h1`
- `font.size.h2`
- `font.size.h3`
- `font.size.h4`
- `font.size.bodyLarge`
- `font.size.body` — default reading size
- `font.size.small`
- `font.size.caption`
- `font.size.code` — micro, for code and labels

## Weights

Weight is used for emphasis, never for decoration.

- `font.weight.light`
- `font.weight.regular`
- `font.weight.medium`
- `font.weight.semibold`
- `font.weight.bold`

## Line height

Body text uses generous line height. Headings are compact.

- `font.lineHeight.body` — comfortable reading rhythm
- `font.lineHeight.heading` — visually tight, with separation from surrounding text
- `font.lineHeight.display` — very tight, for large display

## Letter spacing

- `font.tracking.body` — normal
- `font.tracking.heading` — slight negative tracking at larger sizes
- `font.tracking.display` — significant negative tracking for display
- `font.tracking.uppercase` — wide tracking for small caps labels

## Line length

Body measure is bounded so lines stay readable.

- `font.maxWidth.body` — upper width in characters

---

# Color

## Neutral base

The monochrome foundation (`COLOR_SYSTEM.md`).

- `color.base.ink` — primary text; near-black
- `color.base.paper` — primary background; near-white
- `color.base.surface` — raised panels and cards
- `color.base.border` — dividers and hairlines
- `color.base.muted` — secondary text

## Semantic accent

Reserved for meaning only. Never used as a background fill; only as dot, underline, or focus.

- `color.accent.primary` — primary action and focus
- `color.accent.secondary` — secondary action
- `color.accent.success`
- `color.accent.warning`
- `color.accent.error`
- `color.accent.info`

## State

Interface states are consistent across the ecosystem.

- `color.state.default`
- `color.state.hover`
- `color.state.focus`
- `color.state.active`
- `color.state.disabled`

## Theme

Light and dark share the same semantics. Values are declared per theme.

- theme: light
- theme: dark

Changing theme changes a value, never a role.

---

# UI

These tokens keep components and controls consistent without inventing values inline.

- `radius.sm` — small, chips and badges
- `radius.md` — controls and cards
- `radius.lg` — dialogs and surfaces
- `radius.pill` — full rounding for pills

- `icon.sm`
- `icon.md`
- `icon.lg`

- `interactive.minTarget` — minimum touch/click target size

- `motion.duration.fast`
- `motion.duration.base`
- `motion.duration.slow`
- `motion.easing.default`
- `motion.easing.entrance`
- `motion.easing.exit`
- `motion.reduced` — toggle for reduced-motion users

---

# Breakpoints and layout

Layout adapts at defined breakpoints. Names follow intent, not width.

- `breakpoint.small`
- `breakpoint.medium`
- `breakpoint.large`
- `breakpoint.xlarge`

- `layout.maxWidth` — bounded content column
- `layout.contentPadding` — outer padding at smallest width
- `layout.contentPaddingWide`

---

# Value Reference

These are the locked literal values in force.

Every token listed here is binding. A value not listed here is not in use.

Values use `rem` so the system scales with user zoom (see `TYPOGRAPHY.md`). Root size is `1rem = 16px` unless the user changes it.

## Spacing

Base unit `space.base` = `0.25rem`.

| Token | Value |
| --- | --- |
| `space.0` | `0` |
| `space.1` | `0.25rem` |
| `space.2` | `0.5rem` |
| `space.3` | `0.75rem` |
| `space.4` | `1rem` |
| `space.5` | `1.25rem` |
| `space.6` | `1.5rem` |
| `space.8` | `2rem` |
| `space.12` | `3rem` |
| `space.16` | `4rem` |
| `space.24` | `6rem` |

## Typography

| Token | Value |
| --- | --- |
| `font.size.display` | `4rem` |
| `font.size.h1` | `3rem` |
| `font.size.h2` | `2.25rem` |
| `font.size.h3` | `1.75rem` |
| `font.size.h4` | `1.375rem` |
| `font.size.bodyLarge` | `1.125rem` |
| `font.size.body` | `1rem` |
| `font.size.small` | `0.875rem` |
| `font.size.caption` | `0.75rem` |
| `font.size.code` | `0.875rem` |

| Token | Value |
| --- | --- |
| `font.weight.light` | `300` |
| `font.weight.regular` | `400` |
| `font.weight.medium` | `500` |
| `font.weight.semibold` | `600` |
| `font.weight.bold` | `700` |

| Token | Value |
| --- | --- |
| `font.lineHeight.body` | `1.5` |
| `font.lineHeight.heading` | `1.2` |
| `font.lineHeight.display` | `1.05` |

| Token | Value |
| --- | --- |
| `font.tracking.body` | `0` |
| `font.tracking.heading` | `-0.01em` |
| `font.tracking.display` | `-0.02em` |
| `font.tracking.uppercase` | `0.08em` |

| Token | Value |
| --- | --- |
| `font.maxWidth.body` | `65ch` |

## Color — Light theme

| Token | Value |
| --- | --- |
| `color.base.ink` | `#0A0A0B` |
| `color.base.paper` | `#FFFFFF` |
| `color.base.surface` | `#F5F5F3` |
| `color.base.border` | `#E8E8E6` |
| `color.base.muted` | `#6B707E` |

## Color — Dark theme

| Token | Value |
| --- | --- |
| `color.base.ink` | `#F5F5F3` |
| `color.base.paper` | `#0A0A0B` |
| `color.base.surface` | `#17171A` |
| `color.base.border` | `#2A2A2E` |
| `color.base.muted` | `#9AA0AE` |

## Semantic accent

The accent is single-purpose: meaning only, never a background fill (`COLOR_SYSTEM.md`).

| Token | Value |
| --- | --- |
| `color.accent.primary` | `#6B7EFF` |
| `color.accent.secondary` | `#A8B5FF` |
| `color.accent.success` | `#3E9B6E` |
| `color.accent.warning` | `#E0A23C` |
| `color.accent.error` | `#C94A4A` |
| `color.accent.info` | `#4A90C9` |

## State

| Token | Value |
| --- | --- |
| `color.state.default` | `transparent` |
| `color.state.hover` | `color.base.border` |
| `color.state.focus` | `color.accent.primary` |
| `color.state.active` | `color.base.ink` at `8%` overlay |
| `color.state.disabled` | `color.base.muted` at `40%` opacity |

## UI

| Token | Value |
| --- | --- |
| `radius.sm` | `0.25rem` |
| `radius.md` | `0.5rem` |
| `radius.lg` | `1rem` |
| `radius.pill` | `9999rem` (full) |

| Token | Value |
| --- | --- |
| `icon.sm` | `1rem` |
| `icon.md` | `1.5rem` |
| `icon.lg` | `2rem` |

| Token | Value |
| --- | --- |
| `interactive.minTarget` | `2.75rem` |

## Motion

| Token | Value |
| --- | --- |
| `motion.duration.fast` | `100ms` |
| `motion.duration.base` | `200ms` |
| `motion.duration.slow` | `400ms` |
| `motion.easing.default` | `cubic-bezier(0.2, 0, 0, 1)` |
| `motion.easing.entrance` | `cubic-bezier(0.16, 1, 0.3, 1)` |
| `motion.easing.exit` | `cubic-bezier(0.4, 0, 1, 1)` |
| `motion.reduced` | `0ms` |

## Breakpoints and layout

| Token | Value |
| --- | --- |
| `breakpoint.small` | `40rem` |
| `breakpoint.medium` | `48rem` |
| `breakpoint.large` | `64rem` |
| `breakpoint.xlarge` | `80rem` |

| Token | Value |
| --- | --- |
| `layout.maxWidth` | `75rem` |
| `layout.contentPadding` | `1rem` |
| `layout.contentPaddingWide` | `2rem` |

---

# Locking

Values are locked. They change only through the decision workflow.

A change to any locked value is recorded in `DECISIONS.md` and `CHANGELOG.md`.

---

# Relationship to Documents

- Philosophy & hierarchy — `TYPOGRAPHY.md`
- Color semantics — `COLOR_SYSTEM.md`
- Brand usage — `BRAND.md`
- Decide how a value was chosen — `DECISIONS.md`
- Historical file log — `CHANGELOG.md`

---

# Final Principle

A token should never be magic.

If a future contributor meets a number with no name, that number is an error.