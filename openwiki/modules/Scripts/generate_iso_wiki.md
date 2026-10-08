---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: generate_iso_wiki"
source_path: "Scripts/generate_iso_wiki.py"
description: "generate_iso_wiki.py"
tags: ["module", "generate_iso_wiki"]
timestamp: "2026-10-08T15:04:16Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "a2a679e"
---
# Module Specification: generate_iso_wiki

* **Source Reference:** [Scripts/generate_iso_wiki.py](../../../Scripts/generate_iso_wiki.py)

# Module Overview

## Purpose

generate_iso_wiki.py

## Responsibilities

generate_iso_wiki.py

Primary orchestrator generating the complete ISO/IEC/IEEE 42010:2022 and 15289:2019
compliant wiki documentation in wiki/ adhering strictly to the wiki-iso-documentation-standard skill.

## Dependencies

* `os`

* `sys`

* `shutil`

* `glob`

* `re`

* `wiki_generator.root_pages.get_home_md`

* `wiki_generator.root_pages.get_readme_md`

* `wiki_generator.root_pages.get_sidebar_md`

* `wiki_generator.root_pages.get_index_md`

* `wiki_generator.root_pages.get_glossary_md`

* `wiki_generator.architecture_pages.get_business_context_md`

* `wiki_generator.architecture_pages.get_strategic_design_md`

* `wiki_generator.architecture_pages.get_tactical_design_md`

* `wiki_generator.architecture_pages.get_agent_specifications_md`

* `wiki_generator.architecture_pages.get_runtime_sequences_md`

* `wiki_generator.architecture_pages.get_infrastructure_adapters_md`

* `wiki_generator.architecture_pages.get_mission_data_model_md`

* `wiki_generator.security_pages.get_security_architecture_md`

* `wiki_generator.security_pages.get_hitl_governance_md`

* `wiki_generator.security_pages.get_verification_triad_md`

* `wiki_generator.security_pages.get_compliance_audit_md`

* `wiki_generator.operations_pages.get_user_manual_md`

* `wiki_generator.operations_pages.get_production_operations_md`

* `wiki_generator.operations_pages.get_experiment_logs_md`

* `wiki_generator.quality_pages.get_test_plan_report_md`

* `wiki_generator.module_pages.get_module_pages`

# Each File Documentation

## Imported modules

* `os`

* `sys`

* `shutil`

* `glob`

* `re`

* `wiki_generator.root_pages.get_home_md`

* `wiki_generator.root_pages.get_readme_md`

* `wiki_generator.root_pages.get_sidebar_md`

* `wiki_generator.root_pages.get_index_md`

* `wiki_generator.root_pages.get_glossary_md`

* `wiki_generator.architecture_pages.get_business_context_md`

* `wiki_generator.architecture_pages.get_strategic_design_md`

* `wiki_generator.architecture_pages.get_tactical_design_md`

* `wiki_generator.architecture_pages.get_agent_specifications_md`

* `wiki_generator.architecture_pages.get_runtime_sequences_md`

* `wiki_generator.architecture_pages.get_infrastructure_adapters_md`

* `wiki_generator.architecture_pages.get_mission_data_model_md`

* `wiki_generator.security_pages.get_security_architecture_md`

* `wiki_generator.security_pages.get_hitl_governance_md`

* `wiki_generator.security_pages.get_verification_triad_md`

* `wiki_generator.security_pages.get_compliance_audit_md`

* `wiki_generator.operations_pages.get_user_manual_md`

* `wiki_generator.operations_pages.get_production_operations_md`

* `wiki_generator.operations_pages.get_experiment_logs_md`

* `wiki_generator.quality_pages.get_test_plan_report_md`

* `wiki_generator.module_pages.get_module_pages`

## Exported functions

* `clean_wiki`

* `write_page`

* `generate_all`

* `verify_links`

* `verify_source_coverage`

* `verify_frontmatter`

### Detected Architecture Patterns

Detected roles: General Subsystem

## 2. UML Diagrams

### Class Diagram

_No classes found._

### Sequence Diagram

```plantuml
sequenceDiagram
    clean_wiki->>exists: invoke
    clean_wiki->>makedirs: invoke
    clean_wiki->>listdir: invoke
    clean_wiki->>join: invoke
    clean_wiki->>isdir: invoke
    clean_wiki->>rmtree: invoke
    clean_wiki->>remove: invoke
    write_page->>join: invoke
    write_page->>makedirs: invoke
    write_page->>print: invoke
    write_page->>dirname: invoke
    write_page->>open: invoke
    write_page->>write: invoke
    write_page->>strip: invoke
    generate_all->>print: invoke
    generate_all->>clean_wiki: invoke
    generate_all->>write_page: invoke
    generate_all->>get_module_pages: invoke
    generate_all->>items: invoke
    generate_all->>get_home_md: invoke
    generate_all->>get_readme_md: invoke
    generate_all->>get_sidebar_md: invoke
    generate_all->>get_index_md: invoke
    generate_all->>get_glossary_md: invoke
    generate_all->>get_business_context_md: invoke
    generate_all->>get_strategic_design_md: invoke
    generate_all->>get_tactical_design_md: invoke
    generate_all->>get_agent_specifications_md: invoke
    generate_all->>get_runtime_sequences_md: invoke
    generate_all->>get_infrastructure_adapters_md: invoke
    generate_all->>get_mission_data_model_md: invoke
    generate_all->>get_security_architecture_md: invoke
    generate_all->>get_hitl_governance_md: invoke
    generate_all->>get_verification_triad_md: invoke
    generate_all->>get_compliance_audit_md: invoke
    generate_all->>get_user_manual_md: invoke
    generate_all->>get_production_operations_md: invoke
    generate_all->>get_experiment_logs_md: invoke
    generate_all->>get_test_plan_report_md: invoke
    generate_all->>len: invoke
    verify_links->>print: invoke
    verify_links->>glob: invoke
    verify_links->>compile: invoke
    verify_links->>join: invoke
    verify_links->>dirname: invoke
    verify_links->>open: invoke
    verify_links->>enumerate: invoke
    verify_links->>finditer: invoke
    verify_links->>len: invoke
    verify_links->>split: invoke
    verify_links->>startswith: invoke
    verify_links->>normpath: invoke
    verify_links->>any: invoke
    verify_links->>relpath: invoke
    verify_links->>append: invoke
    verify_links->>group: invoke
    verify_links->>exists: invoke
    verify_source_coverage->>print: invoke
    verify_source_coverage->>glob: invoke
    verify_source_coverage->>join: invoke
    verify_source_coverage->>relpath: invoke
    verify_source_coverage->>exists: invoke
    verify_source_coverage->>append: invoke
    verify_source_coverage->>splitext: invoke
    verify_source_coverage->>len: invoke
    verify_frontmatter->>print: invoke
    verify_frontmatter->>glob: invoke
    verify_frontmatter->>join: invoke
    verify_frontmatter->>relpath: invoke
    verify_frontmatter->>basename: invoke
    verify_frontmatter->>open: invoke
    verify_frontmatter->>read: invoke
    verify_frontmatter->>startswith: invoke
    verify_frontmatter->>append: invoke
    verify_frontmatter->>len: invoke
```

### Component Diagram

```plantuml
component [generate_iso_wiki] as Comp
Comp --> [os]
Comp --> [sys]
Comp --> [shutil]
Comp --> [glob]
Comp --> [re]
Comp --> [get_home_md]
Comp --> [get_readme_md]
Comp --> [get_sidebar_md]
Comp --> [get_index_md]
Comp --> [get_glossary_md]
Comp --> [get_business_context_md]
Comp --> [get_strategic_design_md]
Comp --> [get_tactical_design_md]
Comp --> [get_agent_specifications_md]
Comp --> [get_runtime_sequences_md]
Comp --> [get_infrastructure_adapters_md]
Comp --> [get_mission_data_model_md]
Comp --> [get_security_architecture_md]
Comp --> [get_hitl_governance_md]
Comp --> [get_verification_triad_md]
Comp --> [get_compliance_audit_md]
Comp --> [get_user_manual_md]
Comp --> [get_production_operations_md]
Comp --> [get_experiment_logs_md]
Comp --> [get_test_plan_report_md]
Comp --> [get_module_pages]
```

## 3. Class & Method Specifications

## Standalone Functions

### `clean_wiki() -> Any`

### Description

No description available.

### Inputs

### Output

* **return type**: Any

### `write_page(rel_path: Any, content: Any) -> Any`

### Description

No description available.

### Inputs

* `rel_path`

  - **type**: Any

  - **optional?**: No

* `content`

  - **type**: Any

  - **optional?**: No

### Output

* **return type**: Any

### `generate_all() -> Any`

### Description

No description available.

### Inputs

### Output

* **return type**: Any

### `verify_links() -> Any`

### Description

No description available.

### Inputs

### Output

* **return type**: Any

### `verify_source_coverage() -> Any`

### Description

No description available.

### Inputs

### Output

* **return type**: Any

### `verify_frontmatter() -> Any`

### Description

No description available.

### Inputs

### Output

* **return type**: Any

## Used By

_Not used by any other module._
