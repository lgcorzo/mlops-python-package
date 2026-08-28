---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: test_splitters"
source_path: "tests/utils/test_splitters.py"
description: "No description available."
tags: ["module", "test_splitters"]
timestamp: "2026-08-28T06:13:58Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "3029bb6"
---
# Module Specification: test_splitters

* **Source Reference:** [tests/utils/test_splitters.py](../../../../tests/utils/test_splitters.py)

# Module Overview

## Purpose

No description available.

## Responsibilities

No description available.

## Dependencies

* `regression_model_template.core.schemas`

* `regression_model_template.utils.splitters`

# Each File Documentation

## Imported modules

* `regression_model_template.core.schemas`

* `regression_model_template.utils.splitters`

## Exported functions

* `test_train_test_splitter`

* `test_time_series_splitter`

### Detected Architecture Patterns

Detected roles: General Subsystem

## 2. UML Diagrams

### Class Diagram

_No classes found._

### Sequence Diagram

```plantuml
sequenceDiagram
    test_train_test_splitter->>TrainTestSplitter: invoke
    test_train_test_splitter->>get_n_splits: invoke
    test_train_test_splitter->>list: invoke
    test_train_test_splitter->>split: invoke
    test_train_test_splitter->>len: invoke
    test_time_series_splitter->>TimeSeriesSplitter: invoke
    test_time_series_splitter->>get_n_splits: invoke
    test_time_series_splitter->>list: invoke
    test_time_series_splitter->>enumerate: invoke
    test_time_series_splitter->>split: invoke
    test_time_series_splitter->>len: invoke
    test_time_series_splitter->>max: invoke
    test_time_series_splitter->>min: invoke
```

### Component Diagram

```plantuml
component [test_splitters] as Comp
Comp --> [schemas]
Comp --> [splitters]
```

## 3. Class & Method Specifications

## Standalone Functions

### `test_train_test_splitter(inputs: schemas.Inputs, targets: schemas.Targets) -> None`

### Description

No description available.

### Inputs

* `inputs`

  - **type**: schemas.Inputs

  - **optional?**: No

* `targets`

  - **type**: schemas.Targets

  - **optional?**: No

### Output

* **return type**: None

### `test_time_series_splitter(inputs: schemas.Inputs, targets: schemas.Targets) -> None`

### Description

No description available.

### Inputs

* `inputs`

  - **type**: schemas.Inputs

  - **optional?**: No

* `targets`

  - **type**: schemas.Targets

  - **optional?**: No

### Output

* **return type**: None

## Used By

_Not used by any other module._
