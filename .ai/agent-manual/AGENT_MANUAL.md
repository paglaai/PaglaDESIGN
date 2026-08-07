# PaglaDESIGN Agent Operating Manual

**Version:** 2.0.0  
**Status:** Adopted (canonical Decision D-020)  
**Date:** 2026-08-07  
**License:** © 2026 AYNAGHOR. Intelligence, Unhinged.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Working Relationship](#2-working-relationship)
3. [Token Inheritance](#3-token-inheritance)
4. [Component Inheritance](#4-component-inheritance)
5. [Layout & Templates](#5-layout--templates)
6. [Prompt Formula](#6-prompt-formula)
7. [STITCH Integration](#7-stitch-integration)
8. [Lint Discipline](#8-lint-discipline)
9. [Skills](#9-skills)
10. [MCP Tools](#10-mcp-tools)
11. [Build Playbook](#11-build-playbook)
12. [Anti-Patterns](#12-anti-patterns)

---

## 1. Overview

### 1.1 Purpose

This manual defines the **operating procedure** for any coding agent
(Claude Code, Cursor, Gemini CLI, opencode, PaglaAI launcher CLIs) doing
design-build work in the PaglaAI ecosystem.

The manual is one thing only: **procedure**. It does not define the design
language. The design language lives in PaglaDESIGN (`design-system/`,
`components/`, `brand/`, `templates/`, `css/`), and this manual inherits it.

Any agent reading this manual must first understand that:

- PaglaDESIGN is the **canonical design authority**. This manual never
  overrides it.
- Every token value, component contract, and layout rule referenced here
  lives in PaglaDESIGN. When the two disagree, **PaglaDESIGN wins**.
- This manual's job is to tell the agent *how to work*: how to inherit
  tokens, how to build, how to lint, how to decide.

### 1.2 Scope

| Area | Coverage |
|------|----------|
| Authority | How the manual relates to PaglaDESIGN |
| Tokens | How to inherit token values, never invent them |
| Components | How to choose and compose library components |
| Layout | How to use the layout system and templates |
| Prompting | Formulaic prompt construction for generation tools |
| STITCH | External, optional AI generation — never authority |
| Quality | Lint severity model and discipline |
| Skills | Installed agent skills and their limits |
| MCP | Canonical agent tools exposed by the MCP server |
| Workflow | 6-phase build playbook from brief to deploy |
| Errors | 12 anti-patterns with corrections |

### 1.3 Governance

This manual is governed by canonical Decision **D-020** (recorded in
`../../governance/DECISIONS.md`). It is versioned under Semantic Versioning.

Changes to *values* are decided in PaglaDESIGN and versioned there. Changes to
*procedure* are decided in this manual.

---

## 2. Working Relationship

### 2.1 The Authority Pyramid

```
┌─────────────────────────────────────────────────────────────┐
│                    CANONICAL AUTHORITY                      │
│     PaglaDESIGN — tokens, components, layout, decisions     │
│     design-system/ · components/ · brand/ · templates/      │
│     css/ · governance/ · site/                              │
├─────────────────────────────────────────────────────────────┤
│                    OPERATING PROCEDURE                      │
│     This manual — how agents inherit, build, and validate   │
│     .ai/agent-manual/AGENT_MANUAL.md                        │
├─────────────────────────────────────────────────────────────┤
│                       GENERATORS                            │
│     STITCH and similar tools — external, optional,          │
│     always validated against the authority before use       │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Data Flow

1. **Agent receives build brief** (product requirements)
2. **Agent inherits from the authority** — tokens, components, templates
   (`../../css/tokens.css`, `../../components/COMPONENT_LIBRARY.md`,
   `../../templates/`)
3. **Agent may generate** design variants with STITCH using §6
4. **Agent validates** output against the lint discipline (§8)
5. **Agent implements** following the build playbook (§11)
6. **Agent documents** decisions through canonical governance
   (`../../governance/DECISIONS.md`)

### 2.3 Responsibility Boundaries

| Layer | Owns | Does Not Own |
|-------|------|--------------|
| Authority (PaglaDESIGN) | Tokens, components, layout, decisions | Product-specific logic |
| This manual | Operating procedure | Design values |
| Generators (STITCH) | Variant exploration | Final design decisions |
| Agent | Execution, curation, code quality | Redefinition of the system |

---

## 3. Token Inheritance

### 3.1 Rule

**Tokens are inherited, never redefined.**

All values are locked in `../../design-system/DESIGN_TOKENS.md` and encoded in
`../../css/tokens.css`. An agent does not re-type, paraphrase, or "improve"
these values.

- Look up values with the MCP tool `lookup_token` (§10), or read
  `../../css/tokens.css`.
- Reference tokens **by name** in code (`var(--token-name)`), never by literal
  value.
- Never introduce a new token, palette, font, shadow, or gradient. Adding a
  token is a governance decision
  (`../../governance/DECISIONS.md`).

### 3.2 Where the values live

| Need | Canonical source |
|------|------------------|
| All literal values | `../../design-system/DESIGN_TOKENS.md` (locked, D-010) |
| CSS custom properties | `../../css/tokens.css` (`:root` + `[data-theme="dark"]`) |
| Color semantics | `../../design-system/COLOR_SYSTEM.md` |
| Typography | `../../design-system/TYPOGRAPHY.md` |
| Motion | `../../design-system/MOTION.md` |
| Interaction behavior | `../../design-system/UX_PATTERNS.md` |
| Base element defaults | `../../css/base.css` |
| Single-purpose helpers | `../../css/utilities.css` |

### 3.3 Theming

Light and dark share one semantic structure; only values change between
`[data-theme="light"]` and `[data-theme="dark"]`. Theme is switched by data
attribute, never by re-authoring tokens.

### 3.4 Correct vs. wrong

```css
/* ✅ CORRECT — reference the token */
.card {
  background: var(--color-base-surface);
  border-radius: var(--radius-md);
  padding: var(--space-6);
}

/* ❌ WRONG — hardcoded value invents a number with no name */
.card {
  background: #F5F5F3;
  border-radius: 8px;
  padding: 24px;
}
```

---

## 4. Component Inheritance

### 4.1 Rule

**Components are chosen, never redefined.**

The registry is `../../components/COMPONENT_LIBRARY.md`; the language is
`../../components/COMPONENTS.md`. What is not registered does not exist for an
agent to invent.

Registered components (14):

| Component | Role |
|-----------|------|
| Button | a single, identifiable action |
| Input | capture a single piece of information |
| Chip | a compact label or filter |
| Card | a surface that groups related content |
| List | a vertical sequence of related items |
| Table | a structured comparison of rows and columns |
| Tabs | a set of related views, one visible at a time |
| Modal | a focused task that interrupts the view |
| Toast | a brief, non-blocking status message |
| Menu | actions or links revealed on demand |
| Skeleton | a loading-state placeholder |
| Breadcrumbs | a trail showing where the user is |
| Code Block | a readable, copyable code snippet |
| Terminal | faithful CLI output presentation |

### 4.2 Usage rules

1. Reuse before re-creating. Prefer the registered component to a novel one.
2. Do not invent "variants" that change a component's role. Approved variants
   are listed in the registry.
3. A state change is part of the design; a new component is a governance
   decision.
4. Children of components still inherit tokens.
5. Do not build one-off components for a single screen — use the templates
   (§5) and composition.

### 4.3 Accessible baseline

Every component must meet `../../design-system/ACCESSIBILITY.md`: semantic
HTML, visible focus, keyboard operability, labels, and state shown beyond
color.

---

## 5. Layout & Templates

### 5.1 Layout tokens

Layout uses the canonical tokens: `breakpoint.small/medium/large/xlarge`,
`layout.maxWidth`, `layout.contentPadding*`, and the `space.*` scale. See
`../../design-system/DESIGN_TOKENS.md`.

### 5.2 Templates

Page-level composition is decided in `../../templates/`, not in an agent's
head:

| Template | For |
|----------|-----|
| `hero.md` | opening composition |
| `landing.md` | home page arc |
| `product.md` | product spine |
| `docs.md` | learning-path layout |
| `blog.md` | index and article |
| `case-study.md` | problem → decision → outcome |
| `sections.md` | Feature Grid, CTA, Timeline, Footer |

Wireframes and mockups for the site pages live in `../../wireframes/` and
`../../mockups/`.

### 5.3 Interaction

Behavior follows `../../design-system/UX_PATTERNS.md`: fast state
transitions, native scroll, quiet loading/empty/error states, reduced-motion
safe.

---

## 6. Prompt Formula

The prompt formula is the reusable template for requesting design generation —
from STITCH, or from any capable model. It is procedure, not a model.

**Formula:**

```
[ROLE] + [CONTEXT] + [CONSTRAINTS] + [OUTPUT_SPEC] + [EXAMPLES]
```

### 6.1 ROLE

Name the design persona the generator should assume (e.g. "a calm,
typography-led interface designer"). The persona always inherits the
authority.

### 6.2 CONTEXT

State the what, who, and why:

```
We are building [FEATURE] for [PRODUCT] targeting [AUDIENCE].
The goal is [USER_GOAL] while achieving [BUSINESS_GOAL].
Current state: [EXISTING_SOLUTION_OR_GAP].
```

### 6.3 CONSTRAINTS

Mandatory constraint block:

```
Design Constraints:
- Inherit all tokens from the canonical source (never inline new values)
- Use only registered components
- Follow the template for this page type
- Accessible: semantic HTML, visible focus, keyboard operable
- State is never carried by color alone
- No shadows, gradients, or decoration beyond the system
- Reduced motion must be honored
```

### 6.4 OUTPUT_SPEC

```
Output Requirements:
- Format: [HTML/CSS/…]
- Fidelity: [wireframe/high-fidelity/production]
- Deliverables: [markup + token references + state handling]
- Compliance notes: [deviations + rationale]
```

### 6.5 EXAMPLES

One to three references — existing PaglaAI screens or patterns. Never more;
too many examples dilute the signal.

### 6.6 Prompt anti-patterns

| Anti-Pattern | Correction |
|--------------|------------|
| Vague role | Name a specific design persona |
| Missing constraints | Always include the full constraint block |
| Token values in the prompt | Reference the canonical source, don't inline |
| No accessibility mention | Always include the a11y constraint |
| Too many examples | Max 3, prioritize ecosystem references |

---

## 7. STITCH Integration

> **STITCH is external and optional.** It is a generator, never an authority.

STITCH (and any similar generation tool) produces candidates. Candidates are
curated against the authority before implementation.

### 7.1 Rules

1. **Verify at use** — mode names and availability change. Confirm the current
   capability before prompting.
2. **Never accept output blindly** — every candidate is validated (§8) before
   it is implemented.
3. **Deviations are handled, not absorbed** — a candidate that invents tokens,
   components, or patterns is rejected or corrected; the invention is never
   accepted into the system.
4. **Nothing generated becomes canonical** — new values/components enter only
   through governance (`../../governance/DECISIONS.md`).

### 7.2 Deviation handling

| Severity | Action |
|----------|--------|
| Cosmetic (spacing off by one step) | Fix silently |
| Token drift (wrong value) | Replace with the canonical token |
| Missing accessibility | Add before implementation |
| New invention (token/component) | Remove; propose via governance |
| Structural mismatch (wrong pattern) | Regenerate or build manually |

### 7.3 Absence is fine

If STITCH is unavailable, the workflow does not change — the agent designs
directly from the authority. Generation is optional; validation is not.

---

## 8. Lint Discipline

### 8.1 Severity model

| Severity | Meaning | Action |
|----------|---------|--------|
| `ERROR` | Must fix before merge | Blocks deployment |
| `WARN` | Should fix; explain if not | Requires comment |
| `INFO` | Suggestion | No action required |

### 8.2 Rules

| ID | Rule | Severity |
|----|------|----------|
| R-01 | **Token compliance** — every visual property references a canonical token; no hardcoded values except zero | `ERROR` |
| R-02 | **Registry compliance** — only registered components; approved variants only | `ERROR` |
| R-03 | **Accessibility** — accessible names, labels, visible focus, state beyond color | `ERROR` |
| R-04 | **Semantic HTML** — the right element for the purpose; no div-spam | `WARN` |
| R-05 | **Responsive** — no breakage at `breakpoint.small`; no horizontal scroll | `WARN` |
| R-06 | **Motion** — durations from the motion tokens; reduced-motion honored; no infinite animation without a trigger | `INFO` |
| R-07 | **Theming** — dark and light both pass; nothing hardcoded to one theme | `ERROR` |
| R-08 | **Naming** — token-named classes; no inline value names | `INFO` |

### 8.3 Discipline

- Run the checks after every meaningful change.
- Zero `ERROR`s before merge.
- A `WARN` is either fixed or justified with a comment.
- Nothing ships reviewed for a single theme.

---

## 9. Skills

Installed design skills live in consumer `.opencode/skills/` (e.g. UI/UX Pro
Max, Claude Design Skills, Anthropic's frontend-design).

- Skills provide **process and discipline**, never values.
- Any skill suggestion that conflicts with a locked token or a registered
  component is rejected (D-003, D-004, D-008).
- The canonical sources in §3 and §4 always outrank skill defaults.

---

## 10. MCP Tools

The canonical MCP server lives at `../mcp/server.py` (registered as a local
MCP server in `../../.opencode/opencode.json`).

Tools exposed by the authority:

| Tool | Purpose |
|------|---------|
| `search` | Full-text retrieval over canonical documents |
| `get_doc` | Fetch a canonical document |
| `list_docs` | List canonical documents |
| `lookup_token` | Exact token value from `css/tokens.css` |
| `search_tokens` | Find tokens by name/role |
| `get_context` | Assemble a working context from the authority |

These are the agent-facing tools of the design system. Prefer lookup over
memory: token values change only through governance, and the tool always
returns the current truth.

Nothing in this manual is an MCP tool definition. Tool behavior is defined by
`../mcp/server.py`.

---

## 11. Build Playbook

The 6-phase workflow from brief to deployed, validated output. Every build
follows these phases in order.

```
PHASE 1         PHASE 2        PHASE 3        PHASE 4        PHASE 5       PHASE 6
Brief        →   Inherit    →   Design     →   Validate   →   Implement  →   Deploy
Analysis         from the        (authority     (lint + a11y)   (tokens)      (verify)
                 authority        + optional
                                  generation)
```

### Phase 1 — Brief Analysis

Understand the build and identify the assets involved.

1. Parse the brief.
2. Identify the template (`../../templates/`) and components (`§4`).
3. Identify the tokens involved (`§3`).
4. Note special requirements (a11y, i18n, animation, theming).
5. Flag anything that falls outside the system — that is a governance
   question, not a build-time invention.

**Exit:** brief understood; template and components identified.

### Phase 2 — Inherit from the Authority

Ground every value and contract in the canonical sources.

1. Look up exact token values (`lookup_token` or `../../css/tokens.css`).
2. Read the component contracts (`../../components/COMPONENT_LIBRARY.md`).
3. Study the template and its wireframe/mockup if one exists
   (`../../wireframes/`, `../../mockups/`).
4. Check `../../governance/CHANGELOG.md` for recent changes.

**Exit:** every value and contract verified.

### Phase 3 — Design

Produce the design from the authority, optionally aided by generation (§6/§7).

1. Compose per the template.
2. Optionally generate candidates with STITCH using §6.
3. Curate against the authority.
4. Document any deviation with rationale.

**Exit:** a design that uses only inherited tokens, registered components,
and the chosen template.

### Phase 4 — Validate

Rigorously check the design before implementation.

1. Run the lint discipline (§8).
2. Fix all `ERROR`s; justify or fix `WARN`s.
3. Confirm accessibility baseline (`../../design-system/ACCESSIBILITY.md`).
4. Confirm motion gates (`../../design-system/MOTION.md`).

**Exit:** zero `ERROR`s; a11y and motion gates passed.

### Phase 5 — Implement

Transform the validated design into code.

1. Implement with token references (`var(--token)`), never literals.
2. Use registered components per their contracts.
3. Follow the template structure.
4. Respect the reduced-motion toggle and both themes.
5. Re-run validation on the implementation.

**Exit:** code matches the design; lint clean; both themes verified.

### Phase 6 — Deploy & Verify

Ship and confirm in the running surface.

1. Deploy to the target surface.
2. Verify both themes, keyboard path, zoom, and reduced motion.
3. Confirm no horizontal scroll at `breakpoint.small`.
4. Log any decision that should be recorded
   (`../../governance/DECISIONS.md`).

**Exit:** deployed and verified; decisions recorded.

---

## 12. Anti-Patterns

| # | Anti-Pattern | Correction |
|---|--------------|------------|
| AP-01 | **Hardcoding token values** | Always reference `var(--token-name)` |
| AP-02 | **Skipping brief analysis** | Always complete Phase 1 |
| AP-03 | **Raw HTML where a component exists** | Use the registered component |
| AP-04 | **Ignoring small screens** | Verify at `breakpoint.small` |
| AP-05 | **Inventing tokens or components** | Use the system; propose via governance |
| AP-06 | **Accepting generated output blindly** | Always validate (§8) |
| AP-07 | **Skipping accessibility** | The baseline is non-negotiable |
| AP-08 | **Over-engineering one-offs** | Compose from the library |
| AP-09 | **Not recording decisions** | Document through governance |
| AP-10 | **Testing one theme only** | Both themes always |
| AP-11 | **Skipping playbook phases** | Follow all six phases in order |
| AP-12 | **Redefining the system "for this product"** | The authority is inherited, not forked |

### Deep dive — AP-12

**The Mistake:**

An agent "simplifies" or "modernizes" the system for a single product — new
colors, a bolder typeface, a fresh button style.

**Why It's Wrong:**

PaglaDESIGN exists so products feel like they belong together (D-002, D-004,
D-008). A per-product fork is fragmentation that compounds across the
ecosystem.

**The Correction:**

- If the system lacks something, **propose it through governance**
  (`../../governance/DECISIONS.md`).
- If the system has something, **use it as it is**.
- Consistency outranks individual creativity — see
  `../../templates/product.md`.

---

## Appendix A — Quick Reference Card

### Where values live

| Need | Go to |
|------|-------|
| Token values | `../../css/tokens.css` or `lookup_token` |
| Token rationale | `../../design-system/DESIGN_TOKENS.md` |
| Components | `../../components/COMPONENT_LIBRARY.md` |
| Templates | `../../templates/` |
| Wireframes / mockups | `../../wireframes/` / `../../mockups/` |
| Interaction | `../../design-system/UX_PATTERNS.md` |
| Decisions | `../../governance/DECISIONS.md` |

### One-line playbook

```
Analyze → Inherit → Design → Validate → Implement → Deploy
```

### One-line rule

> *Inherit everything. Invent nothing. Validate always.*

---

*"A great design system does not create identical products. It creates products
that feel like they belong together."* — PaglaDESIGN `VISION.md`

---

© 2026 AYNAGHOR. Intelligence, Unhinged.
