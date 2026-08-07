# MOCKUP — API Reference

> High-fidelity, token-referenced. The anatomy of one endpoint page.

---

# Base

- Paper background; sidebar region with hairline right border; content region
  at full available width (Tables and Code Blocks exceed 65ch deliberately).
- Same semantics as `03-docs.md`, minus the right TOC.

---

# Typography

| Element | Token |
| --- | --- |
| Endpoint title | `font.size.h1`, `font.weight.medium`; the HTTP method in `font.size.small`, `font.tracking.uppercase`, `color.accent.primary` |
| Section headings | `font.size.h2`, `font.weight.medium` |
| Parameter/field names | `font.size.code`, `font.weight.semibold` |
| Descriptions | `font.size.body`, muted where secondary |
| Code | `font.size.code` |

---

# Region treatment

## Endpoint heading

- Method label + path in one line; method colored by meaning
  (`color.accent.primary`), never a fill

## Request

- Code Block (sample request) with copy affordance
- Parameter Table: parameter (code), type (muted), required (text —
  "required" / "optional", never color-only), description

## Response

- Code Block (response schema)
- Field Table: field, type, description

## Errors

- Table: status code, message, retry guidance; error state carries
  `color.accent.error` text only as reinforcement
  (`../design-system/ACCESSIBILITY.md`)

## Examples

- Tabs (underline variant): curl / python / js; one Code Block per panel with
  copy

---

# Components in use

- **Tabs:** underline; active underline `color.accent.primary`
- **Code Block:** header (language), copy with success confirmation
- **Table:** hairline `color.base.border`, header `font.weight.semibold`,
  horizontal scroll below `breakpoint.medium`

---

# Spacing rhythm

- Section gap `space.12`; heading-to-content `space.6`
- Tables `space.6` above/below; Tables span full content width
- Example Tabs `space.4` above the active Code Block

---

# Dark theme

Standard inversion; method accent unchanged; error accent unchanged.

---

# Reduced motion

Tab panels switch instantly under reduced motion with announced selection.
