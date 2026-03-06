import argparse
import yaml
from pathlib import Path

def load_config(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def main(config_path):
    config = load_config(config_path)
    print("Loaded config:")
    print(config)

    # TODO:
    # 1. Load data
    # 2. Build features
    # 3. Create labels
    # 4. Create walk-forward splits
    # 5. Train model
    # 6. Backtest
    # 7. Save metrics

    print("Pipeline skeleton ready.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, required=True)
    args = parser.parse_args()

    main(args.config)
