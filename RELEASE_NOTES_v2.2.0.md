# PaglaDESIGN v2.2.0

Released: 2026-10-19

PaglaDESIGN v2.2.0 introduces the FERN human documentation portal, hardens the MCP design-authority boundary, and makes token compilation, CI validation, downstream dispatch, and GitHub Packages publishing more reliable.

## Highlights

### FERN documentation portal

- Added the FERN-style static documentation renderer and GitHub Pages deployment pipeline.
- Added the FERN portal’s visual token explorer and interactive component-library output.
- Fixed inline Markdown handling so underscores in filenames, code spans, links, image URLs, and badges are not misinterpreted as italics.
- Added page-aware internal link resolution, with GitHub fallbacks for files not published to the portal.
- Added 16 renderer regression tests, including a full-site build check.
- Replaced machine-specific Windows paths with repository-relative configuration.

### MCP security hardening

- Restricted `get_doc` to canonical authority files and approved design-system directories.
- Blocked absolute paths, traversal, hidden paths, secret files, unsupported extensions, and symlinks in any path component.
- Added adversarial tests for traversal, hidden files, symlinks, allowlist enforcement, and search behavior.

### Token and ecosystem integrity

- Replaced validation-only token processing with deterministic CSS generation from `design-system/DESIGN_TOKENS.md`.
- Added generated stylesheet drift detection to CI.
- Enforced the complete `ecosystem.schema.json` using `jsonschema` rather than selected hand-written assertions.
- Normalized the canonical authority repository to `paglaai/pagladesign`.

### Release and automation reliability

- Release publishing now fails on authentication, registry, and packaging errors while safely skipping only verified duplicate-version responses.
- Downstream `design.updated` dispatches now check HTTP status and curl exit codes; failures are no longer silently ignored.
- CI now runs the complete test suite and treats an empty test collection as a failure.
- GitHub Actions dependencies used by the release workflow are pinned to immutable commit SHAs.
- Published `@paglaai/pagladesign@2.2.0` to GitHub Packages.

## Verification

- 26 repository tests passed.
- 16 MCP security tests passed.
- Python compilation, JSON validation, JSON Schema validation, Black formatting, embedded token-action checks, and workflow YAML parsing passed.
- The GitHub Actions release workflow completed successfully and published the package.

## Notable commits

- `caa5216` — Fix setup-node release action pin
- `3f6c397` — Harden MCP boundary and CI release workflows
- `d9c1d76` — Run the whole `tests/` folder in the token job
- `c72a5a8` — Stop italics mangling links, badges, and file names in the docs portal
- `0565d7a` — Bump package and portal version to 2.2.0
- `0eb0563` — Deploy the FERN-style documentation portal to GitHub Pages

## Upgrade

```bash
npm install @paglaai/pagladesign@2.2.0
```

The package includes the canonical CSS token layers, design-system documentation, component documentation, BrandKit assets, fonts, ecosystem registry, and schema.
