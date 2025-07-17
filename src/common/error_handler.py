from typing import Dict

from src.common.exceptions import PokedexBaseError


class ErrorHandler:
    def handle_error(self, error: Exception) -> Dict:
        if not isinstance(error, PokedexBaseError):
            return {
                "name": "unknown error",
                "status_code": 1,
                "details": f"an unknown error was raised:\n{str(error)}",
            }

        return {
            "name": error.name,
            "status_code": error.status_code,
            "details": error.msg,
        }
