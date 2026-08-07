# WIREFRAME — API Reference

> Structural only. The anatomy of one endpoint page.

---

# Question it answers

> What does the API accept, and what does it return?

---

# Layout

```
┌──────────────────────────────────────────────────────────────┐
│ HEADER                                                         │
├───────────────┬───────────────────────────────────────────────┤
│ SIDEBAR        │ CONTENT                                       │
│ API Reference │  BREADCRUMBS  Home/Docs/API Reference          │
│ ├ Authentication│  ──────────────────────────────────────     │
│ ├ Models        │  h1  POST /v1/chat/completions               │
│ └ Endpoints     │  [Code Block — request sample, copy]         │
│   ├ Chat        │  ──────────────────────────────────────     │
│   │ ├ Create    │  h2  Request                                 │
│   │ └ Stream    │  Table: parameter · type · required · desc   │
│   ├ Models      │  ──────────────────────────────────────     │
│   └ Files       │  h2  Response                                │
│ [current page   │  Code Block — response schema                │
│  marked]        │  Table: field · type · description           │
│                 │  ──────────────────────────────────────     │
│                 │  h2  Errors                                  │
│                 │  Table: status · message · retry             │
│                 │  ──────────────────────────────────────     │
│                 │  h2  Examples                                │
│                 │  Tabs: [curl] [python] [js] → one Code Block │
│                 │  ──────────────────────────────────────     │
│                 │  RELATED                                    │
│                 │  ├ Authentication                            │
│                 │  └ Rate limits                               │
└───────────────┴───────────────────────────────────────────────┘
└── FOOTER ──────────────────────────────────────────────────────┘
```

---

# Region table

| Region | Composition | Purpose |
| --- | --- | --- |
| Sidebar | List, current marked | endpoint tree |
| Endpoint heading | h1 + request line | identity |
| Request | Code Block + Table | show and specify |
| Response | Code Block + Table | show and specify |
| Errors | Table | prepare for failure |
| Examples | Tabs → Code Block | exercise |
| Related | List | connect |

---

# Anatomy rule

Every endpoint page follows this exact order — request, response, errors,
examples. One predictable anatomy everywhere
(`../references/INSPIRATION.md`).

---

# Responsive notes

- Sidebar → Menu trigger below `breakpoint.medium`
- Parameter/field Tables scroll horizontally; header row stays readable
- Example Tabs wrap; the active panel stays one Code Block
