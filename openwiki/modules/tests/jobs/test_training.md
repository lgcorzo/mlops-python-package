---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: test_training"
source_path: "tests/jobs/test_training.py"
description: "No description available."
tags: ["module", "test_training"]
timestamp: "2026-08-12T05:53:45Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "ce3f2af"
---
# Module Specification: test_training

* **Source Reference:** [tests/jobs/test_training.py](../../../../tests/jobs/test_training.py)

## 1. Architectural Role & Responsibilities
No description available.

### Detected Architecture Patterns
Detected roles: General Subsystem

## 2. UML Diagrams
### Class Diagram
_No classes found._

### Sequence Diagram
```plantuml
sequenceDiagram
    test_training_job->>RunConfig: invoke
    test_training_job->>client: invoke
    test_training_job->>TrainingJob: invoke
    test_training_job->>get_experiment_by_name: invoke
    test_training_job->>search_runs: invoke
    test_training_job->>get_model_version: invoke
    test_training_job->>run: invoke
    test_training_job->>set: invoke
    test_training_job->>values: invoke
    test_training_job->>items: invoke
    test_training_job->>len: invoke
    test_training_job->>float: invoke
    test_training_job->>readouterr: invoke
```

### Component Diagram
```plantuml
component [test_training] as Comp
Comp --> [capture]
Comp --> [jobs]
Comp --> [metrics]
Comp --> [models]
Comp --> [schemas]
Comp --> [datasets]
Comp --> [registries]
Comp --> [services]
Comp --> [signers]
Comp --> [splitters]
```

## 3. Class & Method Specifications

## Standalone Functions

### `test_training_job(mlflow_service: services.MlflowService, alerts_service: services.AlertsService, logger_service: services.LoggerService, inputs_reader: datasets.ParquetReader, targets_reader: datasets.ParquetReader, model: models.Model, metric: metrics.Metric, train_test_splitter: splitters.Splitter, saver: registries.Saver, signer: signers.Signer, register: registries.Register, capsys: pc.CaptureFixture[str]) -> None`
No description available.

#### Inputs
* `mlflow_service` (`services.MlflowService`)
* `alerts_service` (`services.AlertsService`)
* `logger_service` (`services.LoggerService`)
* `inputs_reader` (`datasets.ParquetReader`)
* `targets_reader` (`datasets.ParquetReader`)
* `model` (`models.Model`)
* `metric` (`metrics.Metric`)
* `train_test_splitter` (`splitters.Splitter`)
* `saver` (`registries.Saver`)
* `signer` (`signers.Signer`)
* `register` (`registries.Register`)
* `capsys` (`pc.CaptureFixture[str]`)

#### Outputs
* `None`

## Dependencies

* `_pytest.capture`
* `regression_model_template.jobs`
* `regression_model_template.core.metrics`
* `regression_model_template.core.models`
* `regression_model_template.core.schemas`
* `regression_model_template.io.datasets`
* `regression_model_template.io.registries`
* `regression_model_template.io.services`
* `regression_model_template.utils.signers`
* `regression_model_template.utils.splitters`

## Used By

_Not used by any other module._
