# config.py
from typing import Any

Config: dict[str, Any] = {}


def init():
    global Config
    Config = {
        "PROGRAM_NAME": "pyadba",
        "PROGRAM_VERSION": "0.1.0",
        "TZ": "US/Central",
        "DEBUG": False,
    }

