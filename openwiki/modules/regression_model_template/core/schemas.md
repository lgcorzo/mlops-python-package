---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: Data Validation Schemas"
source_path: "[[src/regression_model_template/core/schemas.py](../../../../src/regression_model_template/core/schemas.py)](../../../../[src/regression_model_template/core/schemas.py](../../../../src/regression_model_template/core/schemas.py))"
description: "Pandera DataFrame schemas for strict input features, targets, predictions, and SHAP explanation data structures."
tags: ["core", "schemas", "pandera", "validation", "pydantic"]
last_verified_commit: "HEAD"
timestamp: "2026-07-31T16:17:00Z"
generated: "agent:okf-professional-documenter"
verified: "true"
---

# Module Specification: Data Validation Schemas

* **Source File Reference:** `[[src/regression_model_template/core/schemas.py](../../../../src/regression_model_template/core/schemas.py)](../../../../[src/regression_model_template/core/schemas.py](../../../../src/regression_model_template/core/schemas.py))` (Lines: L1-L117)
* **Upstream Dependencies:** `pandera`, `pydantic`
* **Downstream Consumers:** [Modules/RegressionModelTemplate/Jobs/Training](../jobs/training.md), [Modules/RegressionModelTemplate/Controller/KafkaApp](../controller/kafka_app.md)

## 1. Architectural Role & Responsibilities
`schemas.py` defines Pandera DataFrame schemas (`InputsSchema`, `TargetsSchema`, `OutputsSchema`, `SHAPValuesSchema`) to enforce strict type checking, non-null constraints, and numeric range limits across pipeline operations.

## 2. UML 2.0 Class Diagram

```mermaid
classDiagram
    direction BT
    class Schema {
        <<abstract>>
        +check(data: DataFrame) DataFrame
    }
    class InputsSchema {
        +check(data) DataFrame
    }
    class TargetsSchema {
        +check(data) DataFrame
    }
    class OutputsSchema {
        +check(data) DataFrame
    }
    class SHAPValuesSchema {
        +check(data) DataFrame
    }

    Schema <|-- InputsSchema : Inheritance
    Schema <|-- TargetsSchema : Inheritance
    Schema <|-- OutputsSchema : Inheritance
    Schema <|-- SHAPValuesSchema : Inheritance
```

## 3. Class & Method Specifications

### `Schema` (`[[src/regression_model_template/core/schemas.py:L20-L48](../../../../src/regression_model_template/core/schemas.py#L20-L48)](../../../../[src/regression_model_template/core/schemas.py](../../../../src/regression_model_template/core/schemas.py)#L20-L48)`)
* `check(cls, data: pd.DataFrame) -> pd.DataFrame` (L39-L48): Class method executing Pandera schema validation on input DataFrame.

### Concrete Schema Implementations
* `InputsSchema` (L51-L69): Validates raw input features (numeric dtypes, min/max ranges).
* `TargetsSchema` (L75-L79): Validates target ground truth values.
* `OutputsSchema` (L85-L89): Validates prediction outputs.
* `SHAPValuesSchema` (L95-L107): Validates SHAP value matrices.
