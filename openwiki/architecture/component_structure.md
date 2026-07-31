---
iso_doc_type: "Description"
iso_viewpoint: "ComponentView"
type: "architecture"
title: "ISO 42010 Component View — Subsystem Breakdown & Class Diagrams"
description: "Component view detailing subsystem organization, class hierarchies, and UML 2.0 class diagrams."
tags: ["iso42010", "component", "uml", "classdiagram", "architecture"]
last_verified_commit: "HEAD"
timestamp: "2026-07-31T16:17:00Z"
generated: "agent:okf-professional-documenter"
verified: "true"
---

# ISO 42010 Component View: Subsystem Breakdown & UML 2.0 Class Diagrams

## 1. Subsystem Architecture Overview

`mlops-python-package` is organized into 5 primary subsystems:

1. **Controller Subsystem (`controller/`)**: Real-time Kafka consumer/producer and embedded FastAPI web application (`FastAPIKafkaService`).
2. **Pipeline Jobs Subsystem (`jobs/`)**: Job runner abstraction (`Job`) and concrete workflow implementations (`TrainingJob`, `TuningJob`, `EvaluationsJob`, `ExplanationsJob`, `PromotionJob`, `InferenceJob`).
3. **Core Model & Schema Subsystem (`core/`)**: Model wrapper interfaces (`Model`, `BaselineSklearnModel`), Pandera schemas (`InputsSchema`, `TargetsSchema`, `OutputsSchema`), and evaluation metrics (`Metric`, `SklearnMetric`).
4. **I/O & Service Layer (`io/`)**: Data reader/writer abstractions (`Reader`, `ParquetReader`), MLflow registry savers/loaders (`Saver`, `Loader`, `MlflowRegister`), and telemetry services (`LoggerService`, `MlflowService`, `AlertsService`).
5. **Utility Layer (`utils/`)**: Search strategy algorithms (`GridCVSearcher`), signature extraction (`InferSigner`), and dataset splitters (`TrainTestSplitter`, `TimeSeriesSplitter`).

---

## 2. UML 2.0 Class Hierarchy Diagrams

### A. Pipeline Job Abstraction Hierarchy

```mermaid
classDiagram
    direction BT
    class Job {
        <<abstract>>
        +run_config: RunConfig
        +services: List~Service~
        +__enter__() Job
        +__exit__(exc_type, exc_val, exc_tb)
        +run()*
    }
    class TrainingJob {
        +run()
    }
    class TuningJob {
        +run()
    }
    class EvaluationsJob {
        +run()
    }
    class ExplanationsJob {
        +run()
    }
    class PromotionJob {
        +run()
    }
    class InferenceJob {
        +run()
    }

    Job <|-- TrainingJob : Inheritance
    Job <|-- TuningJob : Inheritance
    Job <|-- EvaluationsJob : Inheritance
    Job <|-- ExplanationsJob : Inheritance
    Job <|-- PromotionJob : Inheritance
    Job <|-- InferenceJob : Inheritance
```

### B. Core Model & Evaluation Metrics Hierarchy

```mermaid
classDiagram
    direction BT
    class Model {
        <<abstract>>
        +get_params(deep: bool) Dict
        +set_params()
        +fit(inputs, targets)* Model
        +predict(inputs)* ndarray
        +explain_model()*
        +explain_samples(inputs)*
        +get_internal_model()* Any
    }
    class BaselineSklearnModel {
        -model: Pipeline
        +fit(inputs, targets) BaselineSklearnModel
        +predict(inputs) ndarray
        +explain_model() SHAPExplanation
        +explain_samples(inputs) SHAPExplanation
        +get_internal_model() Pipeline
    }
    class Metric {
        <<abstract>>
        +name: str
        +score(targets, outputs)* float
        +scorer(model, inputs, targets) float
        +to_mlflow()
    }
    class SklearnMetric {
        -metric_fn: Callable
        +score(targets, outputs) float
    }

    Model <|-- BaselineSklearnModel : Realization
    Metric <|-- SklearnMetric : Realization
```

### C. I/O Data Readers, Writers & Registries

```mermaid
classDiagram
    direction BT
    class Reader {
        <<interface>>
        +read()* DataFrame
        +lineage(name, data, targets, predictions) LineageRecord
    }
    class ParquetReader {
        -filepath: Path
        +read() DataFrame
        +lineage(name, data, targets, predictions) LineageRecord
    }
    class Saver {
        <<interface>>
        +save(model, signature, input_example)* ModelInfo
    }
    class CustomSaver {
        +save(model, signature, input_example) ModelInfo
    }
    class BuiltinSaver {
        +save(model, signature, input_example) ModelInfo
    }

    Reader <|.. ParquetReader : Realization
    Saver <|.. CustomSaver : Realization
    Saver <|.. BuiltinSaver : Realization
```
