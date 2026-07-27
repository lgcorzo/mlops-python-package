---
type: script
title: "promotion"
source_path: "src/regression_model_template/jobs/promotion.py"
description: "Define a job for promoting a registered model version with an alias."
tags: [script, regression_model_template]
last_verified_commit: "c0c5dbc"
---

# promotion

Source File: `src/regression_model_template/jobs/promotion.py`

Define a job for promoting a registered model version with an alias.

```mermaid
classDiagram
    class PromotionJob {
        +KIND
        +alias
        +version
        +run() : Any
    }
```

```mermaid
flowchart TD

    promotion --> regression_model_template_jobs
    promotion --> typing
```
