# gmapq.core.google
from .const import GoogleAPIEndpoints
import requests


class GooglePlacesClient:

    def __init__(self, api_key: str):
        self.api_key = api_key

    def text_search(self, query: str, mask: str = "*"):
        """ Generic text search

            query -- Text query for Google Maps
            mask -- Response field mask
        """
        headers = {
            "Content-Type":     "application/json",
            "X-Goog-Api-Key":   self.api_key,
            "X-Goog-FieldMask": mask
        }
        payload = {
            "textQuery": query
        }
        response = requests.post(
            GoogleAPIEndpoints.PLACES_SEARCH_TEXT_URL,
            headers = headers,
            json = payload
        )
        response.raise_for_status()
        return response.json()

    def nearby_search(self, lat: float, lon: float, rad: float):
        """ Nearby coordinate search

            lat -- WGS84 Latitude
            lon -- WGS84 Longitude
            rad -- Radius in metres
        """
        pass

    def id_search(self, id: str, mask: str = "*"):
        """ Id search

            id -- Unique place identifier
            mask -- Response field mask
        """
        headers = {
            "Content-Type":     "application/json",
            "X-Goog-Api-Key":   self.api_key,
            "X-Goog-FieldMask": mask
        }
        response = requests.get(
            f"{GoogleAPIEndpoints.PLACES_BASE_URL}/{id}",
            headers = headers
        )
        response.raise_for_status()
        return response.json()

