---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: module_pages"
source_path: "Scripts/wiki_generator/module_pages.py"
description: "No description available."
tags: ["module", "module_pages"]
timestamp: "2026-10-03T12:52:38Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "d186315"
---
# Module Specification: module_pages

* **Source Reference:** [Scripts/wiki_generator/module_pages.py](../../../../Scripts/wiki_generator/module_pages.py)

# Module Overview

## Purpose

No description available.

## Responsibilities

No description available.

## Dependencies

* `config.make_frontmatter`

# Each File Documentation

## Imported modules

* `config.make_frontmatter`

## Exported functions

* `get_module_pages`

### Detected Architecture Patterns

Detected roles: General Subsystem

## 2. UML Diagrams

### Class Diagram

_No classes found._

### Sequence Diagram

```plantuml
sequenceDiagram
    get_module_pages->>make_frontmatter: invoke
    get_module_pages->>pop: invoke
```

### Component Diagram

```plantuml
component [module_pages] as Comp
Comp --> [make_frontmatter]
```

## 3. Class & Method Specifications

## Standalone Functions

### `get_module_pages() -> Any`

### Description

No description available.

### Inputs

### Output

* **return type**: Any

## Used By

_Not used by any other module._
