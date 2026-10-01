---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "regression_model_template::utils::signers — Cryptographic Attestation"
source_path: "src/regression_model_template/utils/signers.py"
description: "Cryptographic hash signer computing SHA-256 signatures over prediction inputs and outputs."
tags: ["iso42010", "okf", "component_view", "security", "sha256"]
timestamp: "2026-10-01T17:50:00Z"
generated: "agent:wiki-iso-documentation-standard"
verified: "true"
last_verified_commit: "073b5fd"
---

# regression_model_template::utils::signers — Cryptographic Attestation

> **Source**: `src/regression_model_template/utils/signers.py` (Lines: L1-L54)  
> **Layer**: Utilities / Security  
> **Role**: Produces tamper-evident SHA-256 digital signatures over serialized prediction inputs and outputs for compliance auditability.

---

## 1. Class Diagram

```mermaid
classDiagram
    class Signer {
        <<abstract>>
        +str KIND
        +sign(inputs: Inputs, outputs: Outputs) Signature*
    }

    class InferSigner {
        +str KIND = "InferSigner"
        +sign(inputs: Inputs, outputs: Outputs) Signature
    }
    InferSigner --|> Signer : implements
```

---

> *Related: [Security Architecture](../../../security/security_architecture.md) · [Inference Job](../jobs/inference.md)*
