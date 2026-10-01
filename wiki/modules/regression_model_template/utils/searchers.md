---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "regression_model_template::utils::searchers — Hyperparameter Searchers"
source_path: "src/regression_model_template/utils/searchers.py"
description: "Abstract Searcher interface and Grid/Optuna cross-validation hyperparameter optimizers."
tags: ["iso42010", "okf", "component_view", "searchers", "optuna", "grid_search"]
timestamp: "2026-10-01T17:50:00Z"
generated: "agent:wiki-iso-documentation-standard"
verified: "true"
last_verified_commit: "073b5fd"
---

# regression_model_template::utils::searchers — Hyperparameter Searchers

> **Source**: `src/regression_model_template/utils/searchers.py` (Lines: L1-L116)  
> **Layer**: Utilities  
> **Role**: Strategy abstraction executing parameter space traversals (Grid Search, Optuna Bayesian optimization) against regression models.

---

## 1. Class Diagram

```mermaid
classDiagram
    class Searcher {
        <<abstract>>
        +str KIND
        +Grid param_grid
        +search(model: Model, metric: Metric, inputs: Inputs, targets: Targets, cv: CrossValidation) Results*
    }

    class GridCVSearcher {
        +str KIND = "GridCVSearcher"
        +int n_jobs
        +bool refit
        +search(model: Model, metric: Metric, inputs: Inputs, targets: Targets, cv: CrossValidation) Results
    }
    GridCVSearcher --|> Searcher : implements
```

---

> *Related: [Tuning Job](../jobs/tuning.md) · [Splitters](splitters.md)*
