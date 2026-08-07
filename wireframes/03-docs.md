# WIREFRAME — Docs

> Structural only. One documentation page under Documentation.

---

# Question it answers

> How do I use it?

---

# Layout

```
┌──────────────────────────────────────────────────────────────┐
│ HEADER                                                         │
├───────────────┬────────────────────────────┬─────────────────┤
│ SIDEBAR        │ CONTENT                   │ CONTEXT (right)  │
│ (left)         │                           │ (in-page TOC)    │
│ Documentation │  BREADCRUMBS               │  On this page    │
│ ├ Getting      │  Home/Docs/Guide          │  ├ Introduction  │
│ │ Started      │  ─────────────────────    │  ├ Installation  │
│ │ ├ Install    │  h1  Getting Started      │  ├ Quick start   │
│ │ ├ Quick Start│  intro prose (65ch)       │  └ Concepts      │
│ ├ Guides      │  ─────────────────────    │                  │
│ │ ├ Concepts  │  h2 Installation          │                  │
│ │ └ Tutorials │  Code Block (copy)        │                  │
│ ├ API         │  Terminal (real output)   │                  │
│ │ Reference   │  ─────────────────────    │                  │
│ ├ Architecture│  h2 Quick Start           │                  │
│ └ FAQ         │  Steps + Code Block       │                  │
│ [current page │  ─────────────────────    │                  │
│  marked]      │  RELATED (end)            │                  │
│               │  ├ Next: Concepts         │                  │
│               │  └ Previous: —            │                  │
└───────────────┴────────────────────────────┴─────────────────┘
└── FOOTER ─────────────────────────────────────────────────────┘
```

---

# Region table

| Region | Composition | Purpose |
| --- | --- | --- |
| Sidebar | List, current marked | section TOC |
| Content | prose + Code Block + Terminal + Breadcrumbs | teach |
| Context | in-page TOC | orient within page |
| Related | List of links | forward path |
| Footer | Footer | all destinations |

---

# Responsive notes

- Right TOC collapses into content top below `breakpoint.large`
- Sidebar becomes a Menu trigger below `breakpoint.medium`
- Content region takes the full column
- Code Blocks scroll horizontally, never wrap
