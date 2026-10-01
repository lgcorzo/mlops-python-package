---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "regression_model_template::jobs::training — Model Training Pipeline"
source_path: "src/regression_model_template/jobs/training.py"
description: "Trains regression models, evaluates train/test partitions, and logs parameters and artifacts to MLflow."
tags: ["iso42010", "okf", "component_view", "training", "mlflow"]
timestamp: "2026-10-01T17:50:00Z"
generated: "agent:wiki-iso-documentation-standard"
verified: "true"
last_verified_commit: "073b5fd"
---

# regression_model_template::jobs::training — Model Training Pipeline

> **Source**: `src/regression_model_template/jobs/training.py` (Lines: L1-L145)  
> **Layer**: Application  
> **Role**: Ingests training data, splits partitions, fits the model estimator, evaluates train/test error, and registers artifacts with active MLflow runs.

---

## 1. Class Diagram

```mermaid
classDiagram
    class TrainingJob {
        +str KIND = "TrainingJob"
        +RunConfig run_config
        +ReaderKind inputs
        +ReaderKind targets
        +ModelKind model
        +run() Locals
    }
    TrainingJob --|> Job : implements
```

---

> *Related: [Models](../core/models.md) · [Tuning Job](tuning.md)*
