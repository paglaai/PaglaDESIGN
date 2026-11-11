# PaglaDESIGN MCP Server

Model Context Protocol server exposing the PaglaDESIGN design authority to
coding agents. Agents retrieve the canonical design system (tokens, typography,
color, components, decisions, brand, sitemap, content strategy) and ground
their UI work in it — without reading the whole repository.

## What it provides

| Tool | Purpose |
| --- | --- |
| `search(query, k)` | RAG retrieval: most relevant design-system sections for a query (BM25 over heading-chunked Markdown + CSS) |
| `get_doc(path)` | Read a whole canonical document by repo-relative path |
| `list_docs()` | List every indexed document and its section count |
| `lookup_token(name)` | Exact locked value of a design token from `css/tokens.css` |
| `search_tokens(term)` | Fuzzy-find token names by keyword |
| `get_context()` | One-call orientation: repo, authority docs, corpus summary |

## Design

- **Deterministic, zero-cost, no API key.** Retrieval is pure-stdlib BM25 over
  heading-chunked Markdown. No model, no network, no embeddings service. This
  matches the PaglaAI zero-cost, open-source ethos and keeps results reproducible.
- **No magic values.** `lookup_token` reads `css/tokens.css`; a value that can't
  be found is reported as locked and routed through the decision workflow.
- **Safe.** File reads are confined to the repository root (path traversal
  blocked).

## Run

```bash
python -m pip install -r requirements.txt     # mcp>=2.0
python server.py                              # stdio transport (default)
```

On Windows, `run.cmd` launches the server in stdio mode using the active
virtual environment or python from PATH.

## Register with a coding agent

### opencode

Project config `.opencode/opencode.json` registers it as a local MCP
server using `["python3", ".ai/mcp/server.py"]`. Restart opencode after changing config.
`REPO_ROOT` is derived from the server file, so it works from any working directory.

### Claude Code / Cursor / other

Register as a local MCP server pointing at:

```bash
python3 .ai/mcp/server.py
```

## Layout

- `server.py` — MCP server (`FastMCP`, MCP SDK 2.x), stdio transport
- `rag.py` — BM25 retrieval index over canonical Markdown and `css/tokens.css`
- `run.cmd` — Windows launcher
- `requirements.txt` — `mcp>=2.0`

The `mcp` package requires Python 3.10+ (`mcp>=2.0`). Install dependencies via:
`pip install -r requirements.txt`.

## Versioning

The server logs its own `SERVER_VERSION` (0.1.0). Repository releases track
the design system (CHANGELOG); the server version is independent.