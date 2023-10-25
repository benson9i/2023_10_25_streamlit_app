# Import the packages
import requests
import pandas as pd
from io import StringIO
import time


# I want to get the following tickers:
# Indices
# DXY
# GSPC
# NDX
# OVX
# RUI
# VIX
# XOI

# Forex
# USD/AUD
# USD/CAD
# USD/CHF
# USD/EUR
# USD/GBP
# USD/JPY
# USD/MNT
# USD/RUB
# USD/CNY
# USD/INR
# USD/SGD
# USD/VND

# Crypto
# BTC/USD
# ETH/USD
# BNB/USD
# XRP/USD
# SOL/USD
# ADA/USD


# Get data from the API

def fetch_market_data(start_date, end_date):
    # Reading the API key from api_key.txt
    with open("api_key.txt", "r") as file:
        api_key = file.readline().strip()

    base_url = "https://api.twelvedata.com/time_series"

    market_types = {
        "index": {
            "symbols": ["DXY", "GSPC", "NDX", "OVX", "RUI", "VIX", "XOI"],
            "additional_params": {"type": "index", "country": "United States"}
        },
        "forex": {
            "symbols": ["USD/AUD", "USD/CAD", "USD/CHF", "USD/EUR", "USD/GBP", "USD/JPY",
                        "USD/MNT", "USD/RUB", "USD/CNY", "USD/INR", "USD/SGD", "USD/VND"],
            "additional_params": {}
        },
        "crypto": {
            "symbols": ["BTC/USD", "ETH/USD", "BNB/USD", "XRP/USD", "SOL/USD", "ADA/USD"],
            "additional_params": {"exchange": "Binance"}
        }
    }

    all_data = []

    for market, details in market_types.items():
        for symbol in details["symbols"]:
            params = {
                "apikey": api_key,
                "interval": "1day",
                "symbol": symbol,
                "start_date": start_date,
                "end_date": end_date,
                "format": "CSV"
            }
            params.update(details["additional_params"])

            response = requests.get(base_url, params=params)

            if response.status_code != 200:
                print(
                    f"Failed to fetch data for {symbol}. Status code: {response.status_code}")
                continue

            df = pd.read_csv(StringIO(response.text), sep=';')

            if 'datetime' not in df.columns or 'close' not in df.columns:
                print(
                    f"Unexpected data structure for symbol {symbol}. Data:\n{response.text}")
                continue

            df = df[['datetime', 'close']]
            df.rename(columns={"datetime": "date",
                      "close": "closing_price"}, inplace=True)
            df['symbol'] = symbol
            df['type'] = market

            all_data.append(df)

            # Introducing a delay to respect the API's rate limit
            time.sleep(8)  # A delay of 8 seconds

    result_df = pd.concat(all_data, ignore_index=True)

    return result_df


# Example usage:
start_date = "2000-01-01 00:00:00"
end_date = "2023-10-15 00:00:00"
data = fetch_market_data(start_date, end_date)
print(data)

data.to_csv("data_for_app.csv", index=False)


test = pd.read_csv("data_for_app.csv")

# see column types
print(test.dtypes)
