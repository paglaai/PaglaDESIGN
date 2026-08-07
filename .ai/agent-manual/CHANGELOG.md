# PaglaDESIGN Agent Manual — CHANGELOG

This file records changes to the manual itself. Canonical system changes are
recorded in `../../governance/CHANGELOG.md`, not here.

Versioning follows Semantic Versioning.

---

## [2.0.0] - 2026-08-07

### Changed
- **Rewritten as operating procedure** — the manual now inherits the
  canonical system instead of defining it (D-020).
- **§3 Tokens** — replaced the manual's own palette/fonts/spacing tables with
  inheritance rules pointing at `../../css/tokens.css` and
  `../../design-system/DESIGN_TOKENS.md`.
- **§4 Components** — replaced the 11 invented components with the 14
  registered components from `../../components/COMPONENT_LIBRARY.md`.
- **§5 Layout** — replaced the 12-column grid with the canonical layout
  tokens and `../../templates/`.
- **§8 Lint** — replaced the fabricated `pagladesign-lint` CLI with a
  severity model aligned to the canonical rules (R-01 … R-08).
- **§10 MCP** — replaced the 12 fabricated tools with the 6 real tools from
  `../mcp/server.py` (`search`, `get_doc`, `list_docs`, `lookup_token`,
  `search_tokens`, `get_context`).
- **§7 STITCH** — documented as external and optional; never an authority.
- **§9 Skills** — now references installed consumer skills and their limits.
- **Appendix A** — quick reference now points to canonical sources.

### Added
- **§2 Working Relationship** — the authority-pyramid model.

### Removed
- Invented token values (`#FF3E00` accent, `#0A0A0A` palette, gradients,
  shadows), invented fonts, invented components, invented MCP tools.
- Claim of verification against `css/tokens.css` that was false at v1.0.0.
- Duplicate DOCX artifacts.

### Fixed
- `build_docx.py` — wrong source/output paths (`.ai/AGENT_MANUAL.md` and
  `DOC/`), non-canonical "Deep Sea Academic" styling (navy/gold) replaced with
  canonical monochrome tokens.

### Governance
- Adopted under canonical Decision **D-020**.

---

## [1.0.0] - 2026-08-06

- Initial release ("PaglaOS × Stitch × PaglaDESIGN").
- Superseded by 2.0.0. The v1.0.0 content defined values and components that
  disagreed with the canonical authority; it has been replaced rather than
  patched.

---

*© 2026 AYNAGHOR.*
