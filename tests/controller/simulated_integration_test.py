import requests
import time
import subprocess
import os
import sys

# This script will run the actual FastAPI app but mock the Kafka part to allow it to start
# without a real Kafka server.


def run_simulated_test():
    print("Starting Kafka app integration test (Simulated with Mocks)...")

    # We'll use a wrapper script to run the app with mocks
    wrapper_code = """
import sys
from unittest.mock import patch, MagicMock

# Mock Kafka before importing the app
mock_producer = patch('confluent_kafka.Producer').start()
mock_consumer = patch('confluent_kafka.Consumer').start()

from regression_model_template.controller.kafka_app import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8123)
"""
    with open("tests/controller/app_wrapper.py", "w") as f:
        f.write(wrapper_code)

    env = os.environ.copy()
    env["DEFAULT_KAFKA_SERVER"] = "localhost:9092"
    env["DEFAULT_FASTAPI_HOST"] = "127.0.0.1"
    env["DEFAULT_FASTAPI_PORT"] = "8123"

    print("Launching FastAPI server via wrapper...")
    process = subprocess.Popen(
        [sys.executable, "tests/controller/app_wrapper.py"],
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    try:
        # Wait for the server to start
        time.sleep(5)

        print("Checking health endpoint...")
        response = requests.get("http://127.0.0.1:8123/health", timeout=5)
        print(f"Health Response: {response.status_code} - {response.json()}")

        if response.status_code == 200:
            print("Integration test passed!")
        else:
            print(f"Integration test failed with status: {response.status_code}")

    except Exception as e:
        print(f"Integration test encountered an error: {e}")
        raise

    finally:
        print("Shutting down the server...")
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
        if os.path.exists("tests/controller/app_wrapper.py"):
            os.remove("tests/controller/app_wrapper.py")


if __name__ == "__main__":
    run_simulated_test()
