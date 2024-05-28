# utilities_log.py

import sys
from datetime import datetime
import pytz
from typing import Type

import config

TZ: str
TIMEZONE: Type[pytz.timezone]
DEFAULT_DEBUG = False

# RD="\033[31m"
# GN="\033[32m"
# YL="\033[33m"
# BL="\033[34m"
# MG="\033[35m"
# CY="\033[36m"
# NC="\033[0m"
ERR = "\033[31m"
WRN = "\033[33m"
SCS = "\033[32m"
DBG = "\033[35m"
DRY = "\033[36m"
NC = "\033[0m"


def init():
    global config
    global TZ
    global TIMEZONE
    global DEFAULT_DEBUG
    TZ = config.Config['TZ'] if config.Config['TZ'] is not None else "US/Central"
    TIMEZONE = pytz.timezone(TZ)
    DEFAULT_DEBUG = config.Config['DEBUG'] if config.Config['DEBUG'] is not None else False


def timestamp() -> str:
    now = datetime.now(TIMEZONE).replace(microsecond=0)
    return now.isoformat()


def logMsg(*args, **kwargs):
    ts = timestamp()
    print(f"[{ts}]", " ".join(map(str, args)), **kwargs)


def logDbg(*args, **kwargs):
    global config
    output_debug = config.Config['DEBUG'] if config.Config['DEBUG'] is not None else DEFAULT_DEBUG
    if output_debug:
        ts = timestamp()
        print(DBG, file=sys.stderr, end="")
        print(f"[{ts}] [DEBUG]", " ".join(map(str, args)), **kwargs, file=sys.stderr, end="")
        print(NC, file=sys.stderr)


def logErr(*args, **kwargs):
    ts = timestamp()
    print(ERR, file=sys.stderr, end="")
    print(f"[{ts}] [ERROR]", " ".join(map(str, args)), **kwargs, file=sys.stderr, end="")
    print(NC, file=sys.stderr)


def logWarn(*args, **kwargs):
    ts = timestamp()
    print(WRN, file=sys.stderr, end="")
    print(f"[{ts}] [WARNING]", " ".join(map(str, args)), **kwargs, file=sys.stderr, end="")
    print(NC, file=sys.stderr)


def logDryRun(*args, **kwargs):
    print(DRY, file=sys.stderr, end="")
    print(f"[ DRY RUN ] ", " ".join(map(str, args)), **kwargs, file=sys.stderr, end="")
    print(NC, file=sys.stderr)


def logStdErr(*args, **kwargs):
    print(" ".join(map(str, args)), **kwargs, file=sys.stderr)
