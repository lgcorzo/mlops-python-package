---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: settings"
source_path: "src/regression_model_template/settings.py"
description: "Define settings for the application."
tags: ["module", "settings"]
timestamp: "2026-08-07T08:29:41Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "12aa8d5"
---
# Module Specification: settings

* **Source Reference:** [src/regression_model_template/settings.py](../../src/regression_model_template/settings.py)

## 1. Architectural Role & Responsibilities
Define settings for the application.

## 2. UML 2.0 Class Diagram
```plantuml
classDiagram
    direction BT
    class Settings {
    }
    BaseSettings <|-- Settings : Generalization
    class MainSettings {
        +job: jobs.JobKind
    }
    Settings <|-- MainSettings : Generalization
```

## 3. Class & Method Specifications

### `Settings`

Base class for application settings.

Use settings to provide high-level preferences.
i.e., to separate settings from provider (e.g., CLI).

### `MainSettings`

Main settings of the application.

Parameters:
    job (jobs.JobKind): job to run.

#### Attributes
* **`job`** (`jobs.JobKind`)

## Dependencies

* `pydantic`
* `pydantic_settings`
* `regression_model_template.jobs`

## Used By

* [scripts.py](../regression_model_template/scripts.md)
