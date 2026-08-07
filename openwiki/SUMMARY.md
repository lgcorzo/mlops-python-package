---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDescription"
type: "summary"
title: "Summary"
description: "Auto-generated summary."
tags: ["summary"]
timestamp: "2026-08-07T08:29:41Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "12aa8d5"
---
# Summary

## Architecture overview

* [Home](index.md)
* [Logs](logs.md)
* [Diagrams](architecture/diagrams.md)

## Alphabetical class index

* [AlertsService](modules/regression_model_template/io/services.md#alertsservice)
* [BaselineSklearnModel](modules/regression_model_template/core/models.md#baselinesklearnmodel)
* [BuiltinLoader](modules/regression_model_template/io/registries.md#builtinloader)
* [BuiltinSaver](modules/regression_model_template/io/registries.md#builtinsaver)
* [CustomLoader](modules/regression_model_template/io/registries.md#customloader)
* [CustomSaver](modules/regression_model_template/io/registries.md#customsaver)
* [Env](modules/regression_model_template/io/osvariables.md#env)
* [EvaluationsJob](modules/regression_model_template/jobs/evaluations.md#evaluationsjob)
* [ExplanationsJob](modules/regression_model_template/jobs/explanations.md#explanationsjob)
* [FastAPIKafkaService](modules/regression_model_template/controller/kafka_app.md#fastapikafkaservice)
* [FeatureImportancesSchema](modules/regression_model_template/core/schemas.md#featureimportancesschema)
* [GridCVSearcher](modules/regression_model_template/utils/searchers.md#gridcvsearcher)
* [InferSigner](modules/regression_model_template/utils/signers.md#infersigner)
* [InferenceJob](modules/regression_model_template/jobs/inference.md#inferencejob)
* [InputsSchema](modules/regression_model_template/core/schemas.md#inputsschema)
* [Job](modules/regression_model_template/jobs/base.md#job)
* [Loader](modules/regression_model_template/io/registries.md#loader)
* [LoggerService](modules/regression_model_template/io/services.md#loggerservice)
* [MainSettings](modules/regression_model_template/settings.md#mainsettings)
* [Metric](modules/regression_model_template/core/metrics.md#metric)
* [MlflowRegister](modules/regression_model_template/io/registries.md#mlflowregister)
* [MlflowService](modules/regression_model_template/io/services.md#mlflowservice)
* [Model](modules/regression_model_template/core/models.md#model)
* [OutputsSchema](modules/regression_model_template/core/schemas.md#outputsschema)
* [ParquetReader](modules/regression_model_template/io/datasets.md#parquetreader)
* [ParquetWriter](modules/regression_model_template/io/datasets.md#parquetwriter)
* [PredictionRequest](modules/regression_model_template/controller/kafka_app.md#predictionrequest)
* [PredictionResponse](modules/regression_model_template/controller/kafka_app.md#predictionresponse)
* [PredictionService](modules/regression_model_template/controller/kafka_app.md#predictionservice)
* [PromotionJob](modules/regression_model_template/jobs/promotion.md#promotionjob)
* [PropagateHandler](modules/regression_model_template/io/services.md#propagatehandler)
* [RateLimiter](modules/regression_model_template/controller/kafka_app.md#ratelimiter)
* [Reader](modules/regression_model_template/io/datasets.md#reader)
* [Register](modules/regression_model_template/io/registries.md#register)
* [SHAPValuesSchema](modules/regression_model_template/core/schemas.md#shapvaluesschema)
* [Saver](modules/regression_model_template/io/registries.md#saver)
* [Schema](modules/regression_model_template/core/schemas.md#schema)
* [Searcher](modules/regression_model_template/utils/searchers.md#searcher)
* [Service](modules/regression_model_template/io/services.md#service)
* [Settings](modules/regression_model_template/settings.md#settings)
* [Signer](modules/regression_model_template/utils/signers.md#signer)
* [Singleton](modules/regression_model_template/io/osvariables.md#singleton)
* [SklearnMetric](modules/regression_model_template/core/metrics.md#sklearnmetric)
* [Splitter](modules/regression_model_template/utils/splitters.md#splitter)
* [TargetsSchema](modules/regression_model_template/core/schemas.md#targetsschema)
* [Threshold](modules/regression_model_template/core/metrics.md#threshold)
* [TimeSeriesSplitter](modules/regression_model_template/utils/splitters.md#timeseriessplitter)
* [TrainTestSplitter](modules/regression_model_template/utils/splitters.md#traintestsplitter)
* [TrainingJob](modules/regression_model_template/jobs/training.md#trainingjob)
* [TuningJob](modules/regression_model_template/jobs/tuning.md#tuningjob)
* [Writer](modules/regression_model_template/io/datasets.md#writer)

## Public API index

* [default_input_payload](modules/regression_model_template/controller/kafka_app.md#default_input_payload)
* [generate_data](modules/regression_model_template/init_data.md#generate_data)
* [main](modules/regression_model_template/controller/kafka_app.md#main)
* [merge_configs](modules/regression_model_template/io/configs.md#merge_configs)
* [parse_file](modules/regression_model_template/io/configs.md#parse_file)
* [parse_string](modules/regression_model_template/io/configs.md#parse_string)
* [to_object](modules/regression_model_template/io/configs.md#to_object)
* [uri_for_model_alias](modules/regression_model_template/io/registries.md#uri_for_model_alias)
* [uri_for_model_alias_or_version](modules/regression_model_template/io/registries.md#uri_for_model_alias_or_version)
* [uri_for_model_version](modules/regression_model_template/io/registries.md#uri_for_model_version)

## Modules list

* [__init__](modules/regression_model_template/__init__.md)
* [__init__](modules/regression_model_template/controller/__init__.md)
* [__init__](modules/regression_model_template/core/__init__.md)
* [__init__](modules/regression_model_template/io/__init__.md)
* [__init__](modules/regression_model_template/jobs/__init__.md)
* [__init__](modules/regression_model_template/utils/__init__.md)
* [__main__](modules/regression_model_template/__main__.md)
* [base](modules/regression_model_template/jobs/base.md)
* [configs](modules/regression_model_template/io/configs.md)
* [datasets](modules/regression_model_template/io/datasets.md)
* [evaluations](modules/regression_model_template/jobs/evaluations.md)
* [explanations](modules/regression_model_template/jobs/explanations.md)
* [inference](modules/regression_model_template/jobs/inference.md)
* [init_data](modules/regression_model_template/init_data.md)
* [kafka_app](modules/regression_model_template/controller/kafka_app.md)
* [metrics](modules/regression_model_template/core/metrics.md)
* [models](modules/regression_model_template/core/models.md)
* [osvariables](modules/regression_model_template/io/osvariables.md)
* [promotion](modules/regression_model_template/jobs/promotion.md)
* [registries](modules/regression_model_template/io/registries.md)
* [schemas](modules/regression_model_template/core/schemas.md)
* [scripts](modules/regression_model_template/scripts.md)
* [searchers](modules/regression_model_template/utils/searchers.md)
* [services](modules/regression_model_template/io/services.md)
* [settings](modules/regression_model_template/settings.md)
* [signers](modules/regression_model_template/utils/signers.md)
* [splitters](modules/regression_model_template/utils/splitters.md)
* [training](modules/regression_model_template/jobs/training.md)
* [tuning](modules/regression_model_template/jobs/tuning.md)
