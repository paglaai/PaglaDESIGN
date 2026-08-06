# CSS_ARCHITECTURE

> *CSS should implement the design system. It should not define it.*

---

# Purpose

CSS_ARCHITECTURE defines how the PaglaAI design system becomes real, working CSS.

The design language lives in documents.

CSS is the translation layer between those documents and every product.

It exists to make the system predictable, reusable, and fast.

---

# Architecture Principles

- Design tokens first
- Semantic class names
- No magic numbers
- No repeated values
- No component-specific hacks
- Styles that scale across every product

CSS is architecture, not handwriting.

---

# Layer Model

CSS is organized in layers. Each layer builds on the one below it.

1. **Tokens** — the values from `DESIGN_TOKENS.md`
2. **Base** — element defaults and resets
3. **Utilities** — single-purpose helpers
4. **Components** — reusable component styles
5. **Layout** — page and surface structure

Each layer may only depend on the layers beneath it.

No layer reaches upward.

---

# Design Tokens

Tokens are the single source of values.

They are emitted as CSS Custom Properties on a `:root` scope.

Custom properties follow the naming convention from `DESIGN_TOKENS.md`:

`category.role.modifier`

Examples:

- `--color-base-ink`
- `--color-accent-primary`
- `--font-size-body`
- `--space-4`

Tokens are never repeated as literals in component styles.

A component uses the token reference, never the value.

---

# Theming

Light and dark themes share one set of semantic tokens.

A theme changes the value of a token, never its meaning.

Themes are declared by reassigning the same custom properties:

```
:root {
  --color-base-paper: ...;
  --color-base-ink: ...;
}

[data-theme="dark"] {
  --color-base-paper: ...;
  --color-base-ink: ...;
}
```

Components never need to know which theme is active.

---

# Class Naming

Class names are semantic and describe role, not presentation.

A class tells you what something is, not how it looks.

Avoid:

- Presentational names tied to a specific value
- Layout names embedded in component classes
- Single-use names invented per screen

Names should survive value changes.

---

# Structure

- **Base:** element defaults — reset, typography, focus, reduced motion.
- **Utilities:** single-purpose helpers used deliberately, not everywhere.
- **Components:** scoped, reusable, and composed from tokens.
- **Layout:** the page grid, spacing flow, and surface structure.

---

# Spacing

Spacing is never guessed.

Every spacing value comes from the space tokens in `DESIGN_TOKENS.md`.

Rhythm comes from the token scale, not from one-off values.

---

# Typography

Font sizes, weights, line heights, and tracking are typography tokens.

No inline font-size adjustments outside the scale.

---

# Responsive

Layout adapts through the breakpoints in `DESIGN_TOKENS.md`.

Breakpoints use the shared names, not magic widths scattered through files.

---

# Performance

- Fewer dependencies than the value they add.
- No unused CSS shipped.
- No dependency that does not justify its existence.

Performance is part of the architecture, not an afterthought.

---

# Accessibility

Accessibility is written into the CSS, not bolted on:

- Visible focus states on every interactive element
- `prefers-reduced-motion` honored from the start
- Logical source order preserved
- Color-only meaning avoided

---

# Relationship to Documents

- Values — `DESIGN_TOKENS.md`
- Color semantics — `COLOR_SYSTEM.md`
- Type — `TYPOGRAPHY.md`
- Components — `../components/COMPONENTS.md`
- Motion — `MOTION.md`
- Accessibility — `ACCESSIBILITY.md`
- Decision history — `../governance/DECISIONS.md`

---

# Final Principle

Good CSS architecture is mostly invisible.

If a future contributor has to ask where a value came from, the architecture failed.