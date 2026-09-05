---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: datasets"
source_path: "src/regression_model_template/io/datasets.py"
description: "Read/Write datasets from/to external sources/destinations."
tags: ["module", "datasets"]
timestamp: "2026-09-05T05:14:18Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "4860b15"
---
# Module Specification: datasets

* **Source Reference:** [src/regression_model_template/io/datasets.py](../../../../src/regression_model_template/io/datasets.py)

# Module Overview

## Purpose

Read/Write datasets from/to external sources/destinations.

## Responsibilities

Read/Write datasets from/to external sources/destinations.

## Dependencies

* `abc`

* `typing`

* `mlflow.data.pandas_dataset`

* `pandas`

* `pydantic`

# Each File Documentation

## Imported modules

* `abc`

* `typing`

* `mlflow.data.pandas_dataset`

* `pandas`

* `pydantic`

## Exported classes

* `Reader`

* `ParquetReader`

* `Writer`

* `ParquetWriter`

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
    class Reader {
        +KIND: str
        +limit: int | None
        +read(self: Any) pd.DataFrame
        +lineage(self: Any, name: str, data: pd.DataFrame, targets: str | None, predictions: str | None) Lineage
    }
    ABC <|-- Reader : Generalization
    BaseModel <|-- Reader : Generalization
    class ParquetReader {
        +KIND: T.Literal~ParquetReader~
        +path: str
        +read(self: Any) pd.DataFrame
        +lineage(self: Any, name: str, data: pd.DataFrame, targets: str | None, predictions: str | None) Lineage
    }
    Reader <|-- ParquetReader : Generalization
    class Writer {
        +KIND: str
        +write(self: Any, data: pd.DataFrame) None
    }
    ABC <|-- Writer : Generalization
    BaseModel <|-- Writer : Generalization
    class ParquetWriter {
        +KIND: T.Literal~ParquetWriter~
        +path: str
        +write(self: Any, data: pd.DataFrame) None
    }
    Writer <|-- ParquetWriter : Generalization
```

### Sequence Diagram

```plantuml
sequenceDiagram
    ParquetReader.read->>read_parquet: invoke
    ParquetReader.read->>head: invoke
    ParquetReader.lineage->>from_pandas: invoke
    ParquetWriter.write->>to_parquet: invoke
```

### Component Diagram

```plantuml
component [datasets] as Comp
Comp --> [abc]
Comp --> [typing]
Comp --> [pandas_dataset]
Comp --> [pandas]
Comp --> [pydantic]
```

## 3. Class & Method Specifications

# Public Classes

### `Reader`

## Overview

Base class for a dataset reader.

Use a reader to load a dataset in memory.
e.g., to read file, database, cloud storage, ...

Parameters:
    limit (int, optional): maximum number of rows to read. Defaults to None.

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

## Attributes

* **`KIND`**

  - **Type**: str

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`limit`**

  - **Type**: int | None

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

## Public Methods

### `read(self: Any) -> pd.DataFrame`

### Description

Read a dataframe from a dataset.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: pd.DataFrame

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for read

```

### `lineage(self: Any, name: str, data: pd.DataFrame, targets: str | None, predictions: str | None) -> Lineage`

### Description

Generate lineage information.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `name`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `data`

  - **type**: pd.DataFrame

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `targets`

  - **type**: str | None

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: Yes

  - **default value**: None

* `predictions`

  - **type**: str | None

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: Yes

  - **default value**: None

### Output

* **return type**: Lineage

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for lineage

```

### `ParquetReader`

## Overview

Read a dataframe from a parquet file.

Parameters:
    path (str): local path to the dataset.

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

## Attributes

* **`KIND`**

  - **Type**: T.Literal[ParquetReader]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`path`**

  - **Type**: str

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

## Public Methods

### `read(self: Any) -> pd.DataFrame`

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: pd.DataFrame

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for read

```

### `lineage(self: Any, name: str, data: pd.DataFrame, targets: str | None, predictions: str | None) -> Lineage`

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `name`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `data`

  - **type**: pd.DataFrame

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `targets`

  - **type**: str | None

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: Yes

  - **default value**: None

* `predictions`

  - **type**: str | None

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: Yes

  - **default value**: None

### Output

* **return type**: Lineage

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for lineage

```

### `Writer`

## Overview

Base class for a dataset writer.

Use a writer to save a dataset from memory.
e.g., to write file, database, cloud storage, ...

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

## Attributes

* **`KIND`**

  - **Type**: str

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

## Public Methods

### `write(self: Any, data: pd.DataFrame) -> None`

### Description

Write a dataframe to a dataset.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `data`

  - **type**: pd.DataFrame

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: None

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for write

```

### `ParquetWriter`

## Overview

Writer a dataframe to a parquet file.

Parameters:
    path (str): local or S3 path to the dataset.

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

## Attributes

* **`KIND`**

  - **Type**: T.Literal[ParquetWriter]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`path`**

  - **Type**: str

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

## Public Methods

### `write(self: Any, data: pd.DataFrame) -> None`

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `data`

  - **type**: pd.DataFrame

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: None

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for write

```

## Used By

* [evaluations.py](../../regression_model_template/jobs/evaluations.md)

* [explanations.py](../../regression_model_template/jobs/explanations.md)

* [inference.py](../../regression_model_template/jobs/inference.md)

* [training.py](../../regression_model_template/jobs/training.md)

* [tuning.py](../../regression_model_template/jobs/tuning.md)

* [conftest.py](../../tests/conftest.md)

* [test_schemas.py](../../tests/core/test_schemas.md)

* [test_datasets.py](../../tests/io/test_datasets.md)

* [test_evaluations.py](../../tests/jobs/test_evaluations.md)

* [test_explanations.py](../../tests/jobs/test_explanations.md)

* [test_inference.py](../../tests/jobs/test_inference.md)

* [test_training.py](../../tests/jobs/test_training.md)

* [test_tuning.py](../../tests/jobs/test_tuning.md)
