---
type: script
title: "training"
source_path: "src/regression_model_template/jobs/training.py"
description: "Define a job for training and registring a single AI/ML model."
tags: [script, regression_model_template]
last_verified_commit: "abe2ee0"
---

# training

Source File: `src/regression_model_template/jobs/training.py`

Define a job for training and registring a single AI/ML model.

```mermaid
classDiagram
    class TrainingJob {
        +KIND
        +run_config
        +inputs
        +targets
        +model
        +metrics
        +splitter
        +saver
        +signer
        +registry
        +run()
    }
```

```mermaid
flowchart TD
    training --> time
    training --> typing
    training --> mlflow
    training --> pydantic
    training --> mlflow_entities
    training --> regression_model_template_core
    training --> regression_model_template_core
    training --> regression_model_template_io
    training --> regression_model_template_jobs
    training --> regression_model_template_utils
```
