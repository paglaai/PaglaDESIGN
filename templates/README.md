# templates

Reusable page-level compositions.

Templates are not components. They compose components into page-level layouts:
landing page, product page, blog, documentation, case study, hero.

Components live in `components/`; templates live here.

## Files

| Template | Composes |
| --- | --- |
| `hero.md` | The opening composition: headline, summary, terminal, actions |
| `landing.md` | Home page: hero → vision → products → philosophy → updates |
| `product.md` | Product page: hero → overview → features → architecture → FAQ |
| `docs.md` | Documentation page: sidebar → prose → code → next steps |
| `blog.md` | Blog index and article page |
| `case-study.md` | Narrative: problem → solution → outcome |
| `sections.md` | Reusable section compositions: Feature Grid, CTA, Timeline, Footer |

## Conventions

- Every template references components from `../components/COMPONENT_LIBRARY.md`.
- Every spacing, size, and color reference comes from
  `../design-system/DESIGN_TOKENS.md`.
- Interaction follows `../design-system/UX_PATTERNS.md`.
- Wireframes (structural) and mockups (token-referenced) instantiate these
  templates for the PaglaAI.space pages.

Templates describe what to compose and why. Wireframes and mockups decide the
specific content.
