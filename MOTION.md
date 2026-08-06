# MOTION

> *Motion should guide, confirm, and orient. It should never distract.*

---

# Purpose

MOTION defines the motion language of the PaglaAI ecosystem.

Motion has a task: to guide the eye, confirm an action, and orient the user.

It is not entertainment.

It is meaningful, restrained, and fast.

---

# Philosophy

PaglaAI is calm. Its motion is calm too.

Every animation is quiet, purposeful, and quick.

Motion exists to communicate, never to show off.

If removing an animation does not reduce understanding, it does not belong.

---

# Principles of Motion

- **Fast** — never slow the user down
- **Clear** — always explains a change
- **Calm** — never noisy or playful
- **Consistent** — the same motion across products
- **Accessible** — always respects reduced motion

---

# What Motion Is For

Motion guides the user:

- **Orient** — where the user is, and where an element came from
- **Confirm** — that an action registered and the state changed
- **Reveal** — shared information in a controlled way
- **Focus** — drawing the eye to the current task

---

# What Motion Is Not For

- Decoration
- Novelty
- Brand theatrics
- Perpetual attention-seeking

Avoid continuous, looping, or unnecessary animation.

---

# Motion Duration

Motion is brief.

Naming uses the `motion.duration.*` tokens in `DESIGN_TOKENS.md`.

- `motion.duration.fast` — micro-interactions and state changes
- `motion.duration.base` — standard transitions
- `motion.duration.slow` — large or complex movements

Duration never should exceed what the change needs.

---

# Motion Gates

Every animation must pass these gates:

- **Does it have a purpose?** If not, remove it.
- **Does it clarify?** If it adds confusion, remove it.
- **Does it cost performance?** If it hurts, remove it.

An animation that fails a single gate does not belong.

---

# Interactions

| Interaction | Suggested motion |
| --- | --- |
| Hover | fast, subtle |
| Press | no motion or near-instant feedback |
| Focus | focus indicator always visible, never decorative |
| Element appearing | fast entrance, no bounce |
| Element disappearing | fast exit |
| View transition | base duration |
| Dialog / modal | base or slow |

---

# Surface Changes

Do not move the layout for decoration.

Only move something when the movement carries information.

- Respect the content column and surrounding whitespace.
- Never use layout shift to make motion.
- Where possible, guard against content jump with `content-visibility` / size-hinting.

---

# Reduced Motion

Follow the system's reduced-motion preference by default.

When the user and OS request reduced motion:

- Provide `motion.reduced` fast or zero-duration pathways
- Remove non-essential decoration
- Keep orientation and state changes readable

Never force movement on a user who does not want it.

Prefer accessible labels over decorative jumps.

---

# Impact

Motion must carry meaning.

An animation is only acceptable when:

- It guides the user
- It does not obscure the underlying change

If motion is present without purpose, it is noise.

---

# Relationship to Documents

- Tokens and easing — `DESIGN_TOKENS.md`
- Interaction states — `COLOR_SYSTEM.md`
- Component behavior — `COMPONENTS.md`
- Decision history — `DECISIONS.md`

---

# Final Principle

Motion that is felt but never noticed is the only motion worth keeping.

If a user can "see" the animation instead of the change, the animation has failed.