---
type: script
title: "explanations"
source_path: "src/regression_model_template/jobs/explanations.py"
description: "Define a job for explaining the model structure and decisions."
tags: [script, regression_model_template]
last_verified_commit: "c0c5dbc"
---

# explanations

Source File: `src/regression_model_template/jobs/explanations.py`

Define a job for explaining the model structure and decisions.

```mermaid
classDiagram
    class ExplanationsJob {
        +KIND
        +inputs_samples
        +models_explanations
        +samples_explanations
        +alias_or_version
        +loader
        +run() : Any
    }
```

```mermaid
flowchart TD

    explanations --> pydantic
    explanations --> regression_model_template_core
    explanations --> regression_model_template_io
    explanations --> regression_model_template_jobs
    explanations --> typing
```
