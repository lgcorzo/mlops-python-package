---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: schemas"
source_path: "src/regression_model_template/core/schemas.py"
description: "Define and validate dataframe schemas."
tags: ["module", "schemas"]
timestamp: "2026-08-14T05:37:38Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "ce3f2af"
---
# Module Specification: schemas

* **Source Reference:** [src/regression_model_template/core/schemas.py](../../../../src/regression_model_template/core/schemas.py)

## 1. Architectural Role & Responsibilities
Define and validate dataframe schemas.

### Detected Architecture Patterns
Detected roles: DTO

## 2. UML Diagrams
### Class Diagram
```plantuml
classDiagram
    direction BT
    class Schema {
        +check(cls: T.Type~TSchema~, data: pd.DataFrame) papd.DataFrame~TSchema~
    }
    DataFrameModel <|-- Schema : Generalization
    class InputsSchema {
        +instant: papd.Index~padt.UInt32~
        +dteday: papd.Series~padt.DateTime~
        +season: papd.Series~padt.UInt8~
        +yr: papd.Series~padt.UInt8~
        +mnth: papd.Series~padt.UInt8~
        +hr: papd.Series~padt.UInt8~
        +holiday: papd.Series~padt.Bool~
        +weekday: papd.Series~padt.UInt8~
        +workingday: papd.Series~padt.Bool~
        +weathersit: papd.Series~padt.UInt8~
        +temp: papd.Series~padt.Float16~
        +atemp: papd.Series~padt.Float16~
        +hum: papd.Series~padt.Float16~
        +windspeed: papd.Series~padt.Float16~
        +casual: papd.Series~padt.UInt32~
        +registered: papd.Series~padt.UInt32~
    }
    Schema <|-- InputsSchema : Generalization
    class TargetsSchema {
        +instant: papd.Index~padt.UInt32~
        +cnt: papd.Series~padt.UInt32~
    }
    Schema <|-- TargetsSchema : Generalization
    class OutputsSchema {
        +instant: papd.Index~padt.UInt32~
        +prediction: papd.Series~padt.UInt32~
    }
    Schema <|-- OutputsSchema : Generalization
    class SHAPValuesSchema {
    }
    Schema <|-- SHAPValuesSchema : Generalization
    class FeatureImportancesSchema {
        +feature: papd.Series~str~
        +importance: papd.Series~float~
    }
    Schema <|-- FeatureImportancesSchema : Generalization
```

### Sequence Diagram
```plantuml
sequenceDiagram
    Schema.check->>cast: invoke
    Schema.check->>validate: invoke
```

### Component Diagram
```plantuml
component [schemas] as Comp
Comp --> [typing]
Comp --> [pandas]
Comp --> [pandera]
Comp --> [typing]
Comp --> [common]
```

## 3. Class & Method Specifications

### `Schema`

Base class for a dataframe schema.

Use a schema to type your dataframe object.
e.g., to communicate and validate its fields.

#### Public Methods
* **`check(cls: T.Type[TSchema], data: pd.DataFrame) -> papd.DataFrame[TSchema]`**
  - **Purpose**: Check the dataframe with this schema.
  - **Inputs**:
    - `cls` (`T.Type[TSchema]`)
    - `data` (`pd.DataFrame`)
  - **Outputs**: `papd.DataFrame[TSchema]`

### `InputsSchema`

Schema for the project inputs.

#### Attributes
* **`instant`** (`papd.Index[padt.UInt32]`)
* **`dteday`** (`papd.Series[padt.DateTime]`)
* **`season`** (`papd.Series[padt.UInt8]`)
* **`yr`** (`papd.Series[padt.UInt8]`)
* **`mnth`** (`papd.Series[padt.UInt8]`)
* **`hr`** (`papd.Series[padt.UInt8]`)
* **`holiday`** (`papd.Series[padt.Bool]`)
* **`weekday`** (`papd.Series[padt.UInt8]`)
* **`workingday`** (`papd.Series[padt.Bool]`)
* **`weathersit`** (`papd.Series[padt.UInt8]`)
* **`temp`** (`papd.Series[padt.Float16]`)
* **`atemp`** (`papd.Series[padt.Float16]`)
* **`hum`** (`papd.Series[padt.Float16]`)
* **`windspeed`** (`papd.Series[padt.Float16]`)
* **`casual`** (`papd.Series[padt.UInt32]`)
* **`registered`** (`papd.Series[padt.UInt32]`)

### `TargetsSchema`

Schema for the project target.

#### Attributes
* **`instant`** (`papd.Index[padt.UInt32]`)
* **`cnt`** (`papd.Series[padt.UInt32]`)

### `OutputsSchema`

Schema for the project output.

#### Attributes
* **`instant`** (`papd.Index[padt.UInt32]`)
* **`prediction`** (`papd.Series[padt.UInt32]`)

### `SHAPValuesSchema`

Schema for the project shap values.

### `FeatureImportancesSchema`

Schema for the project feature importances.

#### Attributes
* **`feature`** (`papd.Series[str]`)
* **`importance`** (`papd.Series[float]`)

## Dependencies

* `typing`
* `pandas`
* `pandera`
* `pandera.typing`
* `pandera.typing.common`

## Used By

* [kafka_app.py](../../regression_model_template/controller/kafka_app.md)
* [metrics.py](../../regression_model_template/core/metrics.md)
* [models.py](../../regression_model_template/core/models.md)
* [init_data.py](../../regression_model_template/init_data.md)
* [registries.py](../../regression_model_template/io/registries.md)
* [evaluations.py](../../regression_model_template/jobs/evaluations.md)
* [explanations.py](../../regression_model_template/jobs/explanations.md)
* [inference.py](../../regression_model_template/jobs/inference.md)
* [training.py](../../regression_model_template/jobs/training.md)
* [tuning.py](../../regression_model_template/jobs/tuning.md)
* [searchers.py](../../regression_model_template/utils/searchers.md)
* [signers.py](../../regression_model_template/utils/signers.md)
* [splitters.py](../../regression_model_template/utils/splitters.md)
* [conftest.py](../../tests/conftest.md)
* [test_metrics.py](../../tests/core/test_metrics.md)
* [test_models.py](../../tests/core/test_models.md)
* [test_schemas.py](../../tests/core/test_schemas.md)
* [test_datasets.py](../../tests/io/test_datasets.md)
* [test_registries.py](../../tests/io/test_registries.md)
* [test_evaluations.py](../../tests/jobs/test_evaluations.md)
* [test_training.py](../../tests/jobs/test_training.md)
* [test_tuning.py](../../tests/jobs/test_tuning.md)
* [test_searchers.py](../../tests/utils/test_searchers.md)
* [test_signers.py](../../tests/utils/test_signers.md)
* [test_splitters.py](../../tests/utils/test_splitters.md)
