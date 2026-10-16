# PAGLA_UI — Interaction Architecture & Component Contract

> **SEP // INF 004 & 005 · Concept v0.1**  
> *One intent. The right interface. The shortest path to a result.*

---

## 1. The Five Ecosystem Authorities

The PaglaAI ecosystem strictly separates concerns into five distinct authorities:

```
                      ┌────────────────────────────────────────┐
                      │         PaglaGPT (Intelligence)        │
                      │  Reasoning • Intent • Tool Selection   │
                      └──────────────────┬─────────────────────┘
                                         │ Structured Schema Proposal
                                         ▼
                      ┌────────────────────────────────────────┐
                      │          PaglaUI (Interaction)         │
                      │  Component Selection • State • Layout  │
                      └─────────┬────────────────────┬─────────┘
                                │                    │
         Governs Visual Form    │                    │ Governs Tone & Language
                 ▼              │                    │            ▼
   ┌───────────────────────────┐│                    │┌───────────────────────────┐
   │  PaglaDESIGN (Visuals)    ││                    ││   PaglaWRITER (Language)  │
   │  Tokens • Typography • CSS││                    ││   Copy • Voice • Rhythm   │
   └───────────────────────────┘│                    │└───────────────────────────┘
                                ▼                    ▼
                      ┌────────────────────────────────────────┐
                      │           PaglaOS (Execution)          │
                      │  Local Runtime • Tools • Permissions   │
                      └────────────────────────────────────────┘
```

| Authority | Domain | Responsibility |
| :--- | :--- | :--- |
| **`PaglaDESIGN`** | Visual System | Authoritative design tokens (`DESIGN_TOKENS.md`), typography (`Pagla Sans`), monochrome surfaces, spacing grid, and orange accent. |
| **`PaglaWRITER`** | Language | Content voice, terminology, editorial rhythm, and structured brevity. |
| **`PaglaUI`** | Interaction | Intent routing, component state machine, progressive rendering, user controls, and navigation. |
| **`PaglaGPT`** | Intelligence | Intent comprehension, task decomposition, and schema generation. (Never emits unvalidated raw executable UI code). |
| **`PaglaOS`** | Execution | Local tool runner, sandboxed filesystem, process lifecycle, and permission auditing. |

---

## 2. Intent-to-Interface Taxonomy

PaglaUI deterministically maps high-level user intent to specialized component configurations:

| Intent Primitive | Target Outcome | Primary Interface Composition | Core Components Active |
| :--- | :--- | :--- | :--- |
| **Answer** | Fact, definition, or short explanation | **Concise Surface** | `IntentInput`, `ResponseSurface` (with inline citations) |
| **Research** | Deep multi-source investigation | **Research Workspace** | `ResponseSurface`, `ContextPanel`, `ArtifactViewer` |
| **Build** | Multi-phase plan & milestone tracking | **Project Workspace** | `PlanBoard`, `TaskCard`, `ContextRail`, `ApprovalGate` |
| **Visualize** | Relational data, benchmarks, or metrics | **Data View** | `DataView` (Tables, Metric Cards, Charts) |
| **Create** | Long-form documents, assets, or code | **Creative Studio** | `ArtifactViewer`, `ContextPanel`, `ResponseSurface` |
| **Execute** | System modifications, deployments, or scripts | **Execution Console** | `ProgressStream`, `ActionPanel`, `ApprovalGate`, `ExecutionTimeline` |

---

## 3. The Nine Core Components

Every component adheres to a strict state contract (`idle`, `generating`, `needs_input`, `ready`, `awaiting_approval`, `running`, `success`, `error`, `cancelled`).

1. **`IntentInput`**: Multi-modal intent bar supporting natural language, file drops, and intent overrides.
2. **`ResponseSurface`**: Structured typography canvas rendering verified markdown, equations, and citations.
3. **`DataView`**: High-density tables, metric cards, and responsive comparison views.
4. **`TaskWorkspace`**: Comprehensive project planning surface with workstreams, milestones, and task checklists.
5. **`ActionPanel`**: Tool execution controls, rerun triggers, and parameter adjustments.
6. **`ContextPanel`**: Multi-tier context inspector (active repository, memory, environment, connected models).
7. **`ProgressStream`**: Real-time telemetry feed displaying running tools, TTFT, token velocity, and execution status.
8. **`ApprovalGate`**: Non-blocking safety modal explaining consequential operation scope, blast radius, and authorization.
9. **`ArtifactViewer`**: Live code, document, and asset viewer with syntax highlighting and diff inspection.

---

## 4. Governance & Safety Directives

* **Intent Before Layout**: The interface adapts to the smallest surface area that completely solves the problem.
* **Progressive Disclosure**: Secondary controls and telemetry remain in rails until intentionally summoned.
* **No False Execution**: Mock data, generated proposals, and verified operations must never be conflated.
* **Permission-Aware**: High-consequence actions (e.g. filesystem mutations, git pushes, Cloudflare updates) require explicit `ApprovalGate` confirmation.
* **Accessible by Default**: Full WCAG 2.2 AA compliance, visible focus indicators, semantic ARIA landmarks, and reduced-motion adherence.
* **Token Fidelity**: Strictly consumes `DESIGN_TOKENS.md`—zero inline arbitrary values.
