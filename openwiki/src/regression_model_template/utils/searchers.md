---
type: "module-architecture"
title: "searchers"
description: "Technical architecture and class hierarchy for searchers"
tags: ["architecture", "uml", "pyreverse", "openwiki"]
timestamp: "2026-07-30T19:10:46Z"
---

# Module Name: searchers

Source File: `src/regression_model_template/utils/searchers.py`
* **Source Directory Reference:** `src/regression_model_template/utils/`
* **Package Dependency:** Upstream: `sklearn`, `pydantic`, `pandas`, `abc`, `regression_model_template.utils`, `typing`, `regression_model_template.core` | Downstream: None

## 1. Executive Summary & Purpose
Deterministic architectural model extracted via AST parsing for module `searchers`.

## 2. UML 2.0 Class & Inheritance Architecture (Deterministic)
The following class diagram models the object-oriented structure, explicit inheritance hierarchies, and polymorphic interface implementations derived from local AST analysis:

```mermaid
classDiagram
    class Searcher {
        +KIND
        +param_grid
        +search(model, metric, inputs, targets, cv) : Results
    }
    class GridCVSearcher {
        +KIND
        +n_jobs
        +refit
        +verbose
        +error_score
        +return_train_score
        +search(model, metric, inputs, targets, cv) : Results
    }
    Searcher <|-- GridCVSearcher
```

## 3. Package & Class Relations

The following diagram defines the package boundaries and directional inter-package dependencies:

```mermaid
classDiagram
    class Searcher {
        +KIND
        +param_grid
        +search(model, metric, inputs, targets, cv) : Results
    }
    class GridCVSearcher {
        +KIND
        +n_jobs
        +refit
        +verbose
        +error_score
        +return_train_score
        +search(model, metric, inputs, targets, cv) : Results
    }
    Searcher <|-- GridCVSearcher
```

* **Inheritance & Polymorphism:** Detailed breakdown of abstract base classes, interfaces, and concrete overrides.
* **Dependencies:** How classes within this package collaborate externally.

## 4. Execution Flow & Runtime Behavior

The following sequence diagram outlines the execution lifecycle and message passing during core operations:

```mermaid
sequenceDiagram
    autonumber
    participant Caller as Client Interface
    participant Searcher as Searcher
    Caller->>Searcher: search()
    Note over Searcher: Execution of search
    Searcher-->>Caller: Returns status
    participant GridCVSearcher as GridCVSearcher
    Caller->>GridCVSearcher: search()
    Note over GridCVSearcher: Execution of search
    GridCVSearcher->>GridCVSearcher: internal DataFrame()
    GridCVSearcher->>GridCVSearcher: internal fit()
    GridCVSearcher-->>Caller: Returns status
```

---

* **Source Citations:**
  - Class `Searcher`: `src/regression_model_template/utils/searchers.py:34`
  - Method `search`: `src/regression_model_template/utils/searchers.py:49`
  - Class `GridCVSearcher`: `src/regression_model_template/utils/searchers.py:71`
  - Method `search`: `src/regression_model_template/utils/searchers.py:92`

```mermaid
flowchart TD
    searchers --> abc
    searchers --> pandas
    searchers --> pydantic
    searchers --> regression_model_template_core
    searchers --> regression_model_template_utils
    searchers --> sklearn
    searchers --> typing
```
