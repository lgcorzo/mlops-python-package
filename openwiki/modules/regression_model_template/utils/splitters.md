---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: splitters"
source_path: "src/regression_model_template/utils/splitters.py"
description: "Split dataframes into subsets (e.g., train/valid/test)."
tags: ["module", "splitters"]
timestamp: "2026-09-05T05:14:18Z"
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

_No interfaces found._

## Public API

_See exported classes and functions._

## Internal architecture

_See architectural detected patterns and UML._

## Execution flow

_Execution flow depends on public API usage._

## Sequence explanation

_See sequence diagram._

## UML

_See diagrams below._

## Examples

_No module level examples available._

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

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

## Attributes

* **`KIND`**

  - **Type**: str

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

## Public Methods

### `split(self: Any, inputs: schemas.Inputs, targets: schemas.Targets, groups: Index | None) -> TrainTestSplits`

### Description

Split a dataframe into subsets.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `inputs`

  - **type**: schemas.Inputs

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `targets`

  - **type**: schemas.Targets

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `groups`

  - **type**: Index | None

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: Yes

  - **default value**: None

### Output

* **return type**: TrainTestSplits

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for split

```

### `get_n_splits(self: Any, inputs: schemas.Inputs, targets: schemas.Targets, groups: Index | None) -> int`

### Description

Get the number of splits generated.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `inputs`

  - **type**: schemas.Inputs

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `targets`

  - **type**: schemas.Targets

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `groups`

  - **type**: Index | None

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: Yes

  - **default value**: None

### Output

* **return type**: int

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for get_n_splits

```

### `TrainTestSplitter`

## Overview

Split a dataframe into a train and test set.

Parameters:
    shuffle (bool): shuffle the dataset. Default is False.
    test_size (int | float): number/ratio for the test set.
    random_state (int): random state for the splitter object.

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

## Attributes

* **`KIND`**

  - **Type**: T.Literal[TrainTestSplitter]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`shuffle`**

  - **Type**: bool

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`test_size`**

  - **Type**: int | float

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`random_state`**

  - **Type**: int

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

## Public Methods

### `split(self: Any, inputs: schemas.Inputs, targets: schemas.Targets, groups: Index | None) -> TrainTestSplits`

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `inputs`

  - **type**: schemas.Inputs

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `targets`

  - **type**: schemas.Targets

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `groups`

  - **type**: Index | None

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: Yes

  - **default value**: None

### Output

* **return type**: TrainTestSplits

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for split

```

### `get_n_splits(self: Any, inputs: schemas.Inputs, targets: schemas.Targets, groups: Index | None) -> int`

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `inputs`

  - **type**: schemas.Inputs

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `targets`

  - **type**: schemas.Targets

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `groups`

  - **type**: Index | None

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: Yes

  - **default value**: None

### Output

* **return type**: int

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for get_n_splits

```

### `TimeSeriesSplitter`

## Overview

Split a dataframe into fixed time series subsets.

Parameters:
    gap (int): gap between splits.
    n_splits (int): number of split to generate.
    test_size (int | float): number or ratio for the test dataset.

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

## Attributes

* **`KIND`**

  - **Type**: T.Literal[TimeSeriesSplitter]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`gap`**

  - **Type**: int

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`n_splits`**

  - **Type**: int

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`test_size`**

  - **Type**: int | float

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

## Public Methods

### `split(self: Any, inputs: schemas.Inputs, targets: schemas.Targets, groups: Index | None) -> TrainTestSplits`

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `inputs`

  - **type**: schemas.Inputs

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `targets`

  - **type**: schemas.Targets

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `groups`

  - **type**: Index | None

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: Yes

  - **default value**: None

### Output

* **return type**: TrainTestSplits

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for split

```

### `get_n_splits(self: Any, inputs: schemas.Inputs, targets: schemas.Targets, groups: Index | None) -> int`

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `inputs`

  - **type**: schemas.Inputs

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `targets`

  - **type**: schemas.Targets

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `groups`

  - **type**: Index | None

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: Yes

  - **default value**: None

### Output

* **return type**: int

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for get_n_splits

```

## Used By

* [training.py](../../regression_model_template/jobs/training.md)

* [tuning.py](../../regression_model_template/jobs/tuning.md)

* [searchers.py](../../regression_model_template/utils/searchers.md)

* [conftest.py](../../tests/conftest.md)

* [test_training.py](../../tests/jobs/test_training.md)

* [test_tuning.py](../../tests/jobs/test_tuning.md)

* [test_searchers.py](../../tests/utils/test_searchers.md)

* [test_splitters.py](../../tests/utils/test_splitters.md)
