# css

Reference implementation of the PaglaAI design token layer, per
[`design-system/CSS_ARCHITECTURE.md`](../design-system/CSS_ARCHITECTURE.md).

These styles **implement** the design system; they do not define it. Values are
locked in [`design-system/DESIGN_TOKENS.md`](../design-system/DESIGN_TOKENS.md)
and are ported here verbatim.

## Files

- `tokens.css` — canonical token layer. Every locked value from
  `DESIGN_TOKENS.md` as CSS custom properties on `:root` (light) and
  `[data-theme="dark"]` (same semantics, new values).
- `base.css` — Layer 2: reset, element defaults, typography, focus states,
  reduced motion, responsive type scaling.
- `utilities.css` — Layer 3: single-purpose helpers, deliberately used,
  value-driven from tokens.

## Reference, not shipped UI

These files are the **reference implementation** of the token/base layer.
Consumers (e.g. `PaglaAI.space`, future products) import or graft from here so
every surface shares one source of truth.

No UI framework or component package lives in this repository. Frameworks and
rendered surfaces (including brandkit HTML) belong to their consumer repos and
inherit from these tokens (see `DECISIONS.md`, D-013).

## Usage

Load tokens first, then base, then utilities:

```css
@import url("./tokens.css");
@import url("./base.css");
@import url("./utilities.css");
```

Or copy the files and keep them in sync with `DESIGN_TOKENS.md` through the
decision workflow.