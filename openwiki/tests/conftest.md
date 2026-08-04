---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDescription"
type: "concept"
title: "conftest Documentation"
description: "Documentation for tests/conftest.py"
tags: ["module", "conftest"]
timestamp: "2026-08-04T05:28:53Z"
generated: "agent:ast-documentation-generator"
verified: "true"
---

# Module: `tests/conftest.py`

## Overview
**Purpose**: Configuration for the tests.

**Architecture Role**: Infrastructure

**Dependencies**:
- `regression_model_template.core`
- `typing`
- `regression_model_template.io`
- `omegaconf`
- `pytest`
- `_pytest`
- `os`
- `regression_model_template.utils`

**Exported Symbols**:
- `tests_path`
- `data_path`
- `confs_path`
- `inputs_path`
- `targets_path`
- `outputs_path`
- `tmp_outputs_path`
- `tmp_models_explanations_path`
- `tmp_samples_explanations_path`
- `extra_config`
- `inputs_reader`
- `inputs_samples_reader`
- `targets_reader`
- `outputs_reader`
- `tmp_outputs_writer`
- `tmp_models_explanations_writer`
- `tmp_samples_explanations_writer`
- `inputs`
- `inputs_samples`
- `targets`
- `outputs`
- `train_test_splitter`
- `time_series_splitter`
- `searcher`
- `train_test_sets`
- `model`
- `metric`
- `signer`
- `logger_service`
- `logger_caplog`
- `alerts_service`
- `mlflow_service`
- `tests_path_resolver`
- `tmp_path_resolver`
- `signature`
- `saver`
- `loader`
- `register`
- `model_version`
- `model_alias`

## UML Class Diagram
```plantuml
@startuml
@enduml
```

## Call Graph
```plantuml
@startuml
tests_path --> fixture
tests_path --> abspath
tests_path --> dirname
data_path --> fixture
data_path --> join
confs_path --> fixture
confs_path --> join
inputs_path --> fixture
inputs_path --> join
targets_path --> fixture
targets_path --> join
outputs_path --> fixture
outputs_path --> join
tmp_outputs_path --> fixture
tmp_outputs_path --> join
tmp_models_explanations_path --> fixture
tmp_models_explanations_path --> join
tmp_samples_explanations_path --> fixture
tmp_samples_explanations_path --> join
extra_config --> fixture
inputs_reader --> fixture
inputs_reader --> ParquetReader
inputs_samples_reader --> fixture
inputs_samples_reader --> ParquetReader
targets_reader --> fixture
targets_reader --> ParquetReader
outputs_reader --> fixture
outputs_reader --> ParquetReader
outputs_reader --> exists
outputs_reader --> check
outputs_reader --> check
outputs_reader --> fit
outputs_reader --> check
outputs_reader --> ParquetWriter
outputs_reader --> write
outputs_reader --> read
outputs_reader --> read
outputs_reader --> predict
outputs_reader --> BaselineSklearnModel
tmp_outputs_writer --> fixture
tmp_outputs_writer --> ParquetWriter
tmp_models_explanations_writer --> fixture
tmp_models_explanations_writer --> ParquetWriter
tmp_samples_explanations_writer --> fixture
tmp_samples_explanations_writer --> ParquetWriter
inputs --> fixture
inputs --> read
inputs --> check
inputs_samples --> fixture
inputs_samples --> read
inputs_samples --> check
targets --> fixture
targets --> read
targets --> check
outputs --> fixture
outputs --> read
outputs --> check
train_test_splitter --> fixture
train_test_splitter --> TrainTestSplitter
time_series_splitter --> fixture
time_series_splitter --> TimeSeriesSplitter
searcher --> fixture
searcher --> GridCVSearcher
train_test_sets --> fixture
train_test_sets --> next
train_test_sets --> split
train_test_sets --> cast
train_test_sets --> cast
train_test_sets --> cast
train_test_sets --> cast
model --> fixture
model --> BaselineSklearnModel
model --> fit
metric --> fixture
metric --> SklearnMetric
signer --> fixture
signer --> InferSigner
logger_service --> fixture
logger_service --> LoggerService
logger_service --> start
logger_service --> stop
logger_caplog --> logger
logger_caplog --> add
logger_caplog --> remove
alerts_service --> fixture
alerts_service --> AlertsService
alerts_service --> start
alerts_service --> stop
mlflow_service --> fixture
mlflow_service --> MlflowService
mlflow_service --> start
mlflow_service --> stop
tests_path_resolver --> fixture
tests_path_resolver --> register_new_resolver
tmp_path_resolver --> fixture
tmp_path_resolver --> register_new_resolver
signature --> fixture
signature --> sign
saver --> fixture
saver --> CustomSaver
loader --> fixture
loader --> CustomLoader
register --> fixture
register --> MlflowRegister
model_version --> fixture
model_version --> RunConfig
model_version --> run_context
model_version --> save
model_version --> register
model_alias --> fixture
model_alias --> client
model_alias --> set_registered_model_alias
model_alias --> get_model_version_by_alias
@enduml
```

## Classes
## Functions
### Function `tests_path`
- **Description**: Return the path of the tests folder.
- **Inputs**:
- **Output**: `str`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `data_path`
- **Description**: Return the path of the data folder.
- **Inputs**:
  - `tests_path`: str
- **Output**: `str`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `confs_path`
- **Description**: Return the path of the confs folder.
- **Inputs**:
  - `tests_path`: str
- **Output**: `str`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `inputs_path`
- **Description**: Return the path of the inputs dataset.
- **Inputs**:
  - `data_path`: str
- **Output**: `str`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `targets_path`
- **Description**: Return the path of the targets dataset.
- **Inputs**:
  - `data_path`: str
- **Output**: `str`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `outputs_path`
- **Description**: Return the path of the outputs dataset.
- **Inputs**:
  - `data_path`: str
- **Output**: `str`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `tmp_outputs_path`
- **Description**: Return a tmp path for the outputs dataset.
- **Inputs**:
  - `tmp_path`: str
- **Output**: `str`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `tmp_models_explanations_path`
- **Description**: Return a tmp path for the model explanations dataset.
- **Inputs**:
  - `tmp_path`: str
- **Output**: `str`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `tmp_samples_explanations_path`
- **Description**: Return a tmp path for the samples explanations dataset.
- **Inputs**:
  - `tmp_path`: str
- **Output**: `str`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `extra_config`
- **Description**: Extra config for scripts.
- **Inputs**:
- **Output**: `str`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `inputs_reader`
- **Description**: Return a reader for the inputs dataset.
- **Inputs**:
  - `inputs_path`: str
- **Output**: `datasets.ParquetReader`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `inputs_samples_reader`
- **Description**: Return a reader for the inputs samples dataset.
- **Inputs**:
  - `inputs_path`: str
- **Output**: `datasets.ParquetReader`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `targets_reader`
- **Description**: Return a reader for the targets dataset.
- **Inputs**:
  - `targets_path`: str
- **Output**: `datasets.ParquetReader`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `outputs_reader`
- **Description**: Return a reader for the outputs dataset.
- **Inputs**:
  - `outputs_path`: str
  - `inputs_reader`: datasets.ParquetReader
  - `targets_reader`: datasets.ParquetReader
- **Output**: `datasets.ParquetReader`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `tmp_outputs_writer`
- **Description**: Return a writer for the tmp outputs dataset.
- **Inputs**:
  - `tmp_outputs_path`: str
- **Output**: `datasets.ParquetWriter`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `tmp_models_explanations_writer`
- **Description**: Return a writer for the tmp model explanations dataset.
- **Inputs**:
  - `tmp_models_explanations_path`: str
- **Output**: `datasets.ParquetWriter`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `tmp_samples_explanations_writer`
- **Description**: Return a writer for the tmp samples explanations dataset.
- **Inputs**:
  - `tmp_samples_explanations_path`: str
- **Output**: `datasets.ParquetWriter`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `inputs`
- **Description**: Return the inputs data.
- **Inputs**:
  - `inputs_reader`: datasets.ParquetReader
- **Output**: `schemas.Inputs`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `inputs_samples`
- **Description**: Return the inputs samples data.
- **Inputs**:
  - `inputs_samples_reader`: datasets.ParquetReader
- **Output**: `schemas.Inputs`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `targets`
- **Description**: Return the targets data.
- **Inputs**:
  - `targets_reader`: datasets.ParquetReader
- **Output**: `schemas.Targets`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `outputs`
- **Description**: Return the outputs data.
- **Inputs**:
  - `outputs_reader`: datasets.ParquetReader
- **Output**: `schemas.Outputs`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `train_test_splitter`
- **Description**: Return the default train test splitter.
- **Inputs**:
- **Output**: `splitters.TrainTestSplitter`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `time_series_splitter`
- **Description**: Return the default time series splitter.
- **Inputs**:
- **Output**: `splitters.TimeSeriesSplitter`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `searcher`
- **Description**: Return the default searcher object.
- **Inputs**:
- **Output**: `searchers.Searcher`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `train_test_sets`
- **Description**: Return the inputs and targets train and test sets from the splitter.
- **Inputs**:
  - `train_test_splitter`: splitters.Splitter
  - `inputs`: schemas.Inputs
  - `targets`: schemas.Targets
- **Output**: `tuple[schemas.Inputs, schemas.Targets, schemas.Inputs, schemas.Targets]`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `model`
- **Description**: Return a train model for testing.
- **Inputs**:
  - `train_test_sets`: tuple[schemas.Inputs, schemas.Targets, schemas.Inputs, schemas.Targets]
- **Output**: `models.BaselineSklearnModel`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `metric`
- **Description**: Return the default metric.
- **Inputs**:
- **Output**: `metrics.SklearnMetric`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `signer`
- **Description**: Return a model signer.
- **Inputs**:
- **Output**: `signers.Signer`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `logger_service`
- **Description**: Return and start the logger service.
- **Inputs**:
- **Output**: `T.Generator[services.LoggerService, None, None]`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `logger_caplog`
- **Description**: Extend pytest caplog fixture with the logger service (loguru).
- **Inputs**:
  - `caplog`: pl.LogCaptureFixture
  - `logger_service`: services.LoggerService
- **Output**: `T.Generator[pl.LogCaptureFixture, None, None]`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `alerts_service`
- **Description**: Return and start the alerter service.
- **Inputs**:
- **Output**: `T.Generator[services.AlertsService, None, None]`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `mlflow_service`
- **Description**: Return and start the mlflow service.
- **Inputs**:
  - `tmp_path`: str
- **Output**: `T.Generator[services.MlflowService, None, None]`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `tests_path_resolver`
- **Description**: Register the tests path resolver with OmegaConf.
- **Inputs**:
  - `tests_path`: str
- **Output**: `str`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `tmp_path_resolver`
- **Description**: Register the tmp path resolver with OmegaConf.
- **Inputs**:
  - `tmp_path`: str
- **Output**: `str`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `signature`
- **Description**: Return the signature for the testing model.
- **Inputs**:
  - `signer`: signers.Signer
  - `inputs`: schemas.Inputs
  - `outputs`: schemas.Outputs
- **Output**: `signers.Signature`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `saver`
- **Description**: Return the default model saver.
- **Inputs**:
- **Output**: `registries.CustomSaver`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `loader`
- **Description**: Return the default model loader.
- **Inputs**:
- **Output**: `registries.CustomLoader`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `register`
- **Description**: Return the default model register.
- **Inputs**:
- **Output**: `registries.MlflowRegister`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `model_version`
- **Description**: Save and register the default model version.
- **Inputs**:
  - `model`: models.Model
  - `inputs`: schemas.Inputs
  - `signature`: signers.Signature
  - `saver`: registries.Saver
  - `register`: registries.Register
  - `mlflow_service`: services.MlflowService
- **Output**: `registries.Version`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `model_alias`
- **Description**: Promote the default model version with an alias.
- **Inputs**:
  - `model_version`: registries.Version
  - `mlflow_service`: services.MlflowService
- **Output**: `registries.Alias`
- **Side Effects**: Not documented
- **Complexity**: Not documented
