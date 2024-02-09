import requests

def searchCity (cityName: str, limit: int = 1) -> list:
    END_POINT = "https://nominatim.openstreetmap.org/search"
    
    params = {
        "q": cityName,
        "format": "json",
        "addressdetails": 1,
        "limit": limit
    }
    
    response = requests.get(END_POINT, params=params)
    
    if response.status_code == 200:
        #dovrebbe tornare una lista, in caso di errori controlla
        return response.json()

    print(response.status_code)
    print(response.text)

    raise Exception('Errore nell\'API OSM')
