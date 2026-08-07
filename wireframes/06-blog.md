# WIREFRAME — Blog

> Structural only. The article index view.

---

# Question it answers

> What is happening?

---

# Layout

```
┌──────────────────────────────────────────────────────────────┐
│ HEADER                                                         │
├──────────────────────────────────────────────────────────────┤
│   HERO (article variant — left)                                │
│   overline:  BLOG                                             │
│   headline:  Progress, documented                             │
│   summary:   one sentence under 65ch                          │
├──────────────────────────────────────────────────────────────┤
│   FILTER (Chips — wrap)                                        │
│   [All] [Development log] [Release notes] [Design] [Research] │
├──────────────────────────────────────────────────────────────┤
│   POST LIST (Cards, single column)                             │
│   [type chip]  Title                                          │
│   summary line                                                │
│   date · read time · author                                   │
│   ─────────────────────────────────                          │
│   [type chip]  Title                                          │
│   …                                                            │
│   ─────────────────────────────────                          │
│   [type chip]  Title                                          │
│   …                                                            │
├──────────────────────────────────────────────────────────────┤
│   PAGING (Menu or numbered List)                               │
│   ‹ 1 2 3 ›                                                  │
├──────────────────────────────────────────────────────────────┤
│   NEXT STEP (CTA)                                              │
│   primary Button → About or product                            │
├──────────────────────────────────────────────────────────────┤
│ FOOTER                                                         │
└──────────────────────────────────────────────────────────────┘
```

---

# Region table

| Region | Composition | Purpose |
| --- | --- | --- |
| Hero | `../templates/hero.md` | introduce |
| Filter | Chips | narrow by type |
| Post list | Card List | browse |
| Paging | List | step through |
| Next step | CTA | continue |
| Footer | Footer | navigate |

---

# Content rule

- Dates and versions are honest; release notes state the version
  (`../site/CONTENT_STRATEGY.md`)
- Chip filter selection is shown beyond color
  (`../design-system/ACCESSIBILITY.md`)

---

# Responsive notes

- Chips wrap, never scroll horizontally
- Cards become single column below `breakpoint.medium`
- Paging collapses to "prev / next" below `breakpoint.small`
