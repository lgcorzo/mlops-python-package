## v2.1.0 (2026-10-01)

### Feat

- **wiki**: recreate ISO/IEC/IEEE 42010 compliant documentation and skill
- Update AST documentation generator to comply with OKF standards
- Add ASKILL document for AST Documentation Generator
- extract structural and behavioral dependencies using AST type references
- implement AST documentation generator
- add parquet dataset files to git repository
- integrate DVC pipeline execution and MinIO remote storage

### Fix

- **security**: resolve all Dependabot vulnerabilities across urllib3 and virtualenv
- **ci**: use deterministic AST documentation generator in openwiki-update workflow
- **security**: verify security remediations and dependency constraints
- Extract positional-only and keyword-only args in ast doc gen
- make AST documentation generator deterministic and idempotent\n\n- Sort `all_files` in `generate_openwiki.py` to ensure consistent AST parsing order across different environments.\n- Sort dependency graph edges (`edges.sort()`) before appending to PlantUML strings to ensure deterministic outputs.\n- Remove hardcoded leading newlines (`\\n`) in `generate_markdown` `body.append` calls to fix idempotency issues and avoid continuously rewriting trailing whitespaces in Markdown.
- **docs**: Ensure deterministic diagram generation by sorting keys
- add cross-references, architecture diagrams, and fully populated indexes
- **deps**: address cryptography vulnerability for dependabot
- **deps**: sync poetry.lock and requirements.txt with pyproject.toml
- **ci**: allow mlflow file store in test suite for mlflow 3.15+
- **security**: resolve dependency security vulnerabilities
- **docs**: update license badge URL to force cache refresh
- **docs**: update release badge URL to force cache refresh

## v2.0.1 (2026-08-01)

### Feat

- bootstrap OpenWiki documentation with ISO 26514 standards and module specifications
- add uml2-okf-documenter agent skill
- add OKF professional documenter agent skill
- **docs**: add OKF incremental documentation script and registry fix
- **docs**: add OKF incremental documentation script and MLflow registry fixes
- **docs**: add OKF incremental documentation script and fixes
- **docs**: add OKF incremental documentation script
- modernize Docker build and stabilize test suite (#301)
- **security**: add input size validation to prevent DoS
- add CORSMiddleware and TrustedHostMiddleware for security
- **security**: add CORS and TrustedHost middleware
- add CORS and TrustedHost middleware to FastAPI app
- **security**: add CORS and TrustedHost middleware
- **security**: add CORS and TrustedHost middleware
- Add CORSMiddleware and TrustedHostMiddleware
- **security**: add CORS and TrustedHost middleware
- add CORSMiddleware and TrustedHostMiddleware to FastAPI app
- add CORSMiddleware and TrustedHostMiddleware to FastAPI app
- **security**: add CORS and TrustedHost middlewares
- **security**: add CORS and TrustedHost middleware
- **security**: add CORS and TrustedHost middleware
- add CORS and TrustedHost middlewares to FastAPI app
- **security**: add CORS and TrustedHost middleware
- **security**: add CORS and TrustedHost middleware
- add TrustedHost and CORS middleware to FastAPI app
- kafka service docekr imag  modification
- controller foler move
- Kafka env read
- refactor kafka_app.py
- added he
- added example batch
- kafka error mangement
- prediction service  endpoint
- kafka service apidocs
- kafka servide  running v1
- kafka controller
- added script to  deploy mlservice mlflow
- added mlfow os vars
- model_name  change

### Fix

- rename LICENCE.txt to LICENSE.txt and update README badge links
- **docs**: add missing OKF frontmatter to INSTRUCTIONS.md
- add missing import mlflow in check_env.py
- **docs**: restrict doc generation updates to incremental OKF diffs instead of full generation.
- update predict method signature to use schemas.Inputs type hint for model_input
- **docker**: use --force-reinstall when installing application wheel in Dockerfile
- **registries**: remove predict model_input type annotation to resolve MLflow schema UserWarning
- **controller**: add AdminClient topic auto-creation and expand transient error handling
- **controller**: resolve kafka producer config warnings, transient topic error handling, and add workflow_dispatch to publish.yml
- **ci**: add contents: read permission to packages job for checkout
- **ci**: use GITHUB_TOKEN fallback for checkout and update PR action
- **deps**: update dependencies to resolve dependabot vulnerabilities
- Security Remediation Phase 2 - 15 vulnerabilities resolved (#304)
- **ci**: grant write perms for Pages and fix Docker Hub login condition (#302)
- remove unnecessary time.sleep in kafka consumer loop
- stop logging raw payload data at INFO level
- mitigate log DoS and information leakage in kafka_app
- Prevent info leakage and DoS via payload logging
- **tests**: update kafka app tests with valid input data
- **security**: add CORS/TrustedHost middleware and fix formatting
- **security**: prevent information leakage in Kafka app error handling
- **security**: prevent information leakage in Kafka app error handling
- **typing**: achieve full strict mypy compliance and resolve naming conflicts
- **mypy**: resolve errors and remove exclusions
- **settings**: allow extra env vars in settings and env config

### Refactor

- remove entire openwiki documentation directory
- remove legacy documentation generator and utility scripts
- update model predict signature to use schemas.Outputs and remove pandas dependency
- **controller**: resolve architectural, concurrency, validation, and maintainability issues in kafka_app.py
- Log row and column counts for Kafka and HTTP prediction requests.
- kafka_app.py
- reduced complexity prodicer

### Perf

- optimize Kafka producer throughput by removing per-message flush
- optimize Kafka producer throughput by removing per-message flush
- **training**: use head(5) for signature and input_example to speed up model saving
- optimize row length and consistency check in PredictionRequest (#312)
- replace list.pop(0) with collections.deque.popleft in RateLimiter (#305)


- added opentelemetry service

## v2.0.0 (2024-07-28)

### Feat

- **cruft**: adopt cruft and link it to cookiecutter-mlops-package

## v1.1.3 (2024-07-28)

### Fix

- **mlproject**: fix calling mlflow run by adding project run in front

## v1.1.2 (2024-07-28)

### Fix

- **dependencies**: add setuptools to main dependency for mlflow

## v1.1.1 (2024-07-23)

### Fix

- **publish**: fix publication workflow by installing dev dependencies

## v1.1.0 (2024-07-21)

### Feat

- **kpi**: add key performance indicators
- **mlproject**: add mlflow project and tasks
- **monitoring**: add mlflow.evaluate API
- **lineage**: add lineage features through mlflow data api
- **explanations**: add explainability features and tooling
- **data**: add train, test, and sample data
- **notification**: add service and alerts with plyer
- **observability**: add alerting with plyer notifications
- **observability**: add infrastructure through mlflow system metrics

### Fix

- **kpi**: add key performance indicators
- **projects**: change naming convention
- **evaluation**: add evaluation files
- **loading**: use version or alias for loading models
- **warnings**: improve styles and remove warnings
- **mlflow**: remove input examples following the addition of lineage
- **paths**: fix path for explanation job
- **data**: fix models explanations name
- **data**: add parquet data

## v1.0.1 (2024-06-28)

### Fix

- **version**: bump
