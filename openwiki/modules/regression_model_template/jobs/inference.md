---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: Batch & Online Inference Job"
source_path: "[src/regression_model_template/jobs/inference.py](/src/regression_model_template/jobs/inference.py)"
description: "Batch inference job loading production models, executing predictions, and persisting output Parquet files."
tags: ["jobs", "inference", "prediction", "batch", "parquet"]
last_verified_commit: "HEAD"
timestamp: "2026-07-31T16:17:00Z"
generated: "agent:okf-professional-documenter"
verified: "true"
---

# Module Specification: Batch & Online Inference Job

* **Source File Reference:** [`src/regression_model_template/jobs/inference.py`](/src/regression_model_template/jobs/inference.py) (Lines: L17-L66)
* **Upstream Dependencies:** [Modules/RegressionModelTemplate/Jobs/Base](base.md), [Modules/RegressionModelTemplate/IO/Registries](../io/registries.md), [Modules/RegressionModelTemplate/IO/Datasets](../io/datasets.md)
* **Downstream Consumers:** [Modules/RegressionModelTemplate/Scripts](../scripts.md)

## 1. Architectural Role & Responsibilities
`InferenceJob` loads active production model (`CustomLoader`), processes batch input datasets (`ParquetReader`), runs vector predictions, and writes output Parquet predictions (`ParquetWriter`).

## 2. UML 2.0 Class Diagram

```mermaid
classDiagram
    direction BT
    class Job {
        <<abstract>>
        +KIND: str
        +run()*
    }
    class InferenceJob {
        +KIND: Literal
        +inputs: ReaderKind
        +outputs: WriterKind
        +alias_or_version: str | int
        +loader: LoaderKind
        +run() base.Locals
    }
    Job <|-- InferenceJob : Inheritance
```

## 3. Class & Method Specifications

### `InferenceJob` ([`src/regression_model_template/jobs/inference.py:L17-L66`](/src/regression_model_template/jobs/inference.py#L17-L66))
* `run(self)` (L38-L66): Executes batch inference workflow on target dataset inputs.
