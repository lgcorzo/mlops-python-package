---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDescription"
type: "concept"
title: "tuning Documentation"
description: "Documentation for src/regression_model_template/jobs/tuning.py"
tags: ["module", "tuning"]
timestamp: "2026-08-04T05:28:53Z"
generated: "agent:ast-documentation-generator"
verified: "true"
---

# Module: `src/regression_model_template/jobs/tuning.py`

## Overview
**Purpose**: Define a job for finding the best hyperparameters for a model.

**Architecture Role**: Domain Models

**Dependencies**:
- `pydantic`
- `typing`
- `mlflow`
- `regression_model_template.jobs`
- `regression_model_template.core`
- `regression_model_template.io`
- `regression_model_template.utils`

**Exported Symbols**:
- `TuningJob`

## UML Class Diagram
```plantuml
@startuml
class TuningJob {
  +KIND : T.Literal['TuningJob']
  +run_config : services.MlflowService.RunConfig
  +inputs : datasets.ReaderKind
  +targets : datasets.ReaderKind
  +model : models.ModelKind
  +metric : metrics.MetricKind
  +splitter : splitters.SplitterKind
  +searcher : searchers.SearcherKind
  +run(self:Any) : base.Locals
}
base.Job <|-- TuningJob
@enduml
```

## Call Graph
```plantuml
@startuml
TuningJob::run --> logger
TuningJob::run --> info
TuningJob::run --> locals
TuningJob::run --> run_context
TuningJob::run --> info
TuningJob::run --> info
TuningJob::run --> read
TuningJob::run --> check
TuningJob::run --> debug
TuningJob::run --> info
TuningJob::run --> read
TuningJob::run --> check
TuningJob::run --> debug
TuningJob::run --> info
TuningJob::run --> lineage
TuningJob::run --> log_input
TuningJob::run --> debug
TuningJob::run --> info
TuningJob::run --> lineage
TuningJob::run --> log_input
TuningJob::run --> debug
TuningJob::run --> info
TuningJob::run --> info
TuningJob::run --> info
TuningJob::run --> info
TuningJob::run --> search
TuningJob::run --> debug
TuningJob::run --> debug
TuningJob::run --> debug
TuningJob::run --> notify
TuningJob::run --> to_dict
TuningJob::run --> to_dict
@enduml
```

## Classes
### Class `TuningJob`
**Overview**: Find the best hyperparameters for a model.

Parameters:
    run_config (services.MlflowService.RunConfig): mlflow run config.
    inputs (datasets.ReaderKind): reader for the inputs data.
    targets (datasets.ReaderKind): reader for the targets data.
    model (models.ModelKind): machine learning model to tune.
    metric (metrics.MetricKind): tuning metric to optimize.
    splitter (splitters.SplitterKind): data sets splitter.
    searcher: (searchers.SearcherKind): hparams searcher.

#### Attributes
- `KIND`: T.Literal['TuningJob']
- `run_config`: services.MlflowService.RunConfig
- `inputs`: datasets.ReaderKind
- `targets`: datasets.ReaderKind
- `model`: models.ModelKind
- `metric`: metrics.MetricKind
- `splitter`: splitters.SplitterKind
- `searcher`: searchers.SearcherKind
#### Public Methods
##### `run`
- **Description**: Run the tuning job in context.
- **Inputs**:
  - `self`: Any
- **Output**: `base.Locals`
- **Side Effects**: Not documented
- **Complexity**: Not documented

#### Private Methods
## Functions
