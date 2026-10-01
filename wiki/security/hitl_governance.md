---
iso_doc_type: "Policy"
iso_viewpoint: "SecurityView"
type: "security"
title: "Human-in-the-Loop (HITL) Governance Policy"
description: "ISO 42010 SecurityView / ISO 15289 Policy documentation establishing mandatory human verification gates for model promotions and pull requests."
tags: ["iso42010", "okf", "policy", "hitl", "governance"]
timestamp: "2026-10-01T17:50:00Z"
generated: "agent:wiki-iso-documentation-standard"
verified: "true"
last_verified_commit: "073b5fd"
---

# Human-in-the-Loop (HITL) Governance Policy

> **Policy Directive**: Automated agents and CI/CD pipelines are strictly prohibited from automatically merging code into `main` or promoting machine learning models to production aliases without explicit human sign-off.

---

## 1. Governance Principles

1. **Non-Autonomous Production Promotion**: Model promotion to the `champion` alias requires human review of evaluation metrics and XAI reports.
2. **Mandatory Human PR Review**: Autonomous factory agents (Dark Gravity / ZeroClaw / Jules) may create feature branches and open PRs, but **merges into default branches MUST be a manual human action**.
3. **Four-Vertex Promotion Mesh**: Prior to promoting any candidate model, four quality gates must be satisfied:

```mermaid
graph TD
    V1["Vertex 1: Metrics Validation
(MSE / RMSE threshold check)"] --> V2["Vertex 2: Fairness & XAI Audit
(SHAP attribution review)"]
    V2 --> V3["Vertex 3: Security & Signature Gate
(InferSigner attestation)"]
    V3 --> V4["Vertex 4: Human Sign-off
(Data Scientist / Lead approval)"]
    V4 --> PROMOTE["Promote to 'champion' in MLflow"]

    classDef vertex fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#f8fafc;
    classDef action fill:#064e3b,stroke:#34d399,stroke-width:2px,color:#f8fafc;
    class V1,V2,V3,V4 vertex;
    class PROMOTE action;
```

---

## 2. Threshold Check Criteria

| Metric | Promotion Condition | Rationale |
|:---|:---|:---|
| **$R^2$ Score** | $R^2_{	ext{challenger} \ge R^2_{	ext{champion}$ | Model explanatory power must not regress. |
| **RMSE** | $	ext{RMSE}_{	ext{challenger} \le 	ext{RMSE}_{	ext{champion} 	imes 1.02$ | Absolute error must remain within 2% margin. |
| **SHAP Drift** | Top-3 features match baseline ranking | Prevents anomalous feature weight distortions. |
| **Schema Compatibility** | 100% Pandera validation | Guarantees zero input contract breakage. |

---

> *Related: [Verification Triad](verification_triad.md) · [Compliance Audit](compliance_audit.md) · [Master Index](../index.md)*
