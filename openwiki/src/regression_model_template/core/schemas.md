---
type: "module-architecture"
title: "schemas"
description: "Technical architecture and class hierarchy for schemas"
tags: ["architecture", "uml", "pyreverse", "openwiki"]
timestamp: "2026-07-30T19:10:46Z"
---

# Module Name: schemas

* **Source Directory Reference:** `src/regression_model_template/core/`
* **Package Dependency:** Upstream: `pandera.typing`, `pandas`, `pandera.typing.common`, `pandera`, `typing` | Downstream: None

## 1. Executive Summary & Purpose
Deterministic architectural model extracted via AST parsing for module `schemas`.

## 2. UML 2.0 Class & Inheritance Architecture (Deterministic)
The following class diagram models the object-oriented structure, explicit inheritance hierarchies, and polymorphic interface implementations derived from local AST analysis:

```mermaid
classDiagram
    direction BT
    class Schema {
        +check()
    }
    class InputsSchema {
    }
    Schema <|-- InputsSchema : Inheritance / Specialization
    class TargetsSchema {
    }
    Schema <|-- TargetsSchema : Inheritance / Specialization
    class OutputsSchema {
    }
    Schema <|-- OutputsSchema : Inheritance / Specialization
    class SHAPValuesSchema {
    }
    Schema <|-- SHAPValuesSchema : Inheritance / Specialization
    class FeatureImportancesSchema {
    }
    Schema <|-- FeatureImportancesSchema : Inheritance / Specialization
    class Config {
    }
    class Config {
    }
```

## 3. Package & Class Relations

The following diagram defines the package boundaries and directional inter-package dependencies:

```mermaid
classDiagram
    direction LR
    namespace schemas {
        class schemas_module
    }
    class pandera_typing_module
    schemas_module --> pandera_typing_module : imports
    class pandas_module
    schemas_module --> pandas_module : imports
    class pandera_typing_common_module
    schemas_module --> pandera_typing_common_module : imports
    class pandera_module
    schemas_module --> pandera_module : imports
    class typing_module
    schemas_module --> typing_module : imports
```

* **Inheritance & Polymorphism:** Detailed breakdown of abstract base classes, interfaces, and concrete overrides.
* **Dependencies:** How classes within this package collaborate externally.

## 4. Execution Flow & Runtime Behavior

The following sequence diagram outlines the execution lifecycle and message passing during core operations:

```mermaid
sequenceDiagram
    autonumber
    participant Caller as Client Interface
    participant Schema as Schema
    Caller->>Schema: check()
    Note over Schema: Execution of check
    Schema->>Schema: internal cast()
    Schema->>Schema: internal validate()
    Schema-->>Caller: Returns status
    participant InputsSchema as InputsSchema
    participant TargetsSchema as TargetsSchema
    participant OutputsSchema as OutputsSchema
    participant SHAPValuesSchema as SHAPValuesSchema
    participant FeatureImportancesSchema as FeatureImportancesSchema
    participant Config as Config
    participant Config as Config
```

---

* **Source Citations:**
  - Class `Schema`: `src/regression_model_template/core/schemas.py:20`
  - Method `check`: `src/regression_model_template/core/schemas.py:39`
  - Class `InputsSchema`: `src/regression_model_template/core/schemas.py:51`
  - Class `TargetsSchema`: `src/regression_model_template/core/schemas.py:75`
  - Class `OutputsSchema`: `src/regression_model_template/core/schemas.py:85`
  - Class `SHAPValuesSchema`: `src/regression_model_template/core/schemas.py:95`
  - Class `FeatureImportancesSchema`: `src/regression_model_template/core/schemas.py:113`
  - Class `Config`: `src/regression_model_template/core/schemas.py:27`
  - Class `Config`: `src/regression_model_template/core/schemas.py:98`
