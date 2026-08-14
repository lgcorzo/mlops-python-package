---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: searchers"
source_path: "src/regression_model_template/utils/searchers.py"
description: "Find the best hyperparameters for a model."
tags: ["module", "searchers"]
timestamp: "2026-08-14T05:37:38Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "ce3f2af"
---
# Module Specification: searchers

* **Source Reference:** [src/regression_model_template/utils/searchers.py](../../../../src/regression_model_template/utils/searchers.py)

## 1. Architectural Role & Responsibilities
Find the best hyperparameters for a model.

### Detected Architecture Patterns
Detected roles: General Subsystem

## 2. UML Diagrams
### Class Diagram
```plantuml
classDiagram
    direction BT
    class Searcher {
        +KIND: str
        +param_grid: Grid
        +search(self: Any, model: models.Model, metric: metrics.Metric, inputs: schemas.Inputs, targets: schemas.Targets, cv: CrossValidation) Results
    }
    ABC <|-- Searcher : Generalization
    BaseModel <|-- Searcher : Generalization
    class GridCVSearcher {
        +KIND: T.Literal~GridCVSearcher~
        +n_jobs: int | None
        +refit: bool
        +verbose: int
        +error_score: str | float
        +return_train_score: bool
        +search(self: Any, model: models.Model, metric: metrics.Metric, inputs: schemas.Inputs, targets: schemas.Targets, cv: CrossValidation) Results
    }
    Searcher <|-- GridCVSearcher : Generalization
```

### Sequence Diagram
```plantuml
sequenceDiagram
    GridCVSearcher.search->>GridSearchCV: invoke
    GridCVSearcher.search->>fit: invoke
    GridCVSearcher.search->>DataFrame: invoke
```

### Component Diagram
```plantuml
component [searchers] as Comp
Comp --> [abc]
Comp --> [typing]
Comp --> [Union]
Comp --> [pandas]
Comp --> [pydantic]
Comp --> [model_selection]
Comp --> [metrics]
Comp --> [models]
Comp --> [schemas]
Comp --> [splitters]
```

## 3. Class & Method Specifications

### `Searcher`

Base class for a searcher.

Use searcher to fine-tune models.
i.e., to find the best model params.

Parameters:
    param_grid (Grid): mapping of param key -> values.

#### Attributes
* **`KIND`** (`str`)
* **`param_grid`** (`Grid`)

#### Public Methods
* **`search(self: Any, model: models.Model, metric: metrics.Metric, inputs: schemas.Inputs, targets: schemas.Targets, cv: CrossValidation) -> Results`**
  - **Purpose**: Search the best model for the given inputs and targets.
  - **Inputs**:
    - `self` (`Any`)
    - `model` (`models.Model`)
    - `metric` (`metrics.Metric`)
    - `inputs` (`schemas.Inputs`)
    - `targets` (`schemas.Targets`)
    - `cv` (`CrossValidation`)
  - **Outputs**: `Results`

### `GridCVSearcher`

Grid searcher with cross-fold validation.

Convention: metric returns higher values for better models.

Parameters:
    n_jobs (int, optional): number of jobs to run in parallel.
    refit (bool): refit the model after the tuning.
    verbose (int): set the searcher verbosity level.
    error_score (str | float): strategy or value on error.
    return_train_score (bool): include train scores if True.

#### Attributes
* **`KIND`** (`T.Literal[GridCVSearcher]`)
* **`n_jobs`** (`int | None`)
* **`refit`** (`bool`)
* **`verbose`** (`int`)
* **`error_score`** (`str | float`)
* **`return_train_score`** (`bool`)

#### Public Methods
* **`search(self: Any, model: models.Model, metric: metrics.Metric, inputs: schemas.Inputs, targets: schemas.Targets, cv: CrossValidation) -> Results`**
  - **Purpose**: No description available.
  - **Inputs**:
    - `self` (`Any`)
    - `model` (`models.Model`)
    - `metric` (`metrics.Metric`)
    - `inputs` (`schemas.Inputs`)
    - `targets` (`schemas.Targets`)
    - `cv` (`CrossValidation`)
  - **Outputs**: `Results`

## Dependencies

* `abc`
* `typing`
* `typing.Union`
* `pandas`
* `pydantic`
* `sklearn.model_selection`
* `regression_model_template.core.metrics`
* `regression_model_template.core.models`
* `regression_model_template.core.schemas`
* `regression_model_template.utils.splitters`

## Used By

* [tuning.py](../../regression_model_template/jobs/tuning.md)
* [conftest.py](../../tests/conftest.md)
* [test_tuning.py](../../tests/jobs/test_tuning.md)
* [test_searchers.py](../../tests/utils/test_searchers.md)
