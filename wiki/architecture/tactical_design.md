---
iso_doc_type: "Description"
iso_viewpoint: "ComponentView"
type: "architecture"
title: "Tactical Design & Design Patterns"
description: "ISO 42010 ComponentView / ISO 15289 Description documentation for micro-architecture, C4 Level 3 component breakdown, and design patterns."
tags: ["iso42010", "okf", "component_view", "design_patterns", "uml"]
timestamp: "2026-10-01T17:50:00Z"
generated: "agent:wiki-iso-documentation-standard"
verified: "true"
last_verified_commit: "073b5fd"
---

# Tactical Design & Design Patterns

> **Purpose**: Detail the micro-architectural design, design patterns, and C4 Level 3 component interactions across the codebase.

---

## 1. C4 Level 3: Component Diagram

```mermaid
classDiagram
    direction TB

    class Model {
        <<abstract>>
        +fit(inputs, targets) Model*
        +predict(inputs) Outputs*
        +explain_model() FeatureImportances*
        +explain_samples(inputs) SHAPValues*
    }

    class BaselineSklearnModel {
        +int max_depth
        +int n_estimators
        +Pipeline _pipeline
        +fit(inputs, targets) BaselineSklearnModel
        +predict(inputs) Outputs
    }
    BaselineSklearnModel --|> Model : implements

    class Metric {
        <<abstract>>
        +score(targets, outputs) float*
        +scorer(model, inputs, targets) float
        +to_mlflow() MlflowMetric
    }

    class SklearnMetric {
        +score(targets, outputs) float
    }
    SklearnMetric --|> Metric : implements

    class Job {
        <<abstract>>
        +LoggerService logger_service
        +AlertsService alerts_service
        +MlflowService mlflow_service
        +__enter__() Self
        +__exit__() bool
        +run() Locals*
    }

    class TrainingJob {
        +RunConfig run_config
        +ReaderKind inputs
        +ReaderKind targets
        +ModelKind model
        +run() Locals
    }
    TrainingJob --|> Job : implements

    class Reader {
        <<abstract>>
        +read() DataFrame*
        +lineage() Lineage*
    }
    class ParquetReader {
        +str path
        +read() DataFrame
    }
    ParquetReader --|> Reader : implements

    class Splitter {
        <<abstract>>
        +split(inputs, targets) TrainTestSplits*
        +get_n_splits(inputs, targets) int*
    }
    class TimeSeriesSplitter {
        +int gap
        +int n_splits
        +split(inputs, targets) TrainTestSplits
    }
    TimeSeriesSplitter --|> Splitter : implements

    TrainingJob --> Model : trains
    TrainingJob --> Reader : reads inputs
    TrainingJob --> Splitter : splits dataset
```

---

## 2. Design Patterns in Action

### 1. Strategy Pattern
The Strategy pattern defines interchangeable algorithm families:
- **Models (`core/models.py`)**: Client code in `jobs/training.py` or `jobs/inference.py` consumes the abstract `Model` interface. Any estimator (Random Forest, Gradient Boosting, Deep Neural Network) can be substituted transparently.
- **Metrics (`core/metrics.py`)**: Metrics (`MSE`, `MAE`, `R2`) implement the `Metric` interface, providing unified scoring and MLflow threshold export.
- **Splitters (`utils/splitters.py`)**: `TrainTestSplitter` and `TimeSeriesSplitter` encapsulate distinct cross-validation partitioning algorithms.
- **Readers & Writers (`io/datasets.py`)**: `ParquetReader` and `ParquetWriter` isolate specific tabular serialization logic.

### 2. Context Manager / Template Method Pattern
The `Job` base class (`jobs/base.py`) implements the Python context manager protocol (`__enter__` and `__exit__`):
- `__enter__`: Automatically initializes `LoggerService`, `AlertsService`, and `MlflowService`.
- `__exit__`: Manages clean teardown, logs execution duration, and broadcasts failure notifications if unhandled exceptions occur.
- `run()`: The template method overridden by concrete jobs (`TrainingJob`, `TuningJob`, etc.).

### 3. Singleton Pattern
The `Singleton` metaclass in `io/osvariables.py` ensures that runtime environment settings (`Env`) are parsed exactly once from `.env` files and shared immutably across all worker threads.

---

> *Related: [Strategic Design](strategic_design.md) · [Data Model](mission_data_model.md) · [Master Index](../index.md)*
