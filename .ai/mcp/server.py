"""PaglaDESIGN MCP server.

Exposes the PaglaDESIGN design authority to coding agents via Model Context
Protocol. Provides retrieval (RAG) over the repository's Markdown and CSS
token files so agents can ground their work in the canonical design system
without reading the whole repo.

Run with::

    python server.py            # stdio transport (default)

The server speaks stdio MCP and is intended to be registered as a local MCP
server in coding agents (opencode, Claude Code, Cursor, ...). See README.md.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from mcp.server.mcpserver import MCPServer

from rag import INDEX, Chunk, REPO_ROOT, RetrievalResult, tokenize

SERVER_VERSION = "0.1.0"


def _format_result(r: RetrievalResult, include_text: bool = True) -> dict[str, Any]:
    chunk = r.chunk
    out: dict[str, Any] = {
        "doc": chunk.doc,
        "heading": chunk.heading,
        "line": chunk.line,
        "score": round(r.score, 3),
    }
    if include_text:
        out["text"] = chunk.text
    return out


def _safe_read(path: str) -> str | None:
    """Read a repo-relative text file, guarding against path traversal."""
    root = Path(REPO_ROOT).resolve()
    target = (root / path).resolve()
    if root not in target.parents and target != root:
        return None
    if not target.is_file():
        return None
    try:
        return target.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None


mcp = MCPServer(
    "pagladesign",
    title="PaglaDESIGN",
    description=(
        "The PaglaAI design authority. Ground coding work in the canonical "
        "design system: tokens, typography, color, components, decisions, "
        "brand, sitemap, and content strategy."
    ),
    instructions=(
        "Use the search tool to retrieve relevant design-system sections "
        "before proposing UI work. Use lookup_token for exact token values "
        "from css/tokens.css. Use get_doc to read a whole canonical document. "
        "Values are locked; a change requires the decision workflow."
    ),
    version=SERVER_VERSION,
)


@mcp.tool(
    name="search",
    description=(
        "Retrieve the most relevant PaglaDESIGN sections for a query. "
        "Returns doc, heading, line, score, and the chunk text. Use before "
        "any design/UI work to ground decisions in the design authority."
    ),
)
def search(query: str, k: int = 5) -> list[dict[str, Any]]:
    """BM25 retrieval over the indexed PaglaDESIGN corpus."""
    k = max(1, min(k, 20))
    return [_format_result(r) for r in INDEX.query(query, k)]


@mcp.tool(
    name="get_doc",
    description=(
        "Read a whole canonical PaglaDESIGN document by repo-relative path "
        "e.g. 'design-system/DESIGN_TOKENS.md', 'brand/BRAND.md', "
        "'governance/DECISIONS.md'. Returns the raw Markdown."
    ),
)
def get_doc(path: str) -> dict[str, str]:
    """Return a full repository document as Markdown."""
    text = _safe_read(path)
    if text is None:
        return {"error": f"document not found: {path}"}
    return {"doc": path, "content": text}


@mcp.tool(
    name="list_docs",
    description=(
        "List every document indexed in the PaglaDESIGN corpus, with the "
        "number of retrievable sections per document."
    ),
)
def list_docs() -> list[dict[str, Any]]:
    """List all indexed source documents and their section counts."""
    counts: dict[str, int] = {}
    for chunk in INDEX.docs:
        counts[chunk.doc] = counts.get(chunk.doc, 0) + 1
    return [{"doc": doc, "sections": counts[doc]} for doc in INDEX.source_docs]


@mcp.tool(
    name="lookup_token",
    description=(
        "Get the exact locked value(s) of a design token from css/tokens.css. "
        "Accepts either dot form 'color.accent.primary' or the CSS form "
        "'color-accent-primary'. Returns matching CSS custom-property lines."
    ),
)
def lookup_token(name: str) -> dict[str, Any]:
    """Look up a design token value in css/tokens.css."""
    lines = INDEX.lookup_token(name)
    if not lines:
        return {
            "token": name,
            "found": False,
            "note": "Not found in css/tokens.css. Tokens are locked in "
            "design-system/DESIGN_TOKENS.md; propose changes via the "
            "decision workflow.",
        }
    return {"token": name, "found": True, "values": lines}


@mcp.tool(
    name="search_tokens",
    description=(
        "Fuzzy-find design tokens by keyword, returning all token names that "
        "mention the term (e.g. 'accent', 'space', 'font'). Helps discover "
        "the exact token name before lookup_token."
    ),
)
def search_tokens(term: str) -> dict[str, Any]:
    """Return token names in css/tokens.css matching a keyword."""
    token_path = os.path.join(REPO_ROOT, "css", "tokens.css")
    try:
        text = Path(token_path).read_text(encoding="utf-8")
    except OSError:
        return {"term": term, "tokens": []}
    q = set(tokenize(term))
    hits = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("--"):
            continue
        name = stripped.split(":", 1)[0].strip()
        toks = set(tokenize(name))
        if q & toks:
            hits.append(name)
    return {"term": term, "tokens": sorted(hits)}


@mcp.tool(
    name="get_context",
    description=(
        "Return the whole context at once: corpus summary (doc count, source "
        "documents), a list of the most authoritative documents, and where "
        "they live. Useful as a one-call orientation for a fresh agent."
    ),
)
def get_context() -> dict[str, Any]:
    """One-call orientation over the design authority."""
    return {
        "repo": REPO_ROOT,
        "version": SERVER_VERSION,
        "doc_count": INDEX.doc_count,
        "source_docs": INDEX.source_docs,
        "authority": [
            "DESIGN.md",
            "PRINCIPLES.md",
            "VISION.md",
            "brand/BRAND.md",
            "design-system/DESIGN_TOKENS.md",
            "design-system/TYPOGRAPHY.md",
            "design-system/COLOR_SYSTEM.md",
            "design-system/CSS_ARCHITECTURE.md",
            "components/COMPONENTS.md",
            "governance/DECISIONS.md",
            "site/SITEMAP.md",
        ],
    }


if __name__ == "__main__":
    mcp.run(transport="stdio")
