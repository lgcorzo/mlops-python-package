---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: test_registries"
source_path: "tests/io/test_registries.py"
description: "No description available."
tags: ["module", "test_registries"]
timestamp: "2026-08-12T05:53:45Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "ce3f2af"
---
# Module Specification: test_registries

* **Source Reference:** [tests/io/test_registries.py](../../../../tests/io/test_registries.py)

## 1. Architectural Role & Responsibilities
No description available.

### Detected Architecture Patterns
Detected roles: General Subsystem

## 2. UML Diagrams
### Class Diagram
_No classes found._

### Sequence Diagram
```plantuml
sequenceDiagram
    test_uri_for_model_alias->>uri_for_model_alias: invoke
    test_uri_for_model_version->>uri_for_model_version: invoke
    test_uri_for_model_alias_or_version->>uri_for_model_alias_or_version: invoke
    test_uri_for_model_alias_or_version->>uri_for_model_alias: invoke
    test_uri_for_model_alias_or_version->>uri_for_model_version: invoke
    test_custom_pipeline->>CustomSaver: invoke
    test_custom_pipeline->>CustomLoader: invoke
    test_custom_pipeline->>MlflowRegister: invoke
    test_custom_pipeline->>RunConfig: invoke
    test_custom_pipeline->>uri_for_model_version: invoke
    test_custom_pipeline->>load: invoke
    test_custom_pipeline->>get: invoke
    test_custom_pipeline->>run_context: invoke
    test_custom_pipeline->>save: invoke
    test_custom_pipeline->>register: invoke
    test_builtin_pipeline->>BuiltinSaver: invoke
    test_builtin_pipeline->>BuiltinLoader: invoke
    test_builtin_pipeline->>MlflowRegister: invoke
    test_builtin_pipeline->>RunConfig: invoke
    test_builtin_pipeline->>uri_for_model_version: invoke
    test_builtin_pipeline->>load: invoke
    test_builtin_pipeline->>predict: invoke
    test_builtin_pipeline->>get: invoke
    test_builtin_pipeline->>run_context: invoke
    test_builtin_pipeline->>save: invoke
    test_builtin_pipeline->>register: invoke
    test_builtin_pipeline->>check: invoke
```

### Component Diagram
```plantuml
component [test_registries] as Comp
Comp --> [models]
Comp --> [schemas]
Comp --> [registries]
Comp --> [services]
Comp --> [signers]
```

## 3. Class & Method Specifications

## Standalone Functions

### `test_uri_for_model_alias() -> None`
No description available.

#### Inputs

#### Outputs
* `None`

### `test_uri_for_model_version() -> None`
No description available.

#### Inputs

#### Outputs
* `None`

### `test_uri_for_model_alias_or_version() -> None`
No description available.

#### Inputs

#### Outputs
* `None`

### `test_custom_pipeline(model: models.Model, inputs: schemas.Inputs, signature: signers.Signature, mlflow_service: services.MlflowService) -> None`
No description available.

#### Inputs
* `model` (`models.Model`)
* `inputs` (`schemas.Inputs`)
* `signature` (`signers.Signature`)
* `mlflow_service` (`services.MlflowService`)

#### Outputs
* `None`

### `test_builtin_pipeline(model: models.Model, inputs: schemas.Inputs, signature: signers.Signature, mlflow_service: services.MlflowService) -> None`
No description available.

#### Inputs
* `model` (`models.Model`)
* `inputs` (`schemas.Inputs`)
* `signature` (`signers.Signature`)
* `mlflow_service` (`services.MlflowService`)

#### Outputs
* `None`

## Dependencies

* `regression_model_template.core.models`
* `regression_model_template.core.schemas`
* `regression_model_template.io.registries`
* `regression_model_template.io.services`
* `regression_model_template.utils.signers`

## Used By

_Not used by any other module._
