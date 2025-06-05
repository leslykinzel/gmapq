# fmt
import sys
from .const import ANSI


def errorf(msg: str) -> str:
    print(f"{ANSI.red}{msg}{ANSI.reset}", file=sys.stderr)

