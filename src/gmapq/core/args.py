# gmapq.core.args
import argparse


def parse_argv() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    subparser = parser.add_subparsers(
        dest="search",
        required=True
    )

    def _parse_output(subparser: argparse.Namespace):
        subparser.add_argument(
            "-o",
            "--output",
            required=True,
            help="<path> Output file path"
        )

    # text search
    text_parser = subparser.add_parser("text", help="Text search")
    text_parser.add_argument(
        "-q",
        "--query",
        required=True,
        help="<string> Text search query"
    )
    _parse_output(text_parser)

    # id search
    id_parser = subparser.add_parser("id", help="ID search")
    id_parser.add_argument(
        "-q",
        "--query",
        required=True,
        help="<string> Google place ID"
    )
    _parse_output(id_parser)

    # nearby search
    nearby_parser = subparser.add_parser("nearby", help="Nearby search")
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
    _parse_output(nearby_parser)

    return parser.parse_args()

