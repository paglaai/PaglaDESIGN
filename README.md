<p align="center">
  <a href="https://github.com/paglaai/pagladesign">
    <img src="https://raw.githubusercontent.com/paglaai/pagladesign/main/brand/paglaai-wordmark.png" alt="PaglaAI Wordmark" width="460">
  </a>
</p>

<p align="center">
  <strong>The Canonical Design Authority, DesignDNA, and Machine-First UX Operating System for Modern AI Ecosystems.</strong>
</p>

<p align="center">
  <a href="https://paglaai.github.io/pagladesign/"><img src="https://img.shields.io/badge/Docs_Portal-FERN_Style-6B7EFF?style=flat-square&logo=githubpages" alt="Docs Portal"></a>
  <a href="https://github.com/paglaai/pagladesign/actions/workflows/ci.yml"><img src="https://github.com/paglaai/pagladesign/actions/workflows/ci.yml/badge.svg" alt="CI Status"></a>
  <a href="https://github.com/paglaai/pagladesign/releases"><img src="https://img.shields.io/badge/version-2.2.0-0A0A0B?style=flat-square" alt="Version 2.2.0"></a>
  <a href="./design-system/DESIGN_DNA.md"><img src="https://img.shields.io/badge/DesignDNA-Locked_(D--024)-0A0A0B?style=flat-square" alt="DesignDNA Locked"></a>
  <a href="./.ai/mcp"><img src="https://img.shields.io/badge/MCP-FastMCP_v2.0-6B7EFF?style=flat-square" alt="FastMCP Ready"></a>
  <a href="./css/tokens.css"><img src="https://img.shields.io/badge/CSS-Cascade_Layers-0A0A0B?style=flat-square" alt="CSS Cascade Layers"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/license-MIT-0A0A0B?style=flat-square" alt="License MIT"></a>
  <a href="https://github.com/paglaai/pagladesign/generate"><img src="https://img.shields.io/badge/Template-Use_this_Template-6B7EFF?style=flat-square&logo=github" alt="Use this Template"></a>
</p>

---

## Overview

**PaglaDESIGN** is the canonical, machine-readable design authority for the PaglaAI ecosystem. It is **not** a traditional website project, component kit, or application. It is the root visual, editorial, and architectural operating system from which every surface, product, documentation portal, and AI coding agent derives its implementation.

Designed as a **production-ready GitHub template**, this repository establishes a repeatable, audit-tested standard for building and maintaining design authorities in the era of autonomous AI agents and multi-repo architectures.

```
                     ┌────────────────────────────────────────┐
                     │          PaglaDESIGN Template          │
                     │  Tokens • DesignDNA • Specs • Registry │
                     └───────────────────┬────────────────────┘
                                         │ Single Source of Truth (SSOT)
         ┌───────────────────────────────┼───────────────────────────────┐
         ▼                               ▼                               ▼
┌──────────────────┐           ┌──────────────────┐           ┌──────────────────┐
│   Human Surface  │           │   Machine / MCP  │           │   Architecture   │
│ (FERN Renderer)  │           │ (FastMCP Server) │           │ (ADR Governance) │
│ HTML · CSS · Web │           │ Cursor · Claude  │           │ D-001 ... D-024  │
└──────────────────┘           └──────────────────┘           └──────────────────┘
```

### Why a Design Authority Repository?

Traditional UI kits and design files rot because they sit disconnected from code. PaglaDESIGN solves this by treating design as **immutable code and structured data**:

1. **Deterministic Single Source of Truth (SSOT):** Token numbers live exclusively in [`design-system/DESIGN_TOKENS.md`](./design-system/DESIGN_TOKENS.md). The reference CSS ([`css/tokens.css`](./css/tokens.css)) is compiled and verified against the documentation in CI via automated parity assertions ([`tests/test_tokens_parity.py`](./tests/test_tokens_parity.py)).
2. **AI Agent Grounding via FastMCP:** AI coding agents (Claude Code, Cursor, Antigravity) cannot reliably infer UI rules across large codebases without hallucinations. PaglaDESIGN embeds a native **Model Context Protocol (FastMCP 2.0)** retrieval engine over heading-anchored chunks, allowing agents to fetch exact token values and component grammars in milliseconds.
3. **Multi-Audience Documentation Engine:** One canonical Markdown corpus compiles into three distinct formats: **FERN** (human web reading), **MACHINE** (JSON/MCP API context), and **ARCHITECT** (formal ADRs and governance specs).
4. **Permanent DesignDNA Lock:** Strict visual doctrine ([`design-system/DESIGN_DNA.md`](./design-system/DESIGN_DNA.md)) stops developers and agents from reinventing ad-hoc UI, inconsistent colors, or novelty typefaces.

---

## Use this Repo as a Template

You can adopt **PaglaDESIGN** as a turnkey template for your own organization or multi-agent ecosystem.

### 1. Click "Use this template"
Click the **[Use this template](https://github.com/paglaai/pagladesign/generate)** button at the top of this repository (or clone directly):

```bash
git clone https://github.com/paglaai/pagladesign.git my-design-authority
cd my-design-authority
```

### 2. Tailor Your Design System Core

| Layer | Canonical File | Customization Goal |
| :--- | :--- | :--- |
| **Identity & Mark** | [`brand/BRAND.md`](./brand/BRAND.md) & [`brand/`](./brand/) | Replace wordmark, avatar, and core voice principles. |
| **Design DNA** | [`design-system/DESIGN_DNA.md`](./design-system/DESIGN_DNA.md) | Set your immutable visual doctrine (monochrome, accent, rules). |
| **Design Tokens** | [`design-system/DESIGN_TOKENS.md`](./design-system/DESIGN_TOKENS.md) | Define your numbers (modular rem scale, typography, surface effects). |
| **Typeface** | [`design-system/PAGLA_SANS.md`](./design-system/PAGLA_SANS.md) & [`fonts/`](./fonts/) | Load your web and variable fonts (WOFF2 / TTF). |
| **Component Specs** | [`components/COMPONENT_LIBRARY.md`](./components/COMPONENT_LIBRARY.md) | Document your 14 canonical components (button, card, dialog, etc.). |
| **Product Registry** | [`ecosystem.json`](./ecosystem.json) | List all surfaces and repos consuming your design authority. |

### 3. Verify Local Health & Parity

```bash
# Verify all token parity tests pass
python3 -m pytest tests/test_tokens_parity.py -v

# Validate machine-readable ecosystem registry
python3 -m json.tool ecosystem.json > /dev/null
python3 -m json.tool ecosystem.schema.json > /dev/null

# Compile MCP server and RAG indexer
python3 -m py_compile .ai/mcp/server.py .ai/mcp/rag.py
```

---

## Design Doctrine (DesignDNA)

All surfaces in the ecosystem adhere to the locked **DesignDNA** doctrine ([`D-024`](./governance/DECISIONS.md)):

- **Monochrome First:** Interfaces are built on rich ink and pure paper.
  - Light theme: Ink `#0A0A0B` on Paper `#FFFFFF`
  - Dark theme: Ink `#F5F5F3` on Paper `#0A0A0B`
- **Meaning-Only Accent (`#6B7EFF`):** The indigo/blue accent is reserved strictly for interactive focus, active indicators, and text underlines. It is **never** used as a decorative background fill or banner canvas.
- **Typography as Interface:** Hierarchy is achieved through modular scale, font weights (300 to 700), and generous tracking, rather than illustrations or colored badges. Primary family: `"Pagla Sans"`.
- **Generous Whitespace:** Spacing is content. When in doubt, increase spacing by one scale step rather than squeezing controls together ([`PRINCIPLES.md`](./PRINCIPLES.md)).
- **Zero Inline Hacks:** No product or surface invents hex colors, pixel margins, or ad-hoc radius curves inline. Every value maps to a semantic token.

---

## Technical Stack & Architecture

### 1. CSS Cascade Layers (`css/`)

The reference implementation is written in standard, dependency-free CSS leveraging modern CSS Cascade Layers (`@layer`) for deterministic specificity:

```css
/* Layer order declared once at root */
@layer tokens, base, utilities;

@import url("./css/tokens.css");    /* Layer 1: CSS custom properties & @font-face */
@import url("./css/base.css");      /* Layer 2: Accessible element resets & typography */
@import url("./css/utilities.css"); /* Layer 3: Single-purpose atomic utility helpers */
```

- **Tokens Scope:** Root `:root` and `[data-theme="dark"]` custom properties.
- **Zero Specificity Wars:** Utility classes (`.u-mt-4`, `.container`) reside in `@layer utilities` and automatically win over base element selectors (`h1`, `p`, `a`) without requiring `!important`.
- **Standards Compliant:** No dead `@media` queries with CSS variables; all breakpoints resolve to clean literal rem values (`40rem`, `48rem`, `64rem`, `80rem`).

### 2. Machine Grounding: FastMCP 2.0 Server (`.ai/mcp/`)

PaglaDESIGN includes a high-performance local **Model Context Protocol (MCP)** server with an integrated BM25 lexical RAG engine. It indexes the canonical Markdown and CSS files into heading-anchored chunks, allowing coding agents to look up exact tokens and interaction patterns before proposing UI changes.

#### Connecting Agents to PaglaDESIGN

Add this configuration to your local agent configuration:

**For Claude Code / Cursor (`~/.cursor/mcp.json` or `claude_desktop_config.json`):**
```json
{
  "mcpServers": {
    "pagladesign": {
      "command": "python3",
      "args": [
        "/absolute/path/to/pagladesign/.ai/mcp/server.py"
      ]
    }
  }
}
```

**For Antigravity (`~/.gemini/antigravity/mcp/`):**
Registered natively as an active design authority sidecar.

#### Exposed MCP Tools

- `search(query, k)` — BM25 semantic retrieval over design guidelines, returning doc, heading, line number, and text.
- `lookup_token(name)` — Retrieve exact locked CSS custom property lines from `css/tokens.css` (e.g., `lookup_token("color.accent.primary")`).
- `search_tokens(term)` — Fuzzy-find design tokens matching a keyword (e.g. `space`, `radius`, `glass`).
- `get_doc(path)` — Fetch complete canonical documents safely without path traversal.
- `get_context()` — Dynamic one-call orientation surfacing corpus health and all 50+ canonical authority paths.

---

## Ecosystem Registry (`ecosystem.json`)

PaglaDESIGN serves as the registry authority for the entire ecosystem. Rather than duplicating lists across markdown files, all surfaces, products, and pipelines are recorded in [`ecosystem.json`](./ecosystem.json) and validated against [`ecosystem.schema.json`](./ecosystem.schema.json):

| Surface / Product | Role | Category | Status | Target / Repository |
| :--- | :--- | :--- | :--- | :--- |
| **PaglaDESIGN** | `authority` | Design System | `active` | [`paglaai/PaglaDESIGN`](https://github.com/paglaai/PaglaDESIGN) |
| **PaglaAI.space** | `surface` | Web Surface | `active` | [`paglaai/paglaai.space`](https://github.com/paglaai/paglaai.space) |
| **paglaai-docs** | `surface` | Documentation | `active` | [`paglaai/paglaai-docs`](https://github.com/paglaai/paglaai-docs) |
| **PaglaMLX** | `product` | AI Runtime | `active` | [`paglaai/PaglaMLX`](https://github.com/paglaai/PaglaMLX) |
| **PaglaROUTER** | `product` | LLM Gateway | `active` | [`paglaai/PaglaROUTER`](https://github.com/paglaai/PaglaROUTER) |
| **PaglaSHELL** | `product` | Terminal CLI | `active` | [`paglaai/PaglaSHELL`](https://github.com/paglaai/PaglaSHELL) |
| **B3K4R** | `product` | Productivity | `active` | [`paglaai/B3K4R`](https://github.com/paglaai/B3K4R) |
| **PaglaCHAT** | `product` | Chat Interface | `active` | [`paglaai/PaglaCHAT`](https://github.com/paglaai/PaglaCHAT) |
| **PaglaOS** | `product` | Desktop OS | `active` | [`paglaai/KolponaOS`](https://github.com/paglaai/KolponaOS) |
| **apphole.store** | `surface` | App Storefront | `planned` | `https://apphole.store` |
| **SANCTUM** | `runtime` | Sandboxed Engine | `planned` | `paglaai/sanctum` |

### Automation Pipeline: `design.updated`

Whenever a change lands on `main` in PaglaDESIGN touching `css/**`, `design-system/**`, or `ecosystem.json`, GitHub Actions automatically:
1. Validates token compilation & runs the parity test suite.
2. Validates `ecosystem.json` against the schema.
3. Broadcasts a `repository_dispatch` event (`design.updated`) to all downstream consumer repositories via [`.github/workflows/dispatch-downstream.yml`](./.github/workflows/dispatch-downstream.yml) to trigger remote cache invalidation and rebuilds.

---

## Repository Skeleton

```
pagladesign/
├── README.md                           # This document (Design Authority Root)
├── LICENSE                             # MIT License (AYNAGHOR)
├── VISION.md                           # Philosophical mission & ecosystem reason
├── DESIGN.md                           # Foundational design thesis
├── PRINCIPLES.md                       # Standing visual & interaction principles
├── AGENTS.md                           # AI coding agent constitution & rules
├── ecosystem.json                      # Machine-readable ecosystem SSOT registry
├── ecosystem.schema.json               # JSON Schema (Draft 2020-12) validation
│
├── brand/                              # Brand identity, logos, BrandKit specifications
│   ├── paglaai-wordmark.png            # Official high-resolution wordmark
│   ├── pagla-face-black.png            # Vector mark assets
│   ├── BRAND.md                        # Brand identity doctrine
│   └── BRANDKIT.md                     # Brand assets and styling rules
│
├── design-system/                      # The core design authority
│   ├── DESIGN_DNA.md                   # Locked visual & interaction contract (D-024)
│   ├── DESIGN_TOKENS.md                # Locked numeric values (Modular Rem Scale)
│   ├── PAGLA_SANS.md                   # Primary typeface specification
│   ├── PAGLA_UI.md                     # Interaction architecture & intent taxonomy
│   ├── COLOR_SYSTEM.md                 # Monochrome & semantic color mechanics
│   ├── TYPOGRAPHY.md                   # Type scale, hierarchy, rhythm
│   ├── CSS_ARCHITECTURE.md             # Cascade layers, token-to-CSS translation
│   ├── ACCESSIBILITY.md                # Contrast, focus rings, reduced motion
│   ├── MOTION.md                       # Duration tokens and easing curves
│   ├── RENDERER_API.md                 # Multi-renderer frontmatter specification
│   ├── FERN_RENDERER.md                # Human web reading renderer contract
│   ├── MACHINE_RENDERER.md             # Agent / JSON / MCP API contract
│   └── ARCHITECT_RENDERER.md           # Governance / ADR contract
│
├── components/                         # The UI component registry (14 canonical controls)
│   ├── COMPONENTS.md                   # Component grammar & composition principles
│   └── COMPONENT_LIBRARY.md            # Registry (Button, Input, Card, Modal, etc.)
│
├── css/                                # Pure reference implementation
│   ├── tokens.css                      # Generated custom properties (@layer tokens)
│   ├── base.css                        # Semantic resets & element defaults (@layer base)
│   └── utilities.css                   # Atomic single-purpose classes (@layer utilities)
│
├── fonts/                              # Pagla Sans typeface binaries
│   ├── PaglaSans-*.woff2               # High-performance web font weights
│   ├── PaglaSans-*.ttf                 # Print & desktop true-type binaries
│   └── PaglaSans-VF.woff2              # Variable font format
│
├── governance/                         # Immutable architectural governance
│   ├── DECISIONS.md                    # Architectural Decision Records (D-001..D-024)
│   ├── ROADMAP.md                      # Three-phase ecosystem roadmap
│   ├── CHANGELOG.md                    # Historical release log (v1.0..v2.1)
│   └── DOCUMENTATION_STYLE.md          # Technical prose guidelines
│
├── site/                               # Web information architecture
│   ├── CONTENT_STRATEGY.md             # Voice, tone, editorial standards
│   ├── NAVIGATION.md                   # Global navigation structures
│   └── SITEMAP.md                      # Canonical sitemap specification
│
├── templates/                          # Page-level wireframe compositions
├── mockups/                            # High-fidelity visual references
├── wireframes/                         # Low-fidelity layout references
│
├── tests/                              # Automated CI quality gates
│   └── test_tokens_parity.py           # 10-point SSOT token parity test suite
│
├── .ai/                                # Agent infrastructure (Excluded from RAG)
│   ├── AGENT_MANUAL.md                 # 12-section agent operational procedure
│   └── mcp/                            # FastMCP 2.0 stdio retrieval server
│       ├── server.py                   # MCP server entry point & tool handlers
│       ├── rag.py                      # Pure-stdlib BM25 retrieval indexer
│       └── requirements.txt            # Python dependencies (mcp>=2.0)
│
├── .github/                            # GitHub Actions CI/CD workflows
│   ├── actions/build-tokens/           # Token compiler & validator composite action
│   └── workflows/                      # ci.yml, release.yml, dispatch-downstream.yml
│
├── bin/                                # Build utilities
│   └── build_docx.py                   # Regenerate DOC/AGENT_MANUAL.docx
└── DOC/                                # Compiled binary output documents
```

---

## Governance & The Decision Workflow

Architecture in PaglaDESIGN is strictly governed by [`governance/DECISIONS.md`](./governance/DECISIONS.md):

```
Problem Identified → Research & Alternatives → Document in DECISIONS.md → Update CHANGELOG.md → Implementation
```

- **Rule of No Silent Architecture:** Significant changes are documented in `DECISIONS.md` before implementation.
- **Rule of Token Locking ([`D-010`](./governance/DECISIONS.md)):** Numbers in `DESIGN_TOKENS.md` are binding. A value cannot be changed without recording Context, Decision, Alternatives, Trade-offs, and Result.
- **Stable Skeleton ([`D-011`](./governance/DECISIONS.md) / [`D-012`](./governance/DECISIONS.md)):** Top-level directories are immutable. Never add top-level folders or rename directories without an approved ADR.

### Decision Log Highlights

- [`D-001`](./governance/DECISIONS.md#d-001-design-first-documentation-second-implementation-last) — Design First, Documentation Second, Implementation Last.
- [`D-002`](./governance/DECISIONS.md#d-002-typography-as-the-primary-interface) — Typography as the Primary Interface.
- [`D-010`](./governance/DECISIONS.md#d-010-design-tokens-as-the-sole-numerical-authority) — Design Tokens as the Sole Numerical Authority.
- [`D-021`](./governance/DECISIONS.md#d-021-font-naming-normalization-and-surface-effect-tokens) — Canonical `"Pagla Sans"` Typeface Naming.
- [`D-023`](./governance/DECISIONS.md#d-023-ecosystem-registry-and-audit-v20-roadmap) — Canonical Ecosystem Registry (`ecosystem.json`).
- [`D-024`](./governance/DECISIONS.md#d-024-ssot-parity-token-compilation-mcp-modernization-and-ci-gate-sealing) — SSOT Parity, Token Compilation, FastMCP Modernization, and CI Quality Gates.

---

## Quality Gates & Verification

Continuous Integration ([`.github/workflows/ci.yml`](./.github/workflows/ci.yml)) runs on Ubuntu with Python 3.11 to validate:

1. **Tokens Parity & Structure:** Compiles `DESIGN_TOKENS.md`, validates against unescaped dots, asserts `@font-face` rules, and executes `tests/test_tokens_parity.py`.
2. **Ecosystem Registry:** Validates `ecosystem.json` syntax and schema conformance, preventing duplicate IDs or untyped repositories.
3. **MCP Server Health:** Verifies syntax and compilation of the FastMCP 2.0 server and indexing engine with `py_compile`, `black`, and `flake8`.

Run the entire verification suite locally:

```bash
# Run pytest parity suite
pytest tests/test_tokens_parity.py -v

# Validate CSS syntax and layers
python3 -c "
from pathlib import Path
import re
for css in Path('css').glob('*.css'):
    content = css.read_text()
    assert '{' in content and '}' in content
    assert '@media' not in content or 'var(' not in content
print('CSS: PASS')
"
```

---

## License

PaglaDESIGN is open source software licensed under the **[MIT License](./LICENSE)**.  
Pagla Sans is based on Open Sans (SIL Open Font License 1.1 / Apache 2.0).

---

<p align="center">
  <sub>© 2026 AYNAGHOR. PaglaDESIGN is the design authority for the PaglaAI ecosystem. Every surface inherits from here.</sub>
</p>
