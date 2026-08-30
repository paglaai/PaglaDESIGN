# MOCKUP — Footer (OpenAI-scale, PaglaDESIGN)

> High-fidelity, token-referenced. Light is default; dark re-resolves via `[data-theme="dark"]`.

---

# Base

- **Surface:** `color.base.paper` (`#FFFFFF` / `#0A0A0B`), top hairline `color.base.border`
- **Padding:** `space.16` top (section rhythm), `space.8` bottom, `space.12` between grid and bottom bar
- **Layout:** `layout.maxWidth` + `layout.contentPaddingWide`; grid gap `space.8`

---

# Typography

| Element | Token |
| --- | --- |
| Subhead (Research / Products / Developers …) | `font.size.caption`, `font.weight.semibold`, `font.tracking.uppercase`, `color.base.muted`, uppercase |
| List links | `font.size.small`, `font.weight.regular`, `color.base.muted` → `color.base.ink` on hover, underline on hover only |
| Bottom bar text | `font.size.small`, `color.base.muted` |
| Wordmark (if present) | `font.size.h4`, `font.weight.light`, `font.tracking.display`, `color.base.ink` |
| Locale pill | `font.size.small`, `color.base.muted`, pill `radius.pill` |

Spacing: subhead `space.6` top (first subhead 0), `space.3` bottom; list item `space.2` bottom.

---

# Composition

| Column | Subheads & Links | Source |
| --- | --- | --- |
| 1 — Research | Research → Research Index / Overview / Color & Tokens · Latest Advancements → v1.7 / v1.6 / v1.0 · Safety → Accessibility / Motion Safety / Security & Privacy / Trust | `design-system/*`, `governance/CHANGELOG.md` |
| 2 — Products | Products → PaglaCHAT ↗ / PaglaMLX ↗ / PaglaROUTER ↗ / PaglaDESIGN ↗ / PaglaCPP / Release Notes · API Platform → Overview / API Reference ↗ / BrandKit / Docs ↗ | `site/NAVIGATION.md` |
| 3 — Developers / Business | Developers → Docs ↗ / API Reference / Design Tokens ↗ / Resources ↗ / Forum ↗ · Business → Overview / Solutions / Resources / Customer Stories / Contact Sales | `templates/sections.md` |
| 4 — Company | Company → About Us / Our Charter / Careers / News · Support → Help Center ↗ | `about/index.html` |
| 5 — More | More → Stories / Academy / GitHub / Sitemap / Podcast / RSS · Terms & Policies → Terms of Use / Privacy Policy / Other Policies | `governance/*` |

External `↗` only for off-site (`github.com/paglaai/*`); internal stays plain. Display brand `PaglaDESIGN` / `PaglaAI.space` kept in labels; repo URLs use canonical `paglaai/pagladesign`, `paglaai/paglaai.space`.

---

# Bottom bar

| Element | Tokens |
| --- | --- |
| Hairline | `color.base.border`, 1px, `space.6` top padding |
| Social icons | 16px SVG, `fill: currentColor`, target `interactive.minTarget` (44×44), `radius.sm`, `border: 1px transparent` → `color.state.hover` on hover, `color.base.ink` on hover |
| Locale pill | `color.base.surface` bg, `color.base.border`, `radius.pill`, `space.2`/`space.4` padding, `gap: space.2`, globe icon 12px stroke `1.5` |
| Legal | `PaglaAI © 2015–2026` + `Manage Cookies` link (`color.base.muted` → `ink` on hover) |

---

# Dark theme

Same semantics, inverted values: paper `#0A0A0B`, surface `#17171A`, border `#2A2A2E`, muted `#9AA0AE`, ink `#FFFFFF`. Social hover stays `ink` on `hover` border. Locale pill bg `color.base.surface` (`#17171A`) on dark.

---

# Reduced motion

No entrance animation. Hover transitions `color` + `border-color` `motion.duration.fast` `motion.easing.default` only; `motion.reduced` resolves to `0ms`.

---

# Implementation notes

- Grid: `.footer-grid` `repeat(5,1fr)` @64rem, `repeat(2,1fr)` @48rem, `1fr` @<40rem; `margin-bottom: space.12`
- Subhead: `.footer-col__subhead` uppercase muted; first-child `margin-top:0`
- Bottom: `.footer-bottom` + `.footer-social` + `.footer-locale` (see `../paglaai.space/assets/css/site.css` — tokens mirror `site.css`)
- Accessibility: landmark `<footer>` with `aria-label="Site footer"` if multiple footers; social links have `aria-label`
