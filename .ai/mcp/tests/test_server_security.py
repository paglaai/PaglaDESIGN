from pathlib import Path

import pytest

import server


@pytest.fixture()
def repo_root():
    return Path(server.REPO_ROOT)


def test_allowed_authority_document_is_readable():
    content = server._safe_read("design-system/DESIGN_TOKENS.md")
    assert content is not None
    assert "DESIGN_TOKENS" in content


@pytest.mark.parametrize(
    "path",
    [
        "../README.md",
        "design-system/../../README.md",
        "/etc/passwd",
        "C:\\Windows\\win.ini",
        ".git/config",
        ".env",
        ".opencode/opencode.json",
        "package.json",
        "README.txt",
        "references/INSPIRATION.md",
    ],
)
def test_unsafe_or_unapproved_paths_are_blocked(path):
    assert server._safe_read(path) is None


def test_hidden_files_and_directories_are_blocked(repo_root):
    hidden = repo_root / "design-system" / ".hidden.md"
    hidden.write_text("secret", encoding="utf-8")
    try:
        assert server._safe_read("design-system/.hidden.md") is None
    finally:
        hidden.unlink()


def test_symlinked_files_are_blocked(repo_root):
    link = repo_root / "design-system" / "linked.md"
    link.symlink_to(repo_root / "README.md")
    try:
        assert server._safe_read("design-system/linked.md") is None
    finally:
        link.unlink()


def test_symlinked_parent_directories_are_blocked(repo_root):
    parent = repo_root / "design-system" / "linked-dir"
    parent.symlink_to(repo_root / "brand", target_is_directory=True)
    try:
        assert server._safe_read("design-system/linked-dir/BRAND.md") is None
    finally:
        parent.unlink()


def test_search_returns_indexed_design_content():
    results = server.search("DESIGN_TOKENS", k=20)
    assert results
    assert all(
        {"doc", "heading", "line", "score", "text"} <= result.keys()
        for result in results
    )
    assert any("token" in result["text"].lower() for result in results)
