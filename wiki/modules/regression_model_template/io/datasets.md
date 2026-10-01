---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "regression_model_template::io::datasets — Tabular Dataset I/O & Lineage"
source_path: "src/regression_model_template/io/datasets.py"
description: "Abstract Reader/Writer interfaces and concrete Parquet implementations with automated lineage extraction."
tags: ["iso42010", "okf", "component_view", "datasets", "parquet", "lineage"]
timestamp: "2026-10-01T17:50:00Z"
generated: "agent:wiki-iso-documentation-standard"
verified: "true"
last_verified_commit: "073b5fd"
---

# regression_model_template::io::datasets — Tabular Dataset I/O & Lineage

> **Source**: `src/regression_model_template/io/datasets.py` (Lines: L1-L128)  
> **Layer**: Infrastructure  
> **Role**: Standardized reading and writing of tabular Parquet datasets with automated data lineage recording for MLflow tracking.

---

## 1. Class Diagram

```mermaid
classDiagram
    class Reader {
        <<abstract>>
        +str KIND
        +int limit
        +read() DataFrame*
        +lineage(name: str, data: DataFrame, targets, predictions) Lineage
    }

    class ParquetReader {
        +str KIND = "ParquetReader"
        +str path
        +read() DataFrame
        +lineage(name: str, data: DataFrame, targets, predictions) Lineage
    }
    ParquetReader --|> Reader : implements

    class Writer {
        <<abstract>>
        +str KIND
        +write(data: DataFrame) None*
    }

    class ParquetWriter {
        +str KIND = "ParquetWriter"
        +str path
        +write(data: DataFrame) None
    }
    ParquetWriter --|> Writer : implements
```

---

> *Related: [Schemas](../core/schemas.md) · [Data Model](../../../architecture/mission_data_model.md)*
