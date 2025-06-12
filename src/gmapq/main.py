# gmapq
import os
import sys
import json
from gmapq.core.env import get_envvar
from gmapq.core.fmt import errorf
from gmapq.core.args import parse_argv
from gmapq.core.google import GooglePlacesClient


def main():
    try:
        api_key = get_envvar("GOOGLE_PLACES_API_KEY")
    except Exception as e:
        errorf(e)
        return os.EX_CONFIG

    argv = parse_argv()
    # print(argv)
    # print(argv.search)
    # print(argv.query)
    # print(argv.output)
    google = GooglePlacesClient(api_key)

    match argv.search:
        case "text":
            # mask = "places.displayName,places.formattedAddress"
            r = google.text_search(argv.query)
        case _:
            # should be unreachable
            errorf(f"{argv.search} is not available.")
            return os.EX_UNAVAILABLE

    print(json.dumps(r))

    return 0


if __name__ == "__main__":
    sys.exit(main())
