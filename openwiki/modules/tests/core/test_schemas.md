---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: test_schemas"
source_path: "tests/core/test_schemas.py"
description: "No description available."
tags: ["module", "test_schemas"]
timestamp: "2026-08-28T06:13:58Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "3029bb6"
---
# Module Specification: test_schemas

* **Source Reference:** [tests/core/test_schemas.py](../../../../tests/core/test_schemas.py)

# Module Overview

## Purpose

No description available.

## Responsibilities

No description available.

## Dependencies

* `regression_model_template.core.models`

* `regression_model_template.core.schemas`

* `regression_model_template.io.datasets`

# Each File Documentation

## Imported modules

* `regression_model_template.core.models`

* `regression_model_template.core.schemas`

* `regression_model_template.io.datasets`

## Exported functions

* `test_inputs_schema`

* `test_targets_schema`

* `test_outputs_schema`

* `test_shap_values_schema`

* `test_feature_importances_schema`

### Detected Architecture Patterns

Detected roles: DTO

## 2. UML Diagrams

### Class Diagram

_No classes found._

### Sequence Diagram

```plantuml
sequenceDiagram
    test_inputs_schema->>read: invoke
    test_inputs_schema->>check: invoke
    test_targets_schema->>read: invoke
    test_targets_schema->>check: invoke
    test_outputs_schema->>read: invoke
    test_outputs_schema->>check: invoke
    test_shap_values_schema->>explain_samples: invoke
    test_shap_values_schema->>check: invoke
    test_feature_importances_schema->>explain_model: invoke
    test_feature_importances_schema->>check: invoke
```

### Component Diagram

```plantuml
component [test_schemas] as Comp
Comp --> [models]
Comp --> [schemas]
Comp --> [datasets]
```

## 3. Class & Method Specifications

## Standalone Functions

### `test_inputs_schema(inputs_reader: datasets.Reader) -> None`

### Description

No description available.

### Inputs

* `inputs_reader`

  - **type**: datasets.Reader

  - **optional?**: No

### Output

* **return type**: None

### `test_targets_schema(targets_reader: datasets.Reader) -> None`

### Description

No description available.

### Inputs

* `targets_reader`

  - **type**: datasets.Reader

  - **optional?**: No

### Output

* **return type**: None

### `test_outputs_schema(outputs_reader: datasets.Reader) -> None`

### Description

No description available.

### Inputs

* `outputs_reader`

  - **type**: datasets.Reader

  - **optional?**: No

### Output

* **return type**: None

### `test_shap_values_schema(model: models.Model, train_test_sets: tuple[(schemas.Inputs, schemas.Targets, schemas.Inputs, schemas.Targets)]) -> None`

### Description

No description available.

### Inputs

* `model`

  - **type**: models.Model

  - **optional?**: No

* `train_test_sets`

  - **type**: tuple[(schemas.Inputs, schemas.Targets, schemas.Inputs, schemas.Targets)]

  - **optional?**: No

### Output

* **return type**: None

### `test_feature_importances_schema(model: models.Model) -> None`

### Description

No description available.

### Inputs

* `model`

  - **type**: models.Model

  - **optional?**: No

### Output

* **return type**: None

## Used By

_Not used by any other module._
