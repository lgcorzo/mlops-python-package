---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: okf_validate"
source_path: "skills/validate/scripts/okf_validate.py"
description: "OKF v0.2 Conformance Checker for OpenWiki Documentation."
tags: ["module", "okf_validate"]
timestamp: "2026-09-05T05:14:17Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "4860b15"
---
# Module Specification: okf_validate

* **Source Reference:** [skills/validate/scripts/okf_validate.py](../../../../../skills/validate/scripts/okf_validate.py)

# Module Overview

## Purpose

OKF v0.2 Conformance Checker for OpenWiki Documentation.

## Responsibilities

OKF v0.2 Conformance Checker for OpenWiki Documentation.

Validates that all Markdown files under the specified wiki directory
comply with the Open Knowledge Format (OKF) v0.2 schema and
ISO/IEC/IEEE 42010/15289 traceability requirements.

Usage:
    python3 okf_validate.py <wiki_path> [--strict]

Exit codes:
    0 — All validations passed.
    1 — One or more validations failed.

## Dependencies

* `argparse`

* `glob`

* `os`

* `re`

* `sys`

* `typing.Any`

# Each File Documentation

## Imported modules

* `argparse`

* `glob`

* `os`

* `re`

* `sys`

* `typing.Any`

## Exported functions

* `extract_frontmatter`

* `check_frontmatter_fields`

* `check_absolute_paths`

* `check_mermaid_syntax`

* `validate_wiki`

* `main`

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

Detected roles: General Subsystem

## 2. UML Diagrams

### Class Diagram

_No classes found._

### Sequence Diagram

```plantuml
sequenceDiagram
    extract_frontmatter->>split: invoke
    extract_frontmatter->>_parse_yaml: invoke
    extract_frontmatter->>startswith: invoke
    extract_frontmatter->>len: invoke
    check_frontmatter_fields->>get: invoke
    check_frontmatter_fields->>append: invoke
    check_frontmatter_fields->>join: invoke
    check_frontmatter_fields->>sorted: invoke
    check_absolute_paths->>enumerate: invoke
    check_absolute_paths->>splitlines: invoke
    check_absolute_paths->>search: invoke
    check_absolute_paths->>append: invoke
    check_mermaid_syntax->>enumerate: invoke
    check_mermaid_syntax->>splitlines: invoke
    check_mermaid_syntax->>strip: invoke
    check_mermaid_syntax->>startswith: invoke
    check_mermaid_syntax->>append: invoke
    check_mermaid_syntax->>count: invoke
    validate_wiki->>sorted: invoke
    validate_wiki->>print: invoke
    validate_wiki->>glob: invoke
    validate_wiki->>relpath: invoke
    validate_wiki->>extract_frontmatter: invoke
    validate_wiki->>extend: invoke
    validate_wiki->>len: invoke
    validate_wiki->>join: invoke
    validate_wiki->>strip: invoke
    validate_wiki->>append: invoke
    validate_wiki->>check_absolute_paths: invoke
    validate_wiki->>getcwd: invoke
    validate_wiki->>open: invoke
    validate_wiki->>read: invoke
    validate_wiki->>check_frontmatter_fields: invoke
    validate_wiki->>check_mermaid_syntax: invoke
    main->>ArgumentParser: invoke
    main->>add_argument: invoke
    main->>parse_args: invoke
    main->>validate_wiki: invoke
    main->>exit: invoke
    main->>isdir: invoke
    main->>print: invoke
```

### Component Diagram

```plantuml
component [okf_validate] as Comp
Comp --> [argparse]
Comp --> [glob]
Comp --> [os]
Comp --> [re]
Comp --> [sys]
Comp --> [Any]
```

## 3. Class & Method Specifications

## Standalone Functions

### `extract_frontmatter(content: str) -> tuple[(dict[(str, Any)], str)]`

### Description

Split YAML frontmatter from Markdown body.

### Inputs

* `content`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: tuple[(dict[(str, Any)], str)]

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for extract_frontmatter

```

### `check_frontmatter_fields(fm: dict[(str, Any)], filepath: str, strict: bool) -> list[str]`

### Description

Validate required and optional frontmatter fields.

### Inputs

* `fm`

  - **type**: dict[(str, Any)]

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `filepath`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `strict`

  - **type**: bool

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: list[str]

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for check_frontmatter_fields

```

### `check_absolute_paths(body: str, filepath: str) -> list[str]`

### Description

Detect absolute file paths in the document body.

### Inputs

* `body`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `filepath`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: list[str]

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for check_absolute_paths

```

### `check_mermaid_syntax(body: str, filepath: str) -> list[str]`

### Description

Basic structural validation of Mermaid code blocks.

### Inputs

* `body`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `filepath`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: list[str]

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for check_mermaid_syntax

```

### `validate_wiki(wiki_path: str, strict: bool) -> int`

### Description

Validate all .md files under wiki_path. Returns error count.

### Inputs

* `wiki_path`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `strict`

  - **type**: bool

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: Yes

  - **default value**: False

### Output

* **return type**: int

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for validate_wiki

```

### `main() -> None`

### Description

No description available.

### Inputs

### Output

* **return type**: None

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for main

```

## Used By

_Not used by any other module._
