---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: Model Signers"
source_path: "src/regression_model_template/utils/signers.py"
description: "Model signature inference utilities extracting MLflow schema signatures from inputs and outputs."
tags: ["utils", "signers", "mlflow", "signature"]
last_verified_commit: "HEAD"
timestamp: "2026-07-31T16:17:00Z"
---

# Module Specification: Model Signers

* **Source File Reference:** `src/regression_model_template/utils/signers.py` (Lines: L21-L51)
* **Upstream Dependencies:** `mlflow`
* **Downstream Consumers:** [[Modules/RegressionModelTemplate/Jobs/Training]], [[Modules/RegressionModelTemplate/IO/Registries]]

## 1. Architectural Role & Responsibilities
`signers.py` defines `Signer` base class and `InferSigner`. Infers MLflow Model Signature objects (`infer_signature`) defining input feature names, column data types, and output shapes.

## 2. Class Specifications

### `Signer` (`src/regression_model_template/utils/signers.py:L21-L42`)
* `sign(self, inputs, outputs)` (L33-L42): Abstract signature generation method.

### `InferSigner` (`src/regression_model_template/utils/signers.py:L45-L51`)
* `sign(self, inputs, outputs)` (L50-L51): Generates MLflow signature from sample inputs and outputs.
