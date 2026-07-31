---
type: "module-architecture"
title: "metrics"
description: "Technical architecture and class hierarchy for metrics"
tags: ["architecture", "uml", "pyreverse", "openwiki"]
timestamp: "2026-07-30T19:10:46Z"
---

# Module Name: metrics

Source File: `src/regression_model_template/core/metrics.py`
* **Source Directory Reference:** `src/regression_model_template/core/`
* **Package Dependency:** Upstream: `sklearn`, `pydantic`, `mlflow`, `__future__`, `abc`, `pandas`, `mlflow.metrics`, `typing`, `regression_model_template.core` | Downstream: None

## 1. Executive Summary & Purpose
Deterministic architectural model extracted via AST parsing for module `metrics`.

## 2. UML 2.0 Class & Inheritance Architecture (Deterministic)
The following class diagram models the object-oriented structure, explicit inheritance hierarchies, and polymorphic interface implementations derived from local AST analysis:

```mermaid
classDiagram
    class Metric {
        +KIND
        +name
        +greater_is_better
        +score(targets, outputs) : float
        +scorer(model, inputs, targets) : float
        +to_mlflow() : MlflowMetric
    }
    class SklearnMetric {
        +KIND
        +name
        +greater_is_better
        +score(targets, outputs) : float
    }
    Metric <|-- SklearnMetric
    class Threshold {
        +threshold
        +greater_is_better
        +to_mlflow() : MlflowThreshold
    }
```

## 3. Package & Class Relations

The following diagram defines the package boundaries and directional inter-package dependencies:

```mermaid
classDiagram
    class Metric {
        +KIND
        +name
        +greater_is_better
        +score(targets, outputs) : float
        +scorer(model, inputs, targets) : float
        +to_mlflow() : MlflowMetric
    }
    class SklearnMetric {
        +KIND
        +name
        +greater_is_better
        +score(targets, outputs) : float
    }
    Metric <|-- SklearnMetric
    class Threshold {
        +threshold
        +greater_is_better
        +to_mlflow() : MlflowThreshold
    }
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

```mermaid
flowchart TD
    metrics --> __future__
    metrics --> abc
    metrics --> mlflow
    metrics --> mlflow_metrics
    metrics --> pandas
    metrics --> pydantic
    metrics --> regression_model_template_core
    metrics --> sklearn
    metrics --> typing
```
