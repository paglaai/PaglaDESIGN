# ACCESSIBILITY

> *Accessibility is not a feature. It is the baseline.*

---

# Purpose

Accessibility is the requirement that every PaglaAI product be usable by as many people as possible.

It is not a later enhancement or a compliance checkbox.

It is the design baseline, decided from the first line of a page and the first line of code.

---

# Principles

- **Inclusive** — for every ability
- **Mandatory** — never optional, never deferred
- **Semantic** — the right element for the right purpose
- **Verifiable** — meeting a tested baseline, not a guess
- **Quiet** — accessible design is not a special style; it is simply good design

---

# Who This Serves

- People using screen readers
- Keyboard-only users
- Low-vision and color-blind users
- Users with motor or attention differences
- Users on slow connections or small screens

Accessibility that helps these users helps everything.

---

# Baseline

The minimum Accessible baseline for PaglaAI:

- **WCAG AA** — contrast, keyboard, and structure goals
- Screen-reader comprehension for every core task

All new design must meet the baseline before it ships.

---

# Foundations

## Semantic HTML

Use the element that means the thing.

Buttons behave as buttons. Headings describe their hierarchy. Landmarks define regions.

Do not build a button out of a layer and guess.

## Keyboard

Everything is operable without a mouse.

Tab order follows the visual order. Focus moves in a predictable path. Users can escape modals and dismiss dialogs without restarts.

## Contrast

Text contrasts with its background per the color and typography docs.

- Primary text: high contrast
- Small text: never flattened onto a muted background (see `COLOR_SYSTEM.md`)
- Focus indicator is always visible

## Focus

Every interactive element receives a visible focus.

Never remove a default focus ring to polish.

`focus` and `focus-within` make it clear where the user is.

## Labels and placeholders

Every input has a programmatic label.

A placeholder is not a label.

Help text is associated with the field it describes.

---

# All States

Color is never the only carrier of state:

- A `success` or `error` is not just a color
- A symbol or textual cue accompanies the color
- A loading state is announced for screen readers

## Color

Color is reinforced by position, icons, and text. See `COLOR_SYSTEM.md`.

## Motion

Reduced motion is honored per `MOTION.md`. Nothing important relies on movement.

## Writing

Communication is clear and concise, per `CONTENT_STRATEGY.md` and `TYPOGRAPHY.md`.

---

# Guidelines

## Links

Describes the destination.

Link text never says "click here".

## Alt text

Convey the purpose. Decorative images are marked as decorative and skipped.

## Headings

Describe the content. Use one accurate top-level heading per view.

## Errors

The error is explained in plain words, next to the field it concerns.

## Video and audio

Provide text alternatives and captions.

---

# Testing

Standard gates at review:

- **Keyboard:** complete a key task with keyboard only
- **Zoom:** layout remains usable at 200%
- **Motion:** same experience with reduced-motion on
- **Contrast:** automated checks plus manual review
- **Semantic markup:** tested for name, role, and value

Never ship unreviewed.

---

# Relationship to Documents

- Contrast/color — `COLOR_SYSTEM.md`, `DESIGN_TOKENS.md`
- Type — `TYPOGRAPHY.md`
- Semantics & interaction — `COMPONENTS.md`
- Decision history — `DECISIONS.md`

---

# Final Principle

Accessible design is not a separate style.

There is only good design.

Good design includes everyone.