---
type: script
title: "searchers"
source_path: "src/regression_model_template/utils/searchers.py"
description: "Find the best hyperparameters for a model."
tags: [script, regression_model_template]
last_verified_commit: "abe2ee0"
---

# searchers

Source File: `src/regression_model_template/utils/searchers.py`

Find the best hyperparameters for a model.

```mermaid
classDiagram
    class Searcher {
        +KIND
        +param_grid
        +search(model, metric, inputs, targets, cv)
    }
    Searcher <|-- GridCVSearcher
    class GridCVSearcher {
        +KIND
        +n_jobs
        +refit
        +verbose
        +error_score
        +return_train_score
        +search(model, metric, inputs, targets, cv)
    }
```

```mermaid
flowchart TD
    searchers --> abc
    searchers --> typing
    searchers --> typing
    searchers --> pandas
    searchers --> pydantic
    searchers --> sklearn
    searchers --> regression_model_template_core
    searchers --> regression_model_template_utils
```
