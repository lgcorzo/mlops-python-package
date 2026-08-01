---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: schemas"
source_path: "src/regression_model_template/core/schemas.py"
description: "Define and validate dataframe schemas."
tags: ["module", "schemas", "regression_model_template"]
timestamp: "2026-08-01T09:57:53Z"
generated: "agent:uml2-okf-documenter"
verified: "true"
last_verified_commit: "8f9670a"
---

# Module Specification: schemas

* **Source Reference:** [src/regression_model_template/core/schemas.py](../../../src/regression_model_template/core/schemas.py) (Lines: L1-L120)

## 1. Architectural Role & Responsibilities
Define and validate dataframe schemas.

## 2. UML 2.0 Class Diagram
```mermaid
classDiagram
    direction BT
    class Schema {
        +check(cls: T.Type[TSchema], data: pd.DataFrame) papd.DataFrame[TSchema]
    }
    class InputsSchema {
        +instant: papd.Index[padt.UInt32]
        +dteday: papd.Series[padt.DateTime]
        +season: papd.Series[padt.UInt8]
        +yr: papd.Series[padt.UInt8]
        +mnth: papd.Series[padt.UInt8]
        +hr: papd.Series[padt.UInt8]
        +holiday: papd.Series[padt.Bool]
        +weekday: papd.Series[padt.UInt8]
        +workingday: papd.Series[padt.Bool]
        +weathersit: papd.Series[padt.UInt8]
        +temp: papd.Series[padt.Float16]
        +atemp: papd.Series[padt.Float16]
        +hum: papd.Series[padt.Float16]
        +windspeed: papd.Series[padt.Float16]
        +casual: papd.Series[padt.UInt32]
        +registered: papd.Series[padt.UInt32]
    }
    class TargetsSchema {
        +instant: papd.Index[padt.UInt32]
        +cnt: papd.Series[padt.UInt32]
    }
    class OutputsSchema {
        +instant: papd.Index[padt.UInt32]
        +prediction: papd.Series[padt.UInt32]
    }
    class SHAPValuesSchema {
    }
    class FeatureImportancesSchema {
        +feature: papd.Series[str]
        +importance: papd.Series[float]
    }
```

## 3. Class & Method Specifications

### `Schema` ([`src/regression_model_template/core/schemas.py:L20-L48`](../../../src/regression_model_template/core/schemas.py#L20-L48))

Base class for a dataframe schema.

Use a schema to type your dataframe object.
e.g., to communicate and validate its fields.

#### Methods

* **`check(cls: T.Type[TSchema], data: pd.DataFrame) -> papd.DataFrame[TSchema]`** (L39-L48)
  - **Purpose**: Check the dataframe with this schema.
  - **Inputs**:
    - `cls` (`T.Type[TSchema]`): Parameter description.
    - `data` (`pd.DataFrame`): Parameter description.
  - **Outputs**:
    - `papd.DataFrame[TSchema]`: Return value description.

### `InputsSchema` ([`src/regression_model_template/core/schemas.py:L51-L69`](../../../src/regression_model_template/core/schemas.py#L51-L69))

Schema for the project inputs.

#### Methods

*No methods defined.*

### `TargetsSchema` ([`src/regression_model_template/core/schemas.py:L75-L79`](../../../src/regression_model_template/core/schemas.py#L75-L79))

Schema for the project target.

#### Methods

*No methods defined.*

### `OutputsSchema` ([`src/regression_model_template/core/schemas.py:L85-L89`](../../../src/regression_model_template/core/schemas.py#L85-L89))

Schema for the project output.

#### Methods

*No methods defined.*

### `SHAPValuesSchema` ([`src/regression_model_template/core/schemas.py:L95-L107`](../../../src/regression_model_template/core/schemas.py#L95-L107))

Schema for the project shap values.

#### Methods

*No methods defined.*

### `FeatureImportancesSchema` ([`src/regression_model_template/core/schemas.py:L113-L117`](../../../src/regression_model_template/core/schemas.py#L113-L117))

Schema for the project feature importances.

#### Methods

*No methods defined.*
