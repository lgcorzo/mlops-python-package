---
iso_doc_type: "architecture_description"
iso_viewpoint: "information_and_development"
type: "ast_architecture"
mission_id: "lgcorzo-mlops-python-package-476"
verified: "false"
visibility: "public"
---

# AST & Module Architecture (`lgcorzo-mlops-python-package-476`)

## Structural Module Topology

- **Control Plane (`factory-poller`)**: Polls GitHub/GitLab repositories for `autonomous-mission` issues and `main` branch SHA transitions, dispatching work to Kafka and Hatchet.
- **Workflow Engine (`Hatchet` / `factory-worker`)**: Runs the `darkgravitymission-dev-lgcorzo` DAG across `rustant-plan`, `zeroclaw-execute`, `zeroclaw-validate`, `rustant-review`, and `factory-deliver`.
- **Execution Sandbox (`gVisor`)**: Isolates generated unit tests and AST checks (`launch_sandbox_pod`) under `runsc` container sandboxing.
- **Knowledge Graph & Vector Store (`R2R` / `pgvector`)**: Runs `r2r_ingest-files`, `r2r_graph-extraction`, and `r2r_graph-clustering` via Hatchet to populate collection entities, relationships, and Leiden community summaries.

## Verification Evidence

Generated during TDD Green Phase for task `T002` (Generate ISO 42010 / OKF living Wiki (openwiki/Home.md & openwiki/AST_Architecture.md)).
