---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "regression_model_template::utils::splitters — Dataset Partitioning Strategies"
source_path: "src/regression_model_template/utils/splitters.py"
description: "Abstract Splitter interface, TrainTestSplitter, and TimeSeriesSplitter partitioning datasets while respecting temporal order."
tags: ["iso42010", "okf", "component_view", "splitters", "cross_validation"]
timestamp: "2026-10-01T17:50:00Z"
generated: "agent:wiki-iso-documentation-standard"
verified: "true"
last_verified_commit: "073b5fd"
---

# regression_model_template::utils::splitters — Dataset Partitioning Strategies

> **Source**: `src/regression_model_template/utils/splitters.py` (Lines: L1-L111)  
> **Layer**: Utilities  
> **Role**: Strategy abstraction partitioning tabular datasets into train and test splits, supporting random shuffling and strict temporal ordering.

---

## 1. Class Diagram

```mermaid
classDiagram
    class Splitter {
        <<abstract>>
        +str KIND
        +split(inputs: Inputs, targets: Targets, groups: Index | None = None) TrainTestSplits*
        +get_n_splits(inputs: Inputs, targets: Targets, groups: Index | None = None) int*
    }

    class TrainTestSplitter {
        +str KIND = "TrainTestSplitter"
        +bool shuffle
        +int | float test_size
        +int random_state
        +split(inputs: Inputs, targets: Targets, groups: Index | None = None) TrainTestSplits
        +get_n_splits(inputs: Inputs, targets: Targets, groups: Index | None = None) int
    }
    TrainTestSplitter --|> Splitter : implements

    class TimeSeriesSplitter {
        +str KIND = "TimeSeriesSplitter"
        +int gap
        +int n_splits
        +int | float test_size
        +split(inputs: Inputs, targets: Targets, groups: Index | None = None) TrainTestSplits
        +get_n_splits(inputs: Inputs, targets: Targets, groups: Index | None = None) int
    }
    TimeSeriesSplitter --|> Splitter : implements
```

---

> *Related: [Training Job](../jobs/training.md) · [Searchers](searchers.md)*
