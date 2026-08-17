---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: splitters"
source_path: "src/regression_model_template/utils/splitters.py"
description: "Split dataframes into subsets (e.g., train/valid/test)."
tags: ["module", "splitters"]
timestamp: "2026-08-17T05:34:56Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "73b4d7b"
---
# Module Specification: splitters

* **Source Reference:** [src/regression_model_template/utils/splitters.py](../../../../src/regression_model_template/utils/splitters.py)

## 1. Architectural Role & Responsibilities

Split dataframes into subsets (e.g., train/valid/test).

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

### `Splitter`


Base class for a splitter.

Use splitters to split data in sets.
e.g., split between a train/test subsets.

# https://scikit-learn.org/stable/glossary.html#term-CV-splitter

#### Attributes

* **`KIND`** (`str`)

#### Public Methods

* **`split(self: Any, inputs: schemas.Inputs, targets: schemas.Targets, groups: Index | None) -> TrainTestSplits`**

  - **Purpose**: Split a dataframe into subsets.

  - **Inputs**:

    - `self` (`Any`)

    - `inputs` (`schemas.Inputs`)

    - `targets` (`schemas.Targets`)

    - `groups` (`Index | None`)

  - **Outputs**: `TrainTestSplits`

* **`get_n_splits(self: Any, inputs: schemas.Inputs, targets: schemas.Targets, groups: Index | None) -> int`**

  - **Purpose**: Get the number of splits generated.

  - **Inputs**:

    - `self` (`Any`)

    - `inputs` (`schemas.Inputs`)

    - `targets` (`schemas.Targets`)

    - `groups` (`Index | None`)

  - **Outputs**: `int`

### `TrainTestSplitter`


Split a dataframe into a train and test set.

Parameters:
    shuffle (bool): shuffle the dataset. Default is False.
    test_size (int | float): number/ratio for the test set.
    random_state (int): random state for the splitter object.

#### Attributes

* **`KIND`** (`T.Literal[TrainTestSplitter]`)

* **`shuffle`** (`bool`)

* **`test_size`** (`int | float`)

* **`random_state`** (`int`)

#### Public Methods

* **`split(self: Any, inputs: schemas.Inputs, targets: schemas.Targets, groups: Index | None) -> TrainTestSplits`**

  - **Purpose**: No description available.

  - **Inputs**:

    - `self` (`Any`)

    - `inputs` (`schemas.Inputs`)

    - `targets` (`schemas.Targets`)

    - `groups` (`Index | None`)

  - **Outputs**: `TrainTestSplits`

* **`get_n_splits(self: Any, inputs: schemas.Inputs, targets: schemas.Targets, groups: Index | None) -> int`**

  - **Purpose**: No description available.

  - **Inputs**:

    - `self` (`Any`)

    - `inputs` (`schemas.Inputs`)

    - `targets` (`schemas.Targets`)

    - `groups` (`Index | None`)

  - **Outputs**: `int`

### `TimeSeriesSplitter`


Split a dataframe into fixed time series subsets.

Parameters:
    gap (int): gap between splits.
    n_splits (int): number of split to generate.
    test_size (int | float): number or ratio for the test dataset.

#### Attributes

* **`KIND`** (`T.Literal[TimeSeriesSplitter]`)

* **`gap`** (`int`)

* **`n_splits`** (`int`)

* **`test_size`** (`int | float`)

#### Public Methods

* **`split(self: Any, inputs: schemas.Inputs, targets: schemas.Targets, groups: Index | None) -> TrainTestSplits`**

  - **Purpose**: No description available.

  - **Inputs**:

    - `self` (`Any`)

    - `inputs` (`schemas.Inputs`)

    - `targets` (`schemas.Targets`)

    - `groups` (`Index | None`)

  - **Outputs**: `TrainTestSplits`

* **`get_n_splits(self: Any, inputs: schemas.Inputs, targets: schemas.Targets, groups: Index | None) -> int`**

  - **Purpose**: No description available.

  - **Inputs**:

    - `self` (`Any`)

    - `inputs` (`schemas.Inputs`)

    - `targets` (`schemas.Targets`)

    - `groups` (`Index | None`)

  - **Outputs**: `int`

## Dependencies

* `abc`

* `typing`

* `numpy`

* `numpy.typing`

* `pydantic`

* `sklearn.model_selection`

* `regression_model_template.core.schemas`


## Used By

* [training.py](../../regression_model_template/jobs/training.md)

* [tuning.py](../../regression_model_template/jobs/tuning.md)

* [searchers.py](../../regression_model_template/utils/searchers.md)

* [conftest.py](../../tests/conftest.md)

* [test_training.py](../../tests/jobs/test_training.md)

* [test_tuning.py](../../tests/jobs/test_tuning.md)

* [test_searchers.py](../../tests/utils/test_searchers.md)

* [test_splitters.py](../../tests/utils/test_splitters.md)
