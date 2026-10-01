from .config import make_frontmatter

def get_module_pages():
    pages = {}
    
    # =========================================================================
    # PACKAGE ROOT MODULES
    # =========================================================================
    
    # 1. __init__.py
    fm = make_frontmatter(
        doc_type="Description",
        viewpoint="ComponentView",
        concept_type="module",
        title="regression_model_template::__init__ — Package Metadata",
        description="Top-level package initialization and metadata for regression_model_template.",
        tags=["iso42010", "okf", "component_view", "package"],
        source_path="src/regression_model_template/__init__.py"
    )
    pages["modules/regression_model_template/__init__.md"] = fm + "\n\n" + """# regression_model_template::__init__ — Package Metadata

> **Source**: `src/regression_model_template/__init__.py` (Lines: L1-L1)  
> **Layer**: Application Root  
> **Role**: Package root marker and version namespace definition.

---

## 1. Architectural Scope

Defines the primary import namespace for the `regression_model_template` package. Exposes top-level package metadata and version attributes.

```mermaid
graph LR
    PKG["regression_model_template"] --> CTRL["controller/"]
    PKG --> CORE["core/"]
    PKG --> IO["io/"]
    PKG --> JOBS["jobs/"]
    PKG --> UTILS["utils/"]

    classDef pkg fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#f8fafc;
    class PKG,CTRL,CORE,IO,JOBS,UTILS pkg;
```

---

> *Related: [Strategic Design](../../architecture/strategic_design.md) · [Master Index](../../index.md)*
"""

    # 2. __main__.py
    fm = make_frontmatter(
        doc_type="Procedure",
        viewpoint="ComponentView",
        concept_type="module",
        title="regression_model_template::__main__ — CLI Entrypoint",
        description="Top-level module execution dispatcher for python -m regression_model_template.",
        tags=["iso42010", "okf", "component_view", "cli"],
        source_path="src/regression_model_template/__main__.py"
    )
    pages["modules/regression_model_template/__main__.md"] = fm + "\n\n" + """# regression_model_template::__main__ — CLI Entrypoint

> **Source**: `src/regression_model_template/__main__.py` (Lines: L1-L10)  
> **Layer**: Interface  
> **Role**: Command-line entrypoint executing `scripts.main()` upon invocation.

---

## 1. Execution Flow

Delegates standard shell command execution (`python -m regression_model_template`) to `scripts.main`:

```mermaid
sequenceDiagram
    autonumber
    actor User as Terminal / Shell
    participant Main as __main__.py
    participant Scripts as scripts.py

    User->>Main: python -m regression_model_template
    activate Main
    Main->>Scripts: main()
    activate Scripts
    Scripts-->>Main: exit_code
    deactivate Scripts
    Main-->>User: Exit(exit_code)
    deactivate Main
```

---

> *Related: [Scripts Specification](scripts.md) · [User Manual](../../operations/user_manual.md)*
"""

    # 3. init_data.py
    fm = make_frontmatter(
        doc_type="Procedure",
        viewpoint="ComponentView",
        concept_type="module",
        title="regression_model_template::init_data — Synthetic Dataset Generator",
        description="Generates reproducible synthetic regression datasets matching Pandera InputsSchema and TargetsSchema.",
        tags=["iso42010", "okf", "component_view", "data"],
        source_path="src/regression_model_template/init_data.py"
    )
    pages["modules/regression_model_template/init_data.md"] = fm + "\n\n" + """# regression_model_template::init_data — Synthetic Dataset Generator

> **Source**: `src/regression_model_template/init_data.py` (Lines: L1-L66)  
> **Layer**: Utilities / Data Seeding  
> **Role**: Generates reproducible synthetic bike sharing demand regression datasets for development and testing.

---

## 1. Component Architecture & Signatures

```mermaid
classDiagram
    class InitData {
        <<script>>
        +generate_data(output_dir: str = "data") None
        +main() None
    }
```

### `generate_data(output_dir: str = "data") -> None`
- **Source Citation**: `src/regression_model_template/init_data.py:L10-L54`
- **Visibility**: Public (`+`)
- **Behavior**: Synthesizes 1,000 hourly bike-sharing records containing calendar, weather, temperature, humidity, and windspeed features, persisting outputs as `inputs.parquet` and `targets.parquet`.

---

> *Related: [Data Model](../../architecture/mission_data_model.md) · [Datasets](io/datasets.md)*
"""

    # 4. scripts.py
    fm = make_frontmatter(
        doc_type="Procedure",
        viewpoint="ComponentView",
        concept_type="module",
        title="regression_model_template::scripts — CLI Runner & Dispatcher",
        description="Parses command-line arguments and dispatches job configurations to the Job execution context.",
        tags=["iso42010", "okf", "component_view", "cli"],
        source_path="src/regression_model_template/scripts.py"
    )
    pages["modules/regression_model_template/scripts.md"] = fm + "\n\n" + """# regression_model_template::scripts — CLI Runner & Dispatcher

> **Source**: `src/regression_model_template/scripts.py` (Lines: L1-L47)  
> **Layer**: Interface / CLI  
> **Role**: Main script entrypoint loading OmegaConf settings and executing designated lifecycle jobs.

---

## 1. Component Architecture

```mermaid
classDiagram
    class ScriptsModule {
        <<module>>
        +main(argv: list[str] | None = None) int
    }
```

### `main(argv: list[str] | None = None) -> int`
- **Source Citation**: `src/regression_model_template/scripts.py:L31-L47`
- **Visibility**: Public (`+`)
- **Behavior**: Parses command-line flags (e.g. `--config-name`), loads hierarchical configs via `MainSettings`, and executes `job.run()`.

---

> *Related: [Settings](settings.md) · [Base Job](jobs/base.md) · [User Manual](../../operations/user_manual.md)*
"""

    # 5. settings.py
    fm = make_frontmatter(
        doc_type="Specification",
        viewpoint="ComponentView",
        concept_type="module",
        title="regression_model_template::settings — Application Settings",
        description="Pydantic BaseSettings models parsing top-level application configuration.",
        tags=["iso42010", "okf", "component_view", "configuration"],
        source_path="src/regression_model_template/settings.py"
    )
    pages["modules/regression_model_template/settings.md"] = fm + "\n\n" + """# regression_model_template::settings — Application Settings

> **Source**: `src/regression_model_template/settings.py` (Lines: L1-L28)  
> **Layer**: Configuration  
> **Role**: Declares application-wide Pydantic settings models for job execution.

---

## 1. Class Diagram

```mermaid
classDiagram
    class Settings {
        <<pydantic>>
        +model_config: SettingsConfigDict
    }
    class MainSettings {
        <<pydantic>>
        +jobs.JobKind job
    }
    MainSettings --|> Settings : inherits
```

---

> *Related: [Scripts](scripts.md) · [Configs](io/configs.md)*
"""

    # =========================================================================
    # CONTROLLER MODULES
    # =========================================================================

    # 6. controller/__init__.py
    fm = make_frontmatter(
        doc_type="Description",
        viewpoint="ComponentView",
        concept_type="module",
        title="regression_model_template::controller::__init__ — Controller Package",
        description="Package exports for the controller streaming and REST interface.",
        tags=["iso42010", "okf", "component_view", "controller"],
        source_path="src/regression_model_template/controller/__init__.py"
    )
    pages["modules/regression_model_template/controller/__init__.md"] = fm + "\n\n" + """# regression_model_template::controller::__init__ — Controller Package

> **Source**: `src/regression_model_template/controller/__init__.py` (Lines: L1-L1)  
> **Layer**: Interface  
> **Role**: Namespace initialization for API endpoints and Kafka consumers.

---

> *Related: [Kafka App](kafka_app.md) · [Tactical Design](../../../architecture/tactical_design.md)*
"""

    # 7. controller/kafka_app.py
    fm = make_frontmatter(
        doc_type="Specification",
        viewpoint="ComponentView",
        concept_type="module",
        title="regression_model_template::controller::kafka_app — Streaming & REST Prediction Service",
        description="FastAPI application and Confluent Kafka consumer service implementing rate limiting, schema validation, and low-latency inference.",
        tags=["iso42010", "okf", "component_view", "kafka", "fastapi", "rate_limiting"],
        source_path="src/regression_model_template/controller/kafka_app.py"
    )
    pages["modules/regression_model_template/controller/kafka_app.py.md"] = fm + "\n\n" + """# regression_model_template::controller::kafka_app — Streaming & REST Prediction Service

> **Source**: `src/regression_model_template/controller/kafka_app.py` (Lines: L1-L501)  
> **Layer**: Interface / Streaming  
> **Role**: Dual-protocol inference server hosting synchronous FastAPI endpoints and asynchronous Confluent Kafka event consumption.

---

## 1. Class Diagram

```mermaid
classDiagram
    class RateLimiter {
        -int max_requests
        -int window_seconds
        -int max_tracked_ips
        -dict ip_requests
        +is_allowed(ip: str) bool
    }

    class PredictionRequest {
        +Dict~str, Any~ input_data
        +validate_schema() DataFrame
        +check_input_size(v: Dict) Dict$
    }

    class PredictionResponse {
        +Dict~str, Any~ result
    }

    class FastAPIKafkaService {
        -Callable prediction_callback
        -Dict kafka_config
        -str input_topic
        -str output_topic
        +start() None
        +stop() None
        -_consume_messages() None
        -_process_message(msg: Message) None
    }

    class PredictionService {
        -Any model
        +predict(input_data: PredictionRequest) PredictionResponse
    }

    FastAPIKafkaService --> RateLimiter : validates client limits
    FastAPIKafkaService --> PredictionService : invokes model
    PredictionService --> PredictionRequest : validates payload
```

---

## 2. Comprehensive Method Contracts

### `RateLimiter.is_allowed(self, ip: str) -> bool`
- **Source Citation**: `src/regression_model_template/controller/kafka_app.py:L91-L112`
- **Visibility**: Public (`+`)
- **Behavior**: Evaluates request count within sliding window for incoming IP address; raises or evicts old entries when bounds exceed `MAX_TRACKED_IPS`.

### `FastAPIKafkaService._process_message(self, msg: Message) -> None`
- **Source Citation**: `src/regression_model_template/controller/kafka_app.py:L320-L372`
- **Visibility**: Private (`-`)
- **Behavior**: Parses JSON event from Kafka input topic, validates against `PredictionRequest`, calculates predictions, and produces response to output topic.

---

> *Related: [Security Architecture](../../../security/security_architecture.md) · [Production Operations](../../../operations/production_operations.md)*
"""
    # Fix filename mapping
    pages["modules/regression_model_template/controller/kafka_app.md"] = pages.pop("modules/regression_model_template/controller/kafka_app.py.md")

    # =========================================================================
    # CORE DOMAIN MODULES
    # =========================================================================

    # 8. core/__init__.py
    fm = make_frontmatter(
        doc_type="Description",
        viewpoint="ComponentView",
        concept_type="module",
        title="regression_model_template::core::__init__ — Core Domain Package",
        description="Package exports for mathematical domain concepts (Models, Metrics, Schemas).",
        tags=["iso42010", "okf", "component_view", "domain"],
        source_path="src/regression_model_template/core/__init__.py"
    )
    pages["modules/regression_model_template/core/__init__.md"] = fm + "\n\n" + """# regression_model_template::core::__init__ — Core Domain Package

> **Source**: `src/regression_model_template/core/__init__.py` (Lines: L1-L1)  
> **Layer**: Domain (Innermost Onion Architecture Layer)  
> **Role**: Exposes core mathematical abstractions: Model, Metric, and Schemas.

---

> *Related: [Metrics](metrics.md) · [Models](models.md) · [Schemas](schemas.md)*
"""

    # 9. core/metrics.py
    fm = make_frontmatter(
        doc_type="Specification",
        viewpoint="ComponentView",
        concept_type="module",
        title="regression_model_template::core::metrics — Metric Evaluation Abstractions",
        description="Abstract Metric base class, Scikit-Learn metric wrapper, and MLflow threshold evaluators.",
        tags=["iso42010", "okf", "component_view", "metrics", "sklearn"],
        source_path="src/regression_model_template/core/metrics.py"
    )
    pages["modules/regression_model_template/core/metrics.md"] = fm + "\n\n" + """# regression_model_template::core::metrics — Metric Evaluation Abstractions

> **Source**: `src/regression_model_template/core/metrics.py` (Lines: L1-L148)  
> **Layer**: Domain  
> **Role**: Encapsulates regression evaluation scoring functions, threshold criteria, and MLflow serialization.

---

## 1. Class Diagram

```mermaid
classDiagram
    class Metric {
        <<abstract>>
        +str KIND
        +str name
        +bool greater_is_better
        +score(targets: Targets, outputs: Outputs) float*
        +scorer(model: Model, inputs: Inputs, targets: Targets) float
        +to_mlflow() MlflowMetric
    }

    class SklearnMetric {
        +str KIND = "SklearnMetric"
        +str name
        +bool greater_is_better
        +score(targets: Targets, outputs: Outputs) float
    }
    SklearnMetric --|> Metric : implements

    class Threshold {
        +float threshold
        +bool greater_is_better
        +to_mlflow() MlflowThreshold
    }
```

---

## 2. Method Contracts

### `Metric.score(self, targets: schemas.Targets, outputs: schemas.Outputs) -> float`
- **Source Citation**: `src/regression_model_template/core/metrics.py:L44-L53`
- **Visibility**: Public (`+`)
- **Behavior**: Evaluates predictive quality between true targets and model predictions.

---

> *Related: [Models](models.md) · [Evaluations Job](../jobs/evaluations.md)*
"""

    # 10. core/models.py
    fm = make_frontmatter(
        doc_type="Specification",
        viewpoint="ComponentView",
        concept_type="module",
        title="regression_model_template::core::models — Model Abstraction & Baselines",
        description="Abstract Model interface with Pydantic validation, Scikit-Learn pipeline wrapper, and SHAP explainability hooks.",
        tags=["iso42010", "okf", "component_view", "models", "scikit_learn", "shap"],
        source_path="src/regression_model_template/core/models.py"
    )
    pages["modules/regression_model_template/core/models.md"] = fm + "\n\n" + """# regression_model_template::core::models — Model Abstraction & Baselines

> **Source**: `src/regression_model_template/core/models.py` (Lines: L1-L223)  
> **Layer**: Domain  
> **Role**: Unified model contract ensuring consistent fit, predict, parameter inspection, and SHAP explainability across any regression estimator.

---

## 1. Class Diagram

```mermaid
classDiagram
    class Model {
        <<abstract>>
        +str KIND
        +get_params(deep: bool = True) Params
        +set_params(**params) Self
        +fit(inputs: Inputs, targets: Targets) Self*
        +predict(inputs: Any) Outputs*
        +explain_model() FeatureImportances*
        +explain_samples(inputs: Inputs) SHAPValues*
        +get_internal_model() Any*
    }

    class BaselineSklearnModel {
        +str KIND = "BaselineSklearnModel"
        +int max_depth
        +int n_estimators
        +int random_state
        -Pipeline _pipeline
        +fit(inputs: Inputs, targets: Targets) BaselineSklearnModel
        +predict(inputs: Any) Outputs
        +explain_model() FeatureImportances
        +explain_samples(inputs: Inputs) SHAPValues
        +get_internal_model() Pipeline
    }
    BaselineSklearnModel --|> Model : implements
```

---

## 2. Method Contracts

### `BaselineSklearnModel.fit(self, inputs: schemas.Inputs, targets: schemas.Targets) -> 'BaselineSklearnModel'`
- **Source Citation**: `src/regression_model_template/core/models.py:L161-L183`
- **Visibility**: Public (`+`)
- **Behavior**: Assembles Scikit-Learn preprocessing transformers and Random Forest regressor, fitting estimator on validated inputs and targets.

### `BaselineSklearnModel.explain_samples(self, inputs: schemas.Inputs) -> schemas.SHAPValues`
- **Source Citation**: `src/regression_model_template/core/models.py:L204-L214`
- **Visibility**: Public (`+`)
- **Behavior**: Invokes SHAP `TreeExplainer` on the underlying fitted tree models to calculate local Shapley attribution values.

---

> *Related: [Metrics](metrics.md) · [Schemas](schemas.md) · [Training Job](../jobs/training.md)*
"""

    # 11. core/schemas.py
    fm = make_frontmatter(
        doc_type="Specification",
        viewpoint="ComponentView",
        concept_type="module",
        title="regression_model_template::core::schemas — Pandera Data Contracts",
        description="Pandera DataFrameModel schemas enforcing compile-time and runtime validation on Inputs, Targets, Outputs, and SHAP values.",
        tags=["iso42010", "okf", "component_view", "schemas", "pandera"],
        source_path="src/regression_model_template/core/schemas.py"
    )
    pages["modules/regression_model_template/core/schemas.md"] = fm + "\n\n" + """# regression_model_template::core::schemas — Pandera Data Contracts

> **Source**: `src/regression_model_template/core/schemas.py` (Lines: L1-L120)  
> **Layer**: Domain  
> **Role**: Formal tabular contracts guaranteeing type safety, index alignment, and range constraints across all pipeline boundaries.

---

## 1. Class Diagram

```mermaid
classDiagram
    class Schema {
        +check(data: DataFrame) DataFrame$
    }

    class InputsSchema {
        +UInt32 instant
        +DateTime dteday
        +UInt8 season
        +UInt8 yr
        +UInt8 mnth
        +UInt8 hr
        +float temp
        +float hum
        +float windspeed
    }
    InputsSchema --|> Schema : inherits

    class TargetsSchema {
        +UInt32 instant
        +UInt32 cnt
    }
    TargetsSchema --|> Schema : inherits

    class OutputsSchema {
        +UInt32 instant
        +UInt32 prediction
    }
    OutputsSchema --|> Schema : inherits
```

---

> *Related: [Data Model](../../../architecture/mission_data_model.md) · [Datasets](../io/datasets.md)*
"""

    # =========================================================================
    # IO MODULES
    # =========================================================================

    # 12. io/__init__.py
    fm = make_frontmatter(
        doc_type="Description",
        viewpoint="ComponentView",
        concept_type="module",
        title="regression_model_template::io::__init__ — IO Infrastructure Package",
        description="Package exports for Input/Output adapters and external integrations.",
        tags=["iso42010", "okf", "component_view", "io"],
        source_path="src/regression_model_template/io/__init__.py"
    )
    pages["modules/regression_model_template/io/__init__.md"] = fm + "\n\n" + """# regression_model_template::io::__init__ — IO Infrastructure Package

> **Source**: `src/regression_model_template/io/__init__.py` (Lines: L1-L1)  
> **Layer**: Infrastructure  
> **Role**: Namespace initialization for dataset readers/writers, configurations, registries, and platform services.

---

> *Related: [Datasets](datasets.md) · [Services](services.md)*
"""

    # 13. io/configs.py
    fm = make_frontmatter(
        doc_type="Specification",
        viewpoint="ComponentView",
        concept_type="module",
        title="regression_model_template::io::configs — OmegaConf YAML Parsing",
        description="Configuration utilities loading, merging, and resolving hierarchical OmegaConf YAML specifications.",
        tags=["iso42010", "okf", "component_view", "configuration", "omegaconf"],
        source_path="src/regression_model_template/io/configs.py"
    )
    pages["modules/regression_model_template/io/configs.md"] = fm + "\n\n" + """# regression_model_template::io::configs — OmegaConf YAML Parsing

> **Source**: `src/regression_model_template/io/configs.py` (Lines: L1-L68)  
> **Layer**: Infrastructure / Configuration  
> **Role**: Deterministic YAML configuration loader resolving environment variables and hierarchical overrides.

---

## 1. Functional Contracts

### `parse_file(path: str) -> Config`
- **Source Citation**: `src/regression_model_template/io/configs.py:L16-L25`
- **Visibility**: Public (`+`)
- **Behavior**: Loads and parses a local YAML specification file into an OmegaConf dictionary.

### `merge_configs(configs: Sequence[Config]) -> Config`
- **Source Citation**: `src/regression_model_template/io/configs.py:L43-L52`
- **Visibility**: Public (`+`)
- **Behavior**: Deep-merges multiple configuration trees, resolving variable interpolations.

---

> *Related: [Settings](../settings.md) · [OSVariables](osvariables.md)*
"""

    # 14. io/datasets.py
    fm = make_frontmatter(
        doc_type="Specification",
        viewpoint="ComponentView",
        concept_type="module",
        title="regression_model_template::io::datasets — Tabular Dataset I/O & Lineage",
        description="Abstract Reader/Writer interfaces and concrete Parquet implementations with automated lineage extraction.",
        tags=["iso42010", "okf", "component_view", "datasets", "parquet", "lineage"],
        source_path="src/regression_model_template/io/datasets.py"
    )
    pages["modules/regression_model_template/io/datasets.md"] = fm + "\n\n" + """# regression_model_template::io::datasets — Tabular Dataset I/O & Lineage

> **Source**: `src/regression_model_template/io/datasets.py` (Lines: L1-L128)  
> **Layer**: Infrastructure  
> **Role**: Standardized reading and writing of tabular Parquet datasets with automated data lineage recording for MLflow tracking.

---

## 1. Class Diagram

```mermaid
classDiagram
    class Reader {
        <<abstract>>
        +str KIND
        +int limit
        +read() DataFrame*
        +lineage(name: str, data: DataFrame, targets, predictions) Lineage
    }

    class ParquetReader {
        +str KIND = "ParquetReader"
        +str path
        +read() DataFrame
        +lineage(name: str, data: DataFrame, targets, predictions) Lineage
    }
    ParquetReader --|> Reader : implements

    class Writer {
        <<abstract>>
        +str KIND
        +write(data: DataFrame) None*
    }

    class ParquetWriter {
        +str KIND = "ParquetWriter"
        +str path
        +write(data: DataFrame) None
    }
    ParquetWriter --|> Writer : implements
```

---

> *Related: [Schemas](../core/schemas.md) · [Data Model](../../../architecture/mission_data_model.md)*
"""

    # 15. io/osvariables.py
    fm = make_frontmatter(
        doc_type="Specification",
        viewpoint="ComponentView",
        concept_type="module",
        title="regression_model_template::io::osvariables — Environment Settings Singleton",
        description="Thread-safe Singleton environment configuration parsing dotenv variables into Pydantic BaseSettings.",
        tags=["iso42010", "okf", "component_view", "environment", "singleton"],
        source_path="src/regression_model_template/io/osvariables.py"
    )
    pages["modules/regression_model_template/io/osvariables.md"] = fm + "\n\n" + """# regression_model_template::io::osvariables — Environment Settings Singleton

> **Source**: `src/regression_model_template/io/osvariables.py` (Lines: L1-L26)  
> **Layer**: Infrastructure / Configuration  
> **Role**: Thread-safe Singleton environment manager providing centralized access to MLflow endpoints and platform variables.

---

## 1. Class Diagram

```mermaid
classDiagram
    class Singleton {
        -_instances: dict
        +__new__(cls, *args, **kwargs) Singleton$
    }

    class Env {
        +str mlflow_tracking_uri
        +str mlflow_registry_uri
        +str mlflow_experiment_name
        +str mlflow_registered_model_name
    }
    Env --|> Singleton : inherits
```

---

> *Related: [Services](services.md) · [Configs](configs.md)*
"""

    # 16. io/registries.py
    fm = make_frontmatter(
        doc_type="Specification",
        viewpoint="ComponentView",
        concept_type="module",
        title="regression_model_template::io::registries — Model Registry & Loaders",
        description="Abstract Loader/Register interfaces and MLflow model registry integration.",
        tags=["iso42010", "okf", "component_view", "registry", "mlflow"],
        source_path="src/regression_model_template/io/registries.py"
    )
    pages["modules/regression_model_template/io/registries.md"] = fm + "\n\n" + """# regression_model_template::io::registries — Model Registry & Loaders

> **Source**: `src/regression_model_template/io/registries.py` (Lines: L1-L317)  
> **Layer**: Infrastructure  
> **Role**: Interfaces for registering trained model artifacts in MLflow and resolving model versions or aliases into callable prediction adapters.

---

## 1. Class Diagram

```mermaid
classDiagram
    class Loader {
        <<abstract>>
        +str KIND
        +load(uri: str) Loader.Adapter*
    }
    class CustomLoader {
        +load(uri: str) CustomLoader.Adapter
    }
    class BuiltinLoader {
        +load(uri: str) BuiltinLoader.Adapter
    }
    CustomLoader --|> Loader : implements
    BuiltinLoader --|> Loader : implements

    class Register {
        <<abstract>>
        +str KIND
        +dict tags
        +register(name: str, model_uri: str) Version*
    }
    class MlflowRegister {
        +register(name: str, model_uri: str) Version
    }
    MlflowRegister --|> Register : implements
```

---

> *Related: [Services](services.md) · [Promotion Job](../jobs/promotion.md)*
"""

    # 17. io/services.py
    fm = make_frontmatter(
        doc_type="Specification",
        viewpoint="ComponentView",
        concept_type="module",
        title="regression_model_template::io::services — Platform Services Lifecycle",
        description="Lifecycle management for platform services: LoggerService (Loguru), AlertsService, and MlflowService.",
        tags=["iso42010", "okf", "component_view", "services", "mlflow", "logging"],
        source_path="src/regression_model_template/io/services.py"
    )
    pages["modules/regression_model_template/io/services.md"] = fm + "\n\n" + """# regression_model_template::io::services — Platform Services Lifecycle

> **Source**: `src/regression_model_template/io/services.py` (Lines: L1-L252)  
> **Layer**: Infrastructure  
> **Role**: Coordinates the runtime startup, context injection, and shutdown of core platform services: structured logging, desktop/webhook alerts, and MLflow tracking.

---

## 1. Class Diagram

```mermaid
classDiagram
    class Service {
        <<abstract>>
        +start() None*
        +stop() None*
    }

    class LoggerService {
        +str sink
        +str level
        +bool colorize
        +bool serialize
        +start() None
        +logger() Logger
    }
    LoggerService --|> Service : implements

    class AlertsService {
        +bool enable
        +str app_name
        +start() None
        +notify(title: str, message: str) None
    }
    AlertsService --|> Service : implements

    class MlflowService {
        +str tracking_uri
        +str experiment_name
        +start() None
        +run_context(run_config: RunConfig) Generator
        +client() MlflowClient
    }
    MlflowService --|> Service : implements
```

---

> *Related: [Base Job](../jobs/base.md) · [Registries](registries.md)*
"""

    # =========================================================================
    # JOBS MODULES
    # =========================================================================

    # 18. jobs/__init__.py
    fm = make_frontmatter(
        doc_type="Description",
        viewpoint="ComponentView",
        concept_type="module",
        title="regression_model_template::jobs::__init__ — Lifecycle Jobs Package",
        description="Package exports for operational lifecycle jobs.",
        tags=["iso42010", "okf", "component_view", "jobs"],
        source_path="src/regression_model_template/jobs/__init__.py"
    )
    pages["modules/regression_model_template/jobs/__init__.md"] = fm + "\n\n" + """# regression_model_template::jobs::__init__ — Lifecycle Jobs Package

> **Source**: `src/regression_model_template/jobs/__init__.py` (Lines: L1-L26)  
> **Layer**: Application  
> **Role**: Exposes the unified `JobKind` type union across all 6 operational jobs.

---

> *Related: [Base Job](base.md) · [Lifecycle Job Specs](../../../architecture/agent_specifications.md)*
"""

    # 19. jobs/base.py
    fm = make_frontmatter(
        doc_type="Specification",
        viewpoint="ComponentView",
        concept_type="module",
        title="regression_model_template::jobs::base — Job Context Manager Contract",
        description="Abstract Job base class coordinating service start, error handling, notifications, and teardown.",
        tags=["iso42010", "okf", "component_view", "template_method", "context_manager"],
        source_path="src/regression_model_template/jobs/base.py"
    )
    pages["modules/regression_model_template/jobs/base.md"] = fm + "\n\n" + """# regression_model_template::jobs::base — Job Context Manager Contract

> **Source**: `src/regression_model_template/jobs/base.py` (Lines: L1-L85)  
> **Layer**: Application  
> **Role**: Base template method coordinating service lifecycles (`LoggerService`, `AlertsService`, `MlflowService`) via the Python context manager protocol.

---

## 1. Class Diagram

```mermaid
classDiagram
    class Job {
        <<abstract>>
        +str KIND
        +LoggerService logger_service
        +AlertsService alerts_service
        +MlflowService mlflow_service
        +__enter__() Self
        +__exit__(exc_type, exc_val, exc_tb) bool
        +run() Locals*
    }
```

---

> *Related: [Training Job](training.md) · [Tactical Design](../../../architecture/tactical_design.md)*
"""

    # 20. jobs/evaluations.py
    fm = make_frontmatter(
        doc_type="Specification",
        viewpoint="ComponentView",
        concept_type="module",
        title="regression_model_template::jobs::evaluations — Model Evaluation Pipeline",
        description="Evaluates registered model performance against predefined quality thresholds.",
        tags=["iso42010", "okf", "component_view", "evaluation", "metrics"],
        source_path="src/regression_model_template/jobs/evaluations.py"
    )
    pages["modules/regression_model_template/jobs/evaluations.md"] = fm + "\n\n" + """# regression_model_template::jobs::evaluations — Model Evaluation Pipeline

> **Source**: `src/regression_model_template/jobs/evaluations.py` (Lines: L1-L125)  
> **Layer**: Application  
> **Role**: Ingests test partitions, evaluates model predictions against configured metric thresholds, and logs verification reports to MLflow.

---

## 1. Class Diagram

```mermaid
classDiagram
    class EvaluationsJob {
        +str KIND = "EvaluationsJob"
        +RunConfig run_config
        +ReaderKind inputs
        +ReaderKind targets
        +str model_type
        +run() Locals
    }
    EvaluationsJob --|> Job : implements
```

---

> *Related: [Metrics](../core/metrics.md) · [Promotion Job](promotion.md)*
"""

    # 21. jobs/explanations.py
    fm = make_frontmatter(
        doc_type="Specification",
        viewpoint="ComponentView",
        concept_type="module",
        title="regression_model_template::jobs::explanations — SHAP Interpretability Pipeline",
        description="Generates global and local feature attribution values via SHAP TreeExplainer.",
        tags=["iso42010", "okf", "component_view", "xai", "shap"],
        source_path="src/regression_model_template/jobs/explanations.py"
    )
    pages["modules/regression_model_template/jobs/explanations.md"] = fm + "\n\n" + """# regression_model_template::jobs::explanations — SHAP Interpretability Pipeline

> **Source**: `src/regression_model_template/jobs/explanations.py` (Lines: L1-L78)  
> **Layer**: Application  
> **Role**: Calculates global feature importances and local per-sample Shapley attribution values for trained model estimators.

---

## 1. Class Diagram

```mermaid
classDiagram
    class ExplanationsJob {
        +str KIND = "ExplanationsJob"
        +ReaderKind inputs_samples
        +WriterKind models_explanations
        +WriterKind samples_explanations
        +str | int alias_or_version
        +run() Locals
    }
    ExplanationsJob --|> Job : implements
```

---

> *Related: [Models](../core/models.md) · [Compliance Audit](../../../security/compliance_audit.md)*
"""

    # 22. jobs/inference.py
    fm = make_frontmatter(
        doc_type="Specification",
        viewpoint="ComponentView",
        concept_type="module",
        title="regression_model_template::jobs::inference — Batch Prediction Pipeline",
        description="Executes batch predictions on unlabeled inputs with cryptographic signing via InferSigner.",
        tags=["iso42010", "okf", "component_view", "inference", "signing"],
        source_path="src/regression_model_template/jobs/inference.py"
    )
    pages["modules/regression_model_template/jobs/inference.md"] = fm + "\n\n" + """# regression_model_template::jobs::inference — Batch Prediction Pipeline

> **Source**: `src/regression_model_template/jobs/inference.py` (Lines: L1-L66)  
> **Layer**: Application  
> **Role**: Loads designated model artifacts from registry, validates inputs against Pandera schemas, produces predictions, and writes cryptographically signed output files.

---

## 1. Class Diagram

```mermaid
classDiagram
    class InferenceJob {
        +str KIND = "InferenceJob"
        +ReaderKind inputs
        +WriterKind outputs
        +str | int alias_or_version
        +LoaderKind loader
        +run() Locals
    }
    InferenceJob --|> Job : implements
```

---

> *Related: [Signers](../utils/signers.md) · [Kafka App](../controller/kafka_app.md)*
"""

    # 23. jobs/promotion.py
    fm = make_frontmatter(
        doc_type="Specification",
        viewpoint="ComponentView",
        concept_type="module",
        title="regression_model_template::jobs::promotion — Model Registry Promotion Gate",
        description="Promotes evaluated candidate model versions to designated production aliases (e.g. champion) in MLflow.",
        tags=["iso42010", "okf", "component_view", "promotion", "governance"],
        source_path="src/regression_model_template/jobs/promotion.py"
    )
    pages["modules/regression_model_template/jobs/promotion.md"] = fm + "\n\n" + """# regression_model_template::jobs::promotion — Model Registry Promotion Gate

> **Source**: `src/regression_model_template/jobs/promotion.py` (Lines: L1-L57)  
> **Layer**: Application  
> **Role**: Promotes qualified candidate model versions to target aliases (e.g. `champion`) in the MLflow Model Registry.

---

## 1. Class Diagram

```mermaid
classDiagram
    class PromotionJob {
        +str KIND = "PromotionJob"
        +str alias
        +int version
        +run() Locals
    }
    PromotionJob --|> Job : implements
```

---

> *Related: [HITL Governance](../../../security/hitl_governance.md) · [Registries](../io/registries.md)*
"""

    # 24. jobs/training.py
    fm = make_frontmatter(
        doc_type="Specification",
        viewpoint="ComponentView",
        concept_type="module",
        title="regression_model_template::jobs::training — Model Training Pipeline",
        description="Trains regression models, evaluates train/test partitions, and logs parameters and artifacts to MLflow.",
        tags=["iso42010", "okf", "component_view", "training", "mlflow"],
        source_path="src/regression_model_template/jobs/training.py"
    )
    pages["modules/regression_model_template/jobs/training.md"] = fm + "\n\n" + """# regression_model_template::jobs::training — Model Training Pipeline

> **Source**: `src/regression_model_template/jobs/training.py` (Lines: L1-L145)  
> **Layer**: Application  
> **Role**: Ingests training data, splits partitions, fits the model estimator, evaluates train/test error, and registers artifacts with active MLflow runs.

---

## 1. Class Diagram

```mermaid
classDiagram
    class TrainingJob {
        +str KIND = "TrainingJob"
        +RunConfig run_config
        +ReaderKind inputs
        +ReaderKind targets
        +ModelKind model
        +run() Locals
    }
    TrainingJob --|> Job : implements
```

---

> *Related: [Models](../core/models.md) · [Tuning Job](tuning.md)*
"""

    # 25. jobs/tuning.py
    fm = make_frontmatter(
        doc_type="Specification",
        viewpoint="ComponentView",
        concept_type="module",
        title="regression_model_template::jobs::tuning — Hyperparameter Optimization Pipeline",
        description="Executes cross-validated hyperparameter optimization over search spaces using Optuna or Grid search.",
        tags=["iso42010", "okf", "component_view", "tuning", "optuna"],
        source_path="src/regression_model_template/jobs/tuning.py"
    )
    pages["modules/regression_model_template/jobs/tuning.md"] = fm + "\n\n" + """# regression_model_template::jobs::tuning — Hyperparameter Optimization Pipeline

> **Source**: `src/regression_model_template/jobs/tuning.py` (Lines: L1-L104)  
> **Layer**: Application  
> **Role**: Explores multi-dimensional hyperparameter spaces, evaluates candidate configurations across cross-validation splits, and logs trials history to MLflow.

---

## 1. Class Diagram

```mermaid
classDiagram
    class TuningJob {
        +str KIND = "TuningJob"
        +RunConfig run_config
        +ReaderKind inputs
        +ReaderKind targets
        +ModelKind model
        +run() Locals
    }
    TuningJob --|> Job : implements
```

---

> *Related: [Searchers](../utils/searchers.md) · [Training Job](training.md)*
"""

    # =========================================================================
    # UTILS MODULES
    # =========================================================================

    # 26. utils/__init__.py
    fm = make_frontmatter(
        doc_type="Description",
        viewpoint="ComponentView",
        concept_type="module",
        title="regression_model_template::utils::__init__ — Utilities Package",
        description="Package exports for searchers, signers, and dataset splitters.",
        tags=["iso42010", "okf", "component_view", "utils"],
        source_path="src/regression_model_template/utils/__init__.py"
    )
    pages["modules/regression_model_template/utils/__init__.md"] = fm + "\n\n" + """# regression_model_template::utils::__init__ — Utilities Package

> **Source**: `src/regression_model_template/utils/__init__.py` (Lines: L1-L1)  
> **Layer**: Utilities  
> **Role**: Namespace initialization for auxiliary utilities: Searchers, Signers, and Splitters.

---

> *Related: [Searchers](searchers.md) · [Signers](signers.md) · [Splitters](splitters.md)*
"""

    # 27. utils/searchers.py
    fm = make_frontmatter(
        doc_type="Specification",
        viewpoint="ComponentView",
        concept_type="module",
        title="regression_model_template::utils::searchers — Hyperparameter Searchers",
        description="Abstract Searcher interface and Grid/Optuna cross-validation hyperparameter optimizers.",
        tags=["iso42010", "okf", "component_view", "searchers", "optuna", "grid_search"],
        source_path="src/regression_model_template/utils/searchers.py"
    )
    pages["modules/regression_model_template/utils/searchers.md"] = fm + "\n\n" + """# regression_model_template::utils::searchers — Hyperparameter Searchers

> **Source**: `src/regression_model_template/utils/searchers.py` (Lines: L1-L116)  
> **Layer**: Utilities  
> **Role**: Strategy abstraction executing parameter space traversals (Grid Search, Optuna Bayesian optimization) against regression models.

---

## 1. Class Diagram

```mermaid
classDiagram
    class Searcher {
        <<abstract>>
        +str KIND
        +Grid param_grid
        +search(model: Model, metric: Metric, inputs: Inputs, targets: Targets, cv: CrossValidation) Results*
    }

    class GridCVSearcher {
        +str KIND = "GridCVSearcher"
        +int n_jobs
        +bool refit
        +search(model: Model, metric: Metric, inputs: Inputs, targets: Targets, cv: CrossValidation) Results
    }
    GridCVSearcher --|> Searcher : implements
```

---

> *Related: [Tuning Job](../jobs/tuning.md) · [Splitters](splitters.md)*
"""

    # 28. utils/signers.py
    fm = make_frontmatter(
        doc_type="Specification",
        viewpoint="ComponentView",
        concept_type="module",
        title="regression_model_template::utils::signers — Cryptographic Attestation",
        description="Cryptographic hash signer computing SHA-256 signatures over prediction inputs and outputs.",
        tags=["iso42010", "okf", "component_view", "security", "sha256"],
        source_path="src/regression_model_template/utils/signers.py"
    )
    pages["modules/regression_model_template/utils/signers.md"] = fm + "\n\n" + """# regression_model_template::utils::signers — Cryptographic Attestation

> **Source**: `src/regression_model_template/utils/signers.py` (Lines: L1-L54)  
> **Layer**: Utilities / Security  
> **Role**: Produces tamper-evident SHA-256 digital signatures over serialized prediction inputs and outputs for compliance auditability.

---

## 1. Class Diagram

```mermaid
classDiagram
    class Signer {
        <<abstract>>
        +str KIND
        +sign(inputs: Inputs, outputs: Outputs) Signature*
    }

    class InferSigner {
        +str KIND = "InferSigner"
        +sign(inputs: Inputs, outputs: Outputs) Signature
    }
    InferSigner --|> Signer : implements
```

---

> *Related: [Security Architecture](../../../security/security_architecture.md) · [Inference Job](../jobs/inference.md)*
"""

    # 29. utils/splitters.py
    fm = make_frontmatter(
        doc_type="Specification",
        viewpoint="ComponentView",
        concept_type="module",
        title="regression_model_template::utils::splitters — Dataset Partitioning Strategies",
        description="Abstract Splitter interface, TrainTestSplitter, and TimeSeriesSplitter partitioning datasets while respecting temporal order.",
        tags=["iso42010", "okf", "component_view", "splitters", "cross_validation"],
        source_path="src/regression_model_template/utils/splitters.py"
    )
    pages["modules/regression_model_template/utils/splitters.md"] = fm + "\n\n" + """# regression_model_template::utils::splitters — Dataset Partitioning Strategies

> **Source**: `src/regression_model_template/utils/splitters.py` (Lines: L1-L111)  
> **Layer**: Utilities  
> **Role**: Strategy abstraction partitioning tabular datasets into train and test splits, supporting random shuffling and strict temporal ordering.

---

## 1. Class Diagram

```mermaid
classDiagram
    class Splitter {
        <<abstract>>
        +str KIND
        +split(inputs: Inputs, targets: Targets, groups: Index | None = None) TrainTestSplits*
        +get_n_splits(inputs: Inputs, targets: Targets, groups: Index | None = None) int*
    }

    class TrainTestSplitter {
        +str KIND = "TrainTestSplitter"
        +bool shuffle
        +int | float test_size
        +int random_state
        +split(inputs: Inputs, targets: Targets, groups: Index | None = None) TrainTestSplits
        +get_n_splits(inputs: Inputs, targets: Targets, groups: Index | None = None) int
    }
    TrainTestSplitter --|> Splitter : implements

    class TimeSeriesSplitter {
        +str KIND = "TimeSeriesSplitter"
        +int gap
        +int n_splits
        +int | float test_size
        +split(inputs: Inputs, targets: Targets, groups: Index | None = None) TrainTestSplits
        +get_n_splits(inputs: Inputs, targets: Targets, groups: Index | None = None) int
    }
    TimeSeriesSplitter --|> Splitter : implements
```

---

> *Related: [Training Job](../jobs/training.md) · [Searchers](searchers.md)*
"""

    return pages
