"""
Regression tests for the FERN renderer (bin/build_fern.py).

Covers the inline Markdown rules (emphasis must never touch file names, URLs or
code), link rewriting for the published site, and a full site build.
"""

import importlib.util
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

_spec = importlib.util.spec_from_file_location("build_fern", REPO_ROOT / "bin" / "build_fern.py")
build_fern = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(build_fern)

fmt = build_fern.format_inline
GITHUB = "https://github.com/paglaai/pagladesign"


def test_underscores_inside_words_are_not_italic():
    out = fmt("See DESIGN_TOKENS.md and test_tokens_parity for details.")
    assert "<em>" not in out
    assert "DESIGN_TOKENS.md" in out and "test_tokens_parity" in out


def test_real_emphasis_still_works():
    assert fmt("an _emphasised_ word") == "an <em>emphasised</em> word"
    assert fmt("this is *also* italic") == "this is <em>also</em> italic"
    assert fmt("**bold** text") == "<strong>bold</strong> text"
    assert fmt("__bold__ text") == "<strong>bold</strong> text"
    assert fmt("~~gone~~") == "<del>gone</del>"


def test_inline_code_is_left_alone():
    out = fmt("`css/**` and `a_b_c` and `**x**`")
    assert '<code class="doc-code">css/**</code>' in out
    assert '<code class="doc-code">a_b_c</code>' in out
    assert '<code class="doc-code">**x**</code>' in out
    assert "<strong>" not in out and "<em>" not in out


def test_no_stray_asterisks_around_code():
    line = "touching `css/**`, `design-system/**`, or `ecosystem.json`, GitHub Actions run:"
    out = fmt(line)
    assert "<strong>" not in out
    assert "**" not in re.sub(r"<code[^>]*>.*?</code>", "", out)


def test_unpaired_markers_stay_literal():
    assert "**" in fmt("5 ** 3 equals 125")


def test_bold_label_containing_a_link_and_code():
    out = fmt("**Rule of Token Locking ([`D-010`](#decisions)):**")
    assert out.startswith("<strong>") and out.endswith("</strong>")
    assert 'href="#decisions"' in out and "**" not in out


def test_link_addresses_are_not_mangled():
    out = fmt("[doc](https://example.com/DESIGN_DNA.md?x=foo_bar)")
    assert 'href="https://example.com/DESIGN_DNA.md?x=foo_bar"' in out
    assert "<em>" not in out


def test_document_links_point_to_real_site_pages():
    assert 'href="#tokens"' in fmt("[t](design-system/DESIGN_TOKENS.md)")
    assert 'href="#design-dna"' in fmt("[d](./DESIGN_DNA.md)")
    assert 'href="#index"' in fmt("[r](README.md)")
    assert 'href="#decisions"' in fmt("[x](../governance/DECISIONS.md)")
    assert 'href="#ecosystem"' in fmt("[e](ecosystem.json)")


def test_unpublished_files_link_to_github():
    assert f'href="{GITHUB}/blob/main/.github/workflows/ci.yml"' in fmt("[ci](./.github/workflows/ci.yml)")
    assert f'href="{GITHUB}/blob/main/tests/test_tokens_parity.py"' in fmt("[t](tests/test_tokens_parity.py)")
    assert f'href="{GITHUB}/tree/main/.ai/mcp"' in fmt("[m](./.ai/mcp)")
    assert f'href="{GITHUB}/blob/main/ecosystem.schema.json"' in fmt("[s](ecosystem.schema.json)")


def test_published_assets_keep_relative_links():
    assert 'href="./css/tokens.css"' in fmt("[c](./css/tokens.css)")
    assert 'href="./fonts/PaglaSans-VF.woff2"' in fmt("[f](fonts/PaglaSans-VF.woff2)")


def test_external_and_anchor_links_are_untouched():
    assert 'href="https://github.com/paglaai"' in fmt("[g](https://github.com/paglaai)")
    assert 'href="mailto:a@b.co"' in fmt("[m](mailto:a@b.co)")
    assert 'href="#overview"' in fmt("[o](#overview)")


def test_badge_images_keep_their_underscores():
    badge = (
        "[![Docs Portal](https://img.shields.io/badge/Docs_Portal-FERN_Style-6B7EFF"
        "?style=flat-square&logo=githubpages)](https://paglaai.github.io/pagladesign/)"
    )
    out = fmt(badge)
    assert "Docs_Portal-FERN_Style" in out
    assert "<em>" not in out
    assert 'href="https://paglaai.github.io/pagladesign/"' in out


def test_badge_url_with_parentheses_is_not_cut_short():
    out = fmt("![DesignDNA Locked](https://img.shields.io/badge/DesignDNA-Locked_(D--024)-0A0A0B?style=flat-square)")
    assert "Locked_(D--024)-0A0A0B?style=flat-square" in out
    assert out.endswith("</figure>")


def test_full_build_has_no_mangled_or_unpublished_links(tmp_path):
    build_fern.build_fern_site(tmp_path)
    pages = list(tmp_path.glob("*.html"))
    assert len(pages) >= 30
    hrefs = []
    for page in pages:
        hrefs += re.findall(r'href=\\?"([^"\\]*)\\?"', page.read_text(encoding="utf-8"))
    mangled = [h for h in hrefs if "em>" in h or "<" in h]
    assert not mangled, mangled[:5]
    unpublished = [h for h in hrefs if h.startswith(("./.ai", "./.github", "./tests", "../"))]
    assert not unpublished, unpublished[:5]


def test_raw_html_badge_links_work_on_the_site():
    out = fmt(
        '<a href="./.ai/mcp"><img src="https://img.shields.io/badge/MCP-FastMCP_v2.0-6B7EFF'
        '?style=flat-square" alt="FastMCP Ready"></a>'
    )
    assert f'href="{GITHUB}/tree/main/.ai/mcp"' in out
    assert "FastMCP_v2.0-6B7EFF?style=flat-square" in out
    assert fmt('<a href="./LICENSE">x</a>') == f'<a href="{GITHUB}/blob/main/LICENSE">x</a>'
    assert 'href="#design-dna"' in fmt('<a href="./design-system/DESIGN_DNA.md"><img src="a_b_c.png" alt="x"></a>')


def test_raw_html_attributes_are_never_italicised():
    tag = '<img src="https://x.io/a_b_.png" alt="_x_">'
    assert fmt(tag) == tag
