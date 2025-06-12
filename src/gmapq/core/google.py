# gmapq.core.google
from .const import GoogleAPIEndpoints
import requests


class GooglePlacesClient:

    def __init__(self, api_key: str):
        self.api_key = api_key

    def text_search(self, query: str, field_mask: str = "*"):
        headers = {
            "Content-Type":     "application/json",
            "X-Goog-Api-Key":   self.api_key,
            "X-Goog-FieldMask": field_mask
        }
        payload = {
            "textQuery": query
        }
        try:
            response = requests.post(
                GoogleAPIEndpoints.PLACES_SEARCH_TEXT_URL,
                headers=headers,
                json=payload
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return e
