---
type: script
title: "datasets"
source_path: "src/regression_model_template/io/datasets.py"
description: "Read/Write datasets from/to external sources/destinations."
tags: [script, regression_model_template]
last_verified_commit: "c0c5dbc"
---

# datasets

Source File: `src/regression_model_template/io/datasets.py`

Read/Write datasets from/to external sources/destinations.

```mermaid
classDiagram
    class Reader {
        +KIND
        +limit
        +read() : Any
        +lineage(name, data, targets, predictions) : Lineage
    }
    class ParquetReader {
        +KIND
        +path
        +read() : Any
        +lineage(name, data, targets, predictions) : Lineage
    }
    Reader <|-- ParquetReader
    class Writer {
        +KIND
        +write(data) : None
    }
    class ParquetWriter {
        +KIND
        +path
        +write(data) : None
    }
    Writer <|-- ParquetWriter
```

```mermaid
flowchart TD

    datasets --> abc
    datasets --> mlflow
    datasets --> pandas
    datasets --> pydantic
    datasets --> typing
```
