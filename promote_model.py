import mlflow
from mlflow.tracking import MlflowClient
import os


def promote_model():
    tracking_uri = os.getenv("MLFLOW_TRACKING_URI", "http://mlflow.llm-apps.svc.cluster.local:5000")
    registry_uri = os.getenv("MLFLOW_REGISTRY_URI", tracking_uri)
    model_name = os.getenv("MLFLOW_REGISTERED_MODEL_NAME", "regression_model_template")

    mlflow.set_tracking_uri(tracking_uri)
    mlflow.set_registry_uri(registry_uri)

    client = MlflowClient()

    print(f"Promoting {model_name} version 1 to Champion...")
    client.set_registered_model_alias(name=model_name, alias="Champion", version="1")

    # Verify
    model = client.get_model_version_by_alias(name=model_name, alias="Champion")
    print(f"Success! Model {model.name} Version {model.version} is now 'Champion'.")


if __name__ == "__main__":
    promote_model()
