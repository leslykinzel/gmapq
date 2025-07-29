# gmapq.core.env
import os


class Env:

    @staticmethod
    def load(key: str) -> str:
        try:
            return os.environ[key]
        except KeyError:
            raise EnvironmentError(f"Missing required environment variable: {key}")
