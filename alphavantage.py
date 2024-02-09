import requests

class AlphaVantage:
    def __init__(self, apikey: str = "demo"):
        self.__apikey = apikey

    def getHistoryCompact(self, ticker: str = "IBM", interval: str = "5min") -> tuple:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY'
        params = {
            'symbol': ticker,
            'interval': interval,
            'apikey': self.__apikey
        }
        response = requests.get(url, params=params)
        data = response.json()
        timeSeries = data[f'Time Series ({interval})']
        time = list(timeSeries.keys())
        return time, timeSeries


    def getHistoryFull(self, ticker: str = "IBM", interval: str = "5min") -> tuple:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY'
        params = {
            'symbol': ticker,
            'interval': interval,
            'outputsize': 'full',
            'apikey': self.__apikey
        }
        response = requests.get(url, params=params)
        data = response.json()
        timeSeries = data[f'Time Series ({interval})']
        time = list(timeSeries.keys())
        return time, timeSeries

    def getOpenPrices(self, data: dict) -> list:
        return [float(data[time]['1. open']) for time in data]

    def getHighPrices(self, data: dict) -> list:
        return [float(data[time]['2. high']) for time in data]

    def getLowPrices(self, data: dict) -> list:
        return [float(data[time]['3. low']) for time in data]

    def getClosePrices(self, data: dict) -> list:
        return [float(data[time]['4. close']) for time in data]
