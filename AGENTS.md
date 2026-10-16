# AGENTS.md

> PaglaDESIGN is the canonical design authority for the PaglaAI ecosystem — not a website, UI kit, or app. Strengthen the system; don't build product here.

## Read first

1. `README.md` → `VISION.md` → `DESIGN.md` → `PRINCIPLES.md`
2. `governance/DECISIONS.md` (history — read as history, don't contradict) + `governance/ROADMAP.md` (direction)
3. For the task at hand: `design-system/DESIGN_TOKENS.md`, `components/COMPONENT_LIBRARY.md`, `ecosystem.json`
4. Full operating procedure lives in `.ai/AGENT_MANUAL.md` — this file is the quick-start, not a duplicate.

Workflow is Design First, Documentation Second, Implementation Last. One session = one meaningful, versionable artifact.

## Structure (stable — do not reorganize)

Root constitution: `README.md VISION.md DESIGN.md PRINCIPLES.md AGENTS.md LICENSE` stay at root. Docs live in `brand/ components/ design-system/ governance/ site/ templates/ references/`; assets in `css/ fonts/ mockups/ wireframes/`; agent infra in `.ai/`; scripts in `bin/`; site deploy artifacts in `DOC/`. Per D-011/D-012: never rename top-level folders or add new ones without a `DECISIONS.md` entry. `references/` is non-canonical research — never cite it as authority.

## Sources of truth (trust in this order)

- Token values: `design-system/DESIGN_TOKENS.md` (locked, D-010). `css/tokens.css` is the generated reference translation — never invent values inline, never hardcode `#hex`/`rem` in styles; use `var(--…)` (note naming shift: `color.base.ink` in docs → `--color-base-ink` in CSS).
- Components: `components/COMPONENTS.md` is the grammar, `components/COMPONENT_LIBRARY.md` is the registry (14 entries: Button, Input, Chip, Card, List, Table, Tabs, Modal, Toast, Menu, Skeleton + Breadcrumbs, Code Block, Terminal). Used-once ≠ component; no one-offs.
- Ecosystem: `ecosystem.json` (v2.0.0, 16 entries: 9 active · 7 planned) + `ecosystem.schema.json`. `README.md` Ecosystem section points at it — update the JSON, don't duplicate lists in prose.
- Doc frontmatter: `design-system/RENDERER_API.md` — every doc page needs `title` + `audience: [human|machine|architect]`; missing `audience` = skipped by all consumers. Route: FERN→human HTML, MACHINE→JSON/OpenAPI/MCP/prompt bundles, ARCHITECT→RFC/ADR/governance. Never invent renderer logic in a consumer.
- CSS layers: `css/tokens.css` → `css/base.css` → `css/utilities.css`, loaded in that order. No framework, component package, or rendered HTML lives here (D-013) — those belong to consumers (e.g. `paglaai.space` inherits `css/tokens.css`).
- Naming: typeface is `"Pagla Sans"` (D-021), monochrome-first, accent `#6B7EFF` is meaning-only — dot/underline/focus, never a background fill.

## Verify (no root package manager; CI is the gate)

- CI (`.github/workflows/ci.yml`, ubuntu + Python 3.11) triggers on push to `main` / PR, but **skips on `**.md`-only or `LICENSE`-only pushes**. Token/CSS/ecosystem/MCP changes always run.
- Ecosystem: `python3 -m json.tool ecosystem.json > /dev/null && python3 -m json.tool ecosystem.schema.json > /dev/null` — full duplicate-ID / `paglaai/*` / status / role checks live in the `validate-ecosystem` job; mirror them, don't shortcut.
- MCP server (`.ai/mcp/`, deps `mcp>=2.0` via `.ai/mcp/requirements.txt`): `python3 -m py_compile .ai/mcp/server.py .ai/mcp/rag.py`; if editing it, from `.ai/mcp/`: `black --check .`, `flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics`, `pytest` (falls back to the py_compile check when no tests exist).
- DOCX is generated: `python3 bin/build_docx.py` (needs `python-docx`) rebuilds `DOC/AGENT_MANUAL.docx` from `.ai/AGENT_MANUAL.md` — never hand-edit `DOC/`.
- Release (`.github/workflows/release.yml`, on release-published): rebuilds tokens via `.github/actions/build-tokens` and publishes `pagladesign-assets.tar.gz` + `ecosystem.json` + `css/tokens.css`.

## Conventions that differ from defaults

- Significant change → `governance/DECISIONS.md` entry (Context / Decision / Alternatives / Trade-offs / Result) + `governance/CHANGELOG.md` entry + relevant doc update, **before** implementation. No silent architecture.
- Theming: light `:root` default, dark via `[data-theme="dark"]`; default to `prefers-color-scheme`, persist explicit choice to `localStorage`. Always: `font-display: swap`, visible focus, semantic HTML, `prefers-reduced-motion` support, ≥4.5:1 body contrast, ≥`2.75rem` touch targets.
- `.ai/` is agent infrastructure only and excluded from the MCP/RAG index — never index it, never put product docs there.
- Git: `main` only, `origin` = `https://github.com/paglaai/pagladesign.git`. `.gitattributes` `* text=auto` — keep LF. MIT © 2026 AYNAGHOR.

## Gotchas agents actually hit

- `.opencode/opencode.json` registers the `pagladesign` MCP server with a hardcoded Windows interpreter (`D:\PaglaAI\.venv\Scripts\python.exe`). On macOS/Linux run `python3 .ai/mcp/server.py` (stdio) after `pip install -r .ai/mcp/requirements.txt` instead of copying that path. Same staleness in `.ai/mcp/README.md` / `run.cmd` / old `.ai/AGENTS.md` `D:\…` paths.
- `css/tokens.css` `@font-face` blocks still say `"PaglaAI Sans"`; canonical family name is `"Pagla Sans"` (D-021, `DESIGN_TOKENS.md`). Trust the docs for the name.
- `ecosystem.json:roadmap` mirrors `governance/ROADMAP.md` Phase 1 active / Phases 2–3 planned (Audit v2.0, `paglaai/pagladesign#3`) — keep all three in sync when roadmap changes.
