---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: schemas"
source_path: "src/regression_model_template/core/schemas.py"
description: "Define and validate dataframe schemas."
tags: ["module", "schemas"]
timestamp: "2026-09-05T05:14:18Z"
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

_No interfaces found._

## Public API

_See exported classes and functions._

## Internal architecture

_See architectural detected patterns and UML._

## Execution flow

_Execution flow depends on public API usage._

## Sequence explanation

_See sequence diagram._

## UML

_See diagrams below._

## Examples

_No module level examples available._

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

# Public Classes

### `Schema`

## Overview

Base class for a dataframe schema.

Use a schema to type your dataframe object.
e.g., to communicate and validate its fields.

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

## Public Methods

### `check(cls: T.Type[TSchema], data: pd.DataFrame) -> papd.DataFrame[TSchema]`

### Description

Check the dataframe with this schema.

### Inputs

* `cls`

  - **type**: T.Type[TSchema]

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `data`

  - **type**: pd.DataFrame

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: papd.DataFrame[TSchema]

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for check

```

### `InputsSchema`

## Overview

Schema for the project inputs.

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

## Attributes

* **`instant`**

  - **Type**: papd.Index[padt.UInt32]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`dteday`**

  - **Type**: papd.Series[padt.DateTime]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`season`**

  - **Type**: papd.Series[padt.UInt8]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`yr`**

  - **Type**: papd.Series[padt.UInt8]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`mnth`**

  - **Type**: papd.Series[padt.UInt8]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`hr`**

  - **Type**: papd.Series[padt.UInt8]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`holiday`**

  - **Type**: papd.Series[padt.Bool]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`weekday`**

  - **Type**: papd.Series[padt.UInt8]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`workingday`**

  - **Type**: papd.Series[padt.Bool]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`weathersit`**

  - **Type**: papd.Series[padt.UInt8]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`temp`**

  - **Type**: papd.Series[padt.Float16]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`atemp`**

  - **Type**: papd.Series[padt.Float16]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`hum`**

  - **Type**: papd.Series[padt.Float16]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`windspeed`**

  - **Type**: papd.Series[padt.Float16]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`casual`**

  - **Type**: papd.Series[padt.UInt32]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`registered`**

  - **Type**: papd.Series[padt.UInt32]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

### `TargetsSchema`

## Overview

Schema for the project target.

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

## Attributes

* **`instant`**

  - **Type**: papd.Index[padt.UInt32]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`cnt`**

  - **Type**: papd.Series[padt.UInt32]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

### `OutputsSchema`

## Overview

Schema for the project output.

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

## Attributes

* **`instant`**

  - **Type**: papd.Index[padt.UInt32]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`prediction`**

  - **Type**: papd.Series[padt.UInt32]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

### `SHAPValuesSchema`

## Overview

Schema for the project shap values.

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

### `FeatureImportancesSchema`

## Overview

Schema for the project feature importances.

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

## Attributes

* **`feature`**

  - **Type**: papd.Series[str]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`importance`**

  - **Type**: papd.Series[float]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

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
