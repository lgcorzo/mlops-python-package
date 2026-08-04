---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDescription"
type: "concept"
title: "generate_openwiki Documentation"
description: "Documentation for generate_openwiki.py"
tags: ["module", "generate_openwiki"]
timestamp: "2026-08-04T05:28:53Z"
generated: "agent:ast-documentation-generator"
verified: "true"
---

# Module: `generate_openwiki.py`

## Overview
**Purpose**: Module providing various functionalities.

**Architecture Role**: Infrastructure

**Dependencies**:
- `ast`
- `shutil`
- `datetime`
- `sys`
- `re`
- `pathlib`
- `subprocess`
- `os`

**Exported Symbols**:
- `get_git_diff_files`
- `extract_type`
- `parse_docstring_tags`
- `extract_complexity`
- `extract_side_effects`
- `parse_class`
- `parse_function`
- `parse_file`
- `generate_plantuml_class`
- `detect_architecture`
- `generate_markdown`
- `write_file`
- `setup_openwiki_structure`
- `generate_global_diagrams`
- `generate_architecture`
- `generate_summary`
- `main`

## UML Class Diagram
```plantuml
@startuml
@enduml
```

## Call Graph
```plantuml
@startuml
get_git_diff_files --> run
get_git_diff_files --> split
get_git_diff_files --> run
get_git_diff_files --> split
get_git_diff_files --> any
get_git_diff_files --> run
get_git_diff_files --> split
get_git_diff_files --> strip
get_git_diff_files --> strip
get_git_diff_files --> set
get_git_diff_files --> strip
get_git_diff_files --> endswith
get_git_diff_files --> exists
extract_type --> unparse
parse_docstring_tags --> split
parse_docstring_tags --> enumerate
parse_docstring_tags --> lower
parse_docstring_tags --> lower
parse_docstring_tags --> strip
extract_complexity --> parse_docstring_tags
extract_side_effects --> parse_docstring_tags
parse_class --> isinstance
parse_class --> unparse
parse_class --> get_docstring
parse_class --> parse_function
parse_class --> isinstance
parse_class --> append
parse_class --> isinstance
parse_class --> isinstance
parse_class --> append
parse_class --> isinstance
parse_class --> extract_type
parse_class --> append
parse_function --> walk
parse_function --> extract_complexity
parse_function --> extract_side_effects
parse_function --> extract_type
parse_function --> append
parse_function --> isinstance
parse_function --> startswith
parse_function --> get_docstring
parse_function --> isinstance
parse_function --> extract_type
parse_function --> append
parse_function --> isinstance
parse_function --> append
parse_file --> parse
parse_file --> isinstance
parse_file --> open
parse_file --> read
parse_file --> print
parse_file --> get_docstring
parse_file --> isinstance
parse_file --> append
parse_file --> isinstance
parse_file --> append
parse_file --> parse_class
parse_file --> append
parse_file --> isinstance
parse_file --> startswith
parse_file --> append
parse_file --> parse_function
parse_file --> append
parse_file --> startswith
parse_file --> append
generate_plantuml_class --> append
generate_plantuml_class --> join
generate_plantuml_class --> append
generate_plantuml_class --> join
generate_plantuml_class --> append
generate_plantuml_class --> join
generate_plantuml_class --> append
generate_plantuml_class --> append
detect_architecture --> lower
generate_markdown --> detect_architecture
generate_markdown --> strftime
generate_markdown --> set
generate_markdown --> Path
generate_markdown --> now
generate_markdown --> generate_plantuml_class
generate_markdown --> splitlines
generate_markdown --> join
write_file --> makedirs
write_file --> dirname
write_file --> open
write_file --> write
setup_openwiki_structure --> makedirs
setup_openwiki_structure --> join
generate_global_diagrams --> set
generate_global_diagrams --> sorted
generate_global_diagrams --> write_file
generate_global_diagrams --> write_file
generate_global_diagrams --> range
generate_global_diagrams --> add
generate_global_diagrams --> join
generate_global_diagrams --> replace
generate_global_diagrams --> Path
generate_global_diagrams --> len
generate_global_diagrams --> join
generate_global_diagrams --> Path
generate_architecture --> items
generate_architecture --> write_file
generate_architecture --> detect_architecture
generate_architecture --> append
generate_architecture --> replace
generate_summary --> sorted
generate_summary --> sorted
generate_summary --> write_file
generate_summary --> replace
generate_summary --> replace
generate_summary --> append
generate_summary --> startswith
generate_summary --> startswith
generate_summary --> lower
main --> lower
main --> len
main --> print
main --> exit
main --> exists
main --> makedirs
main --> setup_openwiki_structure
main --> walk
main --> generate_summary
main --> generate_global_diagrams
main --> generate_architecture
main --> write_file
main --> rmtree
main --> setup_openwiki_structure
main --> get_git_diff_files
main --> walk
main --> generate_summary
main --> generate_global_diagrams
main --> generate_architecture
main --> print
main --> print
main --> endswith
main --> strftime
main --> join
main --> startswith
main --> parse_file
main --> endswith
main --> append
main --> generate_markdown
main --> join
main --> write_file
main --> now
main --> join
main --> startswith
main --> startswith
main --> replace
main --> parse_file
main --> parse_file
main --> startswith
main --> append
main --> generate_markdown
main --> join
main --> write_file
main --> append
main --> replace
@enduml
```

## Classes
## Functions
### Function `get_git_diff_files`
- **Description**: No description available.
- **Inputs**:
- **Output**: `Any`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `extract_type`
- **Description**: No description available.
- **Inputs**:
  - `annotation`: Any
- **Output**: `Any`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `parse_docstring_tags`
- **Description**: Simple parser to find things like Time O(N) or Side Effects: ... in docstrings.
- **Inputs**:
  - `docstring`: Any
  - `tag`: Any
- **Output**: `Any`
- **Side Effects**: Simple parser to find things like Time O(N) or Side Effects: ... in docstrings.
- **Complexity**: Not documented

### Function `extract_complexity`
- **Description**: No description available.
- **Inputs**:
  - `docstring`: Any
- **Output**: `Any`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `extract_side_effects`
- **Description**: No description available.
- **Inputs**:
  - `docstring`: Any
- **Output**: `Any`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `parse_class`
- **Description**: No description available.
- **Inputs**:
  - `node`: Any
- **Output**: `Any`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `parse_function`
- **Description**: No description available.
- **Inputs**:
  - `node`: Any
- **Output**: `Any`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `parse_file`
- **Description**: No description available.
- **Inputs**:
  - `filepath`: Any
- **Output**: `Any`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `generate_plantuml_class`
- **Description**: No description available.
- **Inputs**:
  - `cls_info`: Any
- **Output**: `Any`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `detect_architecture`
- **Description**: No description available.
- **Inputs**:
  - `filepath`: Any
- **Output**: `Any`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `generate_markdown`
- **Description**: No description available.
- **Inputs**:
  - `module_info`: Any
- **Output**: `Any`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `write_file`
- **Description**: No description available.
- **Inputs**:
  - `path`: Any
  - `content`: Any
- **Output**: `Any`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `setup_openwiki_structure`
- **Description**: No description available.
- **Inputs**:
- **Output**: `Any`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `generate_global_diagrams`
- **Description**: No description available.
- **Inputs**:
  - `modules`: Any
- **Output**: `Any`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `generate_architecture`
- **Description**: No description available.
- **Inputs**:
  - `modules`: Any
- **Output**: `Any`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `generate_summary`
- **Description**: No description available.
- **Inputs**:
  - `modules`: Any
- **Output**: `Any`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `main`
- **Description**: No description available.
- **Inputs**:
- **Output**: `Any`
- **Side Effects**: Not documented
- **Complexity**: Not documented
