---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: conftest"
source_path: "tests/conftest.py"
description: "Configuration for the tests."
tags: ["module", "conftest"]
timestamp: "2026-08-18T05:58:44Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "5aba7e1"
---
# Module Specification: conftest

* **Source Reference:** [tests/conftest.py](../../../tests/conftest.py)

## 1. Architectural Role & Responsibilities

Configuration for the tests.

### Detected Architecture Patterns

Detected roles: General Subsystem

## 2. UML Diagrams

### Class Diagram

_No classes found._

### Sequence Diagram

```plantuml
sequenceDiagram
    tests_path->>fixture: invoke
    tests_path->>abspath: invoke
    tests_path->>dirname: invoke
    data_path->>fixture: invoke
    data_path->>join: invoke
    confs_path->>fixture: invoke
    confs_path->>join: invoke
    inputs_path->>fixture: invoke
    inputs_path->>join: invoke
    targets_path->>fixture: invoke
    targets_path->>join: invoke
    outputs_path->>fixture: invoke
    outputs_path->>join: invoke
    tmp_outputs_path->>fixture: invoke
    tmp_outputs_path->>join: invoke
    tmp_models_explanations_path->>fixture: invoke
    tmp_models_explanations_path->>join: invoke
    tmp_samples_explanations_path->>fixture: invoke
    tmp_samples_explanations_path->>join: invoke
    extra_config->>fixture: invoke
    inputs_reader->>fixture: invoke
    inputs_reader->>ParquetReader: invoke
    inputs_samples_reader->>fixture: invoke
    inputs_samples_reader->>ParquetReader: invoke
    targets_reader->>fixture: invoke
    targets_reader->>ParquetReader: invoke
    outputs_reader->>fixture: invoke
    outputs_reader->>ParquetReader: invoke
    outputs_reader->>exists: invoke
    outputs_reader->>check: invoke
    outputs_reader->>fit: invoke
    outputs_reader->>ParquetWriter: invoke
    outputs_reader->>write: invoke
    outputs_reader->>read: invoke
    outputs_reader->>predict: invoke
    outputs_reader->>BaselineSklearnModel: invoke
    tmp_outputs_writer->>fixture: invoke
    tmp_outputs_writer->>ParquetWriter: invoke
    tmp_models_explanations_writer->>fixture: invoke
    tmp_models_explanations_writer->>ParquetWriter: invoke
    tmp_samples_explanations_writer->>fixture: invoke
    tmp_samples_explanations_writer->>ParquetWriter: invoke
    inputs->>fixture: invoke
    inputs->>read: invoke
    inputs->>check: invoke
    inputs_samples->>fixture: invoke
    inputs_samples->>read: invoke
    inputs_samples->>check: invoke
    targets->>fixture: invoke
    targets->>read: invoke
    targets->>check: invoke
    outputs->>fixture: invoke
    outputs->>read: invoke
    outputs->>check: invoke
    train_test_splitter->>fixture: invoke
    train_test_splitter->>TrainTestSplitter: invoke
    time_series_splitter->>fixture: invoke
    time_series_splitter->>TimeSeriesSplitter: invoke
    searcher->>fixture: invoke
    searcher->>GridCVSearcher: invoke
    train_test_sets->>fixture: invoke
    train_test_sets->>next: invoke
    train_test_sets->>split: invoke
    train_test_sets->>cast: invoke
    model->>fixture: invoke
    model->>BaselineSklearnModel: invoke
    model->>fit: invoke
    metric->>fixture: invoke
    metric->>SklearnMetric: invoke
    signer->>fixture: invoke
    signer->>InferSigner: invoke
    logger_service->>fixture: invoke
    logger_service->>LoggerService: invoke
    logger_service->>start: invoke
    logger_service->>stop: invoke
    logger_caplog->>logger: invoke
    logger_caplog->>add: invoke
    logger_caplog->>remove: invoke
    alerts_service->>fixture: invoke
    alerts_service->>AlertsService: invoke
    alerts_service->>start: invoke
    alerts_service->>stop: invoke
    mlflow_service->>fixture: invoke
    mlflow_service->>MlflowService: invoke
    mlflow_service->>start: invoke
    mlflow_service->>stop: invoke
    tests_path_resolver->>fixture: invoke
    tests_path_resolver->>register_new_resolver: invoke
    tmp_path_resolver->>fixture: invoke
    tmp_path_resolver->>register_new_resolver: invoke
    signature->>fixture: invoke
    signature->>sign: invoke
    saver->>fixture: invoke
    saver->>CustomSaver: invoke
    loader->>fixture: invoke
    loader->>CustomLoader: invoke
    register->>fixture: invoke
    register->>MlflowRegister: invoke
    model_version->>fixture: invoke
    model_version->>RunConfig: invoke
    model_version->>run_context: invoke
    model_version->>save: invoke
    model_version->>register: invoke
    model_alias->>fixture: invoke
    model_alias->>client: invoke
    model_alias->>set_registered_model_alias: invoke
    model_alias->>get_model_version_by_alias: invoke
```

### Component Diagram

```plantuml
component [conftest] as Comp
Comp --> [os]
Comp --> [typing]
Comp --> [omegaconf]
Comp --> [pytest]
Comp --> [logging]
Comp --> [metrics]
Comp --> [models]
Comp --> [schemas]
Comp --> [datasets]
Comp --> [registries]
Comp --> [services]
Comp --> [searchers]
Comp --> [signers]
Comp --> [splitters]
```

## 3. Class & Method Specifications

## Standalone Functions

### `tests_path() -> str`

Return the path of the tests folder.

#### Inputs

#### Outputs
* `str`

### `data_path(tests_path: str) -> str`

Return the path of the data folder.

#### Inputs

* `tests_path` (`str`)

#### Outputs
* `str`

### `confs_path(tests_path: str) -> str`

Return the path of the confs folder.

#### Inputs

* `tests_path` (`str`)

#### Outputs
* `str`

### `inputs_path(data_path: str) -> str`

Return the path of the inputs dataset.

#### Inputs

* `data_path` (`str`)

#### Outputs
* `str`

### `targets_path(data_path: str) -> str`

Return the path of the targets dataset.

#### Inputs

* `data_path` (`str`)

#### Outputs
* `str`

### `outputs_path(data_path: str) -> str`

Return the path of the outputs dataset.

#### Inputs

* `data_path` (`str`)

#### Outputs
* `str`

### `tmp_outputs_path(tmp_path: str) -> str`

Return a tmp path for the outputs dataset.

#### Inputs

* `tmp_path` (`str`)

#### Outputs
* `str`

### `tmp_models_explanations_path(tmp_path: str) -> str`

Return a tmp path for the model explanations dataset.

#### Inputs

* `tmp_path` (`str`)

#### Outputs
* `str`

### `tmp_samples_explanations_path(tmp_path: str) -> str`

Return a tmp path for the samples explanations dataset.

#### Inputs

* `tmp_path` (`str`)

#### Outputs
* `str`

### `extra_config() -> str`

Extra config for scripts.

#### Inputs

#### Outputs
* `str`

### `inputs_reader(inputs_path: str) -> datasets.ParquetReader`

Return a reader for the inputs dataset.

#### Inputs

* `inputs_path` (`str`)

#### Outputs
* `datasets.ParquetReader`

### `inputs_samples_reader(inputs_path: str) -> datasets.ParquetReader`

Return a reader for the inputs samples dataset.

#### Inputs

* `inputs_path` (`str`)

#### Outputs
* `datasets.ParquetReader`

### `targets_reader(targets_path: str) -> datasets.ParquetReader`

Return a reader for the targets dataset.

#### Inputs

* `targets_path` (`str`)

#### Outputs
* `datasets.ParquetReader`

### `outputs_reader(outputs_path: str, inputs_reader: datasets.ParquetReader, targets_reader: datasets.ParquetReader) -> datasets.ParquetReader`

Return a reader for the outputs dataset.

#### Inputs

* `outputs_path` (`str`)

* `inputs_reader` (`datasets.ParquetReader`)

* `targets_reader` (`datasets.ParquetReader`)

#### Outputs
* `datasets.ParquetReader`

### `tmp_outputs_writer(tmp_outputs_path: str) -> datasets.ParquetWriter`

Return a writer for the tmp outputs dataset.

#### Inputs

* `tmp_outputs_path` (`str`)

#### Outputs
* `datasets.ParquetWriter`

### `tmp_models_explanations_writer(tmp_models_explanations_path: str) -> datasets.ParquetWriter`

Return a writer for the tmp model explanations dataset.

#### Inputs

* `tmp_models_explanations_path` (`str`)

#### Outputs
* `datasets.ParquetWriter`

### `tmp_samples_explanations_writer(tmp_samples_explanations_path: str) -> datasets.ParquetWriter`

Return a writer for the tmp samples explanations dataset.

#### Inputs

* `tmp_samples_explanations_path` (`str`)

#### Outputs
* `datasets.ParquetWriter`

### `inputs(inputs_reader: datasets.ParquetReader) -> schemas.Inputs`

Return the inputs data.

#### Inputs

* `inputs_reader` (`datasets.ParquetReader`)

#### Outputs
* `schemas.Inputs`

### `inputs_samples(inputs_samples_reader: datasets.ParquetReader) -> schemas.Inputs`

Return the inputs samples data.

#### Inputs

* `inputs_samples_reader` (`datasets.ParquetReader`)

#### Outputs
* `schemas.Inputs`

### `targets(targets_reader: datasets.ParquetReader) -> schemas.Targets`

Return the targets data.

#### Inputs

* `targets_reader` (`datasets.ParquetReader`)

#### Outputs
* `schemas.Targets`

### `outputs(outputs_reader: datasets.ParquetReader) -> schemas.Outputs`

Return the outputs data.

#### Inputs

* `outputs_reader` (`datasets.ParquetReader`)

#### Outputs
* `schemas.Outputs`

### `train_test_splitter() -> splitters.TrainTestSplitter`

Return the default train test splitter.

#### Inputs

#### Outputs
* `splitters.TrainTestSplitter`

### `time_series_splitter() -> splitters.TimeSeriesSplitter`

Return the default time series splitter.

#### Inputs

#### Outputs
* `splitters.TimeSeriesSplitter`

### `searcher() -> searchers.Searcher`

Return the default searcher object.

#### Inputs

#### Outputs
* `searchers.Searcher`

### `train_test_sets(train_test_splitter: splitters.Splitter, inputs: schemas.Inputs, targets: schemas.Targets) -> tuple[(schemas.Inputs, schemas.Targets, schemas.Inputs, schemas.Targets)]`

Return the inputs and targets train and test sets from the splitter.

#### Inputs

* `train_test_splitter` (`splitters.Splitter`)

* `inputs` (`schemas.Inputs`)

* `targets` (`schemas.Targets`)

#### Outputs
* `tuple[(schemas.Inputs, schemas.Targets, schemas.Inputs, schemas.Targets)]`

### `model(train_test_sets: tuple[(schemas.Inputs, schemas.Targets, schemas.Inputs, schemas.Targets)]) -> models.BaselineSklearnModel`

Return a train model for testing.

#### Inputs

* `train_test_sets` (`tuple[(schemas.Inputs, schemas.Targets, schemas.Inputs, schemas.Targets)]`)

#### Outputs
* `models.BaselineSklearnModel`

### `metric() -> metrics.SklearnMetric`

Return the default metric.

#### Inputs

#### Outputs
* `metrics.SklearnMetric`

### `signer() -> signers.Signer`

Return a model signer.

#### Inputs

#### Outputs
* `signers.Signer`

### `logger_service() -> T.Generator[(services.LoggerService, None, None)]`

Return and start the logger service.

#### Inputs

#### Outputs
* `T.Generator[(services.LoggerService, None, None)]`

### `logger_caplog(caplog: pl.LogCaptureFixture, logger_service: services.LoggerService) -> T.Generator[(pl.LogCaptureFixture, None, None)]`

Extend pytest caplog fixture with the logger service (loguru).

#### Inputs

* `caplog` (`pl.LogCaptureFixture`)

* `logger_service` (`services.LoggerService`)

#### Outputs
* `T.Generator[(pl.LogCaptureFixture, None, None)]`

### `alerts_service() -> T.Generator[(services.AlertsService, None, None)]`

Return and start the alerter service.

#### Inputs

#### Outputs
* `T.Generator[(services.AlertsService, None, None)]`

### `mlflow_service(tmp_path: str) -> T.Generator[(services.MlflowService, None, None)]`

Return and start the mlflow service.

#### Inputs

* `tmp_path` (`str`)

#### Outputs
* `T.Generator[(services.MlflowService, None, None)]`

### `tests_path_resolver(tests_path: str) -> str`

Register the tests path resolver with OmegaConf.

#### Inputs

* `tests_path` (`str`)

#### Outputs
* `str`

### `tmp_path_resolver(tmp_path: str) -> str`

Register the tmp path resolver with OmegaConf.

#### Inputs

* `tmp_path` (`str`)

#### Outputs
* `str`

### `signature(signer: signers.Signer, inputs: schemas.Inputs, outputs: schemas.Outputs) -> signers.Signature`

Return the signature for the testing model.

#### Inputs

* `signer` (`signers.Signer`)

* `inputs` (`schemas.Inputs`)

* `outputs` (`schemas.Outputs`)

#### Outputs
* `signers.Signature`

### `saver() -> registries.CustomSaver`

Return the default model saver.

#### Inputs

#### Outputs
* `registries.CustomSaver`

### `loader() -> registries.CustomLoader`

Return the default model loader.

#### Inputs

#### Outputs
* `registries.CustomLoader`

### `register() -> registries.MlflowRegister`

Return the default model register.

#### Inputs

#### Outputs
* `registries.MlflowRegister`

### `model_version(model: models.Model, inputs: schemas.Inputs, signature: signers.Signature, saver: registries.Saver, register: registries.Register, mlflow_service: services.MlflowService) -> registries.Version`

Save and register the default model version.

#### Inputs

* `model` (`models.Model`)

* `inputs` (`schemas.Inputs`)

* `signature` (`signers.Signature`)

* `saver` (`registries.Saver`)

* `register` (`registries.Register`)

* `mlflow_service` (`services.MlflowService`)

#### Outputs
* `registries.Version`

### `model_alias(model_version: registries.Version, mlflow_service: services.MlflowService) -> registries.Alias`

Promote the default model version with an alias.

#### Inputs

* `model_version` (`registries.Version`)

* `mlflow_service` (`services.MlflowService`)

#### Outputs
* `registries.Alias`

## Dependencies

* `os`

* `typing`

* `omegaconf`

* `pytest`

* `_pytest.logging`

* `regression_model_template.core.metrics`

* `regression_model_template.core.models`

* `regression_model_template.core.schemas`

* `regression_model_template.io.datasets`

* `regression_model_template.io.registries`

* `regression_model_template.io.services`

* `regression_model_template.utils.searchers`

* `regression_model_template.utils.signers`

* `regression_model_template.utils.splitters`

## Used By

_Not used by any other module._
