"""
A script to store all game constants in the game
"""

GRAVITY_FORCE = 9.81
MEASUREMENT_UNIT = 16
PIXEL_SIZE = 1

X_RESOLUION = 1280
Y_RESOLUTION = 720


def scale(x):
    return x * MEASUREMENT_UNIT * PIXEL_SIZE
