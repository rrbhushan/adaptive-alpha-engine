# TODO: Implement Kraken data module 

import pandas as pd 
import numpy as np
import requests


# Inputs you need:
# # symbol (BTCUSDT)
# # interval (1m)
# # start date/time
# # end date/time

# Outputs you return:
# A pandas DataFrame with exactly these columns:
# # timestamp (UTC datetime, aligned to minute)
# # open, high, low, close, volume (floats)

# REST endpoint + pagination behavior:
# Use Kraken endpoint (/0/public/OHLC)
# max limit per request = 1000
# you paginate by moving startTime forward:

# “Polite client” requirements:
# small sleep between calls (ex: 0.2s)
# handle HTTP errors with retries (at least 1–2 retries)
# stop conditions: empty response OR next_start >= end

def getKrakenAPIRequest(symbol: str, interval: int, start: int):
    url = "https://api.kraken.com/0/public/OHLC"

    params = {
        "pair": symbol,
        "interval": interval,
        "since": start,
    }

    response = requests.get(url, params=params)

    print("Status code:", response.status_code)

    if response.status_code != 200:
        print("Error response:", response.text)
        return None

    data = response.json()

    print("Errors:", data["error"])

    if data["error"] != []:
        print("Kraken API error:", data["error"])
        return None

    candles = data["result"][symbol]
    df = pd.DataFrame({
        'timestamp': [row[0] for row in candles],
        'open': [row[1] for row in candles],
        'high': [row[2] for row in candles],
        'low': [row[3] for row in candles],
        'close': [row[4] for row in candles],
        'vwap': [row[5] for row in candles],
        'volume': [row[6] for row in candles],
        'count': [row[7] for row in candles],
    })

    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    cols = ['open', 'high', 'low', 'close', 'vwap', 'volume']
    df[cols] = df[cols].astype(float)
    return df

