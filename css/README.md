# CSS

CSS implementation layer that brings the design system to life.

**Purpose:**
CSS is the translation layer between design philosophy (in documents) and working product.

**Principles:**
- Derive all values from `design-system/DESIGN_TOKENS.md`
- Never invent values inline
- Use CSS Custom Properties (`--color-base-ink`, `--space-4`, etc.)
- Organize in layers: tokens → base → utilities → components → layout
- No magic numbers; no repeated values

**Start here:**
Read `design-system/CSS_ARCHITECTURE.md` for the layer model and implementation strategy.

**Every stylesheet should:**
1. Import or reference tokens
2. Follow the layer model
3. Use semantic class names
4. Support light and dark themes through CSS variables
5. Include focus states and reduced-motion support
