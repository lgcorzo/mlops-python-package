---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: Model Registry Promotion Job"
source_path: "src/regression_model_template/jobs/promotion.py"
description: "Model registry promotion job comparing candidate metrics against production models and transitioning stages in MLflow Registry."
tags: ["jobs", "promotion", "mlflow", "registry", "staging", "production"]
last_verified_commit: "HEAD"
timestamp: "2026-07-31T16:17:00Z"
---

# Module Specification: Model Registry Promotion Job

* **Source File Reference:** `src/regression_model_template/jobs/promotion.py` (Lines: L12-L57)
* **Upstream Dependencies:** [[Modules/RegressionModelTemplate/Jobs/Base]], [[Modules/RegressionModelTemplate/IO/Registries]]
* **Downstream Consumers:** [[Modules/RegressionModelTemplate/Scripts]]

## 1. Architectural Role & Responsibilities
`PromotionJob` compares candidate model metric evaluation scores against existing `Production` models. If candidate performance passes threshold criteria, transitions model stage from `Staging` to `Production` in MLflow Registry (`MlflowRegister`).

## 2. Class & Method Specifications

### `PromotionJob` (`src/regression_model_template/jobs/promotion.py:L12-L57`)
* `run(self)` (L27-L57): Executes automated model promotion check and updates MLflow Model Registry stages.
