---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: test_datasets"
source_path: "tests/io/test_datasets.py"
description: "No description available."
tags: ["module", "test_datasets"]
timestamp: "2026-09-05T11:29:30Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "4860b15"
---
# Module Specification: test_datasets

* **Source Reference:** [tests/io/test_datasets.py](../../../../tests/io/test_datasets.py)

# Module Overview

## Purpose

No description available.

## Responsibilities

No description available.

## Dependencies

* `os`

* `pytest`

* `regression_model_template.core.schemas`

* `regression_model_template.io.datasets`

# Each File Documentation

## Imported modules

* `os`

* `pytest`

* `regression_model_template.core.schemas`

* `regression_model_template.io.datasets`

## Exported functions

* `test_parquet_reader`

* `test_parquet_writer`

### Detected Architecture Patterns

Detected roles: General Subsystem

## 2. UML Diagrams

### Class Diagram

_No classes found._

### Sequence Diagram

```plantuml
sequenceDiagram
    test_parquet_reader->>parametrize: invoke
    test_parquet_reader->>ParquetReader: invoke
    test_parquet_reader->>read: invoke
    test_parquet_reader->>lineage: invoke
    test_parquet_reader->>set: invoke
    test_parquet_reader->>len: invoke
    test_parquet_reader->>input_names: invoke
    test_parquet_writer->>ParquetWriter: invoke
    test_parquet_writer->>write: invoke
    test_parquet_writer->>exists: invoke
```

### Component Diagram

```plantuml
component [test_datasets] as Comp
Comp --> [os]
Comp --> [pytest]
Comp --> [schemas]
Comp --> [datasets]
```

## 3. Class & Method Specifications

## Standalone Functions

### `test_parquet_reader(limit: int | None, inputs_path: str) -> None`

### Description

No description available.

### Inputs

* `limit`

  - **type**: int | None

  - **optional?**: No

* `inputs_path`

  - **type**: str

  - **optional?**: No

### Output

* **return type**: None

### `test_parquet_writer(targets: schemas.Targets, tmp_outputs_path: str) -> None`

### Description

No description available.

### Inputs

* `targets`

  - **type**: schemas.Targets

  - **optional?**: No

* `tmp_outputs_path`

  - **type**: str

  - **optional?**: No

### Output

* **return type**: None

## Used By

_Not used by any other module._
