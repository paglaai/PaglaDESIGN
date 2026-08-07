# HERO

> *The hero answers one question in one breath: what is this, and should I care.*

---

# Purpose

The hero is the opening composition of a page.

It establishes the subject, states the value in one sentence, and offers one
clear next step. It sets the tone for everything that follows.

It is typography-led. No decoration, no gradient, no scene-setting animation
(`../design-system/UX_PATTERNS.md`).

---

# Question it answers

> What is this, and what can I do with it?

---

# Anatomy

The hero composes these building blocks, top to bottom:

1. **Overline** — a small-caps label placing the page in context
   (`font.tracking.uppercase`, `font.size.small`)
2. **Headline** — the single idea, at `font.size.h1` or `font.size.display`
3. **Summary** — one sentence under `font.maxWidth.body` (`65ch`), at
   `font.size.bodyLarge`, in `color.base.muted`
4. **Actions** — one primary Button and, at most, one secondary or ghost Button
5. **Proof of work** — optional: a Terminal or Code Block showing real output
   (`../references/INSPIRATION.md`), or a List of the three strongest facts

---

# Composition

## Spacing rhythm

- Vertical padding: `space.16` to `space.24` above and below the block
- Between overline and headline: `space.4`
- Between headline and summary: `space.5`
- Between summary and actions: `space.8`
- Between actions and the proof block: `space.12`
- Max width: `layout.maxWidth`, with content centered on `font.maxWidth.body`
  for the text column

## Alignment

- Default: centered text on a marketing page, left-aligned in a docs or product
  context with a left-aligned proof block beside it (Grid at
  `breakpoint.large`)
- Never center long prose. Center only when the block is short enough to read
  in one glance

## Responsive

- Below `breakpoint.medium`: the two-column hero (text + proof) collapses to a
  single column, proof below text
- Display size steps down one step on small screens so the headline never
  overflows

---

# Variants

| Variant | Proof of work | Alignment |
| --- | --- | --- |
| Product hero | Terminal or product screenshot | left or centered |
| Docs hero | Code Block (install command) | left |
| Marketing hero | List of facts or none | centered |
| Article hero | Meta (date, author, read time) | left |

---

# Behavior

- The primary action is the one clear next step; the secondary action never
  competes with it (`../site/CONTENT_STRATEGY.md`)
- The proof block is static, faithful, and reduced-motion safe
  (`../design-system/MOTION.md`)
- Headline, summary, and actions enter together once, within
  `motion.duration.base`, if they animate at all

---

# Relationship to Documents

- Components — `../components/COMPONENT_LIBRARY.md`
- Tokens — `../design-system/DESIGN_TOKENS.md`
- Interaction — `../design-system/UX_PATTERNS.md`
- Content — `../site/CONTENT_STRATEGY.md`
