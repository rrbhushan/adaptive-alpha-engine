import argparse
import yaml

from datetime import datetime, timezone

from src.data.kraken import getKrakenAPIRequest
from src.data.cache import get_cache_path, load_cache, save_cache


def load_config(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)


def to_seconds(date_str):
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    dt = dt.replace(tzinfo=timezone.utc)
    return int(dt.timestamp())


def main(config_path):
    config = load_config(config_path)
    print("Loaded config:")

    symbol = config["data"]["symbol"]
    interval = config["data"]["interval"]
    start_str = config["data"]["start"]
    end_str = config["data"]["end"]
    cache_dir = config["data"]["cache_dir"]

    start = to_seconds(start_str)

    print("Symbol:", symbol)
    print("Interval:", interval)
    print("Start:", start)
    print("cache_dir:", cache_dir)

    cache_path = get_cache_path(
        cache_dir=cache_dir,
        symbol=symbol,
        interval=interval,
        start=start_str,
        end=end_str,
    )

    df = load_cache(cache_path)

    if df is None:
        print("Fetching data from Kraken...")
        df = getKrakenAPIRequest(symbol, interval, start)
        save_cache(df, cache_path)
    else:
        print("Using cached data.")

    print(df.head())
    print("Pipeline skeleton ready.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, required=True)
    args = parser.parse_args()

    main(args.config)