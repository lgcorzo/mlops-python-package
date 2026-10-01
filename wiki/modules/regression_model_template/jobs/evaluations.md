---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "regression_model_template::jobs::evaluations — Model Evaluation Pipeline"
source_path: "src/regression_model_template/jobs/evaluations.py"
description: "Evaluates registered model performance against predefined quality thresholds."
tags: ["iso42010", "okf", "component_view", "evaluation", "metrics"]
timestamp: "2026-10-01T17:50:00Z"
generated: "agent:wiki-iso-documentation-standard"
verified: "true"
last_verified_commit: "073b5fd"
---

# regression_model_template::jobs::evaluations — Model Evaluation Pipeline

> **Source**: `src/regression_model_template/jobs/evaluations.py` (Lines: L1-L125)  
> **Layer**: Application  
> **Role**: Ingests test partitions, evaluates model predictions against configured metric thresholds, and logs verification reports to MLflow.

---

## 1. Class Diagram

```mermaid
classDiagram
    class EvaluationsJob {
        +str KIND = "EvaluationsJob"
        +RunConfig run_config
        +ReaderKind inputs
        +ReaderKind targets
        +str model_type
        +run() Locals
    }
    EvaluationsJob --|> Job : implements
```

---

> *Related: [Metrics](../core/metrics.md) · [Promotion Job](promotion.md)*
