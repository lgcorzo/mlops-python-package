---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "regression_model_template::core::schemas — Pandera Data Contracts"
source_path: "src/regression_model_template/core/schemas.py"
description: "Pandera DataFrameModel schemas enforcing compile-time and runtime validation on Inputs, Targets, Outputs, and SHAP values."
tags: ["iso42010", "okf", "component_view", "schemas", "pandera"]
timestamp: "2026-10-01T17:50:00Z"
generated: "agent:wiki-iso-documentation-standard"
verified: "true"
last_verified_commit: "073b5fd"
---

# regression_model_template::core::schemas — Pandera Data Contracts

> **Source**: `src/regression_model_template/core/schemas.py` (Lines: L1-L120)  
> **Layer**: Domain  
> **Role**: Formal tabular contracts guaranteeing type safety, index alignment, and range constraints across all pipeline boundaries.

---

## 1. Class Diagram

```mermaid
classDiagram
    class Schema {
        +check(data: DataFrame) DataFrame$
    }

    class InputsSchema {
        +UInt32 instant
        +DateTime dteday
        +UInt8 season
        +UInt8 yr
        +UInt8 mnth
        +UInt8 hr
        +float temp
        +float hum
        +float windspeed
    }
    InputsSchema --|> Schema : inherits

    class TargetsSchema {
        +UInt32 instant
        +UInt32 cnt
    }
    TargetsSchema --|> Schema : inherits

    class OutputsSchema {
        +UInt32 instant
        +UInt32 prediction
    }
    OutputsSchema --|> Schema : inherits
```

---

> *Related: [Data Model](../../../architecture/mission_data_model.md) · [Datasets](../io/datasets.md)*
