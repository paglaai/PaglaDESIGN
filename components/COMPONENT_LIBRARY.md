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
- **Docs:** `COMPONENTS.md`

## Input

- **Role:** capture a single piece of information
- **States:** default, focus, filled, error, disabled
- **Variants:** text, number, search, password
- **Docs:** `COMPONENTS.md`

## Chip

- **Role:** a compact label or filter
- **States:** default, selected, disabled
- **Variants:** label, filter, removable
- **Docs:** `COMPONENTS.md`

## Card

- **Role:** a surface that groups related content
- **States:** default, hover, focus
- **Variants:** plain, interactive
- **Docs:** `COMPONENTS.md`

## List

- **Role:** a vertical sequence of related items
- **States:** default, hover, focus, selected
- **Variants:** plain, interactive
- **Docs:** `COMPONENTS.md`

## Table

- **Role:** a structured comparison of rows and columns
- **States:** default, hover, focus, sorted
- **Variants:** simple, sortable, expandable
- **Docs:** `COMPONENTS.md`

## Tabs

- **Role:** a set of related views where only one is visible at a time
- **States:** default, selected, focus, disabled
- **Variants:** underline, card, segmented
- **Docs:** `COMPONENTS.md`

## Modal

- **Role:** a focused task that interrupts the current view
- **States:** open, closing, focus-locked
- **Variants:** dialog, confirm
- **Docs:** `COMPONENTS.md`

## Toast

- **Role:** a brief, non-blocking status message
- **States:** show, exit, stacked
- **Variants:** info, success, warning, error
- **Docs:** `COMPONENTS.md`

## Menu

- **Role:** a set of actions or links revealed on demand
- **States:** closed, open, focus, disabled
- **Variants:** action, context
- **Docs:** `COMPONENTS.md`

## Skeleton

- **Role:** a placeholder that communicates loading state
- **States:** loading
- **Variants:** text, block, avatar
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