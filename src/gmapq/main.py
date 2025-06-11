# gmapq
import os
import sys
from gmapq.core.env import get_envvar
from gmapq.core.args import parse_argv
from gmapq.core.fmt import errorf


def main():
    try:
        api_key = get_envvar("GOOGLE_PLACES_API_KEY")
    except Exception as e:
        errorf(e)
        return os.EX_CONFIG

    argv = parse_argv()

    print(api_key)
    print(argv)

    return 0


if __name__ == "__main__":
    sys.exit(main())
