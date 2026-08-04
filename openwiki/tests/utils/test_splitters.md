---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDescription"
type: "concept"
title: "test_splitters Documentation"
description: "Documentation for tests/utils/test_splitters.py"
tags: ["module", "test_splitters"]
timestamp: "2026-08-04T05:28:53Z"
generated: "agent:ast-documentation-generator"
verified: "true"
---

# Module: `tests/utils/test_splitters.py`

## Overview
**Purpose**: Module providing various functionalities.

**Architecture Role**: Infrastructure

**Dependencies**:
- `regression_model_template.core`
- `regression_model_template.utils`

**Exported Symbols**:
- `test_train_test_splitter`
- `test_time_series_splitter`

## UML Class Diagram
```plantuml
@startuml
@enduml
```

## Call Graph
```plantuml
@startuml
test_train_test_splitter --> TrainTestSplitter
test_train_test_splitter --> get_n_splits
test_train_test_splitter --> list
test_train_test_splitter --> split
test_train_test_splitter --> len
test_train_test_splitter --> len
test_train_test_splitter --> len
test_train_test_splitter --> len
test_time_series_splitter --> TimeSeriesSplitter
test_time_series_splitter --> get_n_splits
test_time_series_splitter --> list
test_time_series_splitter --> enumerate
test_time_series_splitter --> split
test_time_series_splitter --> len
test_time_series_splitter --> len
test_time_series_splitter --> len
test_time_series_splitter --> max
test_time_series_splitter --> min
test_time_series_splitter --> len
@enduml
```

## Classes
## Functions
### Function `test_train_test_splitter`
- **Description**: No description available.
- **Inputs**:
  - `inputs`: schemas.Inputs
  - `targets`: schemas.Targets
- **Output**: `None`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `test_time_series_splitter`
- **Description**: No description available.
- **Inputs**:
  - `inputs`: schemas.Inputs
  - `targets`: schemas.Targets
- **Output**: `None`
- **Side Effects**: Not documented
- **Complexity**: Not documented
