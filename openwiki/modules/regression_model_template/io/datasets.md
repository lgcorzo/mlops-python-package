---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: datasets"
source_path: "src/regression_model_template/io/datasets.py"
description: "Read/Write datasets from/to external sources/destinations."
tags: ["module", "datasets"]
timestamp: "2026-08-28T06:13:58Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "3029bb6"
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

## Attributes

* **`KIND`**

  - **Type**: str

* **`limit`**

  - **Type**: int | None

## Public Methods

* **`read(self: Any) -> pd.DataFrame`**

### Description

Read a dataframe from a dataset.

### Inputs

* `self`

  - **type**: Any

  - **optional?**: No

### Output

* **return type**: pd.DataFrame

* **`lineage(self: Any, name: str, data: pd.DataFrame, targets: str | None, predictions: str | None) -> Lineage`**

### Description

Generate lineage information.

### Inputs

* `self`

  - **type**: Any

  - **optional?**: No

* `name`

  - **type**: str

  - **optional?**: No

* `data`

  - **type**: pd.DataFrame

  - **optional?**: No

* `targets`

  - **type**: str | None

  - **optional?**: Yes

  - **default value**: None

* `predictions`

  - **type**: str | None

  - **optional?**: Yes

  - **default value**: None

### Output

* **return type**: Lineage

### `ParquetReader`

## Overview

Read a dataframe from a parquet file.

Parameters:
    path (str): local path to the dataset.

## Attributes

* **`KIND`**

  - **Type**: T.Literal[ParquetReader]

* **`path`**

  - **Type**: str

## Public Methods

* **`read(self: Any) -> pd.DataFrame`**

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **optional?**: No

### Output

* **return type**: pd.DataFrame

* **`lineage(self: Any, name: str, data: pd.DataFrame, targets: str | None, predictions: str | None) -> Lineage`**

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **optional?**: No

* `name`

  - **type**: str

  - **optional?**: No

* `data`

  - **type**: pd.DataFrame

  - **optional?**: No

* `targets`

  - **type**: str | None

  - **optional?**: Yes

  - **default value**: None

* `predictions`

  - **type**: str | None

  - **optional?**: Yes

  - **default value**: None

### Output

* **return type**: Lineage

### `Writer`

## Overview

Base class for a dataset writer.

Use a writer to save a dataset from memory.
e.g., to write file, database, cloud storage, ...

## Attributes

* **`KIND`**

  - **Type**: str

## Public Methods

* **`write(self: Any, data: pd.DataFrame) -> None`**

### Description

Write a dataframe to a dataset.

### Inputs

* `self`

  - **type**: Any

  - **optional?**: No

* `data`

  - **type**: pd.DataFrame

  - **optional?**: No

### Output

* **return type**: None

### `ParquetWriter`

## Overview

Writer a dataframe to a parquet file.

Parameters:
    path (str): local or S3 path to the dataset.

## Attributes

* **`KIND`**

  - **Type**: T.Literal[ParquetWriter]

* **`path`**

  - **Type**: str

## Public Methods

* **`write(self: Any, data: pd.DataFrame) -> None`**

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **optional?**: No

* `data`

  - **type**: pd.DataFrame

  - **optional?**: No

### Output

* **return type**: None

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
