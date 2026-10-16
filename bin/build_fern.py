#!/usr/bin/env python3
"""
bin/build_fern.py — Canonical FERN-Style Static Documentation Generator

Generates the human-facing documentation website for PaglaDESIGN according to:
- design-system/FERN_RENDERER.md (Layout, typography, colors, component mapping)
- design-system/RENDERER_API.md (Audience frontmatter routing)
- css/tokens.css, css/base.css, css/utilities.css (Token-first styling)

Zero external pip dependencies (Python 3 standard library only).
Deterministic, byte-identical output across runs.
"""

import argparse
import html
import json
import os
import pathlib
import re
import shutil
import sys
from typing import Dict, List, Optional, Tuple

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent

DOC_SECTIONS = [
    {
        "id": "overview",
        "title": "Overview",
        "icon": "sparkles",
        "items": [
            {"id": "readme", "title": "Design Authority", "path": "README.md", "slug": "index"},
            {"id": "vision", "title": "Vision", "path": "VISION.md", "slug": "vision"},
            {"id": "design", "title": "Design Philosophy", "path": "DESIGN.md", "slug": "design"},
            {"id": "principles", "title": "Core Principles", "path": "PRINCIPLES.md", "slug": "principles"},
            {"id": "agents", "title": "Agent Operating Model", "path": "AGENTS.md", "slug": "agents"},
        ],
    },
    {
        "id": "brand",
        "title": "Brand",
        "icon": "palette",
        "items": [
            {"id": "brand", "title": "Brand Guidelines", "path": "brand/BRAND.md", "slug": "brand"},
            {"id": "brandkit", "title": "BrandKit", "path": "brand/BRANDKIT.md", "slug": "brandkit"},
        ],
    },
    {
        "id": "design-system",
        "title": "Design System",
        "icon": "ruler",
        "items": [
            {"id": "tokens", "title": "Design Tokens", "path": "design-system/DESIGN_TOKENS.md", "slug": "tokens", "interactive": "tokens"},
            {"id": "design-dna", "title": "Design DNA", "path": "design-system/DESIGN_DNA.md", "slug": "design-dna"},
            {"id": "typography", "title": "Typography", "path": "design-system/TYPOGRAPHY.md", "slug": "typography"},
            {"id": "pagla-sans", "title": "Pagla Sans Spec", "path": "design-system/PAGLA_SANS.md", "slug": "pagla-sans"},
            {"id": "color-system", "title": "Color System", "path": "design-system/COLOR_SYSTEM.md", "slug": "color-system"},
            {"id": "motion", "title": "Motion & Timing", "path": "design-system/MOTION.md", "slug": "motion"},
            {"id": "accessibility", "title": "Accessibility Gates", "path": "design-system/ACCESSIBILITY.md", "slug": "accessibility"},
            {"id": "css-architecture", "title": "CSS Architecture", "path": "design-system/CSS_ARCHITECTURE.md", "slug": "css-architecture"},
            {"id": "icons", "title": "Iconography", "path": "design-system/ICONS.md", "slug": "icons"},
            {"id": "ux-patterns", "title": "UX Patterns", "path": "design-system/UX_PATTERNS.md", "slug": "ux-patterns"},
            {"id": "pagla-ui", "title": "Pagla UI Architecture", "path": "design-system/PAGLA_UI.md", "slug": "pagla-ui"},
        ],
    },
    {
        "id": "components",
        "title": "Components",
        "icon": "box",
        "items": [
            {"id": "components-grammar", "title": "Component Grammar", "path": "components/COMPONENTS.md", "slug": "components-grammar"},
            {"id": "component-library", "title": "Component Registry", "path": "components/COMPONENT_LIBRARY.md", "slug": "component-library", "interactive": "components"},
        ],
    },
    {
        "id": "renderers",
        "title": "Audience Renderers",
        "icon": "cpu",
        "items": [
            {"id": "fern-renderer", "title": "FERN Renderer (Human)", "path": "design-system/FERN_RENDERER.md", "slug": "fern-renderer"},
            {"id": "machine-renderer", "title": "MACHINE Renderer (Agent)", "path": "design-system/MACHINE_RENDERER.md", "slug": "machine-renderer"},
            {"id": "architect-renderer", "title": "ARCHITECT Renderer (RFC)", "path": "design-system/ARCHITECT_RENDERER.md", "slug": "architect-renderer"},
            {"id": "renderer-api", "title": "Renderer API Contract", "path": "design-system/RENDERER_API.md", "slug": "renderer-api"},
            {"id": "audience-spec", "title": "Audience Spec", "path": "governance/AUDIENCE_RENDERER_SPEC.md", "slug": "audience-spec"},
        ],
    },
    {
        "id": "ecosystem",
        "title": "Ecosystem",
        "icon": "globe",
        "items": [
            {"id": "ecosystem-registry", "title": "Ecosystem Registry", "path": "ecosystem.json", "slug": "ecosystem", "interactive": "ecosystem"},
        ],
    },
    {
        "id": "governance",
        "title": "Governance",
        "icon": "shield",
        "items": [
            {"id": "decisions", "title": "Decisions (ADRs)", "path": "governance/DECISIONS.md", "slug": "decisions"},
            {"id": "roadmap", "title": "3-Phase Roadmap", "path": "governance/ROADMAP.md", "slug": "roadmap"},
            {"id": "changelog", "title": "Changelog", "path": "governance/CHANGELOG.md", "slug": "changelog"},
            {"id": "doc-style", "title": "Documentation Style", "path": "governance/DOCUMENTATION_STYLE.md", "slug": "doc-style"},
        ],
    },
]


def parse_frontmatter(content: str) -> Tuple[Dict[str, any], str]:
    """Parse YAML-like frontmatter if present."""
    frontmatter = {}
    body = content
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            raw_fm = parts[1]
            body = parts[2].lstrip("\n")
            for line in raw_fm.splitlines():
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if ":" in line:
                    key, val = line.split(":", 1)
                    key = key.strip()
                    val = val.strip().strip('"').strip("'")
                    if val.startswith("[") and val.endswith("]"):
                        items = [x.strip().strip('"').strip("'") for x in val[1:-1].split(",") if x.strip()]
                        frontmatter[key] = items
                    else:
                        frontmatter[key] = val
    return frontmatter, body


def slugify(text: str) -> str:
    """Generate a valid HTML id slug."""
    text = re.sub(r"[^\w\s-]", "", text.lower()).strip()
    return re.sub(r"[-\s]+", "-", text)


def render_markdown_to_html(raw_markdown: str) -> Tuple[str, List[Dict[str, str]]]:
    """Convert Markdown to semantic FERN-compliant HTML with headings and TOC."""
    toc = []
    lines = raw_markdown.splitlines()
    html_out = []
    in_code_block = False
    code_lang = ""
    code_lines = []
    in_table = False
    table_rows = []
    in_list = False
    list_type = ""

    def close_table():
        nonlocal in_table, table_rows
        if not in_table:
            return ""
        in_table = False
        if not table_rows:
            return ""
        out = ['<div class="doc-table-wrapper"><table class="doc-table">']
        # header
        out.append("<thead><tr>")
        for cell in table_rows[0]:
            out.append(f"<th>{cell}</th>")
        out.append("</tr></thead>")
        # body
        out.append("<tbody>")
        for row in table_rows[1:]:
            out.append("<tr>")
            for cell in row:
                out.append(f"<td>{cell}</td>")
            out.append("</tr>")
        out.append("</tbody></table></div>")
        table_rows = []
        return "".join(out)

    def close_list():
        nonlocal in_list, list_type
        if not in_list:
            return ""
        tag = "ol" if list_type == "ol" else "ul"
        in_list = False
        list_type = ""
        return f"</{tag}>"

    def format_inline(text: str) -> str:
        # Images: ![alt](src)
        text = re.sub(
            r'!\[([^\]]*)\]\(([^)]+)\)',
            r'<figure class="doc-figure"><img src="\2" alt="\1" class="doc-img" loading="lazy"><figcaption class="doc-caption">\1</figcaption></figure>',
            text,
        )
        # Inline code: `code`
        text = re.sub(r'`([^`]+)`', r'<code class="doc-code">\1</code>', text)
        # Strong: **text** or __text__
        text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
        text = re.sub(r'__([^_]+)__', r'<strong>\1</strong>', text)
        # Em: *text* or _text_
        text = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', text)
        text = re.sub(r'_([^_]+)_', r'<em>\1</em>', text)
        # Strikethrough: ~~text~~
        text = re.sub(r'~~([^~]+)~~', r'<del>\1</del>', text)
        # Links: [text](url)
        def replace_link(m):
            txt, url = m.group(1), m.group(2)
            # Rewrite relative internal markdown links to hash or page
            if url.endswith(".md"):
                url = url[:-3]
                if "/" in url:
                    url = url.split("/")[-1]
                url = f"#{url.lower()}"
            elif url.startswith("./") and url.endswith(".md"):
                url = f"#{url[2:-3].lower()}"
            return f'<a href="{url}" class="doc-link">{txt}</a>'

        text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace_link, text)
        return text

    i = 0
    while i < len(lines):
        line = lines[i]

        # Code block fence
        if line.startswith("```"):
            if in_code_block:
                in_code_block = False
                escaped = html.escape("\n".join(code_lines))
                lang_label = f'<span class="doc-code-lang">{code_lang}</span>' if code_lang else ""
                html_out.append(
                    f'<div class="doc-code-block" data-lang="{code_lang}">'
                    f'<div class="doc-code-header">{lang_label}'
                    f'<button class="doc-code-copy" title="Copy code" onclick="copyCode(this)" aria-label="Copy to clipboard">'
                    f'<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>'
                    f'<span>Copy</span></button></div>'
                    f'<pre><code class="doc-code">{escaped}</code></pre></div>'
                )
                code_lines = []
                code_lang = ""
            else:
                html_out.append(close_table())
                html_out.append(close_list())
                in_code_block = True
                code_lang = line.strip("`").strip()
            i += 1
            continue

        if in_code_block:
            code_lines.append(line)
            i += 1
            continue

        # Blank line
        if not line.strip():
            html_out.append(close_table())
            html_out.append(close_list())
            i += 1
            continue

        # Horizontal rule
        if re.match(r"^(\*{3,}|-{3,}|_{3,})$", line.strip()):
            html_out.append(close_table())
            html_out.append(close_list())
            html_out.append('<hr class="doc-hr">')
            i += 1
            continue

        # Headings
        heading_match = re.match(r"^(#{1,4})\s+(.+)$", line)
        if heading_match:
            html_out.append(close_table())
            html_out.append(close_list())
            level = len(heading_match.group(1))
            heading_text = heading_match.group(2).strip()
            slug = slugify(re.sub(r"<[^>]+>", "", heading_text))
            if level in (2, 3):
                toc.append({"level": level, "title": heading_text, "slug": slug})
            formatted_title = format_inline(heading_text)
            anchor = f'<a href="#{slug}" class="doc-heading-anchor" aria-hidden="true">#</a>'
            html_out.append(f'<h{level} id="{slug}" class="doc-h{level}">{formatted_title} {anchor}</h{level}>')
            i += 1
            continue

        # Blockquote / Alert Callouts
        if line.startswith(">"):
            html_out.append(close_table())
            html_out.append(close_list())
            quote_lines = []
            while i < len(lines) and lines[i].startswith(">"):
                quote_lines.append(lines[i].lstrip(">").strip())
                i += 1
            quote_text = " ".join(quote_lines)

            # GitHub style alerts
            alert_match = re.match(r"^\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*(.*)", quote_text)
            if alert_match:
                alert_type = alert_match.group(1).lower()
                alert_body = format_inline(alert_match.group(2).strip())
                html_out.append(
                    f'<div class="doc-callout doc-callout-{alert_type}" role="alert">'
                    f'<div class="doc-callout-header"><strong class="doc-callout-title">{alert_type.upper()}</strong></div>'
                    f'<div class="doc-callout-body">{alert_body}</div></div>'
                )
            else:
                html_out.append(f'<blockquote class="doc-blockquote"><p>{format_inline(quote_text)}</p></blockquote>')
            continue

        # Tables: | col | col |
        if "|" in line and (line.strip().startswith("|") or line.strip().endswith("|")):
            parts = [format_inline(p.strip()) for p in line.strip().strip("|").split("|")]
            # Check if this is divider row
            if all(re.match(r"^:?-+:?$", p.strip()) for p in parts):
                pass  # divider row
            else:
                if not in_table:
                    in_table = True
                    table_rows = [parts]
                else:
                    table_rows.append(parts)
            i += 1
            continue
        elif in_table:
            html_out.append(close_table())

        # Unordered list: - item or * item
        ul_match = re.match(r"^[-*]\s+(.+)$", line)
        if ul_match:
            html_out.append(close_table())
            if not in_list or list_type != "ul":
                html_out.append(close_list())
                html_out.append('<ul class="doc-list">')
                in_list = True
                list_type = "ul"
            html_out.append(f"<li>{format_inline(ul_match.group(1))}</li>")
            i += 1
            continue

        # Ordered list: 1. item
        ol_match = re.match(r"^\d+\.\s+(.+)$", line)
        if ol_match:
            html_out.append(close_table())
            if not in_list or list_type != "ol":
                html_out.append(close_list())
                html_out.append('<ol class="doc-list-ordered">')
                in_list = True
                list_type = "ol"
            html_out.append(f"<li>{format_inline(ol_match.group(1))}</li>")
            i += 1
            continue

        # Standard paragraph
        html_out.append(close_table())
        html_out.append(close_list())
        html_out.append(f'<p class="doc-body">{format_inline(line)}</p>')
        i += 1

    html_out.append(close_table())
    html_out.append(close_list())
    return "\n".join(html_out), toc


def generate_interactive_tokens_html() -> str:
    """Generate visual interactive explorer for tokens."""
    tokens_path = REPO_ROOT / "css" / "tokens.css"
    color_swatches = [
        {"name": "--color-base-paper", "desc": "Page background canvas", "light": "#FFFFFF", "dark": "#0A0A0B"},
        {"name": "--color-base-ink", "desc": "Primary text ink", "light": "#0A0A0B", "dark": "#F5F5F7"},
        {"name": "--color-base-surface", "desc": "Card & sidebar surface", "light": "#F5F5F7", "dark": "#141416"},
        {"name": "--color-base-border", "desc": "Borders & dividing rules", "light": "#E5E5EA", "dark": "#242428"},
        {"name": "--color-base-muted", "desc": "Muted descriptive copy", "light": "#6E6E73", "dark": "#8E8E93"},
        {"name": "--color-accent-primary", "desc": "Meaning & focus accent", "light": "#6B7EFF", "dark": "#6B7EFF"},
        {"name": "--color-accent-secondary", "desc": "High-contrast hover accent", "light": "#a8b5ff", "dark": "#a8b5ff"},
        {"name": "--color-accent-error", "desc": "Destructive & error state", "light": "#FF453A", "dark": "#FF453A"},
        {"name": "--color-accent-success", "desc": "Affirmative & success state", "light": "#30D158", "dark": "#30D158"},
    ]

    type_scale = [
        {"token": "--font-size-display", "val": "3.5rem", "tag": "Display Heading", "wt": "700"},
        {"token": "--font-size-h1", "val": "2.25rem", "tag": "Heading 1", "wt": "600"},
        {"token": "--font-size-h2", "val": "1.75rem", "tag": "Heading 2", "wt": "600"},
        {"token": "--font-size-h3", "val": "1.375rem", "tag": "Heading 3", "wt": "500"},
        {"token": "--font-size-h4", "val": "1.125rem", "tag": "Heading 4", "wt": "500"},
        {"token": "--font-size-body-large", "val": "1.125rem", "tag": "Body Large", "wt": "400"},
        {"token": "--font-size-body", "val": "1rem", "tag": "Body Text", "wt": "400"},
        {"token": "--font-size-small", "val": "0.875rem", "tag": "Small Text", "wt": "400"},
        {"token": "--font-size-caption", "val": "0.75rem", "tag": "Caption", "wt": "400"},
        {"token": "--font-size-code", "val": "0.875rem", "tag": "Monospace Code", "wt": "400"},
    ]

    spacing_scale = [
        ("0.5", "0.125rem"),
        ("1", "0.25rem"),
        ("1.5", "0.375rem"),
        ("2", "0.5rem"),
        ("3", "0.75rem"),
        ("4", "1rem"),
        ("6", "1.5rem"),
        ("8", "2rem"),
        ("12", "3rem"),
        ("16", "4rem"),
        ("24", "6rem"),
    ]

    out = ['<div class="interactive-tokens-explorer">']
    out.append('<h2 id="interactive-color-palette" class="doc-h2">Visual Color System (Semantic Tokens)</h2>')
    out.append('<div class="color-swatch-grid">')
    for sw in color_swatches:
        out.append(
            f'<div class="color-swatch-card" onclick="copyTokenText(\'{sw["name"]}\')">'
            f'<div class="color-swatch-preview" style="background-color: var({sw["name"]});"></div>'
            f'<div class="color-swatch-info">'
            f'<span class="color-swatch-name">{sw["name"]}</span>'
            f'<span class="color-swatch-desc">{sw["desc"]}</span>'
            f'<div class="color-swatch-values">'
            f'<span>Light: <code>{sw["light"]}</code></span>'
            f'<span>Dark: <code>{sw["dark"]}</code></span>'
            f'</div></div></div>'
        )
    out.append('</div>')

    out.append('<h2 id="interactive-typography-scale" class="doc-h2">Typography Scale (Pagla Sans)</h2>')
    out.append('<div class="type-scale-table">')
    for ts in type_scale:
        out.append(
            f'<div class="type-scale-row">'
            f'<div class="type-scale-meta"><code>{ts["token"]}</code><small>{ts["val"]} · weight {ts["wt"]}</small></div>'
            f'<div class="type-scale-sample" style="font-size: var({ts["token"]}); font-weight: {ts["wt"]};">The quick brown fox jumps over the lazy dog.</div>'
            f'</div>'
        )
    out.append('</div>')

    out.append('<h2 id="interactive-spacing-ladder" class="doc-h2">Spacing Ladder (Base 0.25rem / 4px)</h2>')
    out.append('<div class="spacing-ladder">')
    for name, val in spacing_scale:
        clean_name = f"--space-{name.replace('.', '-')}"
        out.append(
            f'<div class="spacing-row">'
            f'<span class="spacing-label"><code>{clean_name}</code> ({val})</span>'
            f'<div class="spacing-bar-container"><div class="spacing-bar" style="width: var({clean_name});"></div></div>'
            f'</div>'
        )
    out.append('</div></div>')
    return "\n".join(out)


def generate_interactive_components_html() -> str:
    """Generate live rendered interactive components showcase."""
    return """
<div class="interactive-components-showcase">
  <h2 id="live-component-preview" class="doc-h2">Interactive Component Library Showcase</h2>
  <p class="doc-body">Living implementations of the 14 registered canonical components, adhering to <code>css/tokens.css</code> and <code>COMPONENT_LIBRARY.md</code>.</p>

  <div class="component-demo-section">
    <h3 class="doc-h3">1. Buttons</h3>
    <div class="component-demo-canvas">
      <button class="pagla-btn pagla-btn-primary">Primary Action</button>
      <button class="pagla-btn pagla-btn-secondary">Secondary Action</button>
      <button class="pagla-btn pagla-btn-ghost">Ghost Action</button>
      <button class="pagla-btn pagla-btn-danger">Danger Action</button>
    </div>
  </div>

  <div class="component-demo-section">
    <h3 class="doc-h3">2. Inputs & Search</h3>
    <div class="component-demo-canvas" style="display: flex; gap: var(--space-4); flex-wrap: wrap;">
      <input type="text" class="pagla-input" placeholder="Standard text input..." style="max-width: 300px;">
      <div style="position: relative; max-width: 300px; width: 100%;">
        <input type="text" class="pagla-input" placeholder="Search tokens or docs..." style="padding-left: 2.25rem;">
        <span style="position: absolute; left: 0.75rem; top: 50%; transform: translateY(-50%); color: var(--color-base-muted);">🔍</span>
      </div>
    </div>
  </div>

  <div class="component-demo-section">
    <h3 class="doc-h3">3. Chips & Badges</h3>
    <div class="component-demo-canvas" style="display: flex; gap: var(--space-2); flex-wrap: wrap;">
      <span class="pagla-chip pagla-chip-active">Status: Active</span>
      <span class="pagla-chip pagla-chip-planned">Status: Planned</span>
      <span class="pagla-chip pagla-chip-accent">Role: Authority</span>
      <span class="pagla-chip pagla-chip-outline">Audience: Human</span>
      <span class="pagla-chip pagla-chip-outline">Audience: Machine</span>
    </div>
  </div>

  <div class="component-demo-section">
    <h3 class="doc-h3">4. Cards & Containers</h3>
    <div class="component-demo-canvas" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: var(--space-4);">
      <div class="pagla-card">
        <h4 style="margin: 0 0 var(--space-2) 0; font-size: var(--font-size-h4);">Flat Surface Card</h4>
        <p style="margin: 0; font-size: var(--font-size-small); color: var(--color-base-muted);">Standard card component utilizing <code>--color-base-surface</code> and <code>--color-base-border</code>.</p>
      </div>
      <div class="pagla-card pagla-card-interactive">
        <h4 style="margin: 0 0 var(--space-2) 0; font-size: var(--font-size-h4);">Interactive Card</h4>
        <p style="margin: 0; font-size: var(--font-size-small); color: var(--color-base-muted);">Elevates and transitions focus accent upon mouse hover.</p>
      </div>
    </div>
  </div>

  <div class="component-demo-section">
    <h3 class="doc-h3">5. Terminal Output</h3>
    <div class="component-demo-canvas">
      <div class="doc-terminal">
        <div class="doc-terminal-header">
          <span class="doc-terminal-dot"></span>
          <span class="doc-terminal-dot"></span>
          <span class="doc-terminal-dot"></span>
          <span class="doc-terminal-title">paglashell — v2.1.0</span>
        </div>
        <div class="doc-terminal-body">
          <div class="doc-terminal-line"><span class="doc-terminal-prompt">➜</span> <span class="doc-terminal-cmd">pagla token get font.size.bodyLarge</span></div>
          <div class="doc-terminal-out">--font-size-body-large: 1.125rem (18px)</div>
          <div class="doc-terminal-line"><span class="doc-terminal-prompt">➜</span> <span class="doc-terminal-cmd">pagla ecosystem validate</span></div>
          <div class="doc-terminal-out doc-terminal-success">✓ 16/16 entries validated against ecosystem.schema.json (Authority: PaglaDESIGN)</div>
        </div>
      </div>
    </div>
  </div>
</div>
"""


def generate_interactive_ecosystem_html() -> str:
    """Generate interactive ecosystem registry explorer."""
    eco_file = REPO_ROOT / "ecosystem.json"
    if not eco_file.exists():
        return "<p>ecosystem.json not found</p>"

    eco = json.loads(eco_file.read_text(encoding="utf-8"))
    entries = eco.get("ecosystem", [])

    out = ['<div class="interactive-ecosystem-explorer">']
    out.append('<h2 id="ecosystem-directory" class="doc-h2">PaglaAI Ecosystem Registry Explorer</h2>')
    out.append(
        f'<p class="doc-body">Single Source of Truth (SSOT) registry version <code>{eco.get("version")}</code>. '
        f'Authority: <strong>{eco.get("authority", {}).get("displayName", "PaglaDESIGN")}</strong>.</p>'
    )

    out.append("""
    <div class="ecosystem-filter-bar">
      <button class="eco-filter-btn active" onclick="filterEcosystem('all', this)">All (16)</button>
      <button class="eco-filter-btn" onclick="filterEcosystem('active', this)">Active (9)</button>
      <button class="eco-filter-btn" onclick="filterEcosystem('planned', this)">Planned (7)</button>
      <button class="eco-filter-btn" onclick="filterEcosystem('role-authority', this)">Authorities</button>
      <button class="eco-filter-btn" onclick="filterEcosystem('role-surface', this)">Surfaces</button>
      <button class="eco-filter-btn" onclick="filterEcosystem('role-product', this)">Products</button>
      <button class="eco-filter-btn" onclick="filterEcosystem('role-runtime', this)">Runtimes</button>
    </div>
    """)

    out.append('<div class="ecosystem-grid">')
    for item in entries:
        status = item.get("status", "planned")
        role = item.get("role", "product")
        audience = " · ".join(item.get("audience", []))
        repo = item.get("repo") or "Unpublished"
        url = item.get("url") or item.get("homepage") or ""
        provides = ", ".join(item.get("provides", [])[:3])
        deploy_info = ""
        if item.get("deploy"):
            provider = item["deploy"].get("provider", "Cloudflare")
            deploy_info = f'<span class="eco-card-deploy">🚀 {provider}</span>'

        out.append(
            f'<div class="eco-card" data-status="{status}" data-role="role-{role}">'
            f'<div class="eco-card-header">'
            f'<h3 class="eco-card-title">{item.get("displayName", item.get("id"))}</h3>'
            f'<span class="pagla-chip pagla-chip-{status}">{status}</span>'
            f'</div>'
            f'<div class="eco-card-category">{item.get("category", "")} · role: <strong>{role}</strong></div>'
            f'<p class="eco-card-desc">{item.get("notes") or item.get("description", "Ecosystem package bound by PaglaDESIGN.")}</p>'
            f'<div class="eco-card-meta">'
            f'<div><strong>Audience:</strong> {audience}</div>'
            f'<div><strong>Provides:</strong> {provides}</div>'
            f'</div>'
            f'<div class="eco-card-footer">'
            f'<code>{repo}</code>'
            f'{deploy_info}'
            f'</div>'
            f'</div>'
        )
    out.append('</div></div>')
    return "\n".join(out)


def build_fern_site(out_dir: pathlib.Path):
    """Build complete FERN static documentation site into out_dir."""
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "css").mkdir(exist_ok=True)
    (out_dir / "fonts").mkdir(exist_ok=True)
    (out_dir / "brand").mkdir(exist_ok=True)

    # 1. Copy reference CSS
    for css_file in ["tokens.css", "base.css", "utilities.css"]:
        src = REPO_ROOT / "css" / css_file
        if src.exists():
            shutil.copy2(src, out_dir / "css" / css_file)

    # 2. Copy fonts
    fonts_dir = REPO_ROOT / "fonts"
    if fonts_dir.exists():
        for f in fonts_dir.glob("*"):
            if f.is_file():
                shutil.copy2(f, out_dir / "fonts" / f.name)

    # 3. Copy brand assets
    brand_dir = REPO_ROOT / "brand"
    if brand_dir.exists():
        for b in brand_dir.glob("*.png"):
            shutil.copy2(b, out_dir / "brand" / b.name)

    # 4. Generate custom FERN layout CSS
    fern_css = generate_fern_css()
    (out_dir / "css" / "fern.css").write_text(fern_css, encoding="utf-8")

    # 5. Process all documentation pages
    all_pages = {}
    search_index = []

    for section in DOC_SECTIONS:
        for item in section["items"]:
            path = REPO_ROOT / item["path"]
            if not path.exists():
                continue
            raw_text = path.read_text(encoding="utf-8", errors="ignore")
            frontmatter, body = parse_frontmatter(raw_text)
            html_content, toc = render_markdown_to_html(body)

            # Append interactive widgets where relevant
            if item.get("interactive") == "tokens":
                html_content += generate_interactive_tokens_html()
            elif item.get("interactive") == "components":
                html_content += generate_interactive_components_html()
            elif item.get("interactive") == "ecosystem":
                html_content += generate_interactive_ecosystem_html()

            page_data = {
                "id": item["id"],
                "slug": item["slug"],
                "section": section["title"],
                "title": item["title"],
                "path": item["path"],
                "frontmatter": frontmatter,
                "html": html_content,
                "toc": toc,
            }
            all_pages[item["slug"]] = page_data
            search_index.append({
                "slug": item["slug"],
                "title": item["title"],
                "section": section["title"],
                "path": item["path"],
            })

    # 6. Generate HTML files
    # Create single-page application index with all pages bundled for instantaneous, zero-latency switching
    full_html = generate_complete_html(all_pages, search_index)
    (out_dir / "index.html").write_text(full_html, encoding="utf-8")

    # Also create fallback standalone pages so direct URLs work on GitHub Pages without server-side routing
    for slug, page in all_pages.items():
        if slug == "index":
            continue
        page_html = generate_complete_html(all_pages, search_index, active_slug=slug)
        (out_dir / f"{slug}.html").write_text(page_html, encoding="utf-8")

    # 7. Add .nojekyll to prevent GitHub Pages Jekyll processing
    (out_dir / ".nojekyll").write_text("", encoding="utf-8")
    print(f"✓ FERN documentation site successfully built into {out_dir}")
    print(f"✓ Rendered {len(all_pages)} canonical documentation pages")


def generate_fern_css() -> str:
    """CSS styling matching design-system/FERN_RENDERER.md using css/tokens.css variables."""
    return """
/* ==========================================================================
   PaglaDESIGN — FERN Human Renderer Stylesheet
   Strict adherence to css/tokens.css custom properties
   ========================================================================== */

:root {
  --sidebar-width: 18.5rem;
  --toc-width: 16rem;
  --header-height: 4.25rem;
}

body {
  margin: 0;
  padding: 0;
  background-color: var(--color-base-paper);
  color: var(--color-base-ink);
  font-family: var(--font-family-sans, "Pagla Sans", -apple-system, BlinkMacSystemFont, sans-serif);
  line-height: var(--font-line-height-body, 1.625);
  font-size: var(--font-size-body, 1rem);
  -webkit-font-smoothing: antialiased;
}

/* Layout Shell */
.app-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

/* Header */
.app-header {
  position: sticky;
  top: 0;
  z-index: 100;
  height: var(--header-height);
  background-color: var(--color-base-paper);
  border-bottom: 1px solid var(--color-base-border);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 var(--space-6);
  backdrop-filter: blur(8px);
}

.header-left {
  display: flex;
  align-items: center;
  gap: var(--space-4);
}

.brand-link {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  text-decoration: none;
  color: var(--color-base-ink);
}

.brand-logo {
  height: 2.25rem;
  width: auto;
  display: block;
}

.badge-version {
  font-size: var(--font-size-caption);
  padding: 0.15rem 0.5rem;
  border-radius: var(--radius-sm, 0.25rem);
  background-color: var(--color-base-surface);
  border: 1px solid var(--color-base-border);
  color: var(--color-accent-primary);
  font-weight: 600;
}

.header-center {
  flex: 1;
  max-width: 32rem;
  margin: 0 var(--space-6);
}

.search-trigger {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--space-2) var(--space-4);
  background-color: var(--color-base-surface);
  border: 1px solid var(--color-base-border);
  border-radius: var(--radius-md, 0.375rem);
  color: var(--color-base-muted);
  font-size: var(--font-size-small);
  cursor: pointer;
  transition: border-color var(--motion-duration-fast, 150ms) ease;
}

.search-trigger:hover {
  border-color: var(--color-accent-primary);
}

.header-right {
  display: flex;
  align-items: center;
  gap: var(--space-3);
}

.icon-btn {
  background: transparent;
  border: 1px solid var(--color-base-border);
  border-radius: var(--radius-md, 0.375rem);
  color: var(--color-base-ink);
  padding: var(--space-2) var(--space-3);
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: var(--space-2);
  font-size: var(--font-size-small);
  transition: all var(--motion-duration-fast, 150ms) ease;
}

.icon-btn:hover {
  background-color: var(--color-base-surface);
  border-color: var(--color-accent-primary);
}

.menu-toggle {
  display: none;
}

/* Main Layout Grid */
.layout-body {
  display: flex;
  flex: 1;
  max-width: 100%;
  margin: 0 auto;
  width: 100%;
}

/* Sidebar Navigation */
.app-sidebar {
  width: var(--sidebar-width);
  border-right: 1px solid var(--color-base-border);
  height: calc(100vh - var(--header-height));
  position: sticky;
  top: var(--header-height);
  overflow-y: auto;
  padding: var(--space-6) var(--space-4);
  box-sizing: border-box;
  background-color: var(--color-base-paper);
}

.nav-section {
  margin-bottom: var(--space-6);
}

.nav-section-title {
  font-size: var(--font-size-caption);
  text-transform: uppercase;
  letter-spacing: var(--font-tracking-wide, 0.05em);
  color: var(--color-base-muted);
  font-weight: 600;
  margin-bottom: var(--space-2);
  padding: 0 var(--space-3);
}

.nav-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.nav-item {
  margin-bottom: 2px;
}

.nav-link {
  display: block;
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius-md, 0.375rem);
  color: var(--color-base-muted);
  text-decoration: none;
  font-size: var(--font-size-small);
  transition: all var(--motion-duration-fast, 150ms) ease;
}

.nav-link:hover {
  color: var(--color-base-ink);
  background-color: var(--color-base-surface);
}

.nav-link.active {
  color: var(--color-accent-primary);
  background-color: var(--color-base-surface);
  font-weight: 500;
}

/* Content Area */
.app-content {
  flex: 1;
  min-width: 0;
  padding: var(--space-8) var(--space-8);
  display: flex;
  justify-content: center;
}

.content-inner {
  max-width: var(--layout-max-width, 75rem);
  width: 100%;
  display: flex;
  gap: var(--space-12);
}

.doc-article {
  flex: 1;
  min-width: 0;
  max-width: var(--font-max-width-body, 65ch);
}

/* Table of Contents */
.app-toc {
  width: var(--toc-width);
  position: sticky;
  top: calc(var(--header-height) + var(--space-8));
  height: fit-content;
  max-height: calc(100vh - var(--header-height) - var(--space-12));
  overflow-y: auto;
  border-left: 1px solid var(--color-base-border);
  padding-left: var(--space-4);
  font-size: var(--font-size-small);
}

.toc-title {
  font-size: var(--font-size-caption);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--color-base-muted);
  font-weight: 600;
  margin-bottom: var(--space-3);
}

.toc-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.toc-link {
  display: block;
  padding: var(--space-1) 0;
  color: var(--color-base-muted);
  text-decoration: none;
  transition: color var(--motion-duration-fast, 150ms) ease;
}

.toc-link:hover {
  color: var(--color-accent-primary);
}

.toc-item-h3 {
  padding-left: var(--space-3);
}

/* Typography elements per FERN_RENDERER.md */
.doc-breadcrumbs {
  margin-bottom: var(--space-4);
  font-size: var(--font-size-small);
  color: var(--color-base-muted);
}

.doc-breadcrumbs a {
  color: var(--color-base-muted);
  text-decoration: none;
}

.doc-breadcrumbs a:hover {
  color: var(--color-accent-primary);
}

.doc-h1 {
  font-size: var(--font-size-h1, 2.25rem);
  font-weight: 600;
  line-height: var(--font-line-height-heading, 1.25);
  margin: 0 0 var(--space-4) 0;
  letter-spacing: var(--font-tracking-heading, -0.03em);
}

.doc-h2 {
  font-size: var(--font-size-h2, 1.75rem);
  font-weight: 600;
  line-height: var(--font-line-height-heading, 1.25);
  margin: var(--space-8) 0 var(--space-3) 0;
  padding-bottom: var(--space-2);
  border-bottom: 1px solid var(--color-base-border);
}

.doc-h3 {
  font-size: var(--font-size-h3, 1.375rem);
  font-weight: 500;
  margin: var(--space-6) 0 var(--space-2) 0;
}

.doc-h4 {
  font-size: var(--font-size-h4, 1.125rem);
  font-weight: 500;
  margin: var(--space-4) 0 var(--space-2) 0;
}

.doc-body {
  font-size: var(--font-size-body, 1rem);
  line-height: var(--font-line-height-body, 1.625);
  margin: 0 0 var(--space-4) 0;
}

.doc-heading-anchor {
  color: var(--color-base-border);
  text-decoration: none;
  font-weight: normal;
  margin-left: var(--space-2);
  opacity: 0;
  transition: opacity var(--motion-duration-fast, 150ms) ease;
}

.doc-h1:hover .doc-heading-anchor,
.doc-h2:hover .doc-heading-anchor,
.doc-h3:hover .doc-heading-anchor {
  opacity: 1;
}

.doc-hr {
  border: 0;
  border-top: 1px solid var(--color-base-border);
  margin: var(--space-8) 0;
}

.doc-link {
  color: var(--color-accent-primary);
  text-decoration: underline;
  text-underline-offset: 0.2em;
  transition: color var(--motion-duration-fast, 150ms) ease;
}

.doc-link:hover {
  color: var(--color-accent-secondary);
}

/* Code block & Terminal */
.doc-code {
  font-family: var(--font-family-mono, ui-monospace, SFMono-Regular, Menlo, monospace);
  font-size: var(--font-size-code, 0.875rem);
  background-color: var(--color-base-surface);
  padding: 0.15rem 0.35rem;
  border-radius: var(--radius-sm, 0.25rem);
  border: 1px solid var(--color-base-border);
}

.doc-code-block {
  margin: var(--space-4) 0;
  background-color: var(--color-base-surface);
  border: 1px solid var(--color-base-border);
  border-radius: var(--radius-md, 0.375rem);
  overflow: hidden;
}

.doc-code-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--space-2) var(--space-4);
  background-color: var(--color-base-paper);
  border-bottom: 1px solid var(--color-base-border);
  font-size: var(--font-size-caption);
  color: var(--color-base-muted);
}

.doc-code-block pre {
  margin: 0;
  padding: var(--space-4);
  overflow-x: auto;
}

.doc-code-block code {
  background: none;
  padding: 0;
  border: none;
  font-size: var(--font-size-code);
  line-height: 1.5;
}

.doc-code-copy {
  background: none;
  border: none;
  color: var(--color-base-muted);
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: var(--space-1);
  font-size: var(--font-size-caption);
}

.doc-code-copy:hover {
  color: var(--color-accent-primary);
}

/* Callout */
.doc-callout {
  padding: var(--space-4);
  border-radius: var(--radius-md, 0.375rem);
  border-left: 4px solid var(--color-accent-primary);
  background-color: var(--color-base-surface);
  margin: var(--space-6) 0;
}

.doc-callout-warning {
  border-left-color: #FF9F0A;
}

.doc-callout-caution {
  border-left-color: var(--color-accent-error);
}

.doc-callout-header {
  margin-bottom: var(--space-2);
}

.doc-callout-title {
  font-size: var(--font-size-small);
  color: var(--color-base-ink);
}

/* Tables */
.doc-table-wrapper {
  overflow-x: auto;
  margin: var(--space-6) 0;
}

.doc-table {
  width: 100%;
  border-collapse: collapse;
  font-size: var(--font-size-small);
}

.doc-table th,
.doc-table td {
  padding: var(--space-3) var(--space-4);
  text-align: left;
  border-bottom: 1px solid var(--color-base-border);
}

.doc-table th {
  background-color: var(--color-base-surface);
  font-weight: 600;
  color: var(--color-base-ink);
}

/* Terminal Component */
.doc-terminal {
  background-color: #0A0A0B;
  color: #F5F5F7;
  border-radius: var(--radius-md, 0.375rem);
  overflow: hidden;
  font-family: var(--font-family-mono, monospace);
  font-size: var(--font-size-code);
  margin: var(--space-6) 0;
  border: 1px solid var(--color-base-border);
}

.doc-terminal-header {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-2) var(--space-4);
  background-color: #141416;
  border-bottom: 1px solid #242428;
}

.doc-terminal-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background-color: #38383a;
}

.doc-terminal-title {
  font-size: var(--font-size-caption);
  color: #8E8E93;
  margin-left: var(--space-2);
}

.doc-terminal-body {
  padding: var(--space-4);
}

.doc-terminal-line {
  display: flex;
  gap: var(--space-2);
  margin-bottom: var(--space-1);
}

.doc-terminal-prompt {
  color: var(--color-accent-primary);
}

.doc-terminal-cmd {
  color: #FFFFFF;
}

.doc-terminal-out {
  color: #8E8E93;
  margin-bottom: var(--space-3);
  padding-left: var(--space-4);
}

.doc-terminal-success {
  color: #30D158;
}

/* Interactive Showcase Components */
.pagla-btn {
  padding: var(--space-2) var(--space-4);
  border-radius: var(--radius-md, 0.375rem);
  font-size: var(--font-size-small);
  font-weight: 500;
  cursor: pointer;
  border: 1px solid transparent;
  transition: all var(--motion-duration-fast, 150ms) ease;
}

.pagla-btn-primary {
  background-color: var(--color-base-ink);
  color: var(--color-base-paper);
}

.pagla-btn-primary:hover {
  background-color: var(--color-accent-primary);
  color: #FFFFFF;
}

.pagla-btn-secondary {
  background-color: var(--color-base-surface);
  border-color: var(--color-base-border);
  color: var(--color-base-ink);
}

.pagla-btn-secondary:hover {
  border-color: var(--color-accent-primary);
}

.pagla-btn-ghost {
  background: transparent;
  color: var(--color-base-ink);
}

.pagla-btn-ghost:hover {
  background-color: var(--color-base-surface);
}

.pagla-btn-danger {
  background-color: var(--color-accent-error);
  color: #FFFFFF;
}

.pagla-input {
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius-md, 0.375rem);
  border: 1px solid var(--color-base-border);
  background-color: var(--color-base-paper);
  color: var(--color-base-ink);
  font-size: var(--font-size-small);
  box-sizing: border-box;
}

.pagla-input:focus {
  outline: none;
  border-color: var(--color-accent-primary);
  box-shadow: 0 0 0 2px rgba(107, 126, 255, 0.2);
}

.pagla-chip {
  display: inline-flex;
  align-items: center;
  padding: 0.15rem 0.5rem;
  border-radius: 9999px;
  font-size: var(--font-size-caption);
  font-weight: 500;
}

.pagla-chip-active {
  background-color: rgba(48, 209, 88, 0.15);
  color: #30D158;
}

.pagla-chip-planned {
  background-color: rgba(107, 126, 255, 0.15);
  color: var(--color-accent-primary);
}

.pagla-chip-accent {
  background-color: var(--color-accent-primary);
  color: #FFFFFF;
}

.pagla-chip-outline {
  border: 1px solid var(--color-base-border);
  color: var(--color-base-muted);
}

.pagla-card {
  padding: var(--space-4);
  background-color: var(--color-base-surface);
  border: 1px solid var(--color-base-border);
  border-radius: var(--radius-md, 0.375rem);
}

.pagla-card-interactive {
  cursor: pointer;
  transition: all var(--motion-duration-fast, 150ms) ease;
}

.pagla-card-interactive:hover {
  border-color: var(--color-accent-primary);
  transform: translateY(-2px);
}

/* Color Swatches Grid */
.color-swatch-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: var(--space-4);
  margin: var(--space-6) 0;
}

.color-swatch-card {
  border: 1px solid var(--color-base-border);
  border-radius: var(--radius-md, 0.375rem);
  overflow: hidden;
  cursor: pointer;
  background-color: var(--color-base-surface);
}

.color-swatch-preview {
  height: 4.5rem;
  border-bottom: 1px solid var(--color-base-border);
}

.color-swatch-info {
  padding: var(--space-3);
}

.color-swatch-name {
  display: block;
  font-family: var(--font-family-mono, monospace);
  font-size: var(--font-size-caption);
  font-weight: 600;
  margin-bottom: var(--space-1);
}

.color-swatch-desc {
  display: block;
  font-size: var(--font-size-caption);
  color: var(--color-base-muted);
  margin-bottom: var(--space-2);
}

.color-swatch-values {
  display: flex;
  justify-content: space-between;
  font-size: 0.7rem;
  color: var(--color-base-muted);
}

/* Typography scale table */
.type-scale-table {
  border: 1px solid var(--color-base-border);
  border-radius: var(--radius-md, 0.375rem);
  margin: var(--space-6) 0;
  overflow: hidden;
}

.type-scale-row {
  display: flex;
  align-items: center;
  padding: var(--space-3) var(--space-4);
  border-bottom: 1px solid var(--color-base-border);
}

.type-scale-row:last-child {
  border-bottom: none;
}

.type-scale-meta {
  width: 14rem;
  flex-shrink: 0;
}

.type-scale-meta small {
  display: block;
  color: var(--color-base-muted);
}

.type-scale-sample {
  flex: 1;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* Spacing ladder */
.spacing-ladder {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
  margin: var(--space-6) 0;
}

.spacing-row {
  display: flex;
  align-items: center;
}

.spacing-label {
  width: 14rem;
  font-size: var(--font-size-small);
}

.spacing-bar-container {
  flex: 1;
}

.spacing-bar {
  height: 1.25rem;
  background-color: var(--color-accent-primary);
  border-radius: var(--radius-sm, 0.25rem);
  min-width: 2px;
}

/* Ecosystem Grid */
.ecosystem-filter-bar {
  display: flex;
  gap: var(--space-2);
  flex-wrap: wrap;
  margin: var(--space-4) 0 var(--space-6) 0;
}

.eco-filter-btn {
  background-color: var(--color-base-surface);
  border: 1px solid var(--color-base-border);
  color: var(--color-base-muted);
  padding: var(--space-1) var(--space-3);
  border-radius: 9999px;
  font-size: var(--font-size-small);
  cursor: pointer;
  transition: all var(--motion-duration-fast, 150ms) ease;
}

.eco-filter-btn:hover,
.eco-filter-btn.active {
  background-color: var(--color-base-ink);
  color: var(--color-base-paper);
  border-color: var(--color-base-ink);
}

.ecosystem-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: var(--space-4);
  margin-top: var(--space-4);
}

.eco-card {
  padding: var(--space-4);
  background-color: var(--color-base-surface);
  border: 1px solid var(--color-base-border);
  border-radius: var(--radius-md, 0.375rem);
  display: flex;
  flex-direction: column;
}

.eco-card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--space-1);
}

.eco-card-title {
  margin: 0;
  font-size: var(--font-size-h4);
}

.eco-card-category {
  font-size: var(--font-size-caption);
  color: var(--color-base-muted);
  margin-bottom: var(--space-2);
}

.eco-card-desc {
  font-size: var(--font-size-small);
  margin: 0 0 var(--space-4) 0;
  flex: 1;
}

.eco-card-meta {
  font-size: var(--font-size-caption);
  color: var(--color-base-muted);
  border-top: 1px solid var(--color-base-border);
  padding-top: var(--space-2);
  margin-bottom: var(--space-3);
}

.eco-card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: var(--font-size-caption);
}

/* Modal Search */
.search-modal {
  display: none;
  position: fixed;
  inset: 0;
  background-color: rgba(0, 0, 0, 0.6);
  z-index: 200;
  align-items: flex-start;
  justify-content: center;
  padding-top: 10vh;
}

.search-modal.open {
  display: flex;
}

.search-box {
  background-color: var(--color-base-paper);
  border: 1px solid var(--color-base-border);
  border-radius: var(--radius-lg, 0.5rem);
  width: 90%;
  max-width: 36rem;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.3);
  overflow: hidden;
}

.search-input-wrap {
  display: flex;
  align-items: center;
  padding: var(--space-3) var(--space-4);
  border-bottom: 1px solid var(--color-base-border);
}

.search-input {
  flex: 1;
  border: none;
  background: transparent;
  font-size: var(--font-size-body);
  color: var(--color-base-ink);
  outline: none;
}

.search-results {
  max-height: 20rem;
  overflow-y: auto;
  list-style: none;
  padding: 0;
  margin: 0;
}

.search-result-item a {
  display: block;
  padding: var(--space-3) var(--space-4);
  text-decoration: none;
  color: var(--color-base-ink);
  border-bottom: 1px solid var(--color-base-border);
}

.search-result-item a:hover {
  background-color: var(--color-base-surface);
}

.search-result-sec {
  font-size: var(--font-size-caption);
  color: var(--color-base-muted);
  display: block;
}

/* Responsive queries */
@media (max-width: 64rem) {
  .app-toc {
    display: none;
  }
}

@media (max-width: 48rem) {
  .menu-toggle {
    display: flex;
  }

  .app-sidebar {
    display: none;
    position: fixed;
    top: var(--header-height);
    left: 0;
    width: 100%;
    height: calc(100vh - var(--header-height));
    z-index: 90;
  }

  .app-sidebar.open {
    display: block;
  }

  .header-center {
    display: none;
  }
}
"""


def generate_complete_html(pages: Dict[str, any], search_index: List[Dict[str, str]], active_slug: str = "index") -> str:
    """Generate the full HTML container with client routing and reactive page switches."""
    active_page = pages.get(active_slug, pages["index"])

    # Build nav HTML
    nav_sections_html = []
    for sec in DOC_SECTIONS:
        items_html = []
        for item in sec["items"]:
            slug = item["slug"]
            is_active = (slug == active_slug)
            active_class = " active" if is_active else ""
            items_html.append(
                f'<li class="nav-item"><a href="#{slug}" class="nav-link{active_class}" data-slug="{slug}" onclick="switchPage(\'{slug}\', event)">{item["title"]}</a></li>'
            )
        nav_sections_html.append(
            f'<div class="nav-section">'
            f'<div class="nav-section-title">{sec["title"]}</div>'
            f'<ul class="nav-list">{"".join(items_html)}</ul>'
            f'</div>'
        )

    # Build bundled pages JSON for instant client-side switching
    pages_bundle_json = json.dumps(
        {
            slug: {
                "title": p["title"],
                "section": p["section"],
                "path": p["path"],
                "html": p["html"],
                "toc": p["toc"],
            }
            for slug, p in pages.items()
        }
    )

    # Build initial TOC HTML
    toc_items_html = []
    for item in active_page["toc"]:
        indent = " toc-item-h3" if item["level"] == 3 else ""
        toc_items_html.append(f'<li class="toc-item{indent}"><a href="#{item["slug"]}" class="toc-link">{item["title"]}</a></li>')
    toc_html = "".join(toc_items_html) or '<li class="toc-item"><span style="color:var(--color-base-muted);">No section anchors</span></li>'

    return f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{active_page["title"]} — PaglaDESIGN Authority</title>
  <meta name="description" content="The canonical design system, BrandKit, website architecture, and UX guidelines for the entire PaglaAI ecosystem.">
  <link rel="icon" type="image/png" href="brand/pagla-face-white.png">
  <link rel="stylesheet" href="css/tokens.css">
  <link rel="stylesheet" href="css/base.css">
  <link rel="stylesheet" href="css/utilities.css">
  <link rel="stylesheet" href="css/fern.css">
</head>
<body>
  <div class="app-container">
    <!-- Header -->
    <header class="app-header">
      <div class="header-left">
        <button class="icon-btn menu-toggle" onclick="toggleSidebar()" aria-label="Toggle Navigation">☰</button>
        <a href="#index" class="brand-link" onclick="switchPage('index', event)">
          <img src="brand/paglaai-wordmark.png" alt="PaglaAI" class="brand-logo">
        </a>
        <span class="badge-version">v2.2.0</span>
      </div>

      <div class="header-center">
        <button class="search-trigger" onclick="openSearchModal()">
          <span>Search documentation, tokens, components...</span>
          <kbd style="border: 1px solid var(--color-base-border); border-radius: 3px; padding: 1px 4px; font-size: 0.75rem;">⌘K</kbd>
        </button>
      </div>

      <div class="header-right">
        <button class="icon-btn" onclick="toggleTheme()" id="themeToggleBtn" title="Toggle color theme">
          <span id="themeIcon">☀️</span> <span id="themeText">Theme</span>
        </button>
        <a href="https://github.com/paglaai/pagladesign" target="_blank" rel="noopener" class="icon-btn">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
          <span>GitHub</span>
        </a>
      </div>
    </header>

    <!-- Layout Body -->
    <div class="layout-body">
      <!-- Sidebar Navigation -->
      <aside class="app-sidebar" id="appSidebar">
        {"".join(nav_sections_html)}
      </aside>

      <!-- Main Content Area -->
      <main class="app-content">
        <div class="content-inner">
          <article class="doc-article" id="docArticle">
            <nav class="doc-breadcrumbs" aria-label="Breadcrumbs">
              <span id="breadcrumbSection">{active_page["section"]}</span> / <span id="breadcrumbTitle">{active_page["title"]}</span>
            </nav>
            <div id="pageHtmlContainer">
              {active_page["html"]}
            </div>
          </article>

          <!-- Table of Contents -->
          <aside class="app-toc" id="appToc">
            <div class="toc-title">On This Page</div>
            <ul class="toc-list" id="tocList">
              {toc_html}
            </ul>
          </aside>
        </div>
      </main>
    </div>
  </div>

  <!-- Search Modal -->
  <div class="search-modal" id="searchModal" onclick="closeSearchOnBackdrop(event)">
    <div class="search-box">
      <div class="search-input-wrap">
        <input type="text" class="search-input" id="modalSearchInput" placeholder="Type to search design system..." oninput="onSearchQuery(this.value)">
      </div>
      <ul class="search-results" id="searchResults"></ul>
    </div>
  </div>

  <!-- Client Router & Interaction Script -->
  <script>
    const PAGES = {pages_bundle_json};
    const SEARCH_INDEX = {json.dumps(search_index)};

    // Theme Management
    function initTheme() {{
      const saved = localStorage.getItem('pagladesign-theme');
      const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      const theme = saved || (prefersDark ? 'dark' : 'light');
      setTheme(theme);
    }}

    function setTheme(theme) {{
      document.documentElement.setAttribute('data-theme', theme);
      localStorage.setItem('pagladesign-theme', theme);
      const icon = document.getElementById('themeIcon');
      const text = document.getElementById('themeText');
      if (theme === 'dark') {{
        icon.textContent = '🌙';
        text.textContent = 'Dark';
      }} else {{
        icon.textContent = '☀️';
        text.textContent = 'Light';
      }}
    }}

    function toggleTheme() {{
      const current = document.documentElement.getAttribute('data-theme') || 'dark';
      setTheme(current === 'dark' ? 'light' : 'dark');
    }}

    // Sidebar Mobile Toggle
    function toggleSidebar() {{
      const sb = document.getElementById('appSidebar');
      sb.classList.toggle('open');
    }}

    // Switch Page
    function switchPage(slug, ev) {{
      if (ev) ev.preventDefault();
      if (!PAGES[slug]) return;

      const page = PAGES[slug];
      document.title = page.title + ' — PaglaDESIGN Authority';
      document.getElementById('breadcrumbSection').textContent = page.section;
      document.getElementById('breadcrumbTitle').textContent = page.title;
      document.getElementById('pageHtmlContainer').innerHTML = page.html;

      // Update Nav Active State
      document.querySelectorAll('.nav-link').forEach(link => {{
        if (link.getAttribute('data-slug') === slug) {{
          link.classList.add('active');
        }} else {{
          link.classList.remove('active');
        }}
      }});

      // Update TOC
      const tocList = document.getElementById('tocList');
      if (page.toc && page.toc.length > 0) {{
        tocList.innerHTML = page.toc.map(item => {{
          const cls = item.level === 3 ? ' class="toc-item toc-item-h3"' : ' class="toc-item"';
          return `<li${{cls}}><a href="#${{item.slug}}" class="toc-link">${{item.title}}</a></li>`;
        }}).join('');
      }} else {{
        tocList.innerHTML = '<li class="toc-item"><span style="color:var(--color-base-muted);">No section anchors</span></li>';
      }}

      // Close mobile sidebar if open
      document.getElementById('appSidebar').classList.remove('open');
      window.location.hash = slug;
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    // Copy Affordance
    function copyCode(btn) {{
      const block = btn.closest('.doc-code-block');
      const code = block.querySelector('code').innerText;
      navigator.clipboard.writeText(code).then(() => {{
        const span = btn.querySelector('span');
        const orig = span.textContent;
        span.textContent = 'Copied!';
        setTimeout(() => {{ span.textContent = orig; }}, 2000);
      }});
    }}

    function copyTokenText(tokenVar) {{
      navigator.clipboard.writeText('var(' + tokenVar + ')').then(() => {{
        alert('Copied var(' + tokenVar + ') to clipboard!');
      }});
    }}

    // Ecosystem Filter
    function filterEcosystem(filter, btn) {{
      document.querySelectorAll('.eco-filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const cards = document.querySelectorAll('.eco-card');
      cards.forEach(card => {{
        if (filter === 'all') {{
          card.style.display = 'flex';
        }} else if (filter === 'active' || filter === 'planned') {{
          card.style.display = card.getAttribute('data-status') === filter ? 'flex' : 'none';
        }} else if (filter.startsWith('role-')) {{
          card.style.display = card.getAttribute('data-role') === filter ? 'flex' : 'none';
        }}
      }});
    }}

    // Search Modal
    function openSearchModal() {{
      const modal = document.getElementById('searchModal');
      modal.classList.add('open');
      const input = document.getElementById('modalSearchInput');
      input.value = '';
      input.focus();
      onSearchQuery('');
    }}

    function closeSearchModal() {{
      document.getElementById('searchModal').classList.remove('open');
    }}

    function closeSearchOnBackdrop(e) {{
      if (e.target.id === 'searchModal') closeSearchModal();
    }}

    function onSearchQuery(q) {{
      const resultsEl = document.getElementById('searchResults');
      q = q.trim().toLowerCase();
      let matches = SEARCH_INDEX;
      if (q) {{
        matches = SEARCH_INDEX.filter(item =>
          item.title.toLowerCase().includes(q) ||
          item.section.toLowerCase().includes(q) ||
          item.slug.toLowerCase().includes(q)
        );
      }}
      if (matches.length === 0) {{
        resultsEl.innerHTML = '<li style="padding:1rem;color:var(--color-base-muted);">No documents found.</li>';
        return;
      }}
      resultsEl.innerHTML = matches.slice(0, 10).map(m => `
        <li class="search-result-item">
          <a href="#${{m.slug}}" onclick="closeSearchModal(); switchPage('${{m.slug}}', event);">
            <strong>${{m.title}}</strong>
            <span class="search-result-sec">${{m.section}} · ${{m.path}}</span>
          </a>
        </li>
      `).join('');
    }}

    // Keybindings (Cmd+K / Escape)
    document.addEventListener('keydown', (e) => {{
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {{
        e.preventDefault();
        openSearchModal();
      }} else if (e.key === 'Escape') {{
        closeSearchModal();
      }}
    }});

    // Hash Router on load
    window.addEventListener('DOMContentLoaded', () => {{
      initTheme();
      const hash = window.location.hash.replace('#', '');
      if (hash && PAGES[hash]) {{
        switchPage(hash);
      }}
    }});
  </script>
</body>
</html>
"""


def main():
    parser = argparse.ArgumentParser(description="Generate PaglaDESIGN FERN-style static site.")
    parser.add_argument(
        "--out-dir",
        type=pathlib.Path,
        default=REPO_ROOT / "DOC" / "site",
        help="Destination directory for static site (default: DOC/site)",
    )
    args = parser.parse_args()
    build_fern_site(args.out_dir)


if __name__ == "__main__":
    main()
