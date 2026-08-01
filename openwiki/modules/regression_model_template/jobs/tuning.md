---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: Hyperparameter Tuning Job"
source_path: "[src/regression_model_template/jobs/tuning.py](/src/regression_model_template/jobs/tuning.py)"
description: "Hyperparameter search optimization pipeline job running GridSearch / RandomSearch CV."
tags: ["jobs", "tuning", "gridsearch", "hyperparameters", "cv"]
last_verified_commit: "HEAD"
timestamp: "2026-07-31T16:17:00Z"
generated: "agent:okf-professional-documenter"
verified: "true"
---

# Module Specification: Hyperparameter Tuning Job

* **Source File Reference:** [`src/regression_model_template/jobs/tuning.py`](/src/regression_model_template/jobs/tuning.py) (Lines: L18-L104)
* **Upstream Dependencies:** [Modules/RegressionModelTemplate/Jobs/Base](base.md), [Modules/RegressionModelTemplate/Utils/Searchers](../utils/searchers.md)
* **Downstream Consumers:** [Modules/RegressionModelTemplate/Scripts](../scripts.md)

## 1. Architectural Role & Responsibilities
`TuningJob` executes cross-validation hyperparameter optimization searches (`GridCVSearcher`), finding optimal parameter combinations and logging search trials to MLflow runs.

## 2. UML 2.0 Class Diagram

```mermaid
classDiagram
    direction BT
    class Job {
        <<abstract>>
        +KIND: str
        +run()*
    }
    class TuningJob {
        +KIND: Literal
        +run_config: RunConfig
        +inputs: ReaderKind
        +targets: ReaderKind
        +model: ModelKind
        +metric: MetricKind
        +splitter: SplitterKind
        +searcher: SearcherKind
        +run() base.Locals
    }
    Job <|-- TuningJob : Inheritance
```

## 3. Class & Method Specifications

### `TuningJob` ([`src/regression_model_template/jobs/tuning.py:L18-L104`](/src/regression_model_template/jobs/tuning.py#L18-L104))
* `run(self)` (L54-L104): Executes hyperparameter optimization across grid search spaces, identifying best parameter set and logging performance metrics.
