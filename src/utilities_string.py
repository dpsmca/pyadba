# utilities_string.py


def string_good(val: str) -> bool:
    return val is not None and val != ""


def string_bad(val: str) -> bool:
    return not string_good(val)


def strings_good(vals: list) -> bool:
    return all(string_good(val) for val in vals)