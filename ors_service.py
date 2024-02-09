import requests

class ors_service:
    def __init__(self, token):
            self.directions_url = 'https://api.openrouteservice.org/v2/directions/driving-car'
            self.headers = {
                'Accept': 'application/json; charset=utf-8',
                'Authorization': f'{token}',
                'Content-Type': 'application/json; charset=utf-8'
            }       

    #distanza tra due punti
    def getDirections(self, start = {'longitude': float, 'latitude': float}, end = {'longitude': float, 'latitude': float}) -> dict:

        body = {
            'coordinates': [
                [start['longitude'], start['latitude']],
                [end['longitude'], end['latitude']]
            ],
        }

        response = requests.post(self.directions_url, json=body, headers=self.headers)
        if response.status_code == 200:
            return response.json()

        raise Exception('Errore nell\'API ORS')

    #distanza tra più punti
    #l'ordine deve essre logitudine, latitudine
    def getDistance(self, coordinates: list) -> dict:

        body = {
            "coordinates": coordinates,
            "geometry": False,
        }
        
        response = requests.post(url = self.directions_url, json = body, headers = self.headers)
        
        if response.status_code == 200:
            return response.json()
        
        raise Exception('Errore nell\'API ORS')

    #dato un json di risposta, ritorna in una lista le lunghezze dei segmenti
    def getLengthsOfSegments (self, json_response: dict) -> list:
        lengths = []

        for segment in json_response['routes'][0]['segments']:
            lengths.append(segment['distance'])

        return lengths

    #dato un json di risposta, ti ritorna la lunghezza totale del percorso
    def extractDistance(self, jsondata):
        return jsondata['routes'][0]['summary']['distance']
