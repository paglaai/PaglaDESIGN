# COMPONENT_LIBRARY

> *The library is a registry, not a decoration.*
> *What is not here does not exist.*

---

# Purpose

COMPONENT_LIBRARY is the registry of every shared component in the PaglaAI ecosystem.

It is the answer to the question:

> Can an existing component solve this?

If a component is not in this library, it is not yet part of the system.

---

# Relationship to COMPONENTS

`COMPONENTS.md` defines the component language — roles, states, anatomy, and rules.

This document registers the components that exist.

- `COMPONENTS.md` — the grammar
- `COMPONENT_LIBRARY.md` — the vocabulary

---

# Library Principles

- One source of truth per component
- Every component documented before it is added
- Every component usable by every product
- Deprecated components are marked, never orphaned
- The library is reviewed, never silent

---

# Registration

A component enters the library through the decision workflow.

1. A recurring need is identified.
2. The design is documented.
3. The change is recorded in `../governance/DECISIONS.md`.
4. The component is registered here.
5. The version moves in `../governance/CHANGELOG.md`.

No component is added by accident.

---

# Component Registry

## Button

- **Role:** a single, identifiable action
- **States:** default, hover, focus, active, disabled, loading
- **Variants:** primary, secondary, ghost, destructive
- **Structure:** label; optional icon; optional loading indicator
- **Behavior:** triggers its action once; disabled blocks without explanation
  (`COMPONENTS.md`); loading replaces the label affordance and is announced for
  screen readers (`../design-system/ACCESSIBILITY.md`)
- **Docs:** `COMPONENTS.md`

## Input

- **Role:** capture a single piece of information
- **States:** default, focus, filled, error, disabled
- **Variants:** text, number, search, password
- **Structure:** label, field, optional helper text, optional error message
- **Behavior:** focus is visible (`color.state.focus`); placeholder is never a
  label (`../design-system/ACCESSIBILITY.md`); error text sits beside the field
  it concerns and states what to do
- **Docs:** `COMPONENTS.md`

## Chip

- **Role:** a compact label or filter
- **States:** default, selected, disabled
- **Variants:** label, filter, removable
- **Structure:** label; optional remove affordance
- **Behavior:** toggles selected state; selection is shown beyond color
  (e.g. a check mark); removable chips offer a labeled removal; never navigates
- **Docs:** `COMPONENTS.md`

## Card

- **Role:** a surface that groups related content
- **States:** default, hover, focus
- **Variants:** plain, interactive
- **Structure:** optional media, content, optional actions
- **Behavior:** plain cards are static; interactive cards are keyboard-focusable
  with one primary action per card; hierarchy comes from spacing and type, not
  decoration (`../design-system/UX_PATTERNS.md`)
- **Docs:** `COMPONENTS.md`

## List

- **Role:** a vertical sequence of related items
- **States:** default, hover, focus, selected
- **Variants:** plain, interactive
- **Structure:** items; optional per-item meta
- **Behavior:** interactive lists navigate or act; selection is shown beyond
  color (`../design-system/ACCESSIBILITY.md`); items remain reachable by keyboard
- **Docs:** `COMPONENTS.md`

## Table

- **Role:** a structured comparison of rows and columns
- **States:** default, hover, focus, sorted
- **Variants:** simple, sortable, expandable
- **Structure:** header, rows, columns; optional sort control
- **Behavior:** sortable columns announce direction; expandable rows toggle with
  keyboard; headers remain associated with their columns
  (`../design-system/ACCESSIBILITY.md`)
- **Docs:** `COMPONENTS.md`

## Tabs

- **Role:** a set of related views where only one is visible at a time
- **States:** default, selected, focus, disabled
- **Variants:** underline, card, segmented
- **Structure:** tablist, tab buttons, tabpanel
- **Behavior:** arrow-key navigation with roving tabindex; exactly one panel
  visible; selection is announced and shown beyond color; panels may be
  reachable directly (`../design-system/UX_PATTERNS.md`)
- **Docs:** `COMPONENTS.md`

## Modal

- **Role:** a focused task that interrupts the current view
- **States:** open, closing, focus-locked
- **Variants:** dialog, confirm
- **Structure:** overlay, dialog, title, content, actions; close affordance
- **Behavior:** focus is trapped; Escape closes and focus returns to the
  trigger; usage is justified, never casual (`COMPONENTS.md`); open/close uses
  `motion.duration.base` or slower (`../design-system/MOTION.md`)
- **Docs:** `COMPONENTS.md`

## Toast

- **Role:** a brief, non-blocking status message
- **States:** show, exit, stacked
- **Variants:** info, success, warning, error
- **Structure:** message; optional action; close affordance
- **Behavior:** appears without stealing focus; auto-dismiss is announced for
  screen readers; toasts stack within one region; color is reinforced by text
  and icon (`../design-system/ACCESSIBILITY.md`)
- **Docs:** `COMPONENTS.md`

## Menu

- **Role:** a set of actions or links revealed on demand
- **States:** closed, open, focus, disabled
- **Variants:** action, context
- **Structure:** trigger, list of actions or links
- **Behavior:** opens on demand; Escape closes; arrow keys navigate the list;
  focus returns to the trigger on close (`../design-system/UX_PATTERNS.md`)
- **Docs:** `COMPONENTS.md`

## Skeleton

- **Role:** a placeholder that communicates loading state
- **States:** loading
- **Variants:** text, block, avatar
- **Structure:** placeholder shapes mirroring the final layout shape
- **Behavior:** static or a gentle fast pulse (`../design-system/MOTION.md`);
  loading is announced; the container reserves its space so nothing relayouts
  (`../design-system/UX_PATTERNS.md`)
- **Docs:** `COMPONENTS.md`

## Breadcrumbs

- **Role:** a trail showing where the user is and the path back
- **States:** default, focus, current (non-link)
- **Variants:** single-line
- **Structure:** ordered list of links ending in the current page as text
- **Behavior:** each link navigates one level back; the current page is text,
  never a link; the trail is announced as navigation
  (`../design-system/ACCESSIBILITY.md`)
- **Docs:** `COMPONENTS.md`

## Code Block

- **Role:** display a snippet of code readably
- **States:** default, focus (copy affordance), copied
- **Variants:** plain, with header, with language
- **Structure:** optional header (filename and/or language), `pre > code`, optional
  copy affordance
- **Behavior:** code renders at `font.size.code`; long lines scroll horizontally
  rather than wrapping by default; copy copies with visible confirmation and is
  keyboard-reachable; syntax highlighting stays minimal
  (`../governance/DOCUMENTATION_STYLE.md`)
- **Docs:** `COMPONENTS.md`

## Terminal

- **Role:** present authentic CLI output and commands
- **States:** default, running (optional), complete
- **Variants:** plain, with prompt
- **Structure:** optional terminal chrome, prompt line, output, optional cursor
- **Behavior:** a faithful, static illustration by default — real output, never
  faked (`../references/INSPIRATION.md`); where interactive, commands run only
  through a visible affordance and the run state is announced
  (`../design-system/UX_PATTERNS.md`)
- **Docs:** `COMPONENTS.md`

---

# Lifecycle

Every component has a lifecycle.

- **Draft** — proposed, not yet registered
- **Active** — registered and supported
- **Deprecated** — registered, no new use
- **Removed** — no longer exists

Only Active components are used in new work.

Deprecation is documented before removal.

---

# Ownership

Every component has a clear owner and a clear scope.

Ownership does not mean exclusivity.

It means one accountable place for decisions about that component.

---

# Quality Gate

A component must meet the baseline before it is registered:

- Accessible (`../design-system/ACCESSIBILITY.md`)
- Token-driven (`../design-system/DESIGN_TOKENS.md`)
- Motion-correct (`../design-system/MOTION.md`)
- Documented (this document)

A component that fails a gate is not registered.

---

# Relationship to Documents

- Component language — `COMPONENTS.md`
- Values — `../design-system/DESIGN_TOKENS.md`
- Color — `../design-system/COLOR_SYSTEM.md`
- Motion — `../design-system/MOTION.md`
- Accessibility — `../design-system/ACCESSIBILITY.md`
- Decisions — `../governance/DECISIONS.md`

---

# Final Principle

A library that is honest about its boundaries stays trustworthy.

An empty slot is better than a wrong component.