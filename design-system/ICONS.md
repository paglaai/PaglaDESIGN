# ICONS

> *An icon should resolve meaning in an instant, then disappear.*

---

# Purpose

ICONS defines the icon language of the PaglaAI ecosystem.

Icons support communication.

They never replace it.

An icon is a visual shortcut to an idea that already has words.

---

# Icon Principles

- **Clarity** — readable at small sizes
- **Consistency** — one visual language across products
- **Purpose** — every icon earns its place
- **Restraint** — fewer, better icons, not more icons
- **Accessibility** — never the only carrier of meaning

---

# Design Language

Icons share one stroke and one optical weight.

- Monochrome first
- Geometric, precise construction
- Consistent stroke width
- Uniform rounding
- No filled/gradient decoration

Icons feel like the mark: quiet, precise, and calm.

---

# Grid

Icons are drawn on a consistent grid.

- A single base grid size
- Oversize-safe padding for optical balance
- Optical adjustment over mathematical centering

The grid is defined in `DESIGN_TOKENS.md`.

---

# Naming

Icons are named by their meaning, never by their shape or position.

A name describes the concept:

- `search` not `magnifier`
- `close` not `x-in-the-corner`
- `save` not `floppy-disk`

Naming is semantic and singular.

---

# Usage

Icons appear at defined sizes only.

Sizes come from the icon tokens in `DESIGN_TOKENS.md`.

- Icons align with the typography they accompany
- Icons sit on the layout grid
- Icons never stretch or distort

---

# Icons with Text

When meaning matters, text is the source.

An icon beside a label reinforces the label.

An icon without a label must be unambiguous — or must not be the only signal.

See `ACCESSIBILITY.md`.

---

# Meaning

Icons inherit the semantics of `COLOR_SYSTEM.md`:

- An icon on its own is not a state
- A warning icon is reinforced by a warning label
- Color never defines the icon; the meaning does

---

# New Icons

Before adding an icon:

Can an existing icon solve this?

Can the current icon evolve?

Will this icon benefit every product?

If yes, add it to the shared library.

If no, it does not belong.

---

# Relationship to Documents

- Sizes and tokens — `DESIGN_TOKENS.md`
- Color semantics — `COLOR_SYSTEM.md`
- Component usage — `../components/COMPONENTS.md`
- Accessibility — `ACCESSIBILITY.md`
- Decision history — `../docs/DECISIONS.md`

---

# Final Principle

A good icon library is small, sharp, and complete.

The best icons are the ones users do not notice.