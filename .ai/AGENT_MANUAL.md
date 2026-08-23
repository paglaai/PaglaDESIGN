# AGENT_MANUAL

> *Operating procedure for AI coding agents working within the PaglaDESIGN authority.*

---

## 1. Mission & Operating Contract

You are contributing to **PaglaDESIGN** — the canonical design authority for the entire PaglaAI ecosystem.

This repository is not a website project. It defines the visual language, user experience, design system, and design governance that every current and future PaglaAI product inherits.

**Your operating contract:**

1. **Design First** (D-001): Never begin by writing code. Begin by understanding the problem, then research, then document, then design, then review, then implement.
2. **Read before working**: Before making any changes, review in order: `README.md` → `VISION.md` → `DESIGN.md` → `PRINCIPLES.md` → `DECISIONS.md` → `ROADMAP.md`.
3. **Protect consistency**: Prefer reusable solutions. Think about the entire ecosystem. Explain important decisions.
4. **Document every meaningful change**: Documentation is part of the deliverable. If introducing a new component, pattern, layout, interaction, or guideline — update the relevant documentation before or alongside implementation.

You are expected to act like a design engineer, not an autocomplete engine.

---

## 2. PaglaDESIGN as Canonical Authority

### 2.1 What PaglaDESIGN Governs

- Brand Identity (`brand/BRAND.md`, `brand/BRANDKIT.md`)
- Design Tokens (`design-system/DESIGN_TOKENS.md`)
- Color System (`design-system/COLOR_SYSTEM.md`)
- Typography (`design-system/TYPOGRAPHY.md`, `design-system/PAGLA_SANS.md`)
- Motion (`design-system/MOTION.md`)
- Accessibility (`design-system/ACCESSIBILITY.md`)
- Icons (`design-system/ICONS.md`)
- CSS Architecture (`design-system/CSS_ARCHITECTURE.md`)
- Components (`components/COMPONENTS.md`, `components/COMPONENT_LIBRARY.md`)
- Templates (`templates/`)
- Wireframes & Mockups (`wireframes/`, `mockups/`)
- Reference CSS (`css/tokens.css`, `css/base.css`, `css/utilities.css`)

### 2.2 The 13 PRINCIPLES

From `PRINCIPLES.md` — these are non-negotiable:

1. Design the System, Not the Page
2. Clarity Over Cleverness
3. Purpose Before Aesthetics
4. Typography Is the Primary Interface
5. Whitespace Is Content
6. Consistency Builds Trust
7. Performance Is Part of User Experience
8. Accessibility Is Non-Negotiable
9. Motion Must Communicate
10. Documentation Before Implementation
11. Think in Ecosystems
12. Timeless Over Trendy
13. Question Everything

### 2.3 Ecosystem

PaglaDESIGN provides the design foundation for:

| Product | Purpose |
|---|---|
| PaglaOS | The operating substrate |
| PaglaAI | Intelligence without permission |
| PaglaAPI | One endpoint, any model |
| PaglaCPP | Systems speed, unhinged scale |
| PaglaROUTER | Route anything, anywhere |
| PaglaMLX | Local inference, infinite context |
| PaglaMTP | Parallel thought, in production |
| PaglaUI | Interface for the post-rational era |
| PaglaBRAND | Brand identity system |
| PaglaCHAT | Conversational interface |

### 2.4 Authority Relationship

D-013 declares: PaglaDESIGN ships the **token + base + utilities** CSS layers as a reference implementation. No UI framework, component package, or rendered HTML surface lives in this repository. Frameworks and rendered surfaces belong to consumer repos (e.g., PaglaAI.space, PaglaSHELL), which inherit from these tokens.

---

## 3. Token Lock (Deep)

### 3.1 Spacing

Base unit `space.base` = `0.25rem`. All spacing distances are multiples of the base unit.

| Token | Value |
|---|---|
| `space.0` | `0` |
| `space.1` | `0.25rem` |
| `space.2` | `0.5rem` |
| `space.3` | `0.75rem` |
| `space.4` | `1rem` |
| `space.5` | `1.25rem` |
| `space.6` | `1.5rem` |
| `space.8` | `2rem` |
| `space.12` | `3rem` |
| `space.16` | `4rem` |
| `space.24` | `6rem` |

### 3.2 Typography

| Token | Value |
|---|---|
| `font.size.display` | `4rem` |
| `font.size.h1` | `3rem` |
| `font.size.h2` | `2.25rem` |
| `font.size.h3` | `1.75rem` |
| `font.size.h4` | `1.375rem` |
| `font.size.bodyLarge` | `1.125rem` |
| `font.size.body` | `1rem` |
| `font.size.small` | `0.875rem` |
| `font.size.caption` | `0.75rem` |
| `font.size.code` | `0.875rem` |

| Token | Value |
|---|---|
| `font.weight.light` | `300` |
| `font.weight.regular` | `400` |
| `font.weight.medium` | `500` |
| `font.weight.semibold` | `600` |
| `font.weight.bold` | `700` |

| Token | Value |
|---|---|
| `font.lineHeight.body` | `1.5` |
| `font.lineHeight.heading` | `1.2` |
| `font.lineHeight.display` | `1.05` |

| Token | Value |
|---|---|
| `font.tracking.body` | `0` |
| `font.tracking.heading` | `-0.01em` |
| `font.tracking.display` | `-0.02em` |
| `font.tracking.uppercase` | `0.08em` |

| Token | Value |
|---|---|
| `font.maxWidth.body` | `65ch` |

### 3.3 Color — Light Theme

| Token | Value |
|---|---|
| `color.base.ink` | `#0A0A0B` |
| `color.base.paper` | `#FFFFFF` |
| `color.base.surface` | `#F5F5F3` |
| `color.base.border` | `#E8E8E6` |
| `color.base.muted` | `#6B707E` |

### 3.4 Color — Dark Theme

| Token | Value |
|---|---|
| `color.base.ink` | `#F5F5F3` |
| `color.base.paper` | `#0A0A0B` |
| `color.base.surface` | `#17171A` |
| `color.base.border` | `#2A2A2E` |
| `color.base.muted` | `#9AA0AE` |

### 3.5 Accent

| Token | Value |
|---|---|
| `color.accent.primary` | `#6B7EFF` |
| `color.accent.secondary` | `#A8B5FF` |
| `color.accent.success` | `#3E9B6E` |
| `color.accent.warning` | `#E0A23C` |
| `color.accent.error` | `#C94A4A` |
| `color.accent.info` | `#4A90C9` |

Accent is single-purpose: meaning only, never a background fill. Only as dot, underline, or focus.

### 3.6 State

| Token | Value |
|---|---|
| `color.state.default` | `transparent` |
| `color.state.hover` | `color.base.border` |
| `color.state.focus` | `color.accent.primary` |
| `color.state.active` | `color.base.ink` at `8%` overlay |
| `color.state.disabled` | `color.base.muted` at `40%` opacity |

### 3.7 UI

| Token | Value |
|---|---|
| `radius.sm` | `0.25rem` |
| `radius.md` | `0.5rem` |
| `radius.lg` | `1rem` |
| `radius.pill` | `9999rem` |
| `icon.sm` | `1rem` |
| `icon.md` | `1.5rem` |
| `icon.lg` | `2rem` |
| `interactive.minTarget` | `2.75rem` |

### 3.8 Motion

| Token | Value |
|---|---|
| `motion.duration.fast` | `100ms` |
| `motion.duration.base` | `200ms` |
| `motion.duration.slow` | `400ms` |
| `motion.easing.default` | `cubic-bezier(0.2, 0, 0, 1)` |
| `motion.easing.entrance` | `cubic-bezier(0.16, 1, 0.3, 1)` |
| `motion.easing.exit` | `cubic-bezier(0.4, 0, 1, 1)` |
| `motion.reduced` | `0ms` |

### 3.9 Surface Effects

| Token | Value |
|---|---|
| `surface.glass.opacity` | `0.72` |
| `surface.glass.blur` | `24px` |
| `surface.glass.border` | `0.08` |
| `surface.clear.opacity` | `0.55` |
| `surface.clear.blur` | `16px` |
| `surface.clear.border` | `0.06` |

### 3.10 Breakpoints & Layout

| Token | Value |
|---|---|
| `breakpoint.small` | `40rem` |
| `breakpoint.medium` | `48rem` |
| `breakpoint.large` | `64rem` |
| `breakpoint.xlarge` | `80rem` |
| `layout.maxWidth` | `75rem` |
| `layout.contentPadding` | `1rem` |
| `layout.contentPaddingWide` | `2rem` |
| `layout.reading` | `42rem` |

### 3.11 Locking Rule

Values are locked (D-010). They change only through the decision workflow. A change to any locked value is recorded in `governance/DECISIONS.md` and `governance/CHANGELOG.md`.

Never invent values inline. Every number must come from this file or `css/tokens.css`.

---

## 4. Component Contract

### 4.1 Registry

11 registered components in `components/COMPONENT_LIBRARY.md`:

| Component | Role |
|---|---|
| Button | Single identifiable action |
| Input | Capture single information |
| Chip | Compact label or filter |
| Card | Contained content group |
| List | Sequential content |
| Table | Structured data |
| Tabs | Switch between views |
| Modal | Focused overlay |
| Toast | Ephemeral notification |
| Menu | Contextual actions |
| Skeleton | Loading placeholder |

### 4.2 Component Anatomy

Every component has: Name, Role, States, Structure, Variants, Behavior.

### 4.3 Shared States

Every interactive component supports: Default, Hover, Focus, Active, Disabled, Loading.

### 4.4 Rules

- One role per component.
- Behavior shared, appearance inherited.
- No one-off components.
- Every component solves a recurring problem.
- If a component is used once, it is not a component.

---

## 5. Pagla Sans Typeface

### 5.1 Design Specification

See `design-system/PAGLA_SANS.md` for the complete specification.

- **Family name:** `"Pagla Sans"`
- **Base:** Open Sans (SIL OFL 1.1 / Apache License 2.0)
- **Modification:** Perfect-circle O & P, lighter weight distribution, open apertures
- **Weights:** Light (300), Regular (400), Medium (500), SemiBold (600), Bold (700)
- **Variable font:** Available with `wght` 300–700, `wdth` 75–100
- **UPM:** 2048

### 5.2 File Formats

| Format | Use | Location |
|---|---|---|
| WOFF2 | Web | `fonts/PaglaSans-*.woff2` |
| TrueType | Desktop, print | `fonts/PaglaSans-*.ttf` |
| Variable WOFF2 | Modern web | `fonts/PaglaSans-VF.woff2` |
| Variable TrueType | Advanced apps | `fonts/PaglaSans-VF.ttf` |

### 5.3 CSS Implementation

```css
@font-face {
  font-family: "Pagla Sans";
  src: url("../fonts/PaglaSans-Regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

Font stack: `"Pagla Sans", system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif`

### 5.4 Usage Rules

- Use Pagla Sans as the primary typeface for all PaglaAI products.
- Respect the weight hierarchy (Light for display, Regular for body, Bold for emphasis).
- Use generous line height (1.5 for body, 1.2 for headings).
- Apply negative tracking at display sizes (-0.02em).
- Never use Light or Thin weights below 14px.
- Never apply faux bold or faux italic.

---

## 6. MCP Integration

### 6.1 PaglaDESIGN MCP Server

The PaglaDESIGN MCP server (`.ai/mcp/server.py`) exposes the design authority to coding agents via Model Context Protocol.

**6 tools:**

| Tool | Purpose |
|---|---|
| `search` | Search design authority sections by query |
| `get_doc` | Read a whole canonical document by path |
| `list_docs` | List every indexed document |
| `lookup_token` | Get exact locked value of a design token |
| `search_tokens` | Fuzzy-find tokens by keyword |
| `get_context` | Get corpus summary and authoritative docs |

**Registered in:** `.opencode/opencode.json`

**Launched with:** `D:\PaglaAI\.venv\Scripts\python.exe .ai\mcp\server.py`

### 6.2 Usage Pattern

Before any UI work, call `search` or `lookup_token` to ground decisions in the design authority. Never guess token values.

```
search("glass effects")  → returns relevant sections
lookup_token("color.accent.primary")  → returns #6B7EFF
get_doc("design-system/DESIGN_TOKENS.md")  → returns full token file
```

### 6.3 RAG Retrieval

The MCP server uses heading-chunked BM25 retrieval over `**/*.md` and `css/tokens.css`. Deterministic, pure-stdlib, no API key, no network.

---

## 7. CSS Architecture

### 7.1 Three Layers

| Layer | File | Purpose |
|---|---|---|
| Tokens | `css/tokens.css` | CSS custom properties (`:root` + `[data-theme="dark"]`) |
| Base | `css/base.css` | Reset, element defaults, typography, focus, reduced motion |
| Utilities | `css/utilities.css` | Single-purpose, token-driven helpers |

### 7.2 Theming

- Light theme is default.
- Dark theme via `[data-theme="dark"]`.
- Theme choice defaults to `prefers-color-scheme`, persists to `localStorage`.

### 7.3 Reference Implementation

These are marked **reference**, not a shipped UI kit. Consumer repos import or graft from here.

---

## 8. Workflow

### 8.1 The Process

```
Vision → Research → Documentation → Design → Review → Prototype → Implementation
```

Implementation is intentionally the final step.

### 8.2 Before Creating Anything New

Ask yourself:
1. Can an existing component solve this?
2. Can the design system evolve instead?
3. Will this benefit every PaglaAI product?

If the answer is yes, improve the design system first.

### 8.3 Decision Workflow

If a change significantly affects the design system:
1. Document in `governance/DECISIONS.md` (what changed, why, alternatives, trade-offs).
2. Update `governance/CHANGELOG.md`.
3. Update relevant documentation.
4. Then implement.

---

## 9. Quality Gates

### 9.1 Token Compliance

- No magic numbers. Every value must be a token reference.
- No hardcoded colors. Use `var(--color-*)`.
- No invented spacing. Use `var(--space-*)`.

### 9.2 Accessibility

- Minimum contrast ratio: 4.5:1 for body text.
- Minimum touch target: 2.75rem (44px).
- `prefers-reduced-motion` support required.
- Semantic HTML required.
- Focus states must be visible.

### 9.3 Performance

- `font-display: swap` for all font faces.
- No unnecessary animations.
- CSS custom properties for theming (no runtime style computation).

### 9.4 Documentation

- Every new component must be registered in `COMPONENT_LIBRARY.md`.
- Every new token must be added to `DESIGN_TOKENS.md`.
- Every architectural change must be recorded in `DECISIONS.md`.

---

## 10. Anti-Patterns

### 10.1 Never Do This

- Invent token values inline.
- Use accent colors as background fills.
- Create one-off components.
- Skip documentation.
- Implement before designing.
- Hardcode colors instead of using CSS custom properties.
- Use Light weight at small sizes.
- Ignore `prefers-reduced-motion`.
- Add decorative animations.

### 10.2 Red Flags

- "I'll just use `#hex` here" → should be `var(--color-*)`.
- "This component is used once" → not a component.
- "I'll document it later" → document now.
- "It's just a small change" → small changes compound.

---

## 11. Governance

### 11.1 Decision Record

Every architectural decision is recorded in `governance/DECISIONS.md` with:
- Context
- Decision
- Alternatives considered
- Trade-offs
- Result

### 11.2 Changelog

`governance/CHANGELOG.md` records when things happened, grouped by version.

### 11.3 Repository Structure

Declared stable (D-012). No further moving or renaming of top-level folders. New content lands in an existing folder, or a documented decision creates a new one.

---

## 12. Quick Reference

### Key Files

| File | Purpose |
|---|---|
| `README.md` | Repository purpose and structure |
| `VISION.md` | Why PaglaAI exists |
| `DESIGN.md` | Design philosophy and pillars |
| `PRINCIPLES.md` | 13 standing principles |
| `AGENTS.md` | Contribution workflow and repository facts |
| `design-system/DESIGN_TOKENS.md` | Locked implementation values |
| `css/tokens.css` | CSS custom properties (reference) |
| `brand/BRAND.md` | Identity, mark, brand usage |
| `components/COMPONENT_LIBRARY.md` | Component registry |
| `governance/DECISIONS.md` | Architectural history |
| `governance/CHANGELOG.md` | Historical log |

### Key Tokens (Quick Lookup)

- **Ink:** `#0A0A0B`
- **Paper:** `#FFFFFF`
- **Accent:** `#6B7EFF`
- **Surface:** `#F5F5F3`
- **Border:** `#E8E8E6`
- **Muted:** `#6B707E`
- **Font:** `"Pagla Sans"`
- **Base spacing:** `0.25rem`
- **Min touch target:** `2.75rem`

### Key Decisions

| Decision | Summary |
|---|---|
| D-001 | Design First, Documentation Second, Implementation Last |
| D-002 | Typography as the Primary Interface |
| D-003 | Pagla Sans as the Primary Typeface |
| D-004 | Monochrome First |
| D-010 | Locking the Token Values |
| D-013 | Design Authority Owns Canonical Tokens |
| D-014 | Agent Tooling (MCP + RAG) |
| D-021 | Font Naming Normalization and Surface Effects |

---

*This manual is operating procedure, not authority. Token values, component definitions, and architectural decisions live in their canonical documents. When in doubt, read the source — never guess.*
