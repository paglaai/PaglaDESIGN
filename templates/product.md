# PRODUCT

> *Every product page follows the same spine. Consistency across products outranks individual creativity.*

---

# Purpose

The product template presents one PaglaAI product: why it exists, what it does,
how it works, and where to start.

Consistency between product pages is the point — a visitor who learns one
product page can navigate any of them.

---

# Question it answers

> Why does this product exist?

---

# Composition

Sections in order:

| # | Section | Question it answers | Building blocks |
| --- | --- | --- | --- |
| 1 | Hero | What is it? | `HERO.md` (product variant, Terminal or screenshot) |
| 2 | Overview | What does it do in one read? | prose block under `font.maxWidth.body` |
| 3 | Problem | What did it replace? | short statement + List of pains |
| 4 | Solution | How does it fix it? | prose + Feature Grid |
| 5 | Key Features | What can I do with it? | Feature Grid, Cards with icon + name + line |
| 6 | Architecture | How is it built? | structural diagram or List of layers |
| 7 | Documentation | How do I learn it? | Code Block (install) + Card into docs |
| 8 | Downloads | How do I get it? | List of download/install options |
| 9 | Roadmap | Where is it going? | Timeline (`sections.md`) |
| 10 | FAQ | What will I ask? | Tabs or List of question/answer pairs |
| 11 | Next step | Where do I go now? | CTA — docs, GitHub, or download |

---

# Spacing rhythm

- Section gap: `space.16`
- Feature Grid rows: `space.8` between items, `space.6` between icon, name, and
  line within a Card
- Alternating paper/surface sections as in `landing.md`

---

# Content discipline

- The hero names the product and one sentence of value; the overview expands,
  never repeats
- Features are behaviors, not adjectives — "runs fully on-device" beats "fast"
- Terminal/Code Block proofs show real output, never implied capability
  (`../references/INSPIRATION.md`)
- Every section that can link out (docs, GitHub, download) offers exactly one
  clear path

---

# Responsive

- Architecture and Features collapse to one column below `breakpoint.medium`
- The hero proof block stacks below the text at `breakpoint.medium`
- Timeline stays a single column; the date rail narrows, never disappears

---

# Behavior

- Tabs (where FAQ or feature details use them) follow the Tabs component
  behavior — arrow-key navigation, one visible panel
- Nothing auto-plays; screenshots and terminals are static
- FAQ answers are navigable by keyboard when expanded inline

---

# Relationship to Documents

- Structure — `../site/SITEMAP.md`
- Content — `../site/CONTENT_STRATEGY.md`
- Sections — `sections.md`
- Components — `../components/COMPONENT_LIBRARY.md`
- Tokens — `../design-system/DESIGN_TOKENS.md`
