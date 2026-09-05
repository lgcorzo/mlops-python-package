---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: conftest"
source_path: "tests/conftest.py"
description: "Configuration for the tests."
tags: ["module", "conftest"]
timestamp: "2026-09-05T05:14:18Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "4860b15"
---
# Module Specification: conftest

* **Source Reference:** [tests/conftest.py](../../../tests/conftest.py)

# Module Overview

## Purpose

Configuration for the tests.

## Responsibilities

Configuration for the tests.

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

# Each File Documentation

## Imported modules

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

## Exported functions

* `tests_path`

* `data_path`

* `confs_path`

* `inputs_path`

* `targets_path`

* `outputs_path`

* `tmp_outputs_path`

* `tmp_models_explanations_path`

* `tmp_samples_explanations_path`

* `extra_config`

* `inputs_reader`

* `inputs_samples_reader`

* `targets_reader`

* `outputs_reader`

* `tmp_outputs_writer`

* `tmp_models_explanations_writer`

* `tmp_samples_explanations_writer`

* `inputs`

* `inputs_samples`

* `targets`

* `outputs`

* `train_test_splitter`

* `time_series_splitter`

* `searcher`

* `train_test_sets`

* `model`

* `metric`

* `signer`

* `logger_service`

* `logger_caplog`

* `alerts_service`

* `mlflow_service`

* `tests_path_resolver`

* `tmp_path_resolver`

* `signature`

* `saver`

* `loader`

* `register`

* `model_version`

* `model_alias`

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

### Description

Return the path of the tests folder.

### Inputs

### Output

* **return type**: str

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for tests_path

```

### `data_path(tests_path: str) -> str`

### Description

Return the path of the data folder.

### Inputs

* `tests_path`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: str

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for data_path

```

### `confs_path(tests_path: str) -> str`

### Description

Return the path of the confs folder.

### Inputs

* `tests_path`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: str

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for confs_path

```

### `inputs_path(data_path: str) -> str`

### Description

Return the path of the inputs dataset.

### Inputs

* `data_path`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: str

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for inputs_path

```

### `targets_path(data_path: str) -> str`

### Description

Return the path of the targets dataset.

### Inputs

* `data_path`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: str

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for targets_path

```

### `outputs_path(data_path: str) -> str`

### Description

Return the path of the outputs dataset.

### Inputs

* `data_path`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: str

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for outputs_path

```

### `tmp_outputs_path(tmp_path: str) -> str`

### Description

Return a tmp path for the outputs dataset.

### Inputs

* `tmp_path`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: str

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for tmp_outputs_path

```

### `tmp_models_explanations_path(tmp_path: str) -> str`

### Description

Return a tmp path for the model explanations dataset.

### Inputs

* `tmp_path`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: str

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for tmp_models_explanations_path

```

### `tmp_samples_explanations_path(tmp_path: str) -> str`

### Description

Return a tmp path for the samples explanations dataset.

### Inputs

* `tmp_path`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: str

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for tmp_samples_explanations_path

```

### `extra_config() -> str`

### Description

Extra config for scripts.

### Inputs

### Output

* **return type**: str

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for extra_config

```

### `inputs_reader(inputs_path: str) -> datasets.ParquetReader`

### Description

Return a reader for the inputs dataset.

### Inputs

* `inputs_path`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: datasets.ParquetReader

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for inputs_reader

```

### `inputs_samples_reader(inputs_path: str) -> datasets.ParquetReader`

### Description

Return a reader for the inputs samples dataset.

### Inputs

* `inputs_path`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: datasets.ParquetReader

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for inputs_samples_reader

```

### `targets_reader(targets_path: str) -> datasets.ParquetReader`

### Description

Return a reader for the targets dataset.

### Inputs

* `targets_path`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: datasets.ParquetReader

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for targets_reader

```

### `outputs_reader(outputs_path: str, inputs_reader: datasets.ParquetReader, targets_reader: datasets.ParquetReader) -> datasets.ParquetReader`

### Description

Return a reader for the outputs dataset.

### Inputs

* `outputs_path`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `inputs_reader`

  - **type**: datasets.ParquetReader

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `targets_reader`

  - **type**: datasets.ParquetReader

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: datasets.ParquetReader

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for outputs_reader

```

### `tmp_outputs_writer(tmp_outputs_path: str) -> datasets.ParquetWriter`

### Description

Return a writer for the tmp outputs dataset.

### Inputs

* `tmp_outputs_path`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: datasets.ParquetWriter

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for tmp_outputs_writer

```

### `tmp_models_explanations_writer(tmp_models_explanations_path: str) -> datasets.ParquetWriter`

### Description

Return a writer for the tmp model explanations dataset.

### Inputs

* `tmp_models_explanations_path`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: datasets.ParquetWriter

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for tmp_models_explanations_writer

```

### `tmp_samples_explanations_writer(tmp_samples_explanations_path: str) -> datasets.ParquetWriter`

### Description

Return a writer for the tmp samples explanations dataset.

### Inputs

* `tmp_samples_explanations_path`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: datasets.ParquetWriter

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for tmp_samples_explanations_writer

```

### `inputs(inputs_reader: datasets.ParquetReader) -> schemas.Inputs`

### Description

Return the inputs data.

### Inputs

* `inputs_reader`

  - **type**: datasets.ParquetReader

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: schemas.Inputs

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for inputs

```

### `inputs_samples(inputs_samples_reader: datasets.ParquetReader) -> schemas.Inputs`

### Description

Return the inputs samples data.

### Inputs

* `inputs_samples_reader`

  - **type**: datasets.ParquetReader

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: schemas.Inputs

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for inputs_samples

```

### `targets(targets_reader: datasets.ParquetReader) -> schemas.Targets`

### Description

Return the targets data.

### Inputs

* `targets_reader`

  - **type**: datasets.ParquetReader

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: schemas.Targets

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for targets

```

### `outputs(outputs_reader: datasets.ParquetReader) -> schemas.Outputs`

### Description

Return the outputs data.

### Inputs

* `outputs_reader`

  - **type**: datasets.ParquetReader

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: schemas.Outputs

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for outputs

```

### `train_test_splitter() -> splitters.TrainTestSplitter`

### Description

Return the default train test splitter.

### Inputs

### Output

* **return type**: splitters.TrainTestSplitter

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for train_test_splitter

```

### `time_series_splitter() -> splitters.TimeSeriesSplitter`

### Description

Return the default time series splitter.

### Inputs

### Output

* **return type**: splitters.TimeSeriesSplitter

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for time_series_splitter

```

### `searcher() -> searchers.Searcher`

### Description

Return the default searcher object.

### Inputs

### Output

* **return type**: searchers.Searcher

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for searcher

```

### `train_test_sets(train_test_splitter: splitters.Splitter, inputs: schemas.Inputs, targets: schemas.Targets) -> tuple[(schemas.Inputs, schemas.Targets, schemas.Inputs, schemas.Targets)]`

### Description

Return the inputs and targets train and test sets from the splitter.

### Inputs

* `train_test_splitter`

  - **type**: splitters.Splitter

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `inputs`

  - **type**: schemas.Inputs

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `targets`

  - **type**: schemas.Targets

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: tuple[(schemas.Inputs, schemas.Targets, schemas.Inputs, schemas.Targets)]

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for train_test_sets

```

### `model(train_test_sets: tuple[(schemas.Inputs, schemas.Targets, schemas.Inputs, schemas.Targets)]) -> models.BaselineSklearnModel`

### Description

Return a train model for testing.

### Inputs

* `train_test_sets`

  - **type**: tuple[(schemas.Inputs, schemas.Targets, schemas.Inputs, schemas.Targets)]

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: models.BaselineSklearnModel

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for model

```

### `metric() -> metrics.SklearnMetric`

### Description

Return the default metric.

### Inputs

### Output

* **return type**: metrics.SklearnMetric

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for metric

```

### `signer() -> signers.Signer`

### Description

Return a model signer.

### Inputs

### Output

* **return type**: signers.Signer

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for signer

```

### `logger_service() -> T.Generator[(services.LoggerService, None, None)]`

### Description

Return and start the logger service.

### Inputs

### Output

* **return type**: T.Generator[(services.LoggerService, None, None)]

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for logger_service

```

### `logger_caplog(caplog: pl.LogCaptureFixture, logger_service: services.LoggerService) -> T.Generator[(pl.LogCaptureFixture, None, None)]`

### Description

Extend pytest caplog fixture with the logger service (loguru).

### Inputs

* `caplog`

  - **type**: pl.LogCaptureFixture

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `logger_service`

  - **type**: services.LoggerService

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: T.Generator[(pl.LogCaptureFixture, None, None)]

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for logger_caplog

```

### `alerts_service() -> T.Generator[(services.AlertsService, None, None)]`

### Description

Return and start the alerter service.

### Inputs

### Output

* **return type**: T.Generator[(services.AlertsService, None, None)]

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for alerts_service

```

### `mlflow_service(tmp_path: str) -> T.Generator[(services.MlflowService, None, None)]`

### Description

Return and start the mlflow service.

### Inputs

* `tmp_path`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: T.Generator[(services.MlflowService, None, None)]

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for mlflow_service

```

### `tests_path_resolver(tests_path: str) -> str`

### Description

Register the tests path resolver with OmegaConf.

### Inputs

* `tests_path`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: str

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for tests_path_resolver

```

### `tmp_path_resolver(tmp_path: str) -> str`

### Description

Register the tmp path resolver with OmegaConf.

### Inputs

* `tmp_path`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: str

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for tmp_path_resolver

```

### `signature(signer: signers.Signer, inputs: schemas.Inputs, outputs: schemas.Outputs) -> signers.Signature`

### Description

Return the signature for the testing model.

### Inputs

* `signer`

  - **type**: signers.Signer

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `inputs`

  - **type**: schemas.Inputs

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `outputs`

  - **type**: schemas.Outputs

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: signers.Signature

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for signature

```

### `saver() -> registries.CustomSaver`

### Description

Return the default model saver.

### Inputs

### Output

* **return type**: registries.CustomSaver

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for saver

```

### `loader() -> registries.CustomLoader`

### Description

Return the default model loader.

### Inputs

### Output

* **return type**: registries.CustomLoader

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for loader

```

### `register() -> registries.MlflowRegister`

### Description

Return the default model register.

### Inputs

### Output

* **return type**: registries.MlflowRegister

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for register

```

### `model_version(model: models.Model, inputs: schemas.Inputs, signature: signers.Signature, saver: registries.Saver, register: registries.Register, mlflow_service: services.MlflowService) -> registries.Version`

### Description

Save and register the default model version.

### Inputs

* `model`

  - **type**: models.Model

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `inputs`

  - **type**: schemas.Inputs

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `signature`

  - **type**: signers.Signature

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `saver`

  - **type**: registries.Saver

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `register`

  - **type**: registries.Register

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `mlflow_service`

  - **type**: services.MlflowService

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: registries.Version

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for model_version

```

### `model_alias(model_version: registries.Version, mlflow_service: services.MlflowService) -> registries.Alias`

### Description

Promote the default model version with an alias.

### Inputs

* `model_version`

  - **type**: registries.Version

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `mlflow_service`

  - **type**: services.MlflowService

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: registries.Alias

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for model_alias

```

## Used By

_Not used by any other module._
