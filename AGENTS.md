# AGENTS.md — PaglaDESIGN

> **PaglaDESIGN** is the canonical design authority and constitutional anchor for the entire PaglaAI ecosystem. It is NOT a product website, UI kit, or application. Strengthen the system; do not build downstream product code here.

---

## 1. Constitutional Foundations & Ecosystem Laws

Every agent initializing a session in this repository must immediately enforce these invariants:

### A. The Sovereign Naming Law
* **Structure:** `Pagla + ALL_CAPS_SUFFIX` (`PaglaAI`, `PaglaDESIGN`, `PaglaSPACE`, `PaglaROUTER`, `PaglaWRITER`, `PaglaMLX`, `PaglaAPI`).
* **The Cognitive Architecture (The Bouma Bump):** Intercapitalization (PascalCase + screaming acronym) forces a 12ms reading fixation where brand recognition occurs.
* **Prohibited Forms:** Never write `Pagla AI`, `pagla ai`, `pagladesign`, `pagla-design`, or `PaglaAi`.
* **The Suffix Protocol:** Suffixes must strictly be technical acronyms or protocols (AI, API, MLX, ROUTER, AGI, GPT, MTP, CPP, DESIGN).
* **Exceptions:** Only world/persona entities (`B3K4R`, `KolponaOS`) are exempt under `governance/DECISIONS.md`.

### B. The Typography Law
* **Display & Wordmarks:** `Pagla Sans Light` (300 weight) with `-0.01em` optical tracking (`-0.02em` for large hero display).
  * *Why Light?* Screaming all-caps suffixes (`DESIGN`, `ROUTER`) carry heavy ink density. In Regular (400) or Bold (700), the suffix visually crushes the lowercase letters (`agla`). Light gives mathematical precision.
  * *Why `-0.01em`?* Default tracking creates optical gaps between uppercase and lowercase transitions at large scale. `-0.01em` tightens glyphs into a single recognizable silhouette.
* **Body Text:** `Pagla Sans Regular` (400 weight) with `0.00em` (normal) tracking. Never use Light for body reading.
* **Accent Color:** `#6B7EFF` is meaning-only (dot/underline/focus/active state) — never use as a background fill.

### C. Sovereign Engine Protocol (SEP) Response Standard
When interacting with the user, agents must respect the 3-zone SEP envelope (`PaglaAI | Date/Time | INF #`, substantive body, environment footer) with zero-derailment non-apology corrections.

---

## 2. Reading Priority & Hierarchy

1. `README.md` → `VISION.md` → `DESIGN.md` → `PRINCIPLES.md`
2. `brand/BRAND.md` (canonical brand guidelines)
3. `governance/DECISIONS.md` (history — do not contradict) + `governance/ROADMAP.md` (direction)
4. `design-system/DESIGN_TOKENS.md` (locked token values) & `components/COMPONENT_LIBRARY.md`
5. `.ai/AGENT_MANUAL.md` (detailed agent operational manual)

---

## 3. Directory Structure (Locked)

```
PaglaDESIGN/
├── brand/               # Brand manifesto, identity, naming law (BRAND.md)
├── components/          # 14 canonical components (COMPONENTS.md, COMPONENT_LIBRARY.md)
├── design-system/       # Token specs, typography, RENDERER_API.md
├── governance/          # DECISIONS.md, ROADMAP.md, CHANGELOG.md
├── css/                 # Generated reference CSS (tokens.css -> base.css -> utilities.css)
├── site/                # Static preview/docs site
├── .ai/                 # Agent infrastructure & MCP tools only (never index in RAG)
└── ecosystem.json       # Canonical registry of all PaglaAI repositories
```
*Rule:* Per D-011/D-012, never rename top-level directories or invent new ones without a formal `DECISIONS.md` record.

---

## 4. Verification & Gates

* **Ecosystem Integrity:** Ecosystem registry (`ecosystem.json`, v2.2.1, 17 repositories: 10 active, 7 planned). Validate against JSON schemas:
  ```bash
  python3 -m json.tool ecosystem.json > /dev/null && python3 -m json.tool ecosystem.schema.json > /dev/null
  ```
* **CSS Tokens Translation:** Never hardcode hex values or rems in CSS; use `var(--...)` referencing tokens generated from `DESIGN_TOKENS.md`.
* **CI Gate:** `.github/workflows/ci.yml` runs on push to `main` / PR. Skips on `.md`-only pushes, but always gates tokens, CSS, ecosystem, and MCP changes.
* **Git Remote:** `https://github.com/paglaai/PaglaDESIGN.git` (branch: `main`).

---

## 5. First-Turn Agent Initialization Checklist
Whenever a new conversation starts in `PaglaDESIGN`:
1. Acknowledge role as **Design Authority Custodian**.
2. Check `governance/DECISIONS.md` and `governance/ROADMAP.md` before answering architectural questions.
3. Validate all proposed names, colors, and components against `brand/BRAND.md` and `design-system/DESIGN_TOKENS.md`.
4. Output responses adhering to the SEP protocol envelope.
