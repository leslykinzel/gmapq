# gmapq
import os
import sys
from argparse import Namespace
from gmapq.core.env import Env
from gmapq.core.fmt import errorf, OutputFormat, Represent
from gmapq.core.args import parse_argv
from gmapq.core.google import GooglePlacesClient, SearchMethod
from requests import HTTPError


def main():
    try:
        api_key = Env.load("GOOGLE_PLACES_API_KEY")
    except Exception as e:
        errorf(e)
        return os.EX_CONFIG

    argv = parse_argv()
    google = GooglePlacesClient(api_key)

    try:
        response = handle_maps_query(argv, google)
        handle_maps_output(argv, response)
    except NotImplementedError:
        errorf("Method is not implemented.")
        return os.EX_UNAVAILABLE
    except HTTPError as e:
        errorf(e)
        return os.EX_PROTOCOL
    except Exception as e:
        errorf(e)
        return os.EX_SOFTWARE

    return os.EX_OK


def handle_maps_query(argv: Namespace, client: GooglePlacesClient) -> dict:
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


def handle_maps_output(argv: Namespace, data: dict) -> None:
    __repr = Represent(data)
    match argv.output:
        case OutputFormat.JSON.value:
            print(__repr.as_json(), file=sys.stdout)
        case OutputFormat.XML.value:
            print(__repr.as_xml(), file=sys.stdout)
        case OutputFormat.CSV.value:
            print(__repr.as_csv(), file=sys.stdout)
        case _:
            print(data)


if __name__ == "__main__":
    sys.exit(main())
