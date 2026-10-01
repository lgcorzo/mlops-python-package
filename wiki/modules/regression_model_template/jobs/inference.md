---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "regression_model_template::jobs::inference — Batch Prediction Pipeline"
source_path: "src/regression_model_template/jobs/inference.py"
description: "Executes batch predictions on unlabeled inputs with cryptographic signing via InferSigner."
tags: ["iso42010", "okf", "component_view", "inference", "signing"]
timestamp: "2026-10-01T17:50:00Z"
generated: "agent:wiki-iso-documentation-standard"
verified: "true"
last_verified_commit: "073b5fd"
---

# regression_model_template::jobs::inference — Batch Prediction Pipeline

> **Source**: `src/regression_model_template/jobs/inference.py` (Lines: L1-L66)  
> **Layer**: Application  
> **Role**: Loads designated model artifacts from registry, validates inputs against Pandera schemas, produces predictions, and writes cryptographically signed output files.

---

## 1. Class Diagram

```mermaid
classDiagram
    class InferenceJob {
        +str KIND = "InferenceJob"
        +ReaderKind inputs
        +WriterKind outputs
        +str | int alias_or_version
        +LoaderKind loader
        +run() Locals
    }
    InferenceJob --|> Job : implements
```

---

> *Related: [Signers](../utils/signers.md) · [Kafka App](../controller/kafka_app.md)*
