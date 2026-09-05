---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: convert_links"
source_path: "skills/validate/scripts/convert_links.py"
description: "No description available."
tags: ["module", "convert_links"]
timestamp: "2026-09-05T11:29:30Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "4860b15"
---
# Module Specification: convert_links

* **Source Reference:** [skills/validate/scripts/convert_links.py](../../../../../skills/validate/scripts/convert_links.py)

# Module Overview

## Purpose

No description available.

## Responsibilities

No description available.

## Dependencies

* `os`

* `re`

* `glob`

# Each File Documentation

## Imported modules

* `os`

* `re`

* `glob`

## Exported functions

* `camel_to_snake`

* `resolve_wiki_link`

* `convert_file`

* `main`

### Detected Architecture Patterns

Detected roles: General Subsystem

## 2. UML Diagrams

### Class Diagram

_No classes found._

### Sequence Diagram

```plantuml
sequenceDiagram
    camel_to_snake->>sub: invoke
    camel_to_snake->>lower: invoke
    resolve_wiki_link->>split: invoke
    resolve_wiki_link->>normpath: invoke
    resolve_wiki_link->>exists: invoke
    resolve_wiki_link->>walk: invoke
    resolve_wiki_link->>append: invoke
    resolve_wiki_link->>join: invoke
    resolve_wiki_link->>relpath: invoke
    resolve_wiki_link->>camel_to_snake: invoke
    resolve_wiki_link->>splitext: invoke
    resolve_wiki_link->>lower: invoke
    convert_file->>dirname: invoke
    convert_file->>compile: invoke
    convert_file->>sub: invoke
    convert_file->>open: invoke
    convert_file->>read: invoke
    convert_file->>strip: invoke
    convert_file->>resolve_wiki_link: invoke
    convert_file->>groups: invoke
    convert_file->>startswith: invoke
    convert_file->>normpath: invoke
    convert_file->>append: invoke
    convert_file->>group: invoke
    convert_file->>split: invoke
    convert_file->>join: invoke
    convert_file->>exists: invoke
    convert_file->>int: invoke
    convert_file->>write: invoke
    convert_file->>relpath: invoke
    convert_file->>len: invoke
    main->>abspath: invoke
    main->>glob: invoke
    main->>print: invoke
    main->>exists: invoke
    main->>join: invoke
    main->>convert_file: invoke
    main->>len: invoke
```

### Component Diagram

```plantuml
component [convert_links] as Comp
Comp --> [os]
Comp --> [re]
Comp --> [glob]
```

## 3. Class & Method Specifications

## Standalone Functions

### `camel_to_snake(name: Any) -> Any`

### Description

No description available.

### Inputs

* `name`

  - **type**: Any

  - **optional?**: No

### Output

* **return type**: Any

### `resolve_wiki_link(link_content: Any, current_file_dir: Any, wiki_root: Any) -> Any`

### Description

No description available.

### Inputs

* `link_content`

  - **type**: Any

  - **optional?**: No

* `current_file_dir`

  - **type**: Any

  - **optional?**: No

* `wiki_root`

  - **type**: Any

  - **optional?**: No

### Output

* **return type**: Any

### `convert_file(file_path: Any, wiki_root: Any) -> Any`

### Description

No description available.

### Inputs

* `file_path`

  - **type**: Any

  - **optional?**: No

* `wiki_root`

  - **type**: Any

  - **optional?**: No

### Output

* **return type**: Any

### `main() -> Any`

### Description

No description available.

### Inputs

### Output

* **return type**: Any

## Used By

_Not used by any other module._
