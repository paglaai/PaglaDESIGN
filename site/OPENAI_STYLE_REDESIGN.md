# OPENAI-STYLE REDESIGN — paglaai.space

> Editorial density, minimal chrome, type-led hierarchy. DesignDNA compliant.

**Status:** Brief (D-024)  
**Target surface:** https://paglaai.space  
**Reference posture:** openai.com (structure & restraint — not a clone)

---

## Goal

Make paglaai.space feel like a peer to openai.com in **editorial clarity**:

- One strong headline
- Short supporting line
- Single primary CTA
- Sparse primary nav
- Product bands that read as a system, not a marketing collage
- Research / blog as secondary, not competing heroes

Wordmarks **PaglaAI** and **OpenAI** are structurally similar (short, all-caps-friendly sans). That is an opportunity for parallel *layout grammar*, not visual imitation of the OpenAI mark.

---

## Non-goals

- Copying OpenAI’s logo, colors, or copy
- Dashboard density
- Heavy illustration or gradient fills
- Accent as background

---

## Page grammar (home)

```
┌─────────────────────────────────────────────┐
│  minimal nav: Products · Docs · Brand · Blog │
├─────────────────────────────────────────────┤
│  HERO                                        │
│  overline (optional)                         │
│  display headline (Pagla Sans Light)         │
│  one sentence ≤ 65ch                         │
│  primary CTA + ghost secondary               │
├─────────────────────────────────────────────┤
│  PRODUCT SYSTEM                              │
│  grid of products from ecosystem.json        │
│  (auto-generated — never hand-maintained)    │
├─────────────────────────────────────────────┤
│  DESIGN AUTHORITY                            │
│  short band → PaglaDESIGN / DesignDNA        │
├─────────────────────────────────────────────┤
│  LATEST (blog / releases)                    │
│  3 cards max from GitHub / blog index        │
├─────────────────────────────────────────────┤
│  FOOTER — sparse, structured                 │
└─────────────────────────────────────────────┘
```

---

## Token mapping

| OpenAI-like trait | PaglaDESIGN mapping |
|-------------------|---------------------|
| Large calm type | `font.size.display` / `h1`, weight light |
| Monochrome base | ink / paper |
| Quiet accent | `#6B7EFF` meaning only |
| Air between sections | `space.16`–`space.24` |
| Narrow reading | `layout.reading` / 65ch |
| Minimal nav | site header utility + 4–5 primary links |

---

## Automation hooks

| Source | Reflects on site as |
|--------|---------------------|
| `ecosystem.json` active products | Product grid / product pages |
| GitHub releases (org) | Latest releases band |
| Public repos (org) | Storefront feed → apphole.store + site products |
| PaglaDESIGN token push | CSS rebuild + hard cache-bust |
| Blog markdown commits | Blog index |

Hand-edited product lists are forbidden once the generator is live.

---

## Implementation phases

1. **DNA lock** — `DESIGN_DNA.md` + D-024 (done in same change set)
2. **Home shell** — hero + nav + footer to editorial grammar
3. **Product grid generator** — read ecosystem.json at build or via worker
4. **Release / repo reflection** — worker already has GitHub token path; extend jobs
5. **apphole.store** — DNS + catalog surface (separate deploy project)

---

## Acceptance

- [ ] Home matches the grammar above
- [ ] No product name on the home grid that is missing from ecosystem.json
- [ ] DesignDNA checklist passes
- [ ] Deploy still green on push to main
