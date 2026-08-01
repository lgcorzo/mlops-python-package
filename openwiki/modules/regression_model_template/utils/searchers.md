---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: Hyperparameter Searchers"
source_path: "[src/regression_model_template/utils/searchers.py](/src/regression_model_template/utils/searchers.py)"
description: "Abstract hyperparameter searcher interface and GridSearchCV implementation."
tags: ["utils", "searchers", "gridsearch", "cv"]
last_verified_commit: "HEAD"
timestamp: "2026-07-31T16:17:00Z"
generated: "agent:okf-professional-documenter"
verified: "true"
---

# Module Specification: Hyperparameter Searchers

* **Source File Reference:** [`src/regression_model_template/utils/searchers.py`](/src/regression_model_template/utils/searchers.py) (Lines: L34-L113)
* **Upstream Dependencies:** `scikit-learn`
* **Downstream Consumers:** [Modules/RegressionModelTemplate/Jobs/Tuning](../jobs/tuning.md)

## 1. Architectural Role & Responsibilities
`searchers.py` defines `Searcher` interface and `GridCVSearcher` implementation for cross-validated hyperparameter optimization.

## 2. UML 2.0 Class Diagram

```mermaid
classDiagram
    direction BT
    class Searcher {
        <<abstract>>
        +KIND: str
        +param_grid: Grid
        +search(model, metric, inputs, targets, cv)* Results
    }
    class GridCVSearcher {
        +KIND: Literal
        +n_jobs: int | None
        +refit: bool
        +verbose: int
        +error_score: str | float
        +return_train_score: bool
        +search(model, metric, inputs, targets, cv) Results
    }
    Searcher <|-- GridCVSearcher : Generalization
```

## 3. Class & Method Specifications

### `Searcher` ([`src/regression_model_template/utils/searchers.py:L34-L68`](/src/regression_model_template/utils/searchers.py#L34-L68))
* `search(self, model, metric, inputs, targets, cv)` (L49-L68): Abstract cross-validation search method.

### `GridCVSearcher` ([`src/regression_model_template/utils/searchers.py:L71-L113`](/src/regression_model_template/utils/searchers.py#L71-L113))
* `search(self, model, metric, inputs, targets, cv)` (L92-L113): Executes Scikit-Learn `GridSearchCV` optimization across defined parameter grids.
