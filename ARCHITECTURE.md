# Architecture: `mlops-python-package` in Dark Gravity

## Ecosystem Role & Tier

- **Tier**: `owned_domain`
- **Role**: First-party enterprise MLOps standard package and live integration testbed for Dark Gravity autonomous factory missions (`EXP-2026-013` Mission `#476` and `EXP-2026-014` Swarm Mode Mission `#478`).
- **Visibility**: `public`

## Internal Component Design

- `confs/`, `dvc.yaml`, `MLproject`: Hydra configuration trees, DVC pipeline stages, and MLflow experiment tracking (`poetry.lock` deterministic builds).
- `openwiki/` & `generate_openwiki.py`: Living ISO/OKF documentation generated on verified runs (`openwiki/AST_Architecture.md`, `openwiki/quickstart.md`).
- `evidence/` & `graphify-out/`: Mission verification logs and structural knowledge graphs ingested post-merge into R2R GraphRAG (`lgcorzo-mlops-python-package` collection).

## Upstream & Downstream Ecosystem Interfaces

```text
GitHub Issues (dark-gravity / autonomous-mission)
   └──► rust_CACD_autonomous_factory (5-step Hatchet DAG + Swarm Mode gVisor lanes)
           ├──► Opens HITL PR in mlops-python-package
           └──► Stage 5 factory-poller index_code -> R2R v3 GraphRAG + r2r-reader
```

## Security Boundary & Governance

- **Vertex 4 HITL Merge Gate**: Autonomous mission branches open PRs (`#477`, `#479`) and wait for green CI (`pytest`, `ruff`) and human review before merging to `main`.
- **Sandboxed Execution**: Agent-driven code changes execute inside ephemeral `gVisor` sandboxes without direct cluster credentials (`DOC-011` compliant).

## Canonical Cross-Links

- [DARK_GRAVITY_MANIFEST.md](./DARK_GRAVITY_MANIFEST.md)
- [REPOSITORIES.md](./REPOSITORIES.md)
- [Global Architecture Portal](https://lgcorzo.github.io/architecture.html)
- [Unified Start-Here Portal](https://lgcorzo.github.io/start-here)
- [AI Auditor Pack](https://lgcorzo.github.io/docs/auditor/)
