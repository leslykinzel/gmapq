# env
import os


def get_envvar(key: str) -> str:
    val = os.getenv(key)
    if val is None:
        raise Exception(f"Missing environment variable: {key}")
    return val

