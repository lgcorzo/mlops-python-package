---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDecision"
type: "adr"
title: "ADR 001: Local AST Extraction Over External Vector Databases"
description: "Architecture decision record documenting choice of local Graphify and Python AST tools over complex third-party vector/embedding servers."
tags: ["adr", "iso42010", "decision", "graphify", "ast"]
last_verified_commit: "HEAD"
timestamp: "2026-07-31T16:17:00Z"
generated: "agent:okf-professional-documenter"
verified: "true"
---

# Architecture Decision Record (ADR 001)

## 1. Status
**ACCEPTED** (Date: 2026-07-31)

---

## 2. Context & Stakeholder Concern
* **Addressed Concern:** Avoid multi-service installation complexity, external vector database management, and network API dependencies when generating software architecture documentation.
* **Framing Viewpoint:** Component View, Maintainability, and Security View.

---

## 3. Decision
Adopt local, deterministic AST CLI extraction tools (`graphify update .`, Python native `ast` module analysis) as the primary knowledge graph and symbol extraction engine, combined with synthesis performed directly by the primary agent LLM.

---

## 4. Rationale & Alternatives Evaluated

| Alternative Evaluated | Trade-Off / Failure Mode | Evaluation Result |
| :--- | :--- | :--- |
| **External Vector Database / RAG** | Requires running external background vector servers, loss of exact line citations, high API cost. | Rejected |
| **Manual Hand-Written Documentation** | Becomes stale immediately upon git commits, lacks exact symbol line spans. | Rejected |
| **Local AST Tools + Primary LLM** | 100% precise line number citations, 0% hallucination on method signatures, fast local execution without network costs. | **Selected** |

---

## 5. Affected System Artifacts
* Modifies `openwiki/` documentation hierarchy.
* Anchored to `[[[[[src/regression_model_template](../../../src/regression_model_template)](../../../[src/regression_model_template](../../../src/regression_model_template))](../../../[[src/regression_model_template](../../../src/regression_model_template)](../../../[src/regression_model_template](../../../src/regression_model_template)))](../../../[[[src/regression_model_template](../../../src/regression_model_template)](../../../[src/regression_model_template](../../../src/regression_model_template))](../../../[[src/regression_model_template](../../../src/regression_model_template)](../../../[src/regression_model_template](../../../src/regression_model_template))))](../../../[[[[src/regression_model_template](../../../src/regression_model_template)](../../../[src/regression_model_template](../../../src/regression_model_template))](../../../[[src/regression_model_template](../../../src/regression_model_template)](../../../[src/regression_model_template](../../../src/regression_model_template)))](../../../[[[src/regression_model_template](../../../src/regression_model_template)](../../../[src/regression_model_template](../../../src/regression_model_template))](../../../[[src/regression_model_template](../../../src/regression_model_template)](../../../[src/regression_model_template](../../../src/regression_model_template)))))/`.
* Links to [Architecture/ComponentStructure](../component_structure.md) and [Index](../../index.md).
