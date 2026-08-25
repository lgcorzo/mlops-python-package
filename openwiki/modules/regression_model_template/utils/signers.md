---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: signers"
source_path: "src/regression_model_template/utils/signers.py"
description: "Generate signatures for AI/ML models."
tags: ["module", "signers"]
timestamp: "2026-08-25T05:40:20Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "74a428a"
---
# Module Specification: signers

* **Source Reference:** [src/regression_model_template/utils/signers.py](../../../../src/regression_model_template/utils/signers.py)

## 1. Architectural Role & Responsibilities

Generate signatures for AI/ML models.

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

## 3. Class & Method Specifications

### `Signer`

Base class for generating model signatures.

Allow to switch between model signing strategies.
e.g., automatic inference, manual model signature, ...

https://mlflow.org/docs/latest/models.html#model-signature-and-input-example

#### Attributes

* **`KIND`** (`str`)

#### Public Methods

* **`sign(self: Any, inputs: schemas.Inputs, outputs: schemas.Outputs) -> Signature`**

  - **Purpose**: Generate a model signature from its inputs/outputs.

  - **Inputs**:

    - `self` (`Any`)

    - `inputs` (`schemas.Inputs`)

    - `outputs` (`schemas.Outputs`)

  - **Outputs**: `Signature`

### `InferSigner`

Generate model signatures from inputs/outputs data.

#### Attributes

* **`KIND`** (`T.Literal[InferSigner]`)

#### Public Methods

* **`sign(self: Any, inputs: schemas.Inputs, outputs: schemas.Outputs) -> Signature`**

  - **Purpose**: No description available.

  - **Inputs**:

    - `self` (`Any`)

    - `inputs` (`schemas.Inputs`)

    - `outputs` (`schemas.Outputs`)

  - **Outputs**: `Signature`

## Dependencies

* `abc`

* `typing`

* `mlflow`

* `pydantic`

* `mlflow.models.signature`

* `regression_model_template.core.schemas`

## Used By

* [registries.py](../../regression_model_template/io/registries.md)

* [training.py](../../regression_model_template/jobs/training.md)

* [conftest.py](../../tests/conftest.md)

* [test_registries.py](../../tests/io/test_registries.md)

* [test_training.py](../../tests/jobs/test_training.md)

* [test_signers.py](../../tests/utils/test_signers.md)
