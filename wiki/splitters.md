---
type: script
title: "splitters"
source_path: "src/regression_model_template/utils/splitters.py"
description: "Split dataframes into subsets (e.g., train/valid/test)."
tags: [script, regression_model_template]
last_verified_commit: "abe2ee0"
---

# splitters

Source File: `src/regression_model_template/utils/splitters.py`

Split dataframes into subsets (e.g., train/valid/test).

```mermaid
classDiagram
    class Splitter {
        +KIND
        +split(inputs, targets, groups)
        +get_n_splits(inputs, targets, groups)
    }
    Splitter <|-- TrainTestSplitter
    class TrainTestSplitter {
        +KIND
        +shuffle
        +test_size
        +random_state
        +split(inputs, targets, groups)
        +get_n_splits(inputs, targets, groups)
    }
    Splitter <|-- TimeSeriesSplitter
    class TimeSeriesSplitter {
        +KIND
        +gap
        +n_splits
        +test_size
        +split(inputs, targets, groups)
        +get_n_splits(inputs, targets, groups)
    }
```

```mermaid
flowchart TD
    splitters --> abc
    splitters --> typing
    splitters --> numpy
    splitters --> numpy_typing
    splitters --> pydantic
    splitters --> sklearn
    splitters --> regression_model_template_core
```
