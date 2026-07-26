---
type: script
title: "signers"
source_path: "src/regression_model_template/utils/signers.py"
description: "Generate signatures for AI/ML models."
tags: [script, regression_model_template]
last_verified_commit: "abe2ee0"
---

# signers

Source File: `src/regression_model_template/utils/signers.py`

Generate signatures for AI/ML models.

```mermaid
classDiagram
    class Signer {
        +KIND
        +sign(inputs, outputs)
    }
    Signer <|-- InferSigner
    class InferSigner {
        +KIND
        +sign(inputs, outputs)
    }
```

```mermaid
flowchart TD
    signers --> abc
    signers --> typing
    signers --> mlflow
    signers --> pydantic
    signers --> mlflow_models
    signers --> regression_model_template_core
```
