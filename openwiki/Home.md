---
iso_doc_type: "architecture_description"
iso_viewpoint: "context"
type: "wiki_home"
generated: true
verified: "false"
visibility: "public"
---

# Architecture Wiki (`lgcorzo-mlops-python-package-476`)

## System Overview

This repository is governed by the Dark Gravity Autonomous CA/CD Factory (`Generate ISO 42010 / OKF living Wiki (openwiki/Home.md & openwiki/AST_Architecture.md)`). All specification, coding, validation, security review, and knowledge indexing stages execute as an orchestrated workflow in Hatchet.

## Core Components & Relationships

- **RustantAgent** orchestrates Stage 2 planning (`rustant-plan`) by querying R2R GraphRAG via `retrieve_context` and producing Spec-Kit SDD task graphs.
- **ZeroClawAgent** executes Stage 3 TDD tasks (`zeroclaw-execute`) and verification (`zeroclaw-validate`) inside isolated gVisor Kubernetes sandbox pods.
- **Aethelgard Security Gate** performs Stage 4 LLM-as-a-Judge SAST forensic review (`rustant-review`) prior to Pull Request delivery (`factory-deliver`).
- **R2R Knowledge Engine** ingests repository AST maps, OKF wikis, and mission evidence into dedicated pgvector collections and builds Leiden community knowledge graphs for cross-agent retrieval.
