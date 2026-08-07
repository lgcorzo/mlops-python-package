---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: signers"
source_path: "src/regression_model_template/utils/signers.py"
description: "Generate signatures for AI/ML models."
tags: ["module", "signers"]
timestamp: "2026-08-07T08:29:41Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "12aa8d5"
---
# Module Specification: signers

* **Source Reference:** [src/regression_model_template/utils/signers.py](../../../src/regression_model_template/utils/signers.py)

## 1. Architectural Role & Responsibilities
Generate signatures for AI/ML models.

## 2. UML 2.0 Class Diagram
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
