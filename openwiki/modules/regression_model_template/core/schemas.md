---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: schemas"
source_path: "src/regression_model_template/core/schemas.py"
description: "Define and validate dataframe schemas."
tags: ["module", "schemas"]
timestamp: "2026-09-06T06:26:18Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "4860b15"
---
# Module Specification: schemas

* **Source Reference:** [src/regression_model_template/core/schemas.py](../../../../src/regression_model_template/core/schemas.py)

# Module Overview

## Purpose

Define and validate dataframe schemas.

## Responsibilities

Define and validate dataframe schemas.

## Dependencies

* `typing`

* `pandas`

* `pandera`

* `pandera.typing`

* `pandera.typing.common`

# Each File Documentation

## Imported modules

* `typing`

* `pandas`

* `pandera`

* `pandera.typing`

* `pandera.typing.common`

## Exported classes

* `Schema`

* `InputsSchema`

* `TargetsSchema`

* `OutputsSchema`

* `SHAPValuesSchema`

* `FeatureImportancesSchema`

## Exported interfaces

_Dependent on implementation_

## Public API

_Dependent on implementation_

## Internal architecture

_Dependent on implementation_

## Execution flow

_Dependent on implementation_

## Sequence explanation

_Dependent on implementation_

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

## Examples

_Dependent on implementation_

## 3. Class & Method Specifications

# Public Classes

### `Schema`

## Overview

Base class for a dataframe schema.

Use a schema to type your dataframe object.
e.g., to communicate and validate its fields.

## Public Methods

* **`check(cls: T.Type[TSchema], data: pd.DataFrame) -> papd.DataFrame[TSchema]`**

### Description

Check the dataframe with this schema.

### Inputs

* `cls`

  - **type**: T.Type[TSchema]

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `data`

  - **type**: pd.DataFrame

  - **meaning**: dataframe to check.

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

### Output

* **return type**: papd.DataFrame[TSchema]

* **semantic meaning**: papd.DataFrame[TSchema]: validated dataframe.

* **possible null values**: _Dependent on implementation_

* **exceptions**: _Dependent on implementation_

### Side Effects

_Dependent on implementation_

### Complexity

Time Complexity: _Dependent on implementation_

Space Complexity: _Dependent on implementation_

### Example

_Dependent on implementation_

### `InputsSchema`

## Overview

Schema for the project inputs.

## Attributes

* **`instant`**

  - **Type**: papd.Index[padt.UInt32]

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`dteday`**

  - **Type**: papd.Series[padt.DateTime]

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`season`**

  - **Type**: papd.Series[padt.UInt8]

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`yr`**

  - **Type**: papd.Series[padt.UInt8]

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`mnth`**

  - **Type**: papd.Series[padt.UInt8]

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`hr`**

  - **Type**: papd.Series[padt.UInt8]

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`holiday`**

  - **Type**: papd.Series[padt.Bool]

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`weekday`**

  - **Type**: papd.Series[padt.UInt8]

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`workingday`**

  - **Type**: papd.Series[padt.Bool]

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`weathersit`**

  - **Type**: papd.Series[padt.UInt8]

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`temp`**

  - **Type**: papd.Series[padt.Float16]

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`atemp`**

  - **Type**: papd.Series[padt.Float16]

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`hum`**

  - **Type**: papd.Series[padt.Float16]

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`windspeed`**

  - **Type**: papd.Series[padt.Float16]

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`casual`**

  - **Type**: papd.Series[padt.UInt32]

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`registered`**

  - **Type**: papd.Series[padt.UInt32]

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

### `TargetsSchema`

## Overview

Schema for the project target.

## Attributes

* **`instant`**

  - **Type**: papd.Index[padt.UInt32]

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`cnt`**

  - **Type**: papd.Series[padt.UInt32]

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

### `OutputsSchema`

## Overview

Schema for the project output.

## Attributes

* **`instant`**

  - **Type**: papd.Index[padt.UInt32]

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`prediction`**

  - **Type**: papd.Series[padt.UInt32]

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

### `SHAPValuesSchema`

## Overview

Schema for the project shap values.

### `FeatureImportancesSchema`

## Overview

Schema for the project feature importances.

## Attributes

* **`feature`**

  - **Type**: papd.Series[str]

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`importance`**

  - **Type**: papd.Series[float]

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

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
