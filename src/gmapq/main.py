# gmapq
import os
import sys
import json
from argparse import Namespace
from gmapq.core.env import get_envvar
from gmapq.core.fmt import errorf
from gmapq.core.args import parse_argv
from gmapq.core.const import SearchMethod
from gmapq.core.google import GooglePlacesClient
from requests import HTTPError


def main():
    try:
        api_key = get_envvar("GOOGLE_PLACES_API_KEY")
    except Exception as e:
        errorf(e)
        return os.EX_CONFIG

    argv = parse_argv()
    google = GooglePlacesClient(api_key)

    try:
        resp = handle_maps_query(argv, google)
    except NotImplementedError:
        errorf("Method is not implemented.")
        return os.EX_UNAVAILABLE
    except HTTPError as e:
        errorf(e)
        return os.EX_PROTOCOL
    except Exception as e:
        errorf(e)
        return os.EX_SOFTWARE

    # TODO: implement output formats
    print(json.dumps(resp, sort_keys=True, indent=4, separators=(",", ": ")))
    return os.EX_OK


def handle_maps_query(argv: Namespace, client: GooglePlacesClient) -> str:
    match argv.search:
        case SearchMethod.TEXT.value:
            resp = client.search_text(
                argv.query,
                argv.mask
            )
        case SearchMethod.ID.value:
            resp = client.search_id(
                argv.query,
                argv.mask
            )
        case SearchMethod.NEARBY.value:
            resp = client.search_nearby_basic(
                argv.query,
                argv.latitude,
                argv.longitude,
                argv.radius,
                argv.mask
            )
        case _:
            # argparse should make this unreachable
            raise NotImplementedError
    return resp


if __name__ == "__main__":
    sys.exit(main())
