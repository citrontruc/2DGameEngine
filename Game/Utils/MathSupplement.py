"""
Additional functions to take care of maths operations.
"""


def sign(x: float | int) -> int:
    return int(x / abs(x)) if x != 0 else 0
