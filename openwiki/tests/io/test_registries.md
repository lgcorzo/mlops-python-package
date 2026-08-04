---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDescription"
type: "concept"
title: "test_registries Documentation"
description: "Documentation for tests/io/test_registries.py"
tags: ["module", "test_registries"]
timestamp: "2026-08-04T05:28:53Z"
generated: "agent:ast-documentation-generator"
verified: "true"
---

# Module: `tests/io/test_registries.py`

## Overview
**Purpose**: Module providing various functionalities.

**Architecture Role**: Infrastructure

**Dependencies**:
- `regression_model_template.core`
- `regression_model_template.io`
- `regression_model_template.utils`

**Exported Symbols**:
- `test_uri_for_model_alias`
- `test_uri_for_model_version`
- `test_uri_for_model_alias_or_version`
- `test_custom_pipeline`
- `test_builtin_pipeline`

## UML Class Diagram
```plantuml
@startuml
@enduml
```

## Call Graph
```plantuml
@startuml
test_uri_for_model_alias --> uri_for_model_alias
test_uri_for_model_version --> uri_for_model_version
test_uri_for_model_alias_or_version --> uri_for_model_alias_or_version
test_uri_for_model_alias_or_version --> uri_for_model_alias_or_version
test_uri_for_model_alias_or_version --> uri_for_model_alias
test_uri_for_model_alias_or_version --> uri_for_model_version
test_custom_pipeline --> CustomSaver
test_custom_pipeline --> CustomLoader
test_custom_pipeline --> MlflowRegister
test_custom_pipeline --> RunConfig
test_custom_pipeline --> uri_for_model_version
test_custom_pipeline --> load
test_custom_pipeline --> get
test_custom_pipeline --> run_context
test_custom_pipeline --> save
test_custom_pipeline --> register
test_custom_pipeline --> get
test_builtin_pipeline --> BuiltinSaver
test_builtin_pipeline --> BuiltinLoader
test_builtin_pipeline --> MlflowRegister
test_builtin_pipeline --> RunConfig
test_builtin_pipeline --> uri_for_model_version
test_builtin_pipeline --> load
test_builtin_pipeline --> predict
test_builtin_pipeline --> get
test_builtin_pipeline --> get
test_builtin_pipeline --> get
test_builtin_pipeline --> run_context
test_builtin_pipeline --> save
test_builtin_pipeline --> register
test_builtin_pipeline --> get
test_builtin_pipeline --> check
@enduml
```

## Classes
## Functions
### Function `test_uri_for_model_alias`
- **Description**: No description available.
- **Inputs**:
- **Output**: `None`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `test_uri_for_model_version`
- **Description**: No description available.
- **Inputs**:
- **Output**: `None`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `test_uri_for_model_alias_or_version`
- **Description**: No description available.
- **Inputs**:
- **Output**: `None`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `test_custom_pipeline`
- **Description**: No description available.
- **Inputs**:
  - `model`: models.Model
  - `inputs`: schemas.Inputs
  - `signature`: signers.Signature
  - `mlflow_service`: services.MlflowService
- **Output**: `None`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `test_builtin_pipeline`
- **Description**: No description available.
- **Inputs**:
  - `model`: models.Model
  - `inputs`: schemas.Inputs
  - `signature`: signers.Signature
  - `mlflow_service`: services.MlflowService
- **Output**: `None`
- **Side Effects**: Not documented
- **Complexity**: Not documented
