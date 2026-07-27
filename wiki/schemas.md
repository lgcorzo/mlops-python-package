---
type: script
title: "schemas"
source_path: "src/regression_model_template/core/schemas.py"
description: "Define and validate dataframe schemas."
tags: [script, regression_model_template]
last_verified_commit: "c0c5dbc"
---

# schemas

Source File: `src/regression_model_template/core/schemas.py`

Define and validate dataframe schemas.

```mermaid
classDiagram
    class Schema {
        +check(cls, data) : Any
    }
    class Schema.Config {
        +coerce
        +strict
    }
    class InputsSchema {
        +instant
        +dteday
        +season
        +yr
        +mnth
        +hr
        +holiday
        +weekday
        +workingday
        +weathersit
        +temp
        +atemp
        +hum
        +windspeed
        +casual
        +registered
    }
    Schema <|-- InputsSchema
    class TargetsSchema {
        +instant
        +cnt
    }
    Schema <|-- TargetsSchema
    class OutputsSchema {
        +instant
        +prediction
    }
    Schema <|-- OutputsSchema
    class SHAPValuesSchema {
    }
    Schema <|-- SHAPValuesSchema
    class SHAPValuesSchema.Config {
        +dtype
        +strict
    }
    class FeatureImportancesSchema {
        +feature
        +importance
    }
    Schema <|-- FeatureImportancesSchema
```

```mermaid
flowchart TD

    schemas --> pandas
    schemas --> pandera
    schemas --> typing
```
