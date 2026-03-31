## TODO: Add caching

# function to generate cache filename deterministically from:
# # symbol, interval, start, end
# # load-if-exists
# # save
# Use Parquet if possible (faster), CSV is fine too.

from pathlib import Path
import pandas as pd


def get_cache_path(cache_dir, symbol, interval, start, end):
    filename = f"{symbol}_{interval}_{start}_{end}.parquet"
    return Path(cache_dir) / filename


def load_cache(path):
    if path.exists():
        print(f"Loading from cache: {path}")
        return pd.read_parquet(path)
    return None


def save_cache(df, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path, index=False)
    print(f"Saved to cache: {path}")