---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDecision"
type: "adr"
title: "ADR 001: Local AST Parsing Over Heavy External LLM Databases"
description: "Decision record documenting choice of local Graphify/Pyreverse AST scripts over complex external LLM search servers."
tags: ["adr", "iso42010", "decision", "ast"]
timestamp: "2026-08-01T09:57:53Z"
generated: "agent:uml2-okf-documenter"
verified: "true"
last_verified_commit: "8f9670a"
---

# Architecture Decision Record: ADR 001

## 1. Status
**ACCEPTED** (Date: 2026-08-01)

## 2. Context & Stakeholder Concern
* **Addressed Concern:** Developers need a reliable, cost-efficient way to verify codebase structural changes and update documentation without relying on heavy external background databases or third-party vector/embedding models.
* **Framing Viewpoint:** Component View & System Maintainability.

## 3. Decision
Adopt lightweight local AST CLI tools (`graphify update .` and `pyreverse` code extraction) as the primary knowledge extraction engine, with synthesis performed exclusively by the primary agent LLM. All structural changes must be verified against this AST index.

## 4. Rationale & Alternatives Evaluated

| Alternative Evaluated | Trade-Off / Failure Mode | Evaluation Result |
| :--- | :--- | :--- |
| **External Vector Search Server** | High token overhead, potential code leakage to third parties, requires background containers. | Rejected |
| **Manual Documentation Maintenance** | High risk of out-of-date documentation, missing method signatures, drift between docs and code. | Rejected |
| **Local AST Engine (Graphify + Pyreverse)** | Zero-hallucination signatures, local execution in seconds, no external service dependencies. | **Selected** |

## 5. Consequences
- **Positive:** Fast documentation updates, exact matching of signatures and line spans, 100% data privacy.
- **Negative:** Requires Python and conda environments with `graphify` and `pylint` installed on the developer workstation.
