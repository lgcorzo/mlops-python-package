# BUILDER STAGE
FROM python:3.12-slim AS builder

WORKDIR /build

# Install Poetry and export plugin
RUN pip install poetry==1.8.3

# Copy dependency files
COPY pyproject.toml poetry.lock README.md ./

# Export requirements.txt from poetry.lock for robust pip installation
# We use --without-hashes to avoid issues with some platforms/versions
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

# Copy source code
COPY src/ ./src/

# Build the wheel
RUN poetry build --format=wheel

# RUNNER STAGE
FROM python:3.12-slim

WORKDIR /app

# Copy requirements and wheel from builder
COPY --from=builder /build/requirements.txt .
COPY --from=builder /build/dist/*.whl .

# Install dependencies from the EXACT versions solved by Poetry
RUN pip install -r requirements.txt
# Install the application wheel
RUN pip install *.whl

# Copy configurations
COPY confs/ ./confs/

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Entrypoint for the Kafka application
CMD ["python", "-m", "regression_model_template.controller.kafka_app"]
