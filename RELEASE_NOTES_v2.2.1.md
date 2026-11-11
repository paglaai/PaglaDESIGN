# PaglaDESIGN v2.2.1

Released: 2026-11-11

PaglaDESIGN v2.2.1 delivers critical audit remediation across MCP retrieval tooling, document generation, ecosystem schema enforcement, and contributor documentation drift, governed under Decision **D-026**.

## Highlights

### MCP Retrieval Hardening & Token Isolation
- **Search Ranking Correction:** Fixed `RetrievalResult.__lt__` comparison logic and sort pipeline in `.ai/mcp/rag.py`. Query results now strictly rank by descending BM25 score, ensuring the most relevant chunks are returned first.
- **Exact Token Value Isolation:** Replaced prefix matching (`startswith`) with exact CSS property matching (`prop.strip() == want`). Looking up `space.1` now returns exclusively `--space-1`, eliminating false-positive matches such as `--space-12` or `--space-1-5`.
- **Authority Boundary Protection:** Added `references` to `_EXCLUDED_DIRS` in the RAG indexer. Research captures, external benchmarks, and non-canonical notes are excluded from semantic search.
- **Host Path Sanitization:** Sanitized `.ai/mcp/server.py` `get_context()` to return repository-relative `"repo": "PaglaDESIGN"`, eliminating local path disclosure. Normalized `.ai/mcp/README.md` and `.ai/mcp/run.cmd` across platforms.

### Document Generation Stability
- **DOCX Empty Cell Guard:** Added empty-run safety guards in `bin/build_docx.py`. Paragraph runs in table cells are safely checked before applying bold styles, preventing `IndexError` crashes on blank header or body cells.
- **Regenerated Word Documentation:** Recompiled `DOC/AGENT_MANUAL.docx` with all safety checks applied.

### Schema & CI Integrity
- **Unique Registry IDs:** Added `"uniqueItems": true` to `ecosystem.schema.json` to formally enforce uniqueness across ecosystem repository identifiers.
- **CI Assertion:** Added an explicit duplicate ID check in `.github/workflows/ci.yml` that halts integration builds if colliding ecosystem IDs are introduced.
- **Automated Regression Suite:** Expanded `tests/test_tokens_parity.py` with `test_ecosystem_registry_unique_ids` and `test_mcp_rag_ranking_and_exact_tokens`.

### Documentation & Reference Harmonization
- **Component Path Fixes:** Repaired broken references pointing to `design-system/COMPONENTS.md` across `governance/AUDIENCE_RENDERER_SPEC.md` and `design-system/FERN_RENDERER.md`, routing directly to canonical `components/COMPONENTS.md`.
- **Reference Cleanliness:** Removed reference to non-existent `references/github/` directory from `references/README.md` and corrected relative links. Stripped machine-specific Windows paths from `references/pagla-mlx/NOTES.md`.
- **Agent Manual Parity:** Harmonized `.ai/AGENT_MANUAL.md` with canonical values from `design-system/DESIGN_TOKENS.md`: updated principle count to 14 (adding Audience Rendering), component registry to 14 (adding Breadcrumbs, Code Block, Terminal), and aligned typography tracking and line-height tokens.
- **Registry Alignment:** Updated `AGENTS.md` and `ecosystem.json` to 17 repositories (10 active, 7 planned) at version 2.2.1.
- **Repository Hygiene:** Purged tracked `.kilo` plan directory and added `.kilo/` and `agent.md` to `.gitignore`.

## Verification

- `tests/test_tokens_parity.py`: 12/12 tests passed (including unique ID and MCP retrieval tests).
- `tests/test_fern_renderer.py`: All 16 tests passed.
- `bin/build_fern.py`: Generated 30 canonical documentation pages with 0 broken links.
- `black --check .ai/mcp` and `flake8 .ai/mcp`: 100% compliant with 0 errors.
- Schema validation: `ecosystem.json` and `ecosystem.schema.json` validated cleanly with `python3 -m json.tool`.

## Installation & Upgrade

Published to **GitHub Packages** (`@paglaai` scope):

```bash
# Configure registry for @paglaai scope:
echo "@paglaai:registry=https://npm.pkg.github.com" >> .npmrc
npm install @paglaai/pagladesign@2.2.1

# Or install directly with the registry flag:
npm install @paglaai/pagladesign@2.2.1 --registry=https://npm.pkg.github.com
```
