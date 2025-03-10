"""Scripts for the CLI application."""

# ruff: noqa: E402

# %% IMPORTS

import argparse
import json
import sys
import logging
import warnings

from regression_model_template import settings
from regression_model_template.io import configs

from opentelemetry import trace, metrics
from opentelemetry._logs import set_logger_provider

from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.resources import Resource
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.exporter.otlp.proto.http._log_exporter import OTLPLogExporter

# %% WARNINGS

# Disable annoying mlflow warnings
warnings.filterwarnings(action="ignore", category=UserWarning)

# %% LOGGING & TELEMETRY SETUP

tracer_provider = TracerProvider()
trace.set_tracer_provider(tracer_provider)
otlp_trace_exporter = OTLPSpanExporter()
tracer_provider.add_span_processor(BatchSpanProcessor(otlp_trace_exporter))

# Logging setup
logger_provider = LoggerProvider()
set_logger_provider(logger_provider)
otlp_log_exporter = OTLPLogExporter()
logger_provider.add_log_record_processor(BatchLogRecordProcessor(otlp_log_exporter))

# Attach OpenTelemetry handler to Python's logging
otel_handler = LoggingHandler(level=logging.INFO, logger_provider=logger_provider)
logging.getLogger().addHandler(otel_handler)

# Root logger configuration
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("regression_model")

# %% PARSERS

parser = argparse.ArgumentParser(description="Run an AI/ML job from YAML/JSON configs.")
parser.add_argument("files", nargs="*", help="Config files for the job (local path only).")
parser.add_argument("-e", "--extras", nargs="*", default=[], help="Config strings for the job.")
parser.add_argument("-s", "--schema", action="store_true", help="Print settings schema and exit.")

# %% SCRIPTS


def main(argv: list[str] | None = None) -> int:
    """Main script for the application."""

    tracer = trace.get_tracer(__name__)

    with tracer.start_as_current_span("main_execution") as span:
        logger.info("Starting the application...")

        args = parser.parse_args(argv)

        if args.schema:
            schema = settings.MainSettings.model_json_schema()
            json.dump(schema, sys.stdout, indent=4)
            logger.info("Schema printed successfully.")
            return 0

        files = [configs.parse_file(file) for file in args.files]
        strings = [configs.parse_string(string) for string in args.extras]

        if len(files) == 0 and len(strings) == 0:
            logger.error("No configs provided.")
            raise RuntimeError("No configs provided.")

        logger.debug(f"Loaded {len(files)} files and {len(strings)} string configs.")

        config = configs.merge_configs([*files, *strings])
        object_ = configs.to_object(config)
        setting = settings.MainSettings.model_validate(object_)

        with setting.job as runner:
            logger.info("Starting job execution...")
            runner.run()
            logger.info("Job execution completed successfully.")

        logger.info("Application finished.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
