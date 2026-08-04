---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDescription"
type: "concept"
title: "osvariables Documentation"
description: "Documentation for src/regression_model_template/io/osvariables.py"
tags: ["module", "osvariables"]
timestamp: "2026-08-04T05:28:53Z"
generated: "agent:ast-documentation-generator"
verified: "true"
---

# Module: `src/regression_model_template/io/osvariables.py`

## Overview
**Purpose**: Module providing various functionalities.

**Architecture Role**: Domain Models

**Dependencies**:
- `typing`
- `pydantic_settings`

**Exported Symbols**:
- `Singleton`
- `Env`

## UML Class Diagram
```plantuml
@startuml
class Singleton {
  +_instances : dict[type, 'Singleton']
  -__new__(cls:type['Singleton']) : 'Singleton'
}
object <|-- Singleton
class Env {
  +mlflow_tracking_uri : str
  +mlflow_registry_uri : str
  +mlflow_experiment_name : str
  +mlflow_registered_model_name : str
}
Singleton <|-- Env
BaseSettings <|-- Env
@enduml
```

## Call Graph
```plantuml
@startuml
Singleton::__new__ --> __new__
Singleton::__new__ --> super
@enduml
```

## Classes
### Class `Singleton`
**Overview**: No description available.

#### Attributes
- `_instances`: dict[type, 'Singleton']
#### Public Methods
#### Private Methods
##### `__new__`
- **Purpose**: No description available.
- **Parameters**: cls
- **Return**: `'Singleton'`

### Class `Env`
**Overview**: No description available.

#### Attributes
- `mlflow_tracking_uri`: str
- `mlflow_registry_uri`: str
- `mlflow_experiment_name`: str
- `mlflow_registered_model_name`: str
#### Public Methods
#### Private Methods
## Functions
