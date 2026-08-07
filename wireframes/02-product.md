# WIREFRAME — Product

> Structural only. Uses the PaglaMLX product as the first instantiation.

---

# Question it answers

> Why does this product exist?

---

# Layout

```
┌──────────────────────────────────────────────────────────────┐
│ HEADER                                                         │
├──────────────────────────────────────────────────────────────┤
│   BREADCRUMBS   Home / Products / PaglaMLX                     │
├──────────────────────────────────────────────────────────────┤
│   HERO (product variant — two column)                          │
│   overline:  PRODUCT                                          │
│   headline:  PaglaMLX                                         │
│   summary:   one sentence of value                            │
│   [primary: docs] [ghost: GitHub]                             │
│   │  Terminal — real install + run output                    │
├──────────────────────────────────────────────────────────────┤
│   OVERVIEW                                                     │
│   prose (maxWidth body)                                       │
├──────────────────────────────────────────────────────────────┤
│   PROBLEM (surface band)                                       │
│   statement + List of pains                                   │
├──────────────────────────────────────────────────────────────┤
│   SOLUTION                                                     │
│   prose + Feature Grid (2 cols)                               │
├──────────────────────────────────────────────────────────────┤
│   KEY FEATURES (Feature Grid — 3 Cards)                        │
│   h2  │  [icon name line] × 3                                 │
├──────────────────────────────────────────────────────────────┤
│   ARCHITECTURE                                                 │
│   List of layers / diagram                                    │
├──────────────────────────────────────────────────────────────┤
│   DOCUMENTATION (surface band)                                 │
│   Code Block (install)  │  Card → getting started             │
├──────────────────────────────────────────────────────────────┤
│   DOWNLOADS                                                    │
│   List: source, binary, package                               │
├──────────────────────────────────────────────────────────────┤
│   ROADMAP (Timeline)                                           │
│   date — milestone — line                                     │
├──────────────────────────────────────────────────────────────┤
│   FAQ (Tabs)                                                   │
│   [tab: install] [tab: usage] [tab: limits] → one panel       │
├──────────────────────────────────────────────────────────────┤
│   NEXT STEP (CTA)                                              │
│   one primary Button → docs or GitHub                         │
├──────────────────────────────────────────────────────────────┤
│ FOOTER                                                         │
└──────────────────────────────────────────────────────────────┘
```

---

# Region table

| Region | Composition | Purpose |
| --- | --- | --- |
| Breadcrumbs | Breadcrumbs | orient in the tree |
| Hero | `../templates/hero.md` product variant | name + value |
| Overview | prose | one-read summary |
| Problem | statement + List | justify existence |
| Solution | prose + Feature Grid | show the fix |
| Key Features | Feature Grid | enumerate capabilities |
| Architecture | List/diagram | show structure |
| Documentation | Code Block + Card | teach |
| Downloads | List | obtain |
| Roadmap | Timeline | show direction |
| FAQ | Tabs | answer questions |
| Next step | CTA | one clear action |

---

# Responsive notes

- Hero and Terminal stack below `breakpoint.medium`
- Feature Grid 3 → 1 column; FAQ Tabs wrap
- Breadcrumbs truncate to two nearest levels on small screens
