---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: signers"
source_path: "src/regression_model_template/utils/signers.py"
description: "Generate signatures for AI/ML models."
tags: ["module", "signers"]
timestamp: "2026-09-05T05:14:18Z"
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

_No interfaces found._

## Public API

_See exported classes and functions._

## Internal architecture

_See architectural detected patterns and UML._

## Execution flow

_Execution flow depends on public API usage._

## Sequence explanation

_See sequence diagram._

## UML

_See diagrams below._

## Examples

_No module level examples available._

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

# Public Classes

### `Signer`

## Overview

Base class for generating model signatures.

Allow to switch between model signing strategies.
e.g., automatic inference, manual model signature, ...

https://mlflow.org/docs/latest/models.html#model-signature-and-input-example

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

## Attributes

* **`KIND`**

  - **Type**: str

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

## Public Methods

### `sign(self: Any, inputs: schemas.Inputs, outputs: schemas.Outputs) -> Signature`

### Description

Generate a model signature from its inputs/outputs.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `inputs`

  - **type**: schemas.Inputs

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `outputs`

  - **type**: schemas.Outputs

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: Signature

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for sign

```

### `InferSigner`

## Overview

Generate model signatures from inputs/outputs data.

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

## Attributes

* **`KIND`**

  - **Type**: T.Literal[InferSigner]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

## Public Methods

### `sign(self: Any, inputs: schemas.Inputs, outputs: schemas.Outputs) -> Signature`

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `inputs`

  - **type**: schemas.Inputs

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `outputs`

  - **type**: schemas.Outputs

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: Signature

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for sign

```

## Used By

* [registries.py](../../regression_model_template/io/registries.md)

* [training.py](../../regression_model_template/jobs/training.md)

* [conftest.py](../../tests/conftest.md)

* [test_registries.py](../../tests/io/test_registries.md)

* [test_training.py](../../tests/jobs/test_training.md)

* [test_signers.py](../../tests/utils/test_signers.md)
