import pandas as pd
import requests
from pprint import pprint


# api key = FR61ESIVDJD2UGI8


def getIntradayData(nemo, interval):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + \
        nemo + '&interval=' + interval + '&apikey=FR61ESIVDJD2UGI8'
    r = requests.get(url)
    dataIntraday = r.json()
    return dataIntraday['Time Series (5min)']


def getDailyDataFrameData(nemo, interval):
    return convertToDf(getIntradayData(nemo, interval))


def convertToDf(data):
    """Convert the result JSON in pandas dataframe"""
    df = pd.DataFrame.from_dict(data, orient='index')

    df = df.reset_index()

    # Rename columns

    df = df.rename(index=str, columns={"index": "date", "1. open": "open",
                                       "2. high": "high", "3. low": "low", "4. close": "close"})

    # Change to datetime

    df['date'] = pd.to_datetime(df['date'])

    # Sort data according to date

    df = df.sort_values(by=['date'])

    # Change the datatype

    df.open = df.open.astype(float)
    df.close = df.close.astype(float)
    df.high = df.high.astype(float)
    df.low = df.low.astype(float)

    # Checks
    df.head()
    df.info()

    return df
