"""
Additional functions to take care of maths operations.
"""
import math


def sign(x: float | int) -> int:
    return int(x / abs(x)) if x != 0 else 0


def normalize(movement: list) -> list:
    length = math.hypot(movement[0], movement[1])
    if length != 0:
        movement[0] /= length
        movement[1] /= length
    return movement
