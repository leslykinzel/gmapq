# gmapq.core.google
from enum import Enum
import requests


class SearchMethod(Enum):
    TEXT   = "text"
    ID     = "id"
    NEARBY = "nearby"


class NearbySearchPreference(Enum):
    DISTANCE   = "DISTANCE"
    POPULARITY = "POPULARITY"


class GoogleAPIEndpoints:
    PLACES_BASE_URL          = "https://places.googleapis.com/v1/places"
    PLACES_SEARCH_TEXT_URL   = f"{PLACES_BASE_URL}:searchText"
    PLACES_SEARCH_NEARBY_URL = f"{PLACES_BASE_URL}:searchNearby"


class GooglePlacesClient:

    def __init__(self, api_key: str):
        self.api_key = api_key

    def search_text(self, query: str, mask: str = "*"):
        """ Generic text search

        Args:
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
            headers=headers,
            json=payload
        )
        response.raise_for_status()
        return response.json()

    def search_nearby_basic(self, query: str, lat: float, lon: float, rad: float, mask: str = "*"):
        """ Basic nearby radius search.

        Args:
            query -- Comma-separated "place-types": https://developers.google.com/maps/documentation/places/web-service/place-types#table-a
            lat -- WGS84 Latitude
            lon -- WGS84 Longitude
            rad -- Radius in metres
        """
        headers = {
            "Content-Type":     "application/json",
            "X-Goog-Api-Key":   self.api_key,
            "X-Goog-FieldMask": mask
        }
        payload = {
            "includedPrimaryTypes": [type for type in query.split(",")],
            "rankPreference": NearbySearchPreference.DISTANCE.value,
            "locationRestriction": {
                "circle": {
                    "center": {
                        "latitude":  lat,
                        "longitude": lon
                    },
                    "radius": rad
                }
            }
        }
        response = requests.post(
            GoogleAPIEndpoints.PLACES_SEARCH_NEARBY_URL,
            headers=headers,
            json=payload
        )
        response.raise_for_status()
        return response.json()

    def search_id(self, id: str, mask: str = "*"):
        """ Id search

        Args:
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
            headers=headers
        )
        response.raise_for_status()
        return response.json()

