# gmapq
import os
import sys
import json
import argparse
from gmapq.core.env import get_envvar
from gmapq.core.fmt import errorf
from gmapq.core.args import parse_argv
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


def handle_maps_query(argv: argparse.Namespace, client: GooglePlacesClient) -> str:
    match argv.search:
        case "text":
            resp = client.text_search(argv.query, argv.mask)
        case "nearby":
            raise NotImplementedError
        case "id":
            raise NotImplementedError
        case _:
            # argparse should make this unreachable
            raise NotImplementedError

    return resp


if __name__ == "__main__":
    sys.exit(main())

