---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: signers"
source_path: "src/regression_model_template/utils/signers.py"
description: "Generate signatures for AI/ML models."
tags: ["module", "signers"]
timestamp: "2026-09-06T06:26:18Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "4860b15"
---
# Module Specification: signers

* **Source Reference:** [src/regression_model_template/utils/signers.py](../../../../src/regression_model_template/utils/signers.py)

# Module Overview

## Purpose

Generate signatures for AI/ML models.

## Responsibilities

Generate signatures for AI/ML models.

## Dependencies

* `abc`

* `typing`

* `mlflow`

* `pydantic`

* `mlflow.models.signature`

* `regression_model_template.core.schemas`

# Each File Documentation

## Imported modules

* `abc`

* `typing`

* `mlflow`

* `pydantic`

* `mlflow.models.signature`

* `regression_model_template.core.schemas`

## Exported classes

* `Signer`

* `InferSigner`

## Exported interfaces

_Dependent on implementation_

## Public API

_Dependent on implementation_

## Internal architecture

_Dependent on implementation_

## Execution flow

_Dependent on implementation_

## Sequence explanation

_Dependent on implementation_

### Detected Architecture Patterns

Detected roles: General Subsystem

## 2. UML Diagrams

### Class Diagram

```plantuml
classDiagram
    direction BT
    class Signer {
        +KIND: str
        +sign(self: Any, inputs: schemas.Inputs, outputs: schemas.Outputs) Signature
    }
    ABC <|-- Signer : Generalization
    BaseModel <|-- Signer : Generalization
    class InferSigner {
        +KIND: T.Literal~InferSigner~
        +sign(self: Any, inputs: schemas.Inputs, outputs: schemas.Outputs) Signature
    }
    Signer <|-- InferSigner : Generalization
```

### Sequence Diagram

```plantuml
sequenceDiagram
    InferSigner.sign->>infer_signature: invoke
```

### Component Diagram

```plantuml
component [signers] as Comp
Comp --> [abc]
Comp --> [typing]
Comp --> [mlflow]
Comp --> [pydantic]
Comp --> [signature]
Comp --> [schemas]
```

## Examples

_Dependent on implementation_

## 3. Class & Method Specifications

# Public Classes

### `Signer`

## Overview

Base class for generating model signatures.

Allow to switch between model signing strategies.
e.g., automatic inference, manual model signature, ...

https://mlflow.org/docs/latest/models.html#model-signature-and-input-example

## Attributes

* **`KIND`**

  - **Type**: str

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

## Public Methods

* **`sign(self: Any, inputs: schemas.Inputs, outputs: schemas.Outputs) -> Signature`**

### Description

Generate a model signature from its inputs/outputs.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `inputs`

  - **type**: schemas.Inputs

  - **meaning**: inputs data.

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `outputs`

  - **type**: schemas.Outputs

  - **meaning**: outputs data.

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

### Output

* **return type**: Signature

* **semantic meaning**: Signature: signature of the model.

* **possible null values**: _Dependent on implementation_

* **exceptions**: _Dependent on implementation_

### Side Effects

_Dependent on implementation_

### Complexity

Time Complexity: _Dependent on implementation_

Space Complexity: _Dependent on implementation_

### Example

_Dependent on implementation_

### `InferSigner`

## Overview

Generate model signatures from inputs/outputs data.

## Attributes

* **`KIND`**

  - **Type**: T.Literal[InferSigner]

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

## Public Methods

* **`sign(self: Any, inputs: schemas.Inputs, outputs: schemas.Outputs) -> Signature`**

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `inputs`

  - **type**: schemas.Inputs

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `outputs`

  - **type**: schemas.Outputs

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

### Output

* **return type**: Signature

* **semantic meaning**: _Dependent on implementation_

* **possible null values**: _Dependent on implementation_

* **exceptions**: _Dependent on implementation_

### Side Effects

_Dependent on implementation_

### Complexity

Time Complexity: _Dependent on implementation_

Space Complexity: _Dependent on implementation_

### Example

_Dependent on implementation_

## Used By

* [registries.py](../../regression_model_template/io/registries.md)

* [training.py](../../regression_model_template/jobs/training.md)

* [conftest.py](../../tests/conftest.md)

* [test_registries.py](../../tests/io/test_registries.md)

* [test_training.py](../../tests/jobs/test_training.md)

* [test_signers.py](../../tests/utils/test_signers.md)
