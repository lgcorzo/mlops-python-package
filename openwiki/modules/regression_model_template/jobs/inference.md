---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: Batch & Online Inference Job"
source_path: "src/regression_model_template/jobs/inference.py"
description: "Batch inference job loading production models, executing predictions, and persisting output Parquet files."
tags: ["jobs", "inference", "prediction", "batch", "parquet"]
last_verified_commit: "HEAD"
timestamp: "2026-07-31T16:17:00Z"
---

# Module Specification: Batch & Online Inference Job

* **Source File Reference:** `src/regression_model_template/jobs/inference.py` (Lines: L17-L66)
* **Upstream Dependencies:** [[Modules/RegressionModelTemplate/Jobs/Base]], [[Modules/RegressionModelTemplate/IO/Registries]], [[Modules/RegressionModelTemplate/IO/Datasets]]
* **Downstream Consumers:** [[Modules/RegressionModelTemplate/Scripts]]

## 1. Architectural Role & Responsibilities
`InferenceJob` loads active production model (`CustomLoader`), processes batch input datasets (`ParquetReader`), runs vector predictions, and writes output Parquet predictions (`ParquetWriter`).

## 2. Class & Method Specifications

### `InferenceJob` (`src/regression_model_template/jobs/inference.py:L17-L66`)
* `run(self)` (L38-L66): Executes batch inference workflow on target dataset inputs.
