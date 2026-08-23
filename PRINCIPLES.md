# PRINCIPLES

> *These principles are the foundation of every design decision made within the PaglaAI ecosystem.*

---

# 1. Design the System, Not the Page

Every solution should strengthen the design system before solving an individual problem.

Avoid creating one-off components, layouts, or interactions.

---

# 2. Clarity Over Cleverness

Users should never have to guess.

Interfaces should communicate purpose immediately.

If forced to choose between creativity and clarity, choose clarity.

---

# 3. Purpose Before Aesthetics

Every visual element must have a purpose.

If an element does not improve communication, usability, or accessibility, reconsider its existence.

Decoration should never become distraction.

---

# 4. Typography Is the Primary Interface

Typography communicates hierarchy, structure, and meaning.

Use typography before relying on colors, borders, or decorative elements.

Well-designed typography reduces the need for additional visual complexity.

---

# 5. Whitespace Is Content

Whitespace is not empty space.

It creates rhythm, improves readability, and allows information to breathe.

Never treat whitespace as wasted space.

---

# 6. Audience Rendering

Documentation serves different audiences. The same source should produce
consistent, purpose-built output for each.

PaglaDESIGN defines three canonical renderers:

- **FERN** — human readers: rich HTML, navigable, themed
- **MACHINE** — programmatic consumers: JSON, OpenAPI, MCP tool bundles, prompt bundles
- **ARCHITECT** — engineers and decision-makers: RFCs, ADRs, governance documents, audit views

Every doc page declares its audience through a standard metadata contract
(`RENDERER_API.md`). Consumers inherit the renderer logic instead of inventing
their own.

Inconsistent rendering is a failure of the design system.

---

# 7. Consistency Builds Trust

Interfaces should feel familiar across every PaglaAI product.

Shared patterns reduce learning, increase confidence, and create a cohesive ecosystem.

Consistency should evolve intentionally, never accidentally.

---

# 8. Performance Is Part of User Experience

Fast interfaces are easier to use.

Every design decision should consider loading time, responsiveness, and simplicity.

Avoid unnecessary complexity that increases visual or technical overhead.

---

# 9. Accessibility Is Non-Negotiable

Design should be usable by as many people as reasonably possible.

Accessibility must be considered from the beginning rather than added later.

Inclusive design creates better experiences for everyone.

---

# 10. Motion Must Communicate

Animation should guide, confirm, and orient users.

Motion should never exist solely for decoration.

If removing an animation does not reduce understanding, it probably does not belong.

---

# 11. Documentation Before Implementation

Every significant design decision should be documented before implementation.

The design system is the source of truth.

Code implements the design system—it does not define it.

---

# 12. Think in Ecosystems

Every decision should benefit the broader PaglaAI ecosystem rather than a single project.

Components, patterns, and documentation should be reusable wherever possible.

Design for tomorrow's products, not only today's requirements.

---

# 13. Timeless Over Trendy

Avoid following short-lived design trends.

Favor simplicity, readability, and longevity.

A timeless interface will outlast fashionable aesthetics.

---

# 14. Question Everything

Every design decision should have a clear reason.

If a decision cannot be explained simply, it should be reconsidered.

Challenge assumptions.

Protect consistency.

Remain intentional.

---

# Final Principle

> **Great design is not achieved by adding more.**
>
> **It is achieved by removing everything that does not serve the user.**