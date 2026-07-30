---
type: "module-architecture"
title: "metrics"
description: "Technical architecture and class hierarchy for metrics"
tags: ["architecture", "uml", "pyreverse", "openwiki"]
timestamp: "2026-07-30T19:10:46Z"
---

# Module Name: metrics

* **Source Directory Reference:** `src/regression_model_template/core/`
* **Package Dependency:** Upstream: `sklearn`, `pydantic`, `mlflow`, `__future__`, `abc`, `pandas`, `mlflow.metrics`, `typing`, `regression_model_template.core` | Downstream: None

## 1. Executive Summary & Purpose
Deterministic architectural model extracted via AST parsing for module `metrics`.

## 2. UML 2.0 Class & Inheritance Architecture (Deterministic)
The following class diagram models the object-oriented structure, explicit inheritance hierarchies, and polymorphic interface implementations derived from local AST analysis:

```mermaid
classDiagram
    direction BT
    class Metric {
        +score()
        +scorer()
        +to_mlflow()
    }
    class SklearnMetric {
        +score()
    }
    Metric <|-- SklearnMetric : Inheritance / Specialization
    class Threshold {
        +to_mlflow()
    }
```

## 3. Package & Class Relations

The following diagram defines the package boundaries and directional inter-package dependencies:

```mermaid
classDiagram
    direction LR
    namespace metrics {
        class metrics_module
    }
    class sklearn_module
    metrics_module --> sklearn_module : imports
    class pydantic_module
    metrics_module --> pydantic_module : imports
    class mlflow_module
    metrics_module --> mlflow_module : imports
    class __future___module
    metrics_module --> __future___module : imports
    class abc_module
    metrics_module --> abc_module : imports
    class pandas_module
    metrics_module --> pandas_module : imports
    class mlflow_metrics_module
    metrics_module --> mlflow_metrics_module : imports
    class typing_module
    metrics_module --> typing_module : imports
    class regression_model_template_core_module
    metrics_module --> regression_model_template_core_module : imports
```

* **Inheritance & Polymorphism:** Detailed breakdown of abstract base classes, interfaces, and concrete overrides.
* **Dependencies:** How classes within this package collaborate externally.

## 4. Execution Flow & Runtime Behavior

The following sequence diagram outlines the execution lifecycle and message passing during core operations:

```mermaid
sequenceDiagram
    autonumber
    participant Caller as Client Interface
    participant Metric as Metric
    Caller->>Metric: score()
    Note over Metric: Execution of score
    Metric-->>Caller: Returns status
    participant SklearnMetric as SklearnMetric
    Caller->>SklearnMetric: score()
    Note over SklearnMetric: Execution of score
    SklearnMetric->>SklearnMetric: internal getattr()
    SklearnMetric->>SklearnMetric: internal float()
    SklearnMetric-->>Caller: Returns status
    participant Threshold as Threshold
    Caller->>Threshold: to_mlflow()
    Note over Threshold: Execution of to_mlflow
    Threshold->>Threshold: internal MlflowThreshold()
    Threshold-->>Caller: Returns status
```

---

* **Source Citations:**
  - Class `Metric`: `src/regression_model_template/core/metrics.py:27`
  - Method `score`: `src/regression_model_template/core/metrics.py:44`
  - Method `scorer`: `src/regression_model_template/core/metrics.py:55`
  - Method `to_mlflow`: `src/regression_model_template/core/metrics.py:70`
  - Class `SklearnMetric`: `src/regression_model_template/core/metrics.py:98`
  - Method `score`: `src/regression_model_template/core/metrics.py:111`
  - Class `Threshold`: `src/regression_model_template/core/metrics.py:126`
  - Method `to_mlflow`: `src/regression_model_template/core/metrics.py:140`
