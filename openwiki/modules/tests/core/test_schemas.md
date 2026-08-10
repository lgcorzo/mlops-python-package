---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: test_schemas"
source_path: "tests/core/test_schemas.py"
description: "No description available."
tags: ["module", "test_schemas"]
timestamp: "2026-08-10T08:55:52Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "8412d40"
---
# Module Specification: test_schemas

* **Source Reference:** [tests/core/test_schemas.py](../../../../tests/core/test_schemas.py)

## 1. Architectural Role & Responsibilities
No description available.

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
    test_feature_importances_schema->>check: invoke
    test_feature_importances_schema->>explain_model: invoke
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
No description available.

#### Inputs
* `inputs_reader` (`datasets.Reader`)

#### Outputs
* `None`

### `test_targets_schema(targets_reader: datasets.Reader) -> None`
No description available.

#### Inputs
* `targets_reader` (`datasets.Reader`)

#### Outputs
* `None`

### `test_outputs_schema(outputs_reader: datasets.Reader) -> None`
No description available.

#### Inputs
* `outputs_reader` (`datasets.Reader`)

#### Outputs
* `None`

### `test_shap_values_schema(model: models.Model, train_test_sets: tuple[(schemas.Inputs, schemas.Targets, schemas.Inputs, schemas.Targets)]) -> None`
No description available.

#### Inputs
* `model` (`models.Model`)
* `train_test_sets` (`tuple[(schemas.Inputs, schemas.Targets, schemas.Inputs, schemas.Targets)]`)

#### Outputs
* `None`

### `test_feature_importances_schema(model: models.Model) -> None`
No description available.

#### Inputs
* `model` (`models.Model`)

#### Outputs
* `None`

## Dependencies

* `regression_model_template.core.models`
* `regression_model_template.core.schemas`
* `regression_model_template.io.datasets`

## Used By

_Not used by any other module._
