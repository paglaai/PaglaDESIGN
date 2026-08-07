# WIREFRAME — BrandKit

> Structural only. One page for how PaglaAI should be represented.

---

# Question it answers

> How should PaglaAI be represented?

---

# Layout

```
┌──────────────────────────────────────────────────────────────┐
│ HEADER                                                         │
├──────────────────────────────────────────────────────────────┤
│   BREADCRUMBS   Home / BrandKit                                │
├──────────────────────────────────────────────────────────────┤
│   HERO (article variant — left)                                │
│   overline:  BRANDKIT                                         │
│   headline:  Represent PaglaAI, exactly                        │
│   summary:   one sentence under 65ch                          │
├──────────────────────────────────────────────────────────────┤
│   TABS                                                         │
│   [Brand] [Logo] [Typography] [Colors] [Icons] [Downloads]     │
│   ───────────────────────────────────────────────────────     │
│   PANEL — Brand                                                │
│   story prose (65ch)                                          │
│   PANEL — Logo                                                 │
│   [Pagla Face, clearspace frame]  + usage List                 │
│   PANEL — Typography                                          │
│   Specimen: PaglaAI Sans  +  token Table                       │
│   PANEL — Colors                                               │
│   swatch Table: token · value · usage                          │
│   PANEL — Icons                                                │
│   icon grid + semantics List                                   │
│   PANEL — Downloads                                            │
│   List: asset → format → Button (Download)                     │
├──────────────────────────────────────────────────────────────┤
│   USAGE GUIDELINES (prose + List)                              │
│   do / don't List of representation rules                      │
├──────────────────────────────────────────────────────────────┤
│   NEXT STEP (CTA)                                              │
│   primary Button → Downloads                                   │
├──────────────────────────────────────────────────────────────┤
│ FOOTER                                                         │
└──────────────────────────────────────────────────────────────┘
```

---

# Region table

| Region | Composition | Purpose |
| --- | --- | --- |
| Breadcrumbs | Breadcrumbs | orient |
| Hero | `../templates/hero.md` | introduce |
| Tabs | Tabs — six panels | section one topic |
| Usage guidelines | prose + List | set boundaries |
| Next step | CTA | download |
| Footer | Footer | navigate |

---

# Content rule

The BrandKit page reflects `../brand/BRAND.md` and nothing else. It is the
consumer surface of the canonical brand — token values come from
`../design-system/DESIGN_TOKENS.md`, never invented here.

---

# Responsive notes

- Tabs collapse to a stacked Menu below `breakpoint.medium`
- Color swatch Table becomes stacked rows; tokens stay readable
- Logo specimen scales down without losing the clearspace frame
