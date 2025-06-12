# gmapq.core.const


class GoogleAPIEndpoints:
    PLACES_BASE_URL = "https://places.googleapis.com/v1/places"
    PLACES_SEARCH_TEXT_URL = f"{PLACES_BASE_URL}:searchText"
    PLACES_SEARCH_NEARBY_URL = f"{PLACES_BASE_URL}:searchNearby"


class ANSI:
    reset = "\033[0m"
    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    white = "\033[37m"

