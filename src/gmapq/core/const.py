# gmapq.core.const
from enum import Enum


class SearchMethod(Enum):
    TEXT   = "text"
    ID     = "id"
    NEARBY = "nearby"


class OutputFormat(Enum):
    JSON = "json"
    XML  = "xml"
    CSV  = "csv"


class NearbySearchPreference(Enum):
    DISTANCE   = "DISTANCE"
    POPULARITY = "POPULARITY"


class GoogleAPIEndpoints:
    PLACES_BASE_URL          = "https://places.googleapis.com/v1/places"
    PLACES_SEARCH_TEXT_URL   = f"{PLACES_BASE_URL}:searchText"
    PLACES_SEARCH_NEARBY_URL = f"{PLACES_BASE_URL}:searchNearby"
