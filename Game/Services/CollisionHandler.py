"""
A class to handle collisions, check which elements are grounded and how to handle collisions.
"""
from Game.Services.Singleton import SingletonMeta


class CollisionHandler(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.list_entities = []

    def check_collisions_between_entities(self):
        pass

    def check_if_grounded(self):
        pass
