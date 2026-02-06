import mlflow
import os
import sys
from confluent_kafka import Producer

def check_env():
    print(f"Tracking URI: {mlflow.get_tracking_uri()}")
    try:
        models = mlflow.search_registered_models()
        print("\nRegistered Models:")
        for m in models:
            print(f"- {m.name}")
            for v in m.latest_versions:
                print(f"  Version {v.version}: Aliases={v.aliases}")
                
        # Check Kafka
        kafka_server = os.getenv("DEFAULT_KAFKA_SERVER", "localhost:9092")
        print(f"\nTesting Kafka Producer to: {kafka_server}")
        p = Producer({'bootstrap.servers': kafka_server, 'socket.timeout.ms': 2000})
        p.produce('test_topic', b'test')
        p.flush(timeout=2.0)
        print("Kafka reachable!")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_env()
