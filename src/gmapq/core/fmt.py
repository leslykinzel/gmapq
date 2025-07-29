# gmapq.core.fmt
import sys
import json
from enum import Enum
from typing import Any
from gmapq.dict2xml import dict2xml


class OutputFormat(Enum):
    JSON = "json"
    XML  = "xml"
    CSV  = "csv"


def errorf(*msg: Any) -> None:
    print(" ".join(str(m) for m in msg), file=sys.stderr)


class Represent:

    def __init__(self, data: dict):
        self.__data = data

    def as_json(self) -> str:
        return json.dumps(
            self.__data,
            sort_keys=True,
            indent=4,
            separators=(",", ": ")
        )

    def as_xml(self) -> str:
        return dict2xml(
            self.__data,
            wrap="all",
            indent="\t"
        )

    def as_csv(self) -> str:
        raise NotImplementedError
