---
type: script
title: "base"
source_path: "src/regression_model_template/jobs/base.py"
description: "Base for high-level project jobs."
tags: [script, regression_model_template]
last_verified_commit: "c0c5dbc"
---

# base

Source File: `src/regression_model_template/jobs/base.py`

Base for high-level project jobs.

```mermaid
classDiagram
    class Job {
        +KIND
        +logger_service
        +alerts_service
        +mlflow_service
        -__enter__() : Any
        -__exit__(exc_type, exc_value, exc_traceback) : Any
        +run() : Locals
    }
```

```mermaid
flowchart TD

    base --> abc
    base --> pydantic
    base --> regression_model_template_io
    base --> types
    base --> typing
```
