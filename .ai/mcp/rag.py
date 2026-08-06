"""PaglaDESIGN RAG indexer.

Builds a heading-aware lexical retrieval index over the repository's Markdown
documents. Used by the MCP server (``server.py``) to answer retrieval queries.

Design keeps this dependency-free (pure stdlib): retrieval is deterministic
BM25-style scoring over heading-chunked sections. No model, no network, no API
key — matching the PaglaAI zero-cost, open-source ethos. The corpus is the
authoritative Markdown; this index is only a view over it.

Index paths: chunks are keyed by their ``doc`` (repo-relative ``.md`` path) and
a ``start_line`` (1-based, absolute in the original file).
"""

from __future__ import annotations

import math
import os
import re
import unicodedata
from dataclasses import dataclass, field

# Root of the PaglaDESIGN repository (parent of this package's parent dir).
try:
    REPO_ROOT = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )
except NameError:  # pragma: no cover - interactive only
    REPO_ROOT = os.getcwd()

# Files/folders we never index into agents.
_EXCLUDED_DIRS = {".git", ".ai", "node_modules", "__pycache__", ".venv", "dist"}
_EXCLUDED_FILES = {"AGENTS.md"}


@dataclass
class Chunk:
    """A heading-anchored section of a document."""

    doc: str  # repo-relative path, e.g. "design-system/DESIGN_TOKENS.md"
    heading: str
    line: int  # absolute line of the chunk start in source file
    text: str

    def __str__(self) -> str:
        return f"{self.doc}#{self.heading} (line {self.line})"


@dataclass
class RetrievalResult:
    score: float
    chunk: Chunk

    def __lt__(self, other: "RetrievalResult") -> bool:
        return self.score > other.score  # descending


_TOKEN_RE = re.compile(r"[\w]+", re.UNICODE)


def _normalize(text: str) -> str:
    return unicodedata.normalize("NFKD", text)


def tokenize(text: str) -> list[str]:
    """Lowercase word tokens (Unicode-aware, no stopword list)."""
    return _TOKEN_RE.findall(_normalize(text).lower())


def _parse_chunks(text: str, doc: str) -> list[Chunk]:
    """Split ``text`` into sections at markdown headings (h1..h3)."""
    lines = text.splitlines()
    chunks: list[Chunk] = []
    current_heading = "Introduction"
    current_lines: list[str] = []
    start = 1
    for i, line in enumerate(lines, start=1):
        m = re.match(r"^(#{1,3})\s+(.+)$", line)
        if m:
            if current_lines:
                chunks.append(
                    Chunk(doc, current_heading, start, "\n".join(current_lines).strip())
                )
            current_heading = m.group(2).strip()
            current_lines = []
            start = i
            continue
        current_lines.append(line)
    if current_lines:
        chunks.append(
            Chunk(doc, current_heading, start, "\n".join(current_lines).strip())
        )
    return [c for c in chunks if c.text]


class RetrievalIndex:
    """BM25-style index over heading-chunked Markdown documents."""

    k1 = 1.5
    b = 0.75

    def __init__(self, root: str | None = None) -> None:
        self.root = os.path.abspath(root or REPO_ROOT)
        self.docs: list[Chunk] = []
        self._tf: list[dict[str, int]] = []
        self._dl: list[int] = []
        self._heading_tf: list[dict[str, int]] = []
        self._df: dict[str, int] = {}
        self._avgdl = 0.0

    # -- corpus --------------------------------------------------------- #

    @staticmethod
    def _iter_markdown(root: str):
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if d not in _EXCLUDED_DIRS]
            for name in filenames:
                if name in _EXCLUDED_FILES:
                    continue
                if name.endswith(".md") or name.endswith(".css"):
                    yield os.path.join(dirpath, name)

    def index(self) -> "RetrievalIndex":
        for path in self._iter_markdown(self.root):
            rel = os.path.relpath(path, self.root).replace("\\", "/")
            try:
                with open(path, "r", encoding="utf-8") as fh:
                    text = fh.read()
            except (OSError, UnicodeDecodeError):
                continue
            self.docs.extend(_parse_chunks(text, rel))
        self._build()
        return self

    def _build(self) -> None:
        for chunk in self.docs:
            toks = tokenize(chunk.text)
            tf: dict[str, int] = {}
            for t in toks:
                tf[t] = tf.get(t, 0) + 1
            # Heading tokens get extra weight so section-titled queries rank.
            htf: dict[str, int] = {}
            for t in tokenize(chunk.heading):
                htf[t] = htf.get(t, 0) + 1
            self._tf.append(tf)
            self._heading_tf.append(htf)
            self._dl.append(len(toks))
            for t in set(tf):
                self._df[t] = self._df.get(t, 0) + 1
        self._avgdl = sum(self._dl) / len(self._dl) if self._dl else 0.0

    # -- retrieval ------------------------------------------------------ #

    def query(self, query: str, k: int = 8) -> list[RetrievalResult]:
        n = len(self.docs)
        if n == 0:
            return []
        q_toks = set(tokenize(query))
        results: list[RetrievalResult] = []
        for idx, tf in enumerate(self._tf):
            dl = self._dl[idx]
            score = 0.0
            htf = self._heading_tf[idx]
            for term in q_toks:
                df = self._df.get(term, 0)
                idf = math.log(1 + (n - df + 0.5) / (df + 0.5))
                f = tf.get(term, 0)
                if f:
                    denom = f + self.k1 * (1 - self.b + self.b * (dl / self._avgdl if self._avgdl else 0.0))
                    score += idf * (f * (self.k1 + 1)) / denom
                if term in htf:  # heading boost
                    score += 2.0 * idf
            if score > 0:
                results.append(RetrievalResult(score, self.docs[idx]))
        results.sort(reverse=True)
        return results[:k]

    def get_chunk(self, doc: str, line: int) -> Chunk | None:
        for c in self.docs:
            if c.doc == doc and c.line == line:
                return c
        return None

    def lookup_token(self, name: str) -> list[str]:
        """Return lines from ``css/tokens.css`` defining ``--name``.

        Token names are dot-separated in documents (``color.accent.primary``)
        and hyphenated in CSS (``--color-accent-primary``).
        """
        token_path = os.path.join(self.root, "css", "tokens.css")
        want = "--" + name.strip().lstrip("-").replace(".", "-").lower()
        try:
            with open(token_path, "r", encoding="utf-8") as fh:
                text = fh.read()
        except (OSError, UnicodeDecodeError):
            return []
        return [
            line for line in text.splitlines()
            if ":" in line and line.strip().startswith(want)
        ]

    @property
    def doc_count(self) -> int:
        return len(self.docs)

    @property
    def source_docs(self) -> list[str]:
        return sorted({c.doc for c in self.docs})


# Convenience singleton: built once at import, reused by MCP handlers.
INDEX = RetrievalIndex().index()
