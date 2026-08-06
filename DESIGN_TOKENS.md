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

Weight is used for emphasis, never for decoration.

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

This section holds the literal switching values currently in force.

> These are deliberately minimal. Final reference values are resolved after the visual identity is fully frozen, and are tuned per the philosophy in `D-005` of `DECISIONS.md`.

- Base unit `space.base` = `0.25rem`
- Typography, accent, and layout literal values — to be locked upon identity sign-off

When values are moved from `to be locked` to a real number, the change is recorded in `DECISIONS.md` and `CHANGELOG.md`.

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