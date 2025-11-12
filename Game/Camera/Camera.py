"""
A camera that focuses where the action is.
"""
from Game.Services.Singleton import SingletonMeta


class Camera(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.max_x = 0
        self.max_y = 0
