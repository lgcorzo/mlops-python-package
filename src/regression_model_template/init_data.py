"""Script to initialize synthetic train and test parquet datasets."""

import argparse
import os
import numpy as np
import pandas as pd
from regression_model_template.core.schemas import InputsSchema, TargetsSchema


def generate_data(output_dir: str = "data") -> None:
    """Generate synthetic regression data and validate schemas."""
    os.makedirs(output_dir, exist_ok=True)
    n = 10000
    dates = pd.date_range("2024-01-01", periods=n, freq="h")
    inputs = pd.DataFrame(
        {
            "dteday": dates,
            "season": np.random.choice([1, 2, 3, 4], size=n).astype("uint8"),
            "yr": np.random.choice([0, 1], size=n).astype("uint8"),
            "mnth": np.random.choice(range(1, 13), size=n).astype("uint8"),
            "hr": np.random.choice(range(0, 24), size=n).astype("uint8"),
            "holiday": np.random.choice([True, False], size=n),
            "weekday": np.random.choice(range(0, 7), size=n).astype("uint8"),
            "workingday": np.random.choice([True, False], size=n),
            "weathersit": np.random.choice([1, 2, 3, 4], size=n).astype("uint8"),
            "temp": np.random.uniform(0.01, 0.99, size=n).astype("float16"),
            "atemp": np.random.uniform(0.01, 0.99, size=n).astype("float16"),
            "hum": np.random.uniform(0.01, 0.99, size=n).astype("float16"),
            "windspeed": np.random.uniform(0.01, 0.99, size=n).astype("float16"),
            "casual": np.random.randint(0, 100, size=n, dtype="uint32"),
            "registered": np.random.randint(0, 100, size=n, dtype="uint32"),
        },
        index=pd.Index(np.arange(n, dtype="uint32"), name="instant"),
    )

    targets = pd.DataFrame(
        {"cnt": (inputs["casual"] + inputs["registered"]).astype("uint32")},
        index=pd.Index(np.arange(n, dtype="uint32"), name="instant"),
    )

    InputsSchema.check(inputs)
    TargetsSchema.check(targets)

    inputs_train = inputs.iloc[:8000]
    targets_train = targets.iloc[:8000]
    inputs_test = inputs.iloc[8000:]
    targets_test = targets.iloc[8000:]

    inputs_train.to_parquet(os.path.join(output_dir, "inputs_train.parquet"))
    targets_train.to_parquet(os.path.join(output_dir, "targets_train.parquet"))
    inputs_test.to_parquet(os.path.join(output_dir, "inputs_test.parquet"))
    targets_test.to_parquet(os.path.join(output_dir, "targets_test.parquet"))

    print(f"Training and test data initialized successfully in {output_dir}")


def main() -> None:
    """CLI entry point for data initialization."""
    parser = argparse.ArgumentParser(description="Initialize dataset files for pipeline execution.")
    parser.add_argument("--output-dir", default="data", help="Directory where parquet files will be written.")
    args = parser.parse_args()
    generate_data(output_dir=args.output_dir)


if __name__ == "__main__":
    main()
