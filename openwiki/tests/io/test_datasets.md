---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDescription"
type: "concept"
title: "test_datasets Documentation"
description: "Documentation for tests/io/test_datasets.py"
tags: ["module", "test_datasets"]
timestamp: "2026-08-04T05:28:53Z"
generated: "agent:ast-documentation-generator"
verified: "true"
---

# Module: `tests/io/test_datasets.py`

## Overview
**Purpose**: Module providing various functionalities.

**Architecture Role**: Infrastructure

**Dependencies**:
- `pytest`
- `regression_model_template.io`
- `regression_model_template.core`
- `os`

**Exported Symbols**:
- `test_parquet_reader`
- `test_parquet_writer`

## UML Class Diagram
```plantuml
@startuml
@enduml
```

## Call Graph
```plantuml
@startuml
test_parquet_reader --> parametrize
test_parquet_reader --> ParquetReader
test_parquet_reader --> read
test_parquet_reader --> lineage
test_parquet_reader --> set
test_parquet_reader --> set
test_parquet_reader --> len
test_parquet_reader --> len
test_parquet_reader --> input_names
test_parquet_writer --> ParquetWriter
test_parquet_writer --> write
test_parquet_writer --> exists
@enduml
```

## Classes
## Functions
### Function `test_parquet_reader`
- **Description**: No description available.
- **Inputs**:
  - `limit`: int | None
  - `inputs_path`: str
- **Output**: `None`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `test_parquet_writer`
- **Description**: No description available.
- **Inputs**:
  - `targets`: schemas.Targets
  - `tmp_outputs_path`: str
- **Output**: `None`
- **Side Effects**: Not documented
- **Complexity**: Not documented
