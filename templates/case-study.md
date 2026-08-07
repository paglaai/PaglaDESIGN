# CASE_STUDY

> *A case study is a story with evidence. The evidence is real.*

---

# Purpose

The case study template composes a narrative page: problem, solution, outcome.

It is used where a product or a design decision is explained in depth. It
persuades by showing, never by claiming.

---

# Question it answers

> What was the problem, what did we do, and what happened?

---

# Composition

Sections in order:

| # | Section | Question it answers | Building blocks |
| --- | --- | --- | --- |
| 1 | Hero | What was done? | `HERO.md` (marketing variant, one-line result in the summary) |
| 2 | Context | What existed before? | prose block under `font.maxWidth.body` |
| 3 | Problem | What was wrong? | statement + List of constraints |
| 4 | Decision | What was chosen? | prose + `Table` of alternatives and trade-offs |
| 5 | Solution | How was it built? | prose, Code Block/Terminal, structural List |
| 6 | Outcome | What changed? | `Table` or List of measurable results |
| 7 | Reflection | What was learned? | prose |
| 8 | Next step | Where do I go? | CTA — related docs or post |

---

# Content discipline

- Outcomes are concrete: versions, timings, or before/after facts — never
  adjectives alone
- The decision section mirrors `../governance/DECISIONS.md` honesty: context,
  decision, alternatives, trade-offs
- Code and terminal output are authentic
  (`../references/INSPIRATION.md`)

---

# Spacing rhythm

- Section gap: `space.16`
- Tables get `space.6` above and below; the reading column applies to prose
  only, tables may use the full content region

---

# Responsive

- Tables scroll horizontally on small screens; the header row stays readable
- The decision Table collapses to stacked Cards below `breakpoint.medium`
- Terminal proof stacks under the prose at `breakpoint.medium`

---

# Behavior

- The outcome Table's most important comparison is the first column pair —
  no added emphasis, no color-coded cells beyond the state accents
- Everything static; no scroll-driven reveals
  (`../design-system/UX_PATTERNS.md`)

---

# Relationship to Documents

- Honest decisions — `../governance/DECISIONS.md`
- Content — `../site/CONTENT_STRATEGY.md`
- Sections — `sections.md`
- Components — `../components/COMPONENT_LIBRARY.md`
