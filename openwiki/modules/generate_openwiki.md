---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: generate_openwiki"
source_path: "generate_openwiki.py"
description: "No description available."
tags: ["module", "generate_openwiki"]
timestamp: "2026-08-13T05:18:56Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "ce3f2af"
---
# Module Specification: generate_openwiki

* **Source Reference:** [generate_openwiki.py](../../generate_openwiki.py)

## 1. Architectural Role & Responsibilities
No description available.

### Detected Architecture Patterns
Detected roles: General Subsystem

## 2. UML Diagrams
### Class Diagram
_No classes found._

### Sequence Diagram
```plantuml
sequenceDiagram
    run_command->>run: invoke
    run_command->>strip: invoke
    run_command->>print: invoke
    get_last_commit->>run_command: invoke
    is_ignored->>split: invoke
    get_changed_files->>run_command: invoke
    get_changed_files->>split: invoke
    get_changed_files->>endswith: invoke
    get_changed_files->>is_ignored: invoke
    delete_generated_docs->>exists: invoke
    delete_generated_docs->>walk: invoke
    delete_generated_docs->>join: invoke
    delete_generated_docs->>remove: invoke
    delete_generated_docs->>rmdir: invoke
    extract_calls->>walk: invoke
    extract_calls->>list: invoke
    extract_calls->>isinstance: invoke
    extract_calls->>fromkeys: invoke
    extract_calls->>append: invoke
    extract_complex_doc->>split: invoke
    extract_complex_doc->>startswith: invoke
    extract_complex_doc->>strip: invoke
    extract_complex_doc->>lower: invoke
    extract_complex_doc->>append: invoke
    extract_complex_doc->>join: invoke
    unparse_annotation->>isinstance: invoke
    unparse_annotation->>unparse: invoke
    unparse_annotation->>unparse_annotation: invoke
    unparse_annotation->>str: invoke
    unparse_annotation->>join: invoke
    extract_docstring->>get_docstring: invoke
    parse_args->>enumerate: invoke
    parse_args->>len: invoke
    parse_args->>append: invoke
    parse_args->>unparse_annotation: invoke
    parse_args->>unparse: invoke
    parse_python_file->>parse: invoke
    parse_python_file->>extract_docstring: invoke
    parse_python_file->>open: invoke
    parse_python_file->>read: invoke
    parse_python_file->>isinstance: invoke
    parse_python_file->>append: invoke
    parse_python_file->>extract_complex_doc: invoke
    parse_python_file->>extract_calls: invoke
    parse_python_file->>startswith: invoke
    parse_python_file->>unparse_annotation: invoke
    parse_python_file->>parse_args: invoke
    clean_plantuml_type->>replace: invoke
    generate_plantuml->>append: invoke
    generate_plantuml->>join: invoke
    generate_plantuml->>clean_plantuml_type: invoke
    generate_plantuml->>split: invoke
    build_registry->>parse_python_file: invoke
    generate_package_diagram_content->>set: invoke
    generate_package_diagram_content->>keys: invoke
    generate_package_diagram_content->>sorted: invoke
    generate_package_diagram_content->>append: invoke
    generate_package_diagram_content->>join: invoke
    generate_package_diagram_content->>split: invoke
    generate_package_diagram_content->>add: invoke
    generate_call_graph->>set: invoke
    generate_call_graph->>items: invoke
    generate_call_graph->>sorted: invoke
    generate_call_graph->>append: invoke
    generate_call_graph->>join: invoke
    generate_call_graph->>add: invoke
    generate_call_graph->>get: invoke
    generate_dependency_graph->>items: invoke
    generate_dependency_graph->>append: invoke
    generate_dependency_graph->>join: invoke
    generate_dependency_graph->>splitext: invoke
    generate_dependency_graph->>basename: invoke
    generate_dependency_graph->>split: invoke
    generate_markdown->>strftime: invoke
    generate_markdown->>get_last_commit: invoke
    generate_markdown->>relpath: invoke
    generate_markdown->>append: invoke
    generate_markdown->>generate_plantuml: invoke
    generate_markdown->>replace: invoke
    generate_markdown->>items: invoke
    generate_markdown->>splitext: invoke
    generate_markdown->>dirname: invoke
    generate_markdown->>lower: invoke
    generate_markdown->>get: invoke
    generate_markdown->>join: invoke
    generate_markdown->>sorted: invoke
    generate_markdown->>basename: invoke
    generate_markdown->>now: invoke
    generate_markdown->>split: invoke
    generate_markdown->>startswith: invoke
    generate_markdown->>splitlines: invoke
    update_index_files->>exists: invoke
    update_index_files->>sort: invoke
    update_index_files->>strftime: invoke
    update_index_files->>get_last_commit: invoke
    update_index_files->>makedirs: invoke
    update_index_files->>sorted: invoke
    update_index_files->>walk: invoke
    update_index_files->>dirname: invoke
    update_index_files->>open: invoke
    update_index_files->>write: invoke
    update_index_files->>list: invoke
    update_index_files->>now: invoke
    update_index_files->>generate_package_diagram_content: invoke
    update_index_files->>generate_dependency_graph: invoke
    update_index_files->>generate_call_graph: invoke
    update_index_files->>keys: invoke
    update_index_files->>endswith: invoke
    update_index_files->>relpath: invoke
    update_index_files->>append: invoke
    update_index_files->>join: invoke
    update_index_files->>lower: invoke
    main->>ArgumentParser: invoke
    main->>add_argument: invoke
    main->>parse_args: invoke
    main->>walk: invoke
    main->>build_registry: invoke
    main->>print: invoke
    main->>makedirs: invoke
    main->>update_index_files: invoke
    main->>delete_generated_docs: invoke
    main->>get_changed_files: invoke
    main->>set: invoke
    main->>list: invoke
    main->>parse_python_file: invoke
    main->>join: invoke
    main->>generate_markdown: invoke
    main->>endswith: invoke
    main->>replace: invoke
    main->>items: invoke
    main->>startswith: invoke
    main->>dirname: invoke
    main->>open: invoke
    main->>write: invoke
    main->>relpath: invoke
    main->>append: invoke
    main->>splitext: invoke
    main->>len: invoke
    main->>basename: invoke
    main->>add: invoke
```

### Component Diagram
```plantuml
component [generate_openwiki] as Comp
Comp --> [argparse]
Comp --> [ast]
Comp --> [datetime]
Comp --> [os]
Comp --> [subprocess]
```

## 3. Class & Method Specifications

## Standalone Functions

### `run_command(command: Any, ignore_errors: Any) -> Any`
No description available.

#### Inputs
* `command` (`Any`)
* `ignore_errors` (`Any`)

#### Outputs
* `Any`

### `get_last_commit() -> Any`
No description available.

#### Inputs

#### Outputs
* `Any`

### `is_ignored(filepath: Any) -> Any`
No description available.

#### Inputs
* `filepath` (`Any`)

#### Outputs
* `Any`

### `get_changed_files() -> Any`
No description available.

#### Inputs

#### Outputs
* `Any`

### `delete_generated_docs() -> Any`
No description available.

#### Inputs

#### Outputs
* `Any`

### `extract_calls(node: Any) -> Any`
No description available.

#### Inputs
* `node` (`Any`)

#### Outputs
* `Any`

### `extract_complex_doc(docstring: Any) -> Any`
No description available.

#### Inputs
* `docstring` (`Any`)

#### Outputs
* `Any`

### `unparse_annotation(node: Any) -> Any`
No description available.

#### Inputs
* `node` (`Any`)

#### Outputs
* `Any`

### `extract_docstring(node: Any) -> Any`
No description available.

#### Inputs
* `node` (`Any`)

#### Outputs
* `Any`

### `parse_args(args: Any) -> Any`
No description available.

#### Inputs
* `args` (`Any`)

#### Outputs
* `Any`

### `parse_python_file(filepath: Any) -> Any`
No description available.

#### Inputs
* `filepath` (`Any`)

#### Outputs
* `Any`

### `clean_plantuml_type(t: Any) -> Any`
Make type string safe for PlantUML.

#### Inputs
* `t` (`Any`)

#### Outputs
* `Any`

### `generate_plantuml(classes: Any) -> Any`
Generate PlantUML class diagram for the classes.

#### Inputs
* `classes` (`Any`)

#### Outputs
* `Any`

### `build_registry(files_to_process: Any) -> Any`
No description available.

#### Inputs
* `files_to_process` (`Any`)

#### Outputs
* `Any`

### `generate_package_diagram_content() -> Any`
No description available.

#### Inputs

#### Outputs
* `Any`

### `generate_call_graph() -> Any`
No description available.

#### Inputs

#### Outputs
* `Any`

### `generate_dependency_graph() -> Any`
No description available.

#### Inputs

#### Outputs
* `Any`

### `generate_markdown(parsed_data: Any, relative_filepath: Any, md_path: Any) -> Any`
No description available.

#### Inputs
* `parsed_data` (`Any`)
* `relative_filepath` (`Any`)
* `md_path` (`Any`)

#### Outputs
* `Any`

### `update_index_files(processed_files: Any) -> Any`
No description available.

#### Inputs
* `processed_files` (`Any`)

#### Outputs
* `Any`

### `main() -> Any`
No description available.

#### Inputs

#### Outputs
* `Any`

## Dependencies

* `argparse`
* `ast`
* `datetime`
* `os`
* `subprocess`

## Used By

_Not used by any other module._
