"""
PaglaDESIGN Token Parity & Architecture Regression Test Suite.

Enforces the Single Source of Truth (SSOT) contract across DESIGN_TOKENS.md,
compiled reference CSS (css/tokens.css, css/base.css, css/utilities.css),
and MCP authority indexing.
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def test_markdown_tokens_parse_without_dots_in_variable_names():
    """Verify all tokens in DESIGN_TOKENS.md normalize to valid CSS identifiers without unescaped dots."""
    token_file = REPO_ROOT / "design-system" / "DESIGN_TOKENS.md"
    assert token_file.exists(), f"{token_file} does not exist"

    content = token_file.read_text(encoding="utf-8")
    tokens = []
    for line in content.splitlines():
        match = re.search(r'\|\s*`?([a-zA-Z0-9_.-]+)`?\s*\|\s*`?([^|]+)`?\s*\|', line)
        if match:
            name, val = match.groups()
            name = name.strip()
            val = val.strip().strip("`")
            if set(name) == {"-"} or set(val) == {"-"} or name.lower() == "token":
                continue

            # Convert camelCase to kebab-case
            clean = re.sub(r'([a-z0-9])([A-Z])', r'\1-\2', name)
            clean = clean.strip().lower().replace(".", "-").replace("/", "-").replace(" ", "-")
            clean = re.sub(r'-+', '-', clean).strip("-")
            var_name = f"--{clean}"

            assert "." not in var_name, f"Unescaped dot found in generated CSS variable: {var_name}"
            tokens.append((var_name, val))

    assert len(tokens) >= 70, f"Expected at least 70 tokens in DESIGN_TOKENS.md, found {len(tokens)}"


def test_tokens_css_parity_with_design_tokens_md():
    """Verify that every variable in DESIGN_TOKENS.md exists in css/tokens.css."""
    token_file = REPO_ROOT / "design-system" / "DESIGN_TOKENS.md"
    tokens_css = REPO_ROOT / "css" / "tokens.css"

    assert tokens_css.exists(), "css/tokens.css missing"
    css_content = tokens_css.read_text(encoding="utf-8")

    # Extract all CSS custom properties defined in css/tokens.css
    css_vars = set()
    for line in css_content.splitlines():
        stripped = line.strip()
        if stripped.startswith("--"):
            var_name = stripped.split(":", 1)[0].strip()
            assert "." not in var_name, f"CSS variable identifier in css/tokens.css has unescaped dot: {var_name}"
            css_vars.add(var_name)

    # Extract all token keys from DESIGN_TOKENS.md
    md_content = token_file.read_text(encoding="utf-8")
    for line in md_content.splitlines():
        match = re.search(r'\|\s*`?([a-zA-Z0-9_.-]+)`?\s*\|\s*`?([^|]+)`?\s*\|', line)
        if match:
            name, _ = match.groups()
            name = name.strip()
            if set(name) == {"-"} or name.lower() == "token":
                continue
            clean = re.sub(r'([a-z0-9])([A-Z])', r'\1-\2', name)
            clean = clean.strip().lower().replace(".", "-").replace("/", "-").replace(" ", "-")
            clean = re.sub(r'-+', '-', clean).strip("-")
            var_name = f"--{clean}"
            assert var_name in css_vars, f"Token {name} ({var_name}) defined in DESIGN_TOKENS.md but missing in css/tokens.css"


def test_typography_line_height_and_tracking_ssot_sync():
    """Verify line-height and tracking tokens in DESIGN_TOKENS.md are in exact parity with css/tokens.css."""
    token_file = REPO_ROOT / "design-system" / "DESIGN_TOKENS.md"
    tokens_css = REPO_ROOT / "css" / "tokens.css"

    md_content = token_file.read_text(encoding="utf-8")
    css_content = tokens_css.read_text(encoding="utf-8")

    pairs = [
        ("font.lineHeight.body", "--font-line-height-body"),
        ("font.tracking.heading", "--font-tracking-heading"),
        ("font.tracking.display", "--font-tracking-display"),
    ]
    for md_key, css_var in pairs:
        md_match = re.search(rf'\|\s*`?{re.escape(md_key)}`?\s*\|\s*`?([^|]+)`?\s*\|', md_content)
        assert md_match, f"Token {md_key} missing in {token_file}"
        md_val = md_match.group(1).strip().strip("`")

        css_match = re.search(rf'{re.escape(css_var)}\s*:\s*([^;]+);', css_content)
        assert css_match, f"Variable {css_var} missing in {tokens_css}"
        css_val = css_match.group(1).strip()

        assert md_val == css_val, f"Parity mismatch for {md_key}: MD '{md_val}' != CSS '{css_val}'"



def test_font_face_family_name_conforms_to_d021():
    """Verify @font-face declarations in css/tokens.css declare 'Pagla Sans' per D-021."""
    tokens_css = REPO_ROOT / "css" / "tokens.css"
    content = tokens_css.read_text(encoding="utf-8")

    assert 'font-family: "PaglaAI Sans";' not in content, "Found stale font-family 'PaglaAI Sans' in tokens.css"
    assert 'font-family: "Pagla Sans";' in content, "Missing canonical font-family 'Pagla Sans' in tokens.css"


def test_link_hover_contrast_and_focus():
    """Verify a:hover has distinct contrast from a default in css/base.css."""
    base_css = REPO_ROOT / "css" / "base.css"
    content = base_css.read_text(encoding="utf-8")

    assert "a:hover {" in content
    assert "color: var(--color-accent-secondary);" in content, "a:hover must use distinct accent secondary token"
    assert "a:focus-visible {" in content


def test_no_dead_media_queries():
    """Verify no CSS file uses invalid var() inside @media feature queries."""
    css_dir = REPO_ROOT / "css"
    for css_file in css_dir.glob("*.css"):
        text = css_file.read_text(encoding="utf-8")
        match = re.search(r'@media[^{]*\bvar\(', text)
        assert match is None, f"Dead @media query with var(...) found in {css_file}"


def test_css_cascade_layers_defined():
    """Verify cascade layers are declared across stylesheets."""
    tokens_css = (REPO_ROOT / "css" / "tokens.css").read_text(encoding="utf-8")
    base_css = (REPO_ROOT / "css" / "base.css").read_text(encoding="utf-8")
    utilities_css = (REPO_ROOT / "css" / "utilities.css").read_text(encoding="utf-8")

    assert "@layer tokens, base, utilities;" in tokens_css
    assert "@layer tokens {" in tokens_css
    assert "@layer base {" in base_css
    assert "@layer utilities {" in utilities_css


def test_utilities_motion_safe_selector():
    """Verify .u-motion-safe is not restricted by :only-child pseudo-class."""
    utilities_css = (REPO_ROOT / "css" / "utilities.css").read_text(encoding="utf-8")
    assert ".u-motion-safe:only-child" not in utilities_css, ".u-motion-safe should not be restricted to :only-child"
    assert ".u-motion-safe {" in utilities_css


def test_duplicate_and_orphaned_files_purged():
    """Verify duplicate fonts and legacy agent manual directories are purged."""
    brand_fonts = REPO_ROOT / "brand" / "fonts"
    assert not brand_fonts.exists(), "brand/fonts/ should be removed in favor of canonical fonts/"

    legacy_manual = REPO_ROOT / ".ai" / "agent-manual"
    assert not legacy_manual.exists(), ".ai/agent-manual/ legacy directory should be removed"

    legacy_agents = REPO_ROOT / ".ai" / "AGENTS.md"
    assert not legacy_agents.exists(), ".ai/AGENTS.md duplicate should be removed; root AGENTS.md is canonical"


def test_mcp_dynamic_authority_discovery():
    """Verify MCP server discovery includes all canonical authority documents."""
    sys.path.insert(0, str(REPO_ROOT / ".ai" / "mcp"))
    import server

    authority = server.get_canonical_authority_files()
    assert "ecosystem.json" in authority
    assert "design-system/DESIGN_TOKENS.md" in authority
    assert "components/COMPONENT_LIBRARY.md" in authority
    assert "design-system/RENDERER_API.md" in authority
    assert len(authority) >= 40
