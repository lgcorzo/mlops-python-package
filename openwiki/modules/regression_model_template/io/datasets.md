---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: datasets"
source_path: "src/regression_model_template/io/datasets.py"
description: "Read/Write datasets from/to external sources/destinations."
tags: ["module", "datasets"]
timestamp: "2026-08-21T05:06:05Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "32cdac7"
---
# Module Specification: datasets

* **Source Reference:** [src/regression_model_template/io/datasets.py](../../../../src/regression_model_template/io/datasets.py)

## 1. Architectural Role & Responsibilities

Read/Write datasets from/to external sources/destinations.

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

### `Reader`

Base class for a dataset reader.

Use a reader to load a dataset in memory.
e.g., to read file, database, cloud storage, ...

Parameters:
    limit (int, optional): maximum number of rows to read. Defaults to None.

#### Attributes

* **`KIND`** (`str`)

* **`limit`** (`int | None`)

#### Public Methods

* **`read(self: Any) -> pd.DataFrame`**

  - **Purpose**: Read a dataframe from a dataset.

  - **Inputs**:

    - `self` (`Any`)

  - **Outputs**: `pd.DataFrame`

* **`lineage(self: Any, name: str, data: pd.DataFrame, targets: str | None, predictions: str | None) -> Lineage`**

  - **Purpose**: Generate lineage information.

  - **Inputs**:

    - `self` (`Any`)

    - `name` (`str`)

    - `data` (`pd.DataFrame`)

    - `targets` (`str | None`)

    - `predictions` (`str | None`)

  - **Outputs**: `Lineage`

### `ParquetReader`

Read a dataframe from a parquet file.

Parameters:
    path (str): local path to the dataset.

#### Attributes

* **`KIND`** (`T.Literal[ParquetReader]`)

* **`path`** (`str`)

#### Public Methods

* **`read(self: Any) -> pd.DataFrame`**

  - **Purpose**: No description available.

  - **Inputs**:

    - `self` (`Any`)

  - **Outputs**: `pd.DataFrame`

* **`lineage(self: Any, name: str, data: pd.DataFrame, targets: str | None, predictions: str | None) -> Lineage`**

  - **Purpose**: No description available.

  - **Inputs**:

    - `self` (`Any`)

    - `name` (`str`)

    - `data` (`pd.DataFrame`)

    - `targets` (`str | None`)

    - `predictions` (`str | None`)

  - **Outputs**: `Lineage`

### `Writer`

Base class for a dataset writer.

Use a writer to save a dataset from memory.
e.g., to write file, database, cloud storage, ...

#### Attributes

* **`KIND`** (`str`)

#### Public Methods

* **`write(self: Any, data: pd.DataFrame) -> None`**

  - **Purpose**: Write a dataframe to a dataset.

  - **Inputs**:

    - `self` (`Any`)

    - `data` (`pd.DataFrame`)

  - **Outputs**: `None`

### `ParquetWriter`

Writer a dataframe to a parquet file.

Parameters:
    path (str): local or S3 path to the dataset.

#### Attributes

* **`KIND`** (`T.Literal[ParquetWriter]`)

* **`path`** (`str`)

#### Public Methods

* **`write(self: Any, data: pd.DataFrame) -> None`**

  - **Purpose**: No description available.

  - **Inputs**:

    - `self` (`Any`)

    - `data` (`pd.DataFrame`)

  - **Outputs**: `None`

## Dependencies

* `abc`

* `typing`

* `mlflow.data.pandas_dataset`

* `pandas`

* `pydantic`

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
