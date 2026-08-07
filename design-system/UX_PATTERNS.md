# UX_PATTERNS

> *Interaction is the quiet part of the design. It should be felt, never noticed.*

---

# Purpose

UX_PATTERNS defines the reusable interaction behaviors of the PaglaAI ecosystem.

Where `../components/COMPONENTS.md` names the parts and `../site/NAVIGATION.md`
maps the routes, this document defines **how states change and how the interface
behaves** — transitions, scroll rhythm, hover, loading, empty, error, not-found,
search, and theme switching.

Patterns are token-driven, not invented per product.

Every behavior here passes the gates of `MOTION.md` and the baseline of
`ACCESSIBILITY.md`. Where a pattern suggests a number, the number comes from
`DESIGN_TOKENS.md`.

---

# Principles

- **State before spectacle** — a state change communicates; decoration does not
- **Fast, by default** — interaction never slows the user down
- **Confirm, never guess** — every action visibly registers
- **Quiet under failure** — errors explain, they never blame
- **Same everywhere** — one behavior in every product
- **Reduced-motion safe** — nothing important relies on movement

---

# Transitions

## State transitions

A control changes state in `motion.duration.fast` (`100ms`) with
`motion.easing.default`.

- **Hover** — the control gains `color.state.hover` (border) instantly; any
  color or surface shift animates within the fast duration
- **Press** — near-instant feedback; the control may show
  `color.state.active` (`color.base.ink` at `8%` overlay) with no easing delay
- **Focus** — the focus indicator appears immediately and stays visible; it is
  never animated away (`ACCESSIBILITY.md`, `COLOR_SYSTEM.md`)

Only **state-carrying** properties transition — background, border, and text
color where a state change exists. Layout properties never animate for state.

## Entrance

New content enters in `motion.duration.base` (`200ms`) with
`motion.easing.entrance`.

- Appears **once** — no bounce, no looping, no stagger for its own sake
- Moves only when the movement carries orientation (`MOTION.md`)
- Respects the content column; never shifts layout to make motion

## Exit

Content leaves in `motion.duration.fast` with `motion.easing.exit`.

Exit is quicker than entrance so the interface clears the way, never lingers.

## View transitions

A full view change uses `motion.duration.base` and `motion.easing.default`.

Keep the transition a single, legible crossfade or displacement. Never run a
page-level animation that re-triggers on every render.

## Reduced motion

Under reduced motion, all durations resolve to `motion.reduced` (`0ms`) and
non-essential decoration is removed. Orientation and state changes stay
readable. See `MOTION.md` — this is the default, not an option.

---

# Scroll rhythm

Scroll is a reading behavior, not a spectacle.

- **Native scroll** — never hijack, never smooth-scroll the whole page against
  the user's preference
- **Sticky chrome** — the primary header may stay visible; pinned sidebars and
  secondary navigation collapse or become skimmable rather than fighting the
  reading column
- **Content first** — the scroll position is preserved across view transitions;
  back navigation returns the user to where they were
- **No scrolljacking** — scroll-driven animation, parallax, and fixed overlays
  are outside the language. If a reveal exists, it is a single entrance that
  runs once under `motion.reduced` rules
- **Progress** — where a long document needs orientation, an in-page
  table of contents or the scroll indicator in `../site/NAVIGATION.md` marks
  position with a token color, never a decoration

---

# Hover

Hover previews a state; it never carries the only meaning.

- Border and surface shift only — never reposition the layout
- `color.state.hover` is `color.base.border`; keep the change within
  `motion.duration.fast`
- Hover never hides or reveals critical content, because hover has no keyboard
  equivalent (`ACCESSIBILITY.md`)
- Secondary cues always accompany hover for pointer users — the focus ring, the
  underline, or the state color does the confirming

---

# Loading, empty, and error states

Every interactive surface declares four states before it ships:

## Loading

- Loading is announced, not implied (`ACCESSIBILITY.md`)
- A spinner or skeleton is optional; a screen-reader announcement and a stable
  layout are not
- Skeletons mirror the final layout shape with `color.base.surface`; the pulse
  or shimmer is `motion.duration.fast`, never a distracting loop
- Loading never triggers layout shift — the container reserves its space

## Empty

- Empty states explain what belongs here and how to fill it
- Lead with the outcome ("No results"), then the next step (the action or link)
- An empty state is content, not a gap

## Error

- Errors are explained in plain words, next to the thing they concern
- `color.accent.error` is reinforced by text — color is never the only carrier
  (`ACCESSIBILITY.md`)
- Retry is the natural next step, not a hidden affordance
- Error messages state what the user can do, not what the system feels

## Transient states

All three states enter and exit within `motion.duration.fast`. A state that
changes meaning mid-display re-announces itself.

---

# Not found (404)

The not-found page is a designed state, not an accident.

- One accurate top-level heading ("Page not found")
- Plain next steps: return to the start, search, or visit the sitemap
- The Pagla Face may carry the message with restraint — the page stays
  monochrome and calm (`D-006`, `D-008`)
- No dead end: every not-found view links forward

---

# Search

Search is navigation with a query (`../site/NAVIGATION.md`).

- A query field has a programmatic label; placeholder text is never the label
- Results appear in the context of the query — the query stays visible and
  editable
- Result titles describe the destination; snippets carry the context
- No results is the empty state above: outcome first, then a suggested query or
  the sitemap
- Keyboard: results are reachable in tab order; Escape closes and returns focus
  to the trigger
- The command/search surface, where used, is a dialog with focus containment
  and a dismiss path

---

# Theme switching

Light and dark share one semantic structure; only values change (`D-010`,
`DESIGN_TOKENS.md`).

- **Default** is the user's `prefers-color-scheme`; the persisted choice wins
  once made
- **Toggle** flips between the two themes; the switch is a control with a
  visible state and a label that changes ("Light" / "Dark")
- **Transition** between themes is a `motion.duration.fast` crossfade of
  token-driven colors, or none under reduced motion — never a jarring flip
- **Consistency** — both themes pass the same contrast baseline; accent colors
  keep their meaning in both
- The choice is remembered across visits; a manual choice overrides the OS
  preference until changed again

---

# Pattern gates

Every interaction pattern must pass:

- **Purpose** — does it communicate a state or orient the user?
- **Parity** — does it have a keyboard equivalent and a non-color cue?
- **Reduced motion** — does it resolve to `motion.reduced`?
- **Token purity** — does it reference a token instead of inventing a value?

A pattern that fails one gate is not used.

---

# Relationship to Documents

- Motion and timing — `MOTION.md`
- State values and theme — `DESIGN_TOKENS.md`, `COLOR_SYSTEM.md`
- Requirements — `ACCESSIBILITY.md`
- Component behavior — `../components/COMPONENTS.md`
- Routes and navigation — `../site/NAVIGATION.md`, `../site/SITEMAP.md`
- Research basis — `../references/INSPIRATION.md`
- Decision history — `../governance/DECISIONS.md`

---

# Final Principle

The best interaction is the one the user never notices.

If a pattern draws attention to itself, it has failed the user.
