---
type: "module-architecture"
title: "datasets"
description: "Technical architecture and class hierarchy for datasets"
tags: ["architecture", "uml", "pyreverse", "openwiki"]
timestamp: "2026-07-30T19:10:46Z"
---

# Module Name: datasets

Source File: `src/regression_model_template/io/datasets.py`
* **Source Directory Reference:** `src/regression_model_template/io/`
* **Package Dependency:** Upstream: `pydantic`, `pandas`, `abc`, `typing`, `mlflow.data.pandas_dataset` | Downstream: None

## 1. Executive Summary & Purpose
Deterministic architectural model extracted via AST parsing for module `datasets`.

## 2. UML 2.0 Class & Inheritance Architecture (Deterministic)
The following class diagram models the object-oriented structure, explicit inheritance hierarchies, and polymorphic interface implementations derived from local AST analysis:

```mermaid
classDiagram
    class Reader {
        +KIND
        +limit
        +read() : Any
        +lineage(name, data, targets, predictions) : Lineage
    }
    class ParquetReader {
        +KIND
        +path
        +read() : Any
        +lineage(name, data, targets, predictions) : Lineage
    }
    Reader <|-- ParquetReader
    class Writer {
        +KIND
        +write(data) : None
    }
    class ParquetWriter {
        +KIND
        +path
        +write(data) : None
    }
    Writer <|-- ParquetWriter
```

## 3. Package & Class Relations

The following diagram defines the package boundaries and directional inter-package dependencies:

```mermaid
classDiagram
    class Reader {
        +KIND
        +limit
        +read() : Any
        +lineage(name, data, targets, predictions) : Lineage
    }
    class ParquetReader {
        +KIND
        +path
        +read() : Any
        +lineage(name, data, targets, predictions) : Lineage
    }
    Reader <|-- ParquetReader
    class Writer {
        +KIND
        +write(data) : None
    }
    class ParquetWriter {
        +KIND
        +path
        +write(data) : None
    }
    Writer <|-- ParquetWriter
```

* **Inheritance & Polymorphism:** Detailed breakdown of abstract base classes, interfaces, and concrete overrides.
* **Dependencies:** How classes within this package collaborate externally.

## 4. Execution Flow & Runtime Behavior

The following sequence diagram outlines the execution lifecycle and message passing during core operations:

```mermaid
sequenceDiagram
    autonumber
    participant Caller as Client Interface
    participant Reader as Reader
    Caller->>Reader: read()
    Note over Reader: Execution of read
    Reader-->>Caller: Returns status
    participant ParquetReader as ParquetReader
    Caller->>ParquetReader: read()
    Note over ParquetReader: Execution of read
    ParquetReader->>ParquetReader: internal read_parquet()
    ParquetReader->>ParquetReader: internal head()
    ParquetReader-->>Caller: Returns status
    participant Writer as Writer
    Caller->>Writer: write()
    Note over Writer: Execution of write
    Writer-->>Caller: Returns status
    participant ParquetWriter as ParquetWriter
    Caller->>ParquetWriter: write()
    Note over ParquetWriter: Execution of write
    ParquetWriter->>ParquetWriter: internal to_parquet()
    ParquetWriter-->>Caller: Returns status
```

---

* **Source Citations:**
  - Class `Reader`: `src/regression_model_template/io/datasets.py:19`
  - Method `read`: `src/regression_model_template/io/datasets.py:34`
  - Method `lineage`: `src/regression_model_template/io/datasets.py:42`
  - Class `ParquetReader`: `src/regression_model_template/io/datasets.py:62`
  - Method `read`: `src/regression_model_template/io/datasets.py:73`
  - Method `lineage`: `src/regression_model_template/io/datasets.py:80`
  - Class `Writer`: `src/regression_model_template/io/datasets.py:95`
  - Method `write`: `src/regression_model_template/io/datasets.py:105`
  - Class `ParquetWriter`: `src/regression_model_template/io/datasets.py:113`
  - Method `write`: `src/regression_model_template/io/datasets.py:124`

```mermaid
flowchart TD
    datasets --> abc
    datasets --> mlflow
    datasets --> pandas
    datasets --> pydantic
    datasets --> typing
```
