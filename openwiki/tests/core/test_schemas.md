---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDescription"
type: "concept"
title: "test_schemas Documentation"
description: "Documentation for tests/core/test_schemas.py"
tags: ["module", "test_schemas"]
timestamp: "2026-08-04T05:28:53Z"
generated: "agent:ast-documentation-generator"
verified: "true"
---

# Module: `tests/core/test_schemas.py`

## Overview
**Purpose**: Module providing various functionalities.

**Architecture Role**: DTOs

**Dependencies**:
- `regression_model_template.core`
- `regression_model_template.io`

**Exported Symbols**:
- `test_inputs_schema`
- `test_targets_schema`
- `test_outputs_schema`
- `test_shap_values_schema`
- `test_feature_importances_schema`

## UML Class Diagram
```plantuml
@startuml
@enduml
```

## Call Graph
```plantuml
@startuml
test_inputs_schema --> read
test_inputs_schema --> check
test_targets_schema --> read
test_targets_schema --> check
test_outputs_schema --> read
test_outputs_schema --> check
test_shap_values_schema --> explain_samples
test_shap_values_schema --> check
test_feature_importances_schema --> explain_model
test_feature_importances_schema --> check
@enduml
```

## Classes
## Functions
### Function `test_inputs_schema`
- **Description**: No description available.
- **Inputs**:
  - `inputs_reader`: datasets.Reader
- **Output**: `None`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `test_targets_schema`
- **Description**: No description available.
- **Inputs**:
  - `targets_reader`: datasets.Reader
- **Output**: `None`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `test_outputs_schema`
- **Description**: No description available.
- **Inputs**:
  - `outputs_reader`: datasets.Reader
- **Output**: `None`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `test_shap_values_schema`
- **Description**: No description available.
- **Inputs**:
  - `model`: models.Model
  - `train_test_sets`: tuple[schemas.Inputs, schemas.Targets, schemas.Inputs, schemas.Targets]
- **Output**: `None`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `test_feature_importances_schema`
- **Description**: No description available.
- **Inputs**:
  - `model`: models.Model
- **Output**: `None`
- **Side Effects**: Not documented
- **Complexity**: Not documented
