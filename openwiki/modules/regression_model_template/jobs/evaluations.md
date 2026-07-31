---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: Model Evaluation Job"
source_path: "src/regression_model_template/jobs/evaluations.py"
description: "Standalone model validation job evaluating candidate models against holdout test datasets."
tags: ["jobs", "evaluations", "validation", "metrics", "test"]
last_verified_commit: "HEAD"
timestamp: "2026-07-31T16:17:00Z"
---

# Module Specification: Model Evaluation Job

* **Source File Reference:** `src/regression_model_template/jobs/evaluations.py` (Lines: L19-L125)
* **Upstream Dependencies:** [[Modules/RegressionModelTemplate/Jobs/Base]], [[Modules/RegressionModelTemplate/Core/Metrics]], [[Modules/RegressionModelTemplate/IO/Registries]]
* **Downstream Consumers:** [[Modules/RegressionModelTemplate/Scripts]]

## 1. Architectural Role & Responsibilities
`EvaluationsJob` loads trained model candidates from MLflow Registry (`CustomLoader`), evaluates model predictions against unseen test holdout datasets, and records metric thresholds (`Threshold`).

## 2. Class & Method Specifications

### `EvaluationsJob` (`src/regression_model_template/jobs/evaluations.py:L19-L125`)
* `run(self)` (L50-L125): Loads model, evaluates regression metrics on holdout test set, and updates evaluation report artifacts.
