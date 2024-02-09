import requests

class OpenWeatherMap:

    def __init__(self, apikey: str):
        self.__apikey = apikey
        self.__API_ENDPOINT = 'https://api.openweathermap.org/data/2.5'

    def getCurrentWeather(self, lat: float, lon: float) -> dict:
        ENDP = f'{self.__API_ENDPOINT}/weather'
        
        params = {
            'lat': lat,
            'lon': lon,
            'appid': self.__apikey,
            'units': 'metric',
            'lang': 'it'
        }

        response = requests.get(ENDP, params=params)
        
        if response.status_code == 200:
            return response.json()

        raise Exception('Errore nell\'API OWM')

    def getFutureWeather(self, lat: float, lon: float) -> dict:

        ENDP = f'{self.__API_ENDPOINT}/weather'
        
        params = {
            'lat': lat,
            'lon': lon,
            'appid': self.__apikey,
            'units': 'metric',
            'lang': 'it'
        }

        response = requests.get(ENDP, params=params)
        
        if response.status_code == 200:
            return response.json()

        raise Exception('Errore nell\'API OWM')

    def getWeatherInDay(self, weather: dict, day: int) -> dict:
        return weather['list'][day*8]
