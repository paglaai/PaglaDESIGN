# .ai

Agent tooling for coding agents working in the PaglaAI ecosystem.

This folder was removed in v0.9 (D-012) because it had no real content. It
returns in v1.1 (D-014) for a concrete reason: **agent infrastructure**.

## Contents

- `mcp/` — PaglaDESIGN MCP server with RAG retrieval over the repository's
  canonical Markdown and token CSS. Lets coding agents ground UI work in the
  design authority instead of guessing values.
- `agent-manual/` — the agent operating procedure (D-020). Operating rules
  only; it inherits tokens, components, templates, and MCP tools from the
  authority instead of redefining them. Includes `build_docx.py`, which
  generates a styled Word copy of the manual.

## Convention

Anything here exists to help **agents** work consistently with the design
system. It is not product code. It is not documentation of the design language
itself (that lives in `design-system/`, `brand/`, `governance/`, etc.).

Keep the corpus authoritative: this folder is excluded from the RAG index so
agent tooling never retrieves itself.
