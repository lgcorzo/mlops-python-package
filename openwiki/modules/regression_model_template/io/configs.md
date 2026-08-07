---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: configs"
source_path: "src/regression_model_template/io/configs.py"
description: "Parse, merge, and convert config objects."
tags: ["module", "configs"]
timestamp: "2026-08-07T08:29:41Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "12aa8d5"
---
# Module Specification: configs

* **Source Reference:** [src/regression_model_template/io/configs.py](../../../src/regression_model_template/io/configs.py)

## 1. Architectural Role & Responsibilities
Parse, merge, and convert config objects.

## 2. UML 2.0 Class Diagram
_No classes found._

## 3. Class & Method Specifications

## Standalone Functions

### `parse_file(path: str) -> Config`
Parse a config file from a path.

Args:
    path (str): path to local config.

Returns:
    Config: representation of the config file.

#### Inputs
* `path` (`str`)

#### Outputs
* `Config`

### `parse_string(string: str) -> Config`
Parse the given config string.

Args:
    string (str): content of config string.

Returns:
    Config: representation of the config string.

#### Inputs
* `string` (`str`)

#### Outputs
* `Config`

### `merge_configs(configs: T.Sequence[Config]) -> Config`
Merge a list of config into a single config.

Args:
    configs (T.Sequence[Config]): list of configs.

Returns:
    Config: representation of the merged config objects.

#### Inputs
* `configs` (`T.Sequence[Config]`)

#### Outputs
* `Config`

### `to_object(config: Config, resolve: bool) -> object`
Convert a config object to a python object.

Args:
    config (Config): representation of the config.
    resolve (bool): resolve variables. Defaults to True.

Returns:
    object: conversion of the config to a python object.

#### Inputs
* `config` (`Config`)
* `resolve` (`bool`)

#### Outputs
* `object`

## Dependencies

* `typing`
* `omegaconf`

## Used By

* [scripts.py](../../regression_model_template/scripts.md)
