# gmapq.core.args
import argparse
from gmapq.core.const import SearchMethod


def parse_argv() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    subparser = parser.add_subparsers(
        dest="search",
        required=True
    )

    def _parse_output(subparser: argparse.ArgumentParser):
        subparser.add_argument(
            "-o",
            "--output",
            required=True,
            choices=["json", "xml", "csv"],
            help="<string> Output format"
        )

    # text search
    text_parser = subparser.add_parser(SearchMethod.TEXT.value, help="Text search")
    text_parser.add_argument(
        "-q",
        "--query",
        required=True,
        help="<string> Text search query"
    )
    text_parser.add_argument(
        "-m",
        "--mask",
        required=False,
        default="*",
        help="<string> Protocol buffer field mask"
    )
    _parse_output(text_parser)

    # id search
    id_parser = subparser.add_parser(SearchMethod.ID.value, help="ID search")
    id_parser.add_argument(
        "-q",
        "--query",
        required=True,
        help="<string> Google place ID"
    )
    id_parser.add_argument(
        "-m",
        "--mask",
        required=False,
        default="*",
        help="<string> Protocol buffer field mask"
    )
    _parse_output(id_parser)

    # nearby search
    nearby_parser = subparser.add_parser(SearchMethod.NEARBY.value, help="Nearby search")
    nearby_parser.add_argument(
        "-q",
        "--query",
        required=True,
        help="<string> Comma separated strings https://developers.google.com/maps/documentation/places/web-service/place-types#table-a"
    )
    nearby_parser.add_argument(
        "-x",
        "--latitude",
        required=True,
        help="<float> WGS84 Latitude"
    )
    nearby_parser.add_argument(
        "-y",
        "--longitude",
        required=True,
        help="<float> WGS84 Longitude"
    )
    nearby_parser.add_argument(
        "-r",
        "--radius",
        required=True,
        help="<float> Radius in metres"
    )
    nearby_parser.add_argument(
        "-m",
        "--mask",
        required=False,
        default="*",
        help="<string> Protocol buffer field mask"
    )
    _parse_output(nearby_parser)

    return parser.parse_args()

