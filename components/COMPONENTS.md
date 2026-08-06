# COMPONENTS

> *A component is a shared behavior, not a decoration.*

---

# Purpose

COMPONENTS defines the component language of the PaglaAI ecosystem.

A component is a reusable piece of interface with a defined role, structure, and behavior.

Components are the building blocks shared across every product.

They exist to keep interactions consistent and to reduce duplicate work.

---

# Component Principles

- One role per component.
- Behavior shared, appearance inherited.
- No one-off components.
- Every component solves a recurring problem.
- Every component earns its place in the library.

If a component is used once, it is not a component.

---

# Component Anatomy

Every component shares a common anatomy:

- **Name**
- **Role** — what it communicates or does
- **States** — the states it can occupy
- **Structure** — the elements it contains
- **Variants** — approved changes, nothing more
- **Behavior** — how it responds to interaction

A component ignores what differs between products.

A component defines what must stay the same.

---

# Shared States

Every interactive component supports the same state set:

- Default
- Hover
- Focus
- Active
- Disabled
- Loading

States are consistent across the ecosystem (`../design-system/COLOR_SYSTEM.md`).

A user should never have to learn a new interaction just because they switched products.

---

# Component Language

## Button

A single, identifiable action.

Roles by emphasis:

- Primary — the recommended action
- Secondary — an alternative action
- Ghost — a quiet, low-emphasis action
- Destructive — an irreversible or dangerous action

Buttons signal a clear next step.

## Input

A field that captures a single piece of information.

Always accompanied by a clear label. Helps a user enter correct data (`../design-system/ACCESSIBILITY.md`).

## Chip

A compact label or filter.

Turns on and off. Never used for navigation to another context.

## Card

A surface that groups related content.

Structure and hierarchy between cards are communicated by spacing and type, not decoration.

## List

A vertical sequence of related items.

## Table

A structured comparison of rows and columns.

## Tabs

A set of related views where only one is visible at a time.

## Modal

A focused task that interrupts the current view.

Modal should be justified, never casual.

## Toast

A brief, non-blocking confirmation or status message.

## Menu

A set of actions or links revealed on demand.

## Skeleton

A placeholder that communicates loading state without motion-spam.

---

# Rules

- Reuse before re-creating.
- Prefer the existing component to a novel one.
- Extend the system when it benefits every product.
- Never build a one-off that only a team needs.
- A state change is part of the design; a new implementation is documented before it is built.

---

# Guidance

## Sizing and spacing

Follow the `../design-system/DESIGN_TOKENS.md` scale.

Spacing between components comes from the shared space tokens, not component-specific glue.

## Focus

Every focusable component shows a visible, keyboard-accessible focus state.

Never remove focus styling to "clean up" a screen.

## Disabled

Disabled is a stripped-down state, not a hint.

A disabled button communicates that the action is not available; it does not explain why. When the reason matters, add explanatory text.

## Responsive

Components inform the breakpoints of `../design-system/DESIGN_TOKENS.md`.

They should scale without completely separate mobile structures.

## Motion

Any motion a component uses comes from `../design-system/MOTION.md`, and respects the reduced-motion toggle.

---

# Naming

Components are named by role, not by look.

Use semantic, singular names (button, chip, menu) —

Product-specific names without a shared role are not library members.

---

# Relationship to Documents

- Appearance and color — `../design-system/DESIGN_TOKENS.md`, `../design-system/COLOR_SYSTEM.md`
- Typography in components — `../design-system/TYPOGRAPHY.md`
- Behavior — this document
- Decision history — `../docs/DECISIONS.md`

---

# Final Principle

Good components disappear into the product they serve.

A user should notice the task, not the component that enabled it.