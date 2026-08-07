---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: datasets"
source_path: "src/regression_model_template/io/datasets.py"
description: "Read/Write datasets from/to external sources/destinations."
tags: ["module", "datasets"]
timestamp: "2026-08-07T08:29:41Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "12aa8d5"
---
# Module Specification: datasets

* **Source Reference:** [src/regression_model_template/io/datasets.py](../../../src/regression_model_template/io/datasets.py)

## 1. Architectural Role & Responsibilities
Read/Write datasets from/to external sources/destinations.

## 2. UML 2.0 Class Diagram
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
