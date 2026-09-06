---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: searchers"
source_path: "src/regression_model_template/utils/searchers.py"
description: "Find the best hyperparameters for a model."
tags: ["module", "searchers"]
timestamp: "2026-09-06T06:26:18Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "4860b15"
---
# Module Specification: searchers

* **Source Reference:** [src/regression_model_template/utils/searchers.py](../../../../src/regression_model_template/utils/searchers.py)

# Module Overview

## Purpose

Find the best hyperparameters for a model.

## Responsibilities

Find the best hyperparameters for a model.

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

# Each File Documentation

## Imported modules

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

## Exported classes

* `Searcher`

* `GridCVSearcher`

## Exported interfaces

_Dependent on implementation_

## Public API

_Dependent on implementation_

## Internal architecture

_Dependent on implementation_

## Execution flow

_Dependent on implementation_

## Sequence explanation

_Dependent on implementation_

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

## Examples

_Dependent on implementation_

## 3. Class & Method Specifications

# Public Classes

### `Searcher`

## Overview

Base class for a searcher.

Use searcher to fine-tune models.
i.e., to find the best model params.

## Attributes

* **`KIND`**

  - **Type**: str

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`param_grid`**

  - **Type**: Grid

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

## Public Methods

* **`search(self: Any, model: models.Model, metric: metrics.Metric, inputs: schemas.Inputs, targets: schemas.Targets, cv: CrossValidation) -> Results`**

### Description

Search the best model for the given inputs and targets.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `model`

  - **type**: models.Model

  - **meaning**: AI/ML model to fine-tune.

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `metric`

  - **type**: metrics.Metric

  - **meaning**: main metric to optimize.

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `inputs`

  - **type**: schemas.Inputs

  - **meaning**: model inputs for tuning.

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `targets`

  - **type**: schemas.Targets

  - **meaning**: model targets for tuning.

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `cv`

  - **type**: CrossValidation

  - **meaning**: choice for cross-fold validation.

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

### Output

* **return type**: Results

* **semantic meaning**: Results: all the results of the searcher execution process.

* **possible null values**: _Dependent on implementation_

* **exceptions**: _Dependent on implementation_

### Side Effects

_Dependent on implementation_

### Complexity

Time Complexity: _Dependent on implementation_

Space Complexity: _Dependent on implementation_

### Example

_Dependent on implementation_

### `GridCVSearcher`

## Overview

Grid searcher with cross-fold validation.

Convention: metric returns higher values for better models.

## Attributes

* **`KIND`**

  - **Type**: T.Literal[GridCVSearcher]

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`n_jobs`**

  - **Type**: int | None

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`refit`**

  - **Type**: bool

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`verbose`**

  - **Type**: int

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`error_score`**

  - **Type**: str | float

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`return_train_score`**

  - **Type**: bool

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

## Public Methods

* **`search(self: Any, model: models.Model, metric: metrics.Metric, inputs: schemas.Inputs, targets: schemas.Targets, cv: CrossValidation) -> Results`**

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `model`

  - **type**: models.Model

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `metric`

  - **type**: metrics.Metric

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `inputs`

  - **type**: schemas.Inputs

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `targets`

  - **type**: schemas.Targets

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `cv`

  - **type**: CrossValidation

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

### Output

* **return type**: Results

* **semantic meaning**: _Dependent on implementation_

* **possible null values**: _Dependent on implementation_

* **exceptions**: _Dependent on implementation_

### Side Effects

_Dependent on implementation_

### Complexity

Time Complexity: _Dependent on implementation_

Space Complexity: _Dependent on implementation_

### Example

_Dependent on implementation_

## Used By

* [tuning.py](../../regression_model_template/jobs/tuning.md)

* [conftest.py](../../tests/conftest.md)

* [test_tuning.py](../../tests/jobs/test_tuning.md)

* [test_searchers.py](../../tests/utils/test_searchers.md)
