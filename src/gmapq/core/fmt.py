# gmapq.core.fmt
import sys
from typing import Any


def errorf(*msg: Any) -> None:
    print(" ".join(str(m) for m in msg), file=sys.stderr)
