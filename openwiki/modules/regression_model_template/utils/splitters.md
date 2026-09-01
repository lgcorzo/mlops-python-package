---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: splitters"
source_path: "src/regression_model_template/utils/splitters.py"
description: "Split dataframes into subsets (e.g., train/valid/test)."
tags: ["module", "splitters"]
timestamp: "2026-09-01T16:59:35Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "193029c"
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

## Public Methods

* **`split(self: Any, inputs: schemas.Inputs, targets: schemas.Targets, groups: Index | None) -> TrainTestSplits`**

### Description

Split a dataframe into subsets.

### Inputs

* `self`

  - **type**: Any

  - **optional?**: No

* `inputs`

  - **type**: schemas.Inputs

  - **optional?**: No

* `targets`

  - **type**: schemas.Targets

  - **optional?**: No

* `groups`

  - **type**: Index | None

  - **optional?**: Yes

  - **default value**: None

### Output

* **return type**: TrainTestSplits

* **`get_n_splits(self: Any, inputs: schemas.Inputs, targets: schemas.Targets, groups: Index | None) -> int`**

### Description

Get the number of splits generated.

### Inputs

* `self`

  - **type**: Any

  - **optional?**: No

* `inputs`

  - **type**: schemas.Inputs

  - **optional?**: No

* `targets`

  - **type**: schemas.Targets

  - **optional?**: No

* `groups`

  - **type**: Index | None

  - **optional?**: Yes

  - **default value**: None

### Output

* **return type**: int

### `TrainTestSplitter`

## Overview

Split a dataframe into a train and test set.

Parameters:
    shuffle (bool): shuffle the dataset. Default is False.
    test_size (int | float): number/ratio for the test set.
    random_state (int): random state for the splitter object.

## Attributes

* **`KIND`**

  - **Type**: T.Literal[TrainTestSplitter]

* **`shuffle`**

  - **Type**: bool

* **`test_size`**

  - **Type**: int | float

* **`random_state`**

  - **Type**: int

## Public Methods

* **`split(self: Any, inputs: schemas.Inputs, targets: schemas.Targets, groups: Index | None) -> TrainTestSplits`**

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **optional?**: No

* `inputs`

  - **type**: schemas.Inputs

  - **optional?**: No

* `targets`

  - **type**: schemas.Targets

  - **optional?**: No

* `groups`

  - **type**: Index | None

  - **optional?**: Yes

  - **default value**: None

### Output

* **return type**: TrainTestSplits

* **`get_n_splits(self: Any, inputs: schemas.Inputs, targets: schemas.Targets, groups: Index | None) -> int`**

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **optional?**: No

* `inputs`

  - **type**: schemas.Inputs

  - **optional?**: No

* `targets`

  - **type**: schemas.Targets

  - **optional?**: No

* `groups`

  - **type**: Index | None

  - **optional?**: Yes

  - **default value**: None

### Output

* **return type**: int

### `TimeSeriesSplitter`

## Overview

Split a dataframe into fixed time series subsets.

Parameters:
    gap (int): gap between splits.
    n_splits (int): number of split to generate.
    test_size (int | float): number or ratio for the test dataset.

## Attributes

* **`KIND`**

  - **Type**: T.Literal[TimeSeriesSplitter]

* **`gap`**

  - **Type**: int

* **`n_splits`**

  - **Type**: int

* **`test_size`**

  - **Type**: int | float

## Public Methods

* **`split(self: Any, inputs: schemas.Inputs, targets: schemas.Targets, groups: Index | None) -> TrainTestSplits`**

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **optional?**: No

* `inputs`

  - **type**: schemas.Inputs

  - **optional?**: No

* `targets`

  - **type**: schemas.Targets

  - **optional?**: No

* `groups`

  - **type**: Index | None

  - **optional?**: Yes

  - **default value**: None

### Output

* **return type**: TrainTestSplits

* **`get_n_splits(self: Any, inputs: schemas.Inputs, targets: schemas.Targets, groups: Index | None) -> int`**

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **optional?**: No

* `inputs`

  - **type**: schemas.Inputs

  - **optional?**: No

* `targets`

  - **type**: schemas.Targets

  - **optional?**: No

* `groups`

  - **type**: Index | None

  - **optional?**: Yes

  - **default value**: None

### Output

* **return type**: int

## Used By

* [training.py](../../regression_model_template/jobs/training.md)

* [tuning.py](../../regression_model_template/jobs/tuning.md)

* [searchers.py](../../regression_model_template/utils/searchers.md)

* [conftest.py](../../tests/conftest.md)

* [test_training.py](../../tests/jobs/test_training.md)

* [test_tuning.py](../../tests/jobs/test_tuning.md)

* [test_searchers.py](../../tests/utils/test_searchers.md)

* [test_splitters.py](../../tests/utils/test_splitters.md)
