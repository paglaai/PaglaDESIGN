# WIREFRAME — About

> Structural only. Who is behind the ecosystem and why it exists.

---

# Question it answers

> Who is behind PaglaAI, and why is it being built?

---

# Layout

```
┌──────────────────────────────────────────────────────────────┐
│ HEADER                                                         │
├──────────────────────────────────────────────────────────────┤
│   HERO (article variant — left)                                │
│   overline:  ABOUT                                            │
│   headline:  Built openly, locally                            │
│   summary:   one sentence under 65ch                          │
├──────────────────────────────────────────────────────────────┤
│   MISSION (prose, 65ch)                                        │
│   why the ecosystem exists                                    │
├──────────────────────────────────────────────────────────────┤
│   THE ARCHITECT (prose + List)                                 │
│   who leads it, honestly                                      │
├──────────────────────────────────────────────────────────────┤
│   VALUES (3 Cards)                                             │
│   [Local first] [Open] [Simple]                               │
├──────────────────────────────────────────────────────────────┤
│   TIMELINE (Timeline)                                          │
│   date — milestone — line                                     │
│   date — milestone — line                                     │
│   date — milestone — line                                     │
├──────────────────────────────────────────────────────────────┤
│   CONTACT (List or CTA)                                        │
│   email · GitHub · community                                  │
├──────────────────────────────────────────────────────────────┤
│ FOOTER                                                         │
└──────────────────────────────────────────────────────────────┘
```

---

# Region table

| Region | Composition | Purpose |
| --- | --- | --- |
| Hero | `../templates/hero.md` | introduce |
| Mission | prose | answer why |
| The Architect | prose + List | answer who |
| Values | 3 Cards | answer what guides |
| Timeline | Timeline | show the path |
| Contact | List/CTA | connect |
| Footer | Footer | navigate |

---

# Content rule

Keep it authentic. Avoid unnecessary biography
(`../site/CONTENT_STRATEGY.md`). The timeline reflects `../governance/CHANGELOG.md`
milestones — no invented dates.

---

# Responsive notes

- Value Cards stack below `breakpoint.medium`
- Timeline stays single column; date rail narrows but never hides
- Contact List stacks below `breakpoint.small`
