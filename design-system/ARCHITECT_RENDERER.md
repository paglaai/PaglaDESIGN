# ARCHITECT_RENDERER

> *The governance renderer. What a decision-maker sees when they read a PaglaAI architecture document.*

---

# Purpose

ARCHITECT_RENDERER defines how PaglaDESIGN Markdown is rendered into
architecture decision records, governance documents, and audit views for
engineers, architects, and auditors.

It specifies two output formats: RFC/ADR template and governance/audit
document. Both formats share the same source and frontmatter.

ARCHITECT does not render HTML for web surfers. It produces structured
governance artifacts that become part of the design system's decision history.

---

# Output Formats

| Format | Use Case | Consumer |
|---|---|---|
| **RFC / ADR** | Architecture decision record | Engineering teams, design reviews, audit trails |
| **Governance document** | Policy, standard, or governance page | Governance UI, compliance tools |

---

# RFC / ADR Format

An RFC (Request for Comments) or ADR (Architecture Decision Record) documents
a decision with its full context.

The structure mirrors the format used in `governance/DECISIONS.md`, ensuring
consistency between authored decisions and rendered output.

```yaml
---
title: "RFC-0042: Event Pipeline Architecture"
audience:
  - architect
version: "0.1.0"
status: draft
---
```

```markdown
# RFC-0042: Event Pipeline Architecture

## Context

PaglaDESIGN v2 introduces an Audience Renderer architecture. When a
documentation page changes, downstream repositories must be notified. The
current system has no mechanism for this.

## Decision

Implement a CI/CD workflow that detects PaglaDESIGN directive changes,
validates frontmatter schema, publishes a `design.updated` event, and triggers
downstream repositories.

## Alternatives

- Manual notification via issue creation. Rejected — error-prone and delayed.
- Polling by downstream repos. Rejected — adds load and complexity to consumers.
- Webhook from PaglaDESIGN. Deferred — requires hosting infrastructure.

## Trade-offs

The event pipeline adds CI/CD complexity but creates a reliable, automated
chain-reaction across the ecosystem. Downstream repos no longer need to track
PaglaDESIGN manually.

## Result

Downstream repositories receive structured events. The design authority remains
the single source of truth. Consumer surfaces update automatically.
```

**Rules:**

- The rendered RFC/ADR follows the exact section order: Context, Decision,
  Alternatives, Trade-offs, Result.
- Additional sections (e.g. Implementation, References) may follow Result.
- `version` reflects the RFC draft state. `0.x.0` indicates draft; `1.0.0`
  indicates accepted.
- `status` reflects lifecycle: `draft`, `active` (accepted), `deprecated`.
- The output is Markdown formatted for governance review — it may be rendered
  into PDF, HTML, or included in meeting decks.

---

# Governance Document Format

A governance document covers policy, standards, or process definitions.

```yaml
---
title: "Design Review Process"
audience:
  - architect
status: active
---
```

```markdown
# Design Review Process

## Purpose

Every significant change to PaglaDESIGN must be reviewed before implementation.

## Scope

This process applies to:
- New components
- New patterns
- Token value changes
- Architectural decisions

## Steps

1. Author the change in a feature branch.
2. Open a Pull Request against `main`.
3. Request review from the design authority maintainers.
4. Address review comments.
5. Merge when approved.

## Exceptions

Emergency fixes may bypass review with post-hoc documentation within 48 hours.

## Relationship

- Decision workflow — `governance/DECISIONS.md`
- Documentation standards — `governance/DOCUMENTATION_STYLE.md`
```

**Rules:**

- Purpose is stated first.
- Scope is explicit.
- Steps are sequential and numbered.
- Exceptions are documented, not implied.
- Related documents are linked at the end.

---

# Decision Record Structure

ARCHITECT enforces the same decision-record structure used in
`governance/DECISIONS.md`.

Every RFC/ADR must contain:

| Section | Required | Description |
|---|---|---|
| **Context** | Yes | The problem being solved |
| **Decision** | Yes | What was chosen |
| **Alternatives** | Yes | What was considered and rejected |
| **Trade-offs** | Yes | What was gained and what was given up |
| **Result** | Yes | The impact on the system |

Missing any section makes the record incomplete. ARCHITECT renders a warning
rather than filling the gap.

---

# Audit UI

ARCHITECT produces data for an audit view that shows decision lineage and
version history.

The audit view consumes the same frontmatter and body content, but presents it
in a structured timeline:

| Field | Source | Description |
|---|---|---|
| Title | `title` frontmatter | Decision or document title |
| Version | `version` frontmatter | Current version |
| Status | `status` frontmatter | Lifecycle state |
| Audience | `audience` frontmatter | Target renderers |
| Dependencies | `dependencies` frontmatter | Linked documents |
| Date | Git commit date | Last modification |
| Author | Git author | Last contributor |
| Decisions | Internal links | Related RFCs and ADRs |

The audit view is rendered by the consumer surface. ARCHITECT provides the
structured data; the consumer renders it.

---

# Deprecation

When a document's `status` is `deprecated`, ARCHITECT renders it with:

- A deprecation notice at the top of the document.
- The original content below.
- Links to the replacement document if one exists.

Deprecated documents are not removed. They remain in the source for historical
reference. The audit view shows the deprecation lineage.

---

# Relationship to Existing Documents

ARCHITECT is a consumer of existing governance documents, not a replacement.

| Document | Role |
|---|---|
| `governance/DECISIONS.md` | Canonical decision record format. ARCHITECT renders RFCs/ADRs in the same structure. |
| `governance/DOCUMENTATION_STYLE.md` | Writing standards. Governance documents follow these rules. |
| `governance/AUDIENCE_RENDERER_SPEC.md` | Constitutional spec. ARCHITECT is one of the three specified renderers. |
| `design-system/RENDERER_API.md` | Metadata contract. ARCHITECT reads `audience`, `version`, `status`, and `dependencies`. |
| `design-system/DESIGN_TOKENS.md` | Token values. ARCHITECT does not apply visual tokens; governance UIs may. |

---

# Accessibility

Governance documents are read by engineers and decision-makers. They must still
meet the accessibility baseline.

Minimum requirements:

- Semantic heading hierarchy
- Descriptive link text
- Screen-reader-friendly table structure
- Keyboard navigation in audit views

---

# Idempotency

ARCHITECT output is idempotent.

Given the same source Markdown, the same frontmatter, and the same renderer
version, the output is byte-identical across runs.

No timestamps, author names, or environment-dependent values are included in
the rendered RFC/ADR or governance document output.

---

# Relationship to Documents

- Constitutional spec — `governance/AUDIENCE_RENDERER_SPEC.md`
- Renderer API — `design-system/RENDERER_API.md`
- Decision records — `governance/DECISIONS.md`
- Documentation standards — `governance/DOCUMENTATION_STYLE.md`
- Token values — `design-system/DESIGN_TOKENS.md`

---

# Final Principle

> **Decisions are the architecture.**
>
> **Records are the evidence.**
>
> **Governance is the process.**
