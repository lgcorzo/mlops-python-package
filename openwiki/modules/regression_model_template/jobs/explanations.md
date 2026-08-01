---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: SHAP Explanations Job"
source_path: "[src/regression_model_template/jobs/explanations.py](/src/regression_model_template/jobs/explanations.py)"
description: "Model explainability job generating SHAP global feature importances and sample-level explanations."
tags: ["jobs", "explanations", "shap", "feature_importance", "explainability"]
last_verified_commit: "HEAD"
timestamp: "2026-07-31T16:17:00Z"
generated: "agent:okf-professional-documenter"
verified: "true"
---

# Module Specification: SHAP Explanations Job

* **Source File Reference:** [`src/regression_model_template/jobs/explanations.py`](/src/regression_model_template/jobs/explanations.py) (Lines: L16-L78)
* **Upstream Dependencies:** [Modules/RegressionModelTemplate/Jobs/Base](base.md), [Modules/RegressionModelTemplate/Core/Models](../core/models.md)
* **Downstream Consumers:** [Modules/RegressionModelTemplate/Scripts](../scripts.md)

## 1. Architectural Role & Responsibilities
`ExplanationsJob` invokes SHAP explainers (`explain_model()`, `explain_samples()`), logging global feature importance summary plots and local attribution matrices to MLflow.

## 2. UML 2.0 Class Diagram

```mermaid
classDiagram
    direction BT
    class Job {
        <<abstract>>
        +KIND: str
        +run()*
    }
    class ExplanationsJob {
        +KIND: Literal
        +inputs_samples: ReaderKind
        +models_explanations: WriterKind
        +samples_explanations: WriterKind
        +alias_or_version: str | int
        +loader: LoaderKind
        +run() base.Locals
    }
    Job <|-- ExplanationsJob : Inheritance
```

## 3. Class & Method Specifications

### `ExplanationsJob` ([`src/regression_model_template/jobs/explanations.py:L16-L78`](/src/regression_model_template/jobs/explanations.py#L16-L78))
* `run(self)` (L39-L78): Generates SHAP explanation values for test set samples and logs explainability figures.
