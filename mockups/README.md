# mockups

High-fidelity visual mockups.

Mockups are token-referenced — every color, size, and spacing decision names
its token from `../design-system/DESIGN_TOKENS.md`. They instantiate the
wireframes for the PaglaAI.space pages.

## Files

| File | Page |
| --- | --- |
| `01-home.md` | Home |
| `02-product.md` | Product (PaglaMLX) |
| `03-docs.md` | Documentation |
| `04-api-reference.md` | API Reference |
| `05-brandkit.md` | BrandKit |
| `06-blog.md` | Blog index |
| `07-about.md` | About |
| `08-404.md` | Not found |

## Conventions

- Light theme is the default; the dark theme re-resolves every surface through
  `[data-theme="dark"]` (D-010).
- Accent (`color.accent.primary`) is meaning-only, never a background fill
  (D-004).
- Motion follows `../design-system/MOTION.md` and resolves to `motion.reduced`
  under reduced motion.
- The system is flat — no shadows, no gradients, no elevation (D-008).
