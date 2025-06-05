# gmapq

# std
import os
import sys


def main():
    return 0


def getenv(key: str) -> str|None:
    return os.getenv(key) or (print(
        f"Missing environment variable: {key}"
    ), sys.exit(1))[0]


if __name__ == "__main__":
    sys.exit(main())

