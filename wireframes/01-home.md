# WIREFRAME — Home

> Structural only. Components and content are decided by the mockup.

---

# Question it answers

> What is PaglaAI?

---

# Layout

```
┌──────────────────────────────────────────────────────────────┐
│ HEADER  [wordmark]  [nav: Products Docs BrandKit Blog About]  [theme]│
├──────────────────────────────────────────────────────────────┤
│                                                                │
│   HERO (marketing variant — centered)                          │
│   overline:  PAGLA · LOCAL AI, OPENLY BUILT                     │
│   headline:  The local AI ecosystem                            │
│   summary:   one sentence under 65ch                           │
│   [primary Button]  [ghost Button]                             │
│   │  Terminal (real output)                                  │
│                                                                │
├──────────────────────────────────────────────────────────────┤
│   VISION                                                       │
│   h2 statement + prose (maxWidth body)                        │
├──────────────────────────────────────────────────────────────┤
│   ECOSYSTEM (surface band)                                     │
│   h2  │  List: PaglaMLX · PaglaCPP · PaglaROUTER · …           │
├──────────────────────────────────────────────────────────────┤
│   PRODUCTS (Feature Grid — 3 Cards)                            │
│   h2  │  [Card icon+name+line] [Card] [Card]                   │
├──────────────────────────────────────────────────────────────┤
│   PHILOSOPHY (3 Cards)                                         │
│   h2  │  [Principle] [Principle] [Principle]                   │
├──────────────────────────────────────────────────────────────┤
│   DOCUMENTATION                                                │
│   h2  │  Code Block (install)  │  Card → docs                  │
├──────────────────────────────────────────────────────────────┤
│   UPDATES (List with dates)                                    │
│   h2  │  post → date → read time                               │
├──────────────────────────────────────────────────────────────┤
│   COMMUNITY (CTA)                                              │
│   h2 statement + one primary Button                            │
├──────────────────────────────────────────────────────────────┤
│ FOOTER  [product links][docs][github][brand][blog][about][legal]│
└──────────────────────────────────────────────────────────────┘
```

---

# Region table

| Region | Composition | Purpose |
| --- | --- | --- |
| Header | `../templates/sections.md` Footer inverse + `../site/NAVIGATION.md` | orient + navigate |
| Hero | `../templates/hero.md` | answer "what is this" |
| Vision | statement block | answer "why it exists" |
| Ecosystem | surface band + List | show the whole |
| Products | Feature Grid | show what exists today |
| Philosophy | 3 Cards | show how it is built |
| Documentation | Code Block + Card | open the learning path |
| Updates | List with dates | show it is alive |
| Community | CTA | one clear next step |
| Footer | Footer | all destinations |

---

# Responsive notes

- Hero collapses to single column below `breakpoint.medium`; display headline
  steps down one size
- Feature Grid 3 → 1 column; Philosophy 3 → 1 column
- Header nav → Menu trigger below `breakpoint.medium`
