---
type: "module-architecture"
title: "splitters"
description: "Technical architecture and class hierarchy for splitters"
tags: ["architecture", "uml", "pyreverse", "openwiki"]
timestamp: "2026-07-30T19:10:46Z"
---

# Module Name: splitters

* **Source Directory Reference:** `src/regression_model_template/utils/`
* **Package Dependency:** Upstream: `sklearn`, `pydantic`, `abc`, `numpy`, `typing`, `regression_model_template.core`, `numpy.typing` | Downstream: None

## 1. Executive Summary & Purpose
Deterministic architectural model extracted via AST parsing for module `splitters`.

## 2. UML 2.0 Class & Inheritance Architecture (Deterministic)
The following class diagram models the object-oriented structure, explicit inheritance hierarchies, and polymorphic interface implementations derived from local AST analysis:

```mermaid
classDiagram
    direction BT
    class Splitter {
        +split()
        +get_n_splits()
    }
    class TrainTestSplitter {
        +split()
        +get_n_splits()
    }
    Splitter <|-- TrainTestSplitter : Inheritance / Specialization
    class TimeSeriesSplitter {
        +split()
        +get_n_splits()
    }
    Splitter <|-- TimeSeriesSplitter : Inheritance / Specialization
```

## 3. Package & Class Relations

The following diagram defines the package boundaries and directional inter-package dependencies:

```mermaid
classDiagram
    direction LR
    namespace splitters {
        class splitters_module
    }
    class sklearn_module
    splitters_module --> sklearn_module : imports
    class pydantic_module
    splitters_module --> pydantic_module : imports
    class abc_module
    splitters_module --> abc_module : imports
    class numpy_module
    splitters_module --> numpy_module : imports
    class typing_module
    splitters_module --> typing_module : imports
    class regression_model_template_core_module
    splitters_module --> regression_model_template_core_module : imports
    class numpy_typing_module
    splitters_module --> numpy_typing_module : imports
```

* **Inheritance & Polymorphism:** Detailed breakdown of abstract base classes, interfaces, and concrete overrides.
* **Dependencies:** How classes within this package collaborate externally.

## 4. Execution Flow & Runtime Behavior

The following sequence diagram outlines the execution lifecycle and message passing during core operations:

```mermaid
sequenceDiagram
    autonumber
    participant Caller as Client Interface
    participant Splitter as Splitter
    Caller->>Splitter: split()
    Note over Splitter: Execution of split
    Splitter-->>Caller: Returns status
    participant TrainTestSplitter as TrainTestSplitter
    Caller->>TrainTestSplitter: split()
    Note over TrainTestSplitter: Execution of split
    TrainTestSplitter->>TrainTestSplitter: internal len()
    TrainTestSplitter->>TrainTestSplitter: internal arange()
    TrainTestSplitter-->>Caller: Returns status
    participant TimeSeriesSplitter as TimeSeriesSplitter
    Caller->>TimeSeriesSplitter: split()
    Note over TimeSeriesSplitter: Execution of split
    TimeSeriesSplitter->>TimeSeriesSplitter: internal split()
    TimeSeriesSplitter->>TimeSeriesSplitter: internal TimeSeriesSplit()
    TimeSeriesSplitter-->>Caller: Returns status
```

---

* **Source Citations:**
  - Class `Splitter`: `src/regression_model_template/utils/splitters.py:24`
  - Method `split`: `src/regression_model_template/utils/splitters.py:36`
  - Method `get_n_splits`: `src/regression_model_template/utils/splitters.py:49`
  - Class `TrainTestSplitter`: `src/regression_model_template/utils/splitters.py:62`
  - Method `split`: `src/regression_model_template/utils/splitters.py:77`
  - Method `get_n_splits`: `src/regression_model_template/utils/splitters.py:84`
  - Class `TimeSeriesSplitter`: `src/regression_model_template/utils/splitters.py:88`
  - Method `split`: `src/regression_model_template/utils/splitters.py:103`
  - Method `get_n_splits`: `src/regression_model_template/utils/splitters.py:107`
