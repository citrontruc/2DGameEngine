"""
A Component to generate level components from a level Json description.
"""
from Game.Levels.LevelComponents.FloorPlatform import FloorPlatform
from Game.Scenes.Levels.Level import Level
from Game.Services.Singleton import SingletonMeta


class LevelComponentsFactory(metaclass=SingletonMeta):
    def __init__(self) -> None:
        pass

    def create_level(self, level_description: dict) -> Level:
        return Level(level_description)

    def create_floor_platform(self, component_description: dict) -> FloorPlatform:
        return FloorPlatform(component_description)
