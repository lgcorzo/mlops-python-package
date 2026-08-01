---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: Model Evaluation Job"
source_path: "[src/regression_model_template/jobs/evaluations.py](/src/regression_model_template/jobs/evaluations.py)"
description: "Standalone model validation job evaluating candidate models against holdout test datasets."
tags: ["jobs", "evaluations", "validation", "metrics", "test"]
last_verified_commit: "HEAD"
timestamp: "2026-07-31T16:17:00Z"
generated: "agent:okf-professional-documenter"
verified: "true"
---

# Module Specification: Model Evaluation Job

* **Source File Reference:** [`src/regression_model_template/jobs/evaluations.py`](/src/regression_model_template/jobs/evaluations.py) (Lines: L19-L125)
* **Upstream Dependencies:** [Modules/RegressionModelTemplate/Jobs/Base](base.md), [Modules/RegressionModelTemplate/Core/Metrics](../core/metrics.md), [Modules/RegressionModelTemplate/IO/Registries](../io/registries.md)
* **Downstream Consumers:** [Modules/RegressionModelTemplate/Scripts](../scripts.md)

## 1. Architectural Role & Responsibilities

`EvaluationsJob` implements model validation workflows. It loads model candidates from the MLflow model registry, executes evaluation suites against unseen datasets, enforces quality gate thresholds, and raises alerts on failures.

## 2. UML 2.0 Class Diagram

```mermaid
classDiagram
    direction BT
    class Job {
        <<abstract>>
        +run_config: RunConfig
        +services: List~Service~
        +__enter__() Job
        +__exit__(exc_type, exc_val, exc_tb)
        +run()*
    }
    class EvaluationsJob {
        +KIND: Literal["EvaluationsJob"]
        +run_config: RunConfig
        +inputs: ReaderKind
        +targets: ReaderKind
        +model_type: str
        +alias_or_version: str | int
        +metrics: MetricsKind
        +evaluators: list~str~
        +thresholds: dict~str, Threshold~
        +run() base.Locals
    }

    Job <|-- EvaluationsJob : Generalization
```

## 3. Execution Workflow Sequence Diagram

```mermaid
sequenceDiagram
    autonumber
    actor User as Developer / CLI
    participant Job as EvaluationsJob
    participant Services as Services Lifecycle
    participant Inputs as ParquetReader (Inputs)
    participant Targets as ParquetReader (Targets)
    participant MLflow as MLflow Service
    participant Alerts as AlertsService

    User->>Job: with EvaluationsJob(...)
    activate Job
    Job->>Services: __enter__()
    activate Services
    Services-->>Job: services active
    deactivate Services
    
    User->>Job: run()
    Job->>MLflow: start run_context()
    activate MLflow
    
    Job->>Inputs: read()
    activate Inputs
    Inputs-->>Job: inputs dataframe
    deactivate Inputs
    Job->>Job: InputsSchema.check(inputs)
    
    Job->>Targets: read()
    activate Targets
    Targets-->>Job: targets dataframe
    deactivate Targets
    Job->>Job: TargetsSchema.check(targets)
    
    Job->>MLflow: log_input(inputs_lineage)
    Job->>MLflow: log_input(targets_lineage)
    
    Job->>MLflow: evaluate(dataset, model_uri, extra_metrics)
    MLflow-->>Job: evaluations result
    
    Job->>MLflow: validate_evaluation_results()
    
    Job->>Alerts: notify("Evaluations Job Finished")
    activate Alerts
    Alerts-->>Job: notified
    deactivate Alerts
    
    MLflow-->>Job: run complete
    deactivate MLflow
    
    Job-->>User: base.Locals
    deactivate Job
    
    User->>Job: __exit__()
    activate Job
    Job->>Services: stop services
    deactivate Job
```

## 4. Class & Method Specifications

### `EvaluationsJob` ([`src/regression_model_template/jobs/evaluations.py:L19-L125`](/src/regression_model_template/jobs/evaluations.py#L19-L125))

#### `run(self) -> base.Locals`
* **Visibility:** Public (`+`)
* **Polymorphism:** Overrides the abstract `run()` method defined in `Job` (polymorphic implementation).
* **Behavior:** Enforces the model evaluation and validation pipeline. Reads dataset inputs/targets, performs validation against schemas, queries candidate models, computes metrics via MLflow, validates metrics against threshold targets, and sends notifications.

##### Input Parameters (Instantiated via Constructor):
| Parameter | Data Type | Required / Default | Semantic Description |
| :--- | :--- | :--- | :--- |
| `run_config` | `services.MlflowService.RunConfig` | Default (`RunConfig(name="Evaluations")`) | Configures MLflow tracking run parameters. |
| `inputs` | `datasets.ReaderKind` | **Required** | Reader configuration for inputs data. |
| `targets` | `datasets.ReaderKind` | **Required** | Reader configuration for targets data. |
| `model_type` | `str` | Default (`"regressor"`) | Targeted ML workload category (e.g. regressor, classifier). |
| `alias_or_version` | `str \| int` | Default (`"Champion"`) | Target model alias or version in MLflow registry. |
| `metrics` | `metrics_.MetricsKind` | Default (`[SklearnMetric()]`) | Metric evaluation suite. |
| `evaluators` | `list[str]` | Default (`["default"]`) | Evaluator engines to execute. |
| `thresholds` | `dict[str, metrics_.Threshold]` | Default (`{"r2_score": Threshold(0.5)}`) | Minimum metric validation thresholds. |

##### Return Value & Output Shape:
| Return Type | Scenario | Description |
| :--- | :--- | :--- |
| `base.Locals` | Success | Dict containing local execution variables (dataframes, metrics, and run properties). |

##### Thrown Exceptions & Error States:
* `ValueError`: Raised if metric thresholds are violated.
* `ValidationError`: Raised if dataset inputs/targets violate schema requirements.
