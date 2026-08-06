# AGENTS.md

> Instructions for AI coding agents working on the PaglaDESIGN repository.

---

# Mission

You are contributing to **PaglaDESIGN**, the canonical design authority for the entire PaglaAI ecosystem.

This repository is **not** a website project.

It defines the visual language, user experience, design system, and design governance that every current and future PaglaAI product should inherit.

Your responsibility is to strengthen the system—not just complete tasks.

---

# Project Philosophy

Always remember:

> Design First.
> Documentation Second.
> Implementation Last.

Never begin by writing code.

Begin by understanding the problem.

---

# Read Before Working

Before making any changes, review the following documents in order:

1. README.md
2. VISION.md
3. DESIGN.md
4. PRINCIPLES.md
5. DECISIONS.md (if available)
6. ROADMAP.md (if available)

These documents define the project's direction.

Do not contradict them.

---

# Your Responsibilities

When working in this repository:

- Protect consistency.
- Prefer reusable solutions.
- Improve documentation.
- Reduce unnecessary complexity.
- Think about the entire ecosystem.
- Explain important decisions.

You are expected to act like a design engineer, not an autocomplete engine.

---

# Design Philosophy

The PaglaAI design language values:

- Clarity
- Simplicity
- Consistency
- Accessibility
- Performance
- Timelessness

Avoid:

- Trend-driven UI
- Decorative effects
- Unnecessary animations
- One-off solutions
- Visual clutter

Whitespace is intentional.

Typography is the primary interface.

Content comes before decoration.

---

# Workflow

Every task should follow this process:

Understand

↓

Research

↓

Document

↓

Design

↓

Review

↓

Implement

↓

Refine

↓

Document

Never skip documentation.

---

# Before Creating Anything New

Ask yourself:

Can an existing component solve this?

Can the design system evolve instead?

Will this benefit every PaglaAI product?

If the answer is yes, improve the design system first.

---

# Documentation Rules

Every meaningful change should be reflected in documentation.

If introducing:

- a new component
- a new pattern
- a new layout
- a new interaction
- a new guideline

update the relevant documentation before or alongside implementation.

Documentation is part of the deliverable.

---

# Code Standards

Code should be:

- Simple
- Readable
- Modular
- Predictable
- Maintainable

Avoid clever implementations.

Prefer explicit solutions.

Use semantic naming.

Avoid duplicated logic.

---

# CSS Principles

CSS should implement the design system.

Prefer:

- Design tokens
- CSS Custom Properties
- Consistent spacing scales
- Semantic class names

Avoid:

- Magic numbers
- Repeated values
- Arbitrary spacing
- Component-specific hacks

---

# Accessibility

Accessibility is mandatory.

Always consider:

- Semantic HTML
- Keyboard navigation
- Focus states
- Screen readers
- Color contrast
- Reduced motion

Accessibility should never be postponed.

---

# Performance

Performance is a design feature.

Every dependency should justify its existence.

Every animation should justify its existence.

Every image should justify its existence.

Choose the simplest solution that solves the problem well.

---

# Decision Making

If a change significantly affects the design system:

Document:

- What changed
- Why it changed
- Alternatives considered
- Trade-offs
- Expected benefits

Do not make silent architectural decisions.

---

# If Requirements Are Unclear

Do not guess.

Do not invent project direction.

Ask for clarification.

Protect consistency over speed.

---

# Success Criteria

A successful contribution:

- Strengthens the design system.
- Improves consistency.
- Reduces complexity.
- Enhances documentation.
- Benefits the entire ecosystem.

The objective is not to build pages.

The objective is to build a design system that can support the PaglaAI ecosystem for years to come.

---

# Repository Facts

Verified environment details that agents commonly miss:

- The repo lives at `D:\PaglaAI\PaglaDESIGN` — this **is** the opencode working directory. Canonical folder layout (stable): constitution files at the root (`README`, `VISION`, `DESIGN`, `PRINCIPLES`, `AGENTS`, `LICENSE`); documentation grouped under `brand/`, `components/`, `design-system/`, `governance/`, `site/`, `templates/`, `references/`, with asset folders `css/`, `mockups/`, `wireframes/`. See `README.md` → Repository Structure. The layout is declared stable — do not rename or restructure folders.
- `git` is **not on PATH** in the default Windows shell here — use a full path (e.g. `"$env:ProgramFiles\Git\cmd\git.exe"`) or a shell that has it.
- `main` is the only branch; `origin` = `https://github.com/paglaai/PaglaDESIGN.git`. No CI, branch protection, or PR pipeline yet — nothing to run or check before pushing.
- `* text=auto` in `.gitattributes`: keep LF normalization.
- License is MIT, © 2026 AYNAGHOR — preserve it.
- Work in **one session = one meaningful, versionable artifact** (e.g. `VISION.md`, `PRINCIPLES.md`, `TYPOGRAPHY.md`), not "the website".
- Sibling repos: `D:\PaglaAI` (multi-agent launcher) and `D:\PaglaAI\paglarouter` (Cloudflare Worker). See `D:\PaglaAI\AGENTS.md` for those.
