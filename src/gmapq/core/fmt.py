# gmapq.core.fmt
import sys


def errorf(*msg: str) -> str:
    print(" ".join(str(m) for m in msg), file=sys.stderr)

