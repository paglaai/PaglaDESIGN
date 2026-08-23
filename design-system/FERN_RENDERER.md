# FERN_RENDERER

> *The human-facing renderer. What a reader sees when they open a PaglaAI doc page.*

---

# Purpose

FERN_RENDERER defines how PaglaDESIGN Markdown is rendered into rich,
accessible, themed HTML for human readers.

It specifies component mapping, typography, layout, navigation, and
accessibility requirements. It does not provide a framework, build step, or
runtime. Those belong to the consumer surface — `PaglaAI.space`, product
documentation portals, and any other surface that serves human readers.

---

# Output Format

FERN produces structured HTML with semantic class names.

The output is token-referenced. Every value that affects presentation comes from
`css/tokens.css` custom properties. No value is invented here.

```html
<article class="doc-page">
  <nav class="doc-breadcrumbs" aria-label="Breadcrumb">
    <ol>
      <li><a href="/">Home</a></li>
      <li><a href="/docs/">Documentation</a></li>
      <li aria-current="page">Design Tokens</li>
    </ol>
  </nav>
  <h1 class="doc-h1">Design Tokens</h1>
  <div class="doc-body">
    <p>...</p>
  </div>
</article>
```

The `doc-` prefix distinguishes renderer output classes from component library
classes. Component classes use their library names (e.g. `btn`, `card`, `tabs`).

---

# Typography

FERN uses the type scale defined in `css/tokens.css`.

| Markdown Element | HTML | CSS Class | Token Reference |
|---|---|---|---|
| `# Heading` | `h1` | `.doc-h1` | `--font-size-h1`, `--font-weight-semibold`, `--font-line-height-heading` |
| `## Heading` | `h2` | `.doc-h2` | `--font-size-h2`, `--font-weight-semibold`, `--font-line-height-heading` |
| `### Heading` | `h3` | `.doc-h3` | `--font-size-h3`, `--font-weight-medium`, `--font-line-height-heading` |
| `#### Heading` | `h4` | `.doc-h4` | `--font-size-h4`, `--font-weight-medium`, `--font-line-height-heading` |
| Body paragraph | `p` | `.doc-body` | `--font-size-body`, `--font-line-height-body` |
| Large body | `p` | `.doc-body-large` | `--font-size-body-large`, `--font-line-height-body` |
| Small text | `small` | `.doc-small` | `--font-size-small` |
| Caption | `figcaption` | `.doc-caption` | `--font-size-caption` |
| Code inline | `code` | `.doc-code` | `--font-size-code`, monospace |
| Code block | `pre > code` | `.doc-code-block` | `--font-size-code` |

Reading measure is bounded by `--font-max-width-body: 65ch`.

---

# Layout

FERN respects the layout tokens defined in `css/tokens.css`.

| Layout Concern | Token | Value |
|---|---|---|
| Content width | `--layout-max-width` | `75rem` |
| Content padding | `--layout-content-padding` | `1rem` |
| Wide content padding | `--layout-content-padding-wide` | `2rem` |
| Reading measure | `--font-max-width-body` | `65ch` |

Spacing between sections follows the `0.25rem` base unit:

- Section gap: `--space-8` (`2rem`)
- Paragraph gap: `--space-4` (`1rem`)
- Inline gap: `--space-2` (`0.5rem`)

---

# Color

FERN uses the semantic color tokens. No raw hex values are rendered.

| Purpose | Token |
|---|---|
| Page background | `--color-base-paper` |
| Text color | `--color-base-ink` |
| Surface (cards, sidebars) | `--color-base-surface` |
| Borders | `--color-base-border` |
| Muted text | `--color-base-muted` |
| Links | `--color-accent-primary` |
| Focus indicator | `--color-state-focus` |
| Hover state | `--color-state-hover` |

Dark theme is resolved through `[data-theme="dark"]` (D-010). FERN does not
define theme logic; it inherits the resolved values.

---

# Component Mapping

FERN maps Markdown elements to components registered in
`components/COMPONENT_LIBRARY.md`. Only Active components are used.

| Markdown Pattern | Rendered Component | Component Role |
|---|---|---|
| `![alt](src)` | `img` inside a `figure` | Content image |
| `[text](url)` | `a` | Link |
| `` `code` `` | `code.doc-code` | Inline code |
| ```` ```lang ``` ```` | `Code Block` component | Code presentation |
| ``` console output ``` | `Terminal` component | CLI output |
| `- item` / `* item` | `ul > li` | Unordered list |
| `1. item` | `ol > li` | Ordered list |
| `> quote` | `blockquote` | Block quote |
| `| col | col |` | `Table` component | Structured comparison |
| `---` (between sections) | Tabs or section break | Related view switch |
| `[[TOC]]` | `Breadcrumbs` component | Navigation trail |

Components are used as documented. No variant is invented.

---

# Navigation

FERN renders two navigation patterns.

**Breadcrumbs** — a trail showing the current page's location in the site
hierarchy.

Uses the `Breadcrumbs` component from `COMPONENT_LIBRARY.md`. The current page
is text, never a link.

**Table of Contents** — generated from `h2` and `h3` headings in the document
body. Sticky on desktop. Hidden on mobile.

Both patterns follow the accessibility requirements in
`design-system/ACCESSIBILITY.md`.

---

# Theme Resolution

FERN does not implement theme switching.

Theme resolution is handled by the consumer surface. FERN inherits the active
theme through `[data-theme="dark"]` and the token values in `css/tokens.css`.

The consumer's theme toggle is an implementation detail outside this document.

---

# Motion

FERN applies motion only where `design-system/MOTION.md` permits.

Permitted motion:

- Focus transitions: `--motion-duration-fast`
- Hover state changes: `--motion-duration-base`
- Inertial scrolling on TOC: `--motion-duration-base`

No motion is applied to page transitions, section reveals, or decorative
elements.

Reduced motion is respected via `prefers-reduced-motion`. When active, all
motion durations resolve to `--motion-reduced: 0ms`.

---

# Accessibility Gates

FERN output must pass the baseline defined in `design-system/ACCESSIBILITY.md`.

Minimum requirements:

- Semantic HTML: `article`, `nav`, `main`, `section`, `heading` hierarchy
- Focus visible: `color-state-focus` on every interactive element
- Minimum target: `--interactive-min-target: 2.75rem` for all interactive
  elements
- Reduced motion: `prefers-reduced-motion` honored
- Screen reader: landmarks, labels, and live regions where appropriate
- Contrast: text meets WCAG AA against its background using the semantic
  tokens

---

# Responsive Behavior

FERN adapts to the breakpoints defined in `css/tokens.css`:

| Breakpoint | Token | Width |
|---|---|---|
| Small | `--breakpoint-small` | `40rem` |
| Medium | `--breakpoint-medium` | `48rem` |
| Large | `--breakpoint-large` | `64rem` |
| Extra large | `--breakpoint-xlarge` | `80rem` |

On small screens:
- Navigation collapses to a single column.
- TOC moves to the bottom or is hidden.
- Code blocks scroll horizontally rather than wrapping.

No breakpoint invents its own spacing or typography scale.

---

# Code Blocks

Code blocks use the `Code Block` component from `COMPONENT_LIBRARY.md`.

Rules:
- Code renders at `font-size-code`.
- Long lines scroll horizontally; wrapping is opt-in via a class.
- Syntax highlighting stays minimal (D-004).
- Copy affordance is keyboard-reachable and announced for screen readers.
- Language label is shown when present.

---

# Terminal Output

CLI output uses the `Terminal` component from `COMPONENT_LIBRARY.md`.

Rules:
- Static by default: real output, never faked.
- Terminal chrome is optional.
- Prompt lines are styled distinctly.
- Interactive terminal affordances are explicit and announced.

---

# Error and Empty States

Pages may fail to render. FERN defines two fallback states:

**Empty state** — the page has no renderable content after routing.

Rendered as a `Card` component with a message and a link to the documentation
index.

**Error state** — the frontmatter is invalid or the source is malformed.

Rendered as a `Card` component with an error message. The error is specific
enough to act on (e.g. "audience array is empty" rather than "invalid page").

Both states use `--color-accent-error` for emphasis.

---

# Relationship to Documents

- Token values — `design-system/DESIGN_TOKENS.md`
- Token CSS — `css/tokens.css`
- Component library — `components/COMPONENT_LIBRARY.md`
- Component language — `design-system/COMPONENTS.md`
- CSS implementation — `design-system/CSS_ARCHITECTURE.md`
- Accessibility baseline — `design-system/ACCESSIBILITY.md`
- Motion principles — `design-system/MOTION.md`
- Renderer API — `design-system/RENDERER_API.md`
- Constitutional spec — `governance/AUDIENCE_RENDERER_SPEC.md`

---

# Final Principle

> **FERN serves the reader.**
>
> **It does not decorate.**
>
> **It communicates.**
