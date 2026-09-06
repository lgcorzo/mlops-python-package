---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: splitters"
source_path: "src/regression_model_template/utils/splitters.py"
description: "Split dataframes into subsets (e.g., train/valid/test)."
tags: ["module", "splitters"]
timestamp: "2026-09-06T06:26:18Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "4860b15"
---
# Module Specification: splitters

* **Source Reference:** [src/regression_model_template/utils/splitters.py](../../../../src/regression_model_template/utils/splitters.py)

# Module Overview

## Purpose

Split dataframes into subsets (e.g., train/valid/test).

## Responsibilities

Split dataframes into subsets (e.g., train/valid/test).

## Dependencies

* `abc`

* `typing`

* `numpy`

* `numpy.typing`

* `pydantic`

* `sklearn.model_selection`

* `regression_model_template.core.schemas`

# Each File Documentation

## Imported modules

* `abc`

* `typing`

* `numpy`

* `numpy.typing`

* `pydantic`

* `sklearn.model_selection`

* `regression_model_template.core.schemas`

## Exported classes

* `Splitter`

* `TrainTestSplitter`

* `TimeSeriesSplitter`

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
    class Splitter {
        +KIND: str
        +split(self: Any, inputs: schemas.Inputs, targets: schemas.Targets, groups: Index | None) TrainTestSplits
        +get_n_splits(self: Any, inputs: schemas.Inputs, targets: schemas.Targets, groups: Index | None) int
    }
    ABC <|-- Splitter : Generalization
    BaseModel <|-- Splitter : Generalization
    class TrainTestSplitter {
        +KIND: T.Literal~TrainTestSplitter~
        +shuffle: bool
        +test_size: int | float
        +random_state: int
        +split(self: Any, inputs: schemas.Inputs, targets: schemas.Targets, groups: Index | None) TrainTestSplits
        +get_n_splits(self: Any, inputs: schemas.Inputs, targets: schemas.Targets, groups: Index | None) int
    }
    Splitter <|-- TrainTestSplitter : Generalization
    class TimeSeriesSplitter {
        +KIND: T.Literal~TimeSeriesSplitter~
        +gap: int
        +n_splits: int
        +test_size: int | float
        +split(self: Any, inputs: schemas.Inputs, targets: schemas.Targets, groups: Index | None) TrainTestSplits
        +get_n_splits(self: Any, inputs: schemas.Inputs, targets: schemas.Targets, groups: Index | None) int
    }
    Splitter <|-- TimeSeriesSplitter : Generalization
```

### Sequence Diagram

```plantuml
sequenceDiagram
    TrainTestSplitter.split->>arange: invoke
    TrainTestSplitter.split->>train_test_split: invoke
    TrainTestSplitter.split->>len: invoke
    TimeSeriesSplitter.split->>TimeSeriesSplit: invoke
    TimeSeriesSplitter.split->>split: invoke
```

### Component Diagram

```plantuml
component [splitters] as Comp
Comp --> [abc]
Comp --> [typing]
Comp --> [numpy]
Comp --> [typing]
Comp --> [pydantic]
Comp --> [model_selection]
Comp --> [schemas]
```

## Examples

_Dependent on implementation_

## 3. Class & Method Specifications

# Public Classes

### `Splitter`

## Overview

Base class for a splitter.

Use splitters to split data in sets.
e.g., split between a train/test subsets.

# https://scikit-learn.org/stable/glossary.html#term-CV-splitter

## Attributes

* **`KIND`**

  - **Type**: str

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

## Public Methods

* **`split(self: Any, inputs: schemas.Inputs, targets: schemas.Targets, groups: Index | None) -> TrainTestSplits`**

### Description

Split a dataframe into subsets.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `inputs`

  - **type**: schemas.Inputs

  - **meaning**: model inputs.

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `targets`

  - **type**: schemas.Targets

  - **meaning**: model targets.

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `groups`

  - **type**: Index | None

  - **meaning**: group labels.

  - **valid values**: _Dependent on implementation_

  - **optional?**: Yes

  - **default value**: None

### Output

* **return type**: TrainTestSplits

* **semantic meaning**: TrainTestSplits: iterator over the dataframe train/test splits.

* **possible null values**: _Dependent on implementation_

* **exceptions**: _Dependent on implementation_

### Side Effects

_Dependent on implementation_

### Complexity

Time Complexity: _Dependent on implementation_

Space Complexity: _Dependent on implementation_

### Example

_Dependent on implementation_

* **`get_n_splits(self: Any, inputs: schemas.Inputs, targets: schemas.Targets, groups: Index | None) -> int`**

### Description

Get the number of splits generated.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `inputs`

  - **type**: schemas.Inputs

  - **meaning**: models inputs.

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `targets`

  - **type**: schemas.Targets

  - **meaning**: model targets.

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `groups`

  - **type**: Index | None

  - **meaning**: group labels.

  - **valid values**: _Dependent on implementation_

  - **optional?**: Yes

  - **default value**: None

### Output

* **return type**: int

* **semantic meaning**: int: number of splits generated.

* **possible null values**: _Dependent on implementation_

* **exceptions**: _Dependent on implementation_

### Side Effects

_Dependent on implementation_

### Complexity

Time Complexity: _Dependent on implementation_

Space Complexity: _Dependent on implementation_

### Example

_Dependent on implementation_

### `TrainTestSplitter`

## Overview

Split a dataframe into a train and test set.

## Attributes

* **`KIND`**

  - **Type**: T.Literal[TrainTestSplitter]

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`shuffle`**

  - **Type**: bool

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`test_size`**

  - **Type**: int | float

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`random_state`**

  - **Type**: int

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

## Public Methods

* **`split(self: Any, inputs: schemas.Inputs, targets: schemas.Targets, groups: Index | None) -> TrainTestSplits`**

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

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

* `groups`

  - **type**: Index | None

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: Yes

  - **default value**: None

### Output

* **return type**: TrainTestSplits

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

* **`get_n_splits(self: Any, inputs: schemas.Inputs, targets: schemas.Targets, groups: Index | None) -> int`**

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

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

* `groups`

  - **type**: Index | None

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: Yes

  - **default value**: None

### Output

* **return type**: int

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

### `TimeSeriesSplitter`

## Overview

Split a dataframe into fixed time series subsets.

## Attributes

* **`KIND`**

  - **Type**: T.Literal[TimeSeriesSplitter]

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`gap`**

  - **Type**: int

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`n_splits`**

  - **Type**: int

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`test_size`**

  - **Type**: int | float

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

## Public Methods

* **`split(self: Any, inputs: schemas.Inputs, targets: schemas.Targets, groups: Index | None) -> TrainTestSplits`**

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

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

* `groups`

  - **type**: Index | None

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: Yes

  - **default value**: None

### Output

* **return type**: TrainTestSplits

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

* **`get_n_splits(self: Any, inputs: schemas.Inputs, targets: schemas.Targets, groups: Index | None) -> int`**

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

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

* `groups`

  - **type**: Index | None

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: Yes

  - **default value**: None

### Output

* **return type**: int

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

* [training.py](../../regression_model_template/jobs/training.md)

* [tuning.py](../../regression_model_template/jobs/tuning.md)

* [searchers.py](../../regression_model_template/utils/searchers.md)

* [conftest.py](../../tests/conftest.md)

* [test_training.py](../../tests/jobs/test_training.md)

* [test_tuning.py](../../tests/jobs/test_tuning.md)

* [test_searchers.py](../../tests/utils/test_searchers.md)

* [test_splitters.py](../../tests/utils/test_splitters.md)
