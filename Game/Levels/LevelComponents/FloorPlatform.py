"""
A class to create and render the basic floor components.
"""
from Game.Levels.ILevelComponent import ILevelComponent


class FloorPlatform(ILevelComponent):
    def __init__(self) -> None:
        super().__init__()

    def load(self, world):
        return super().load(world)

    def update(self, dt):
        return super().update(dt)

    def draw(self, surface):
        return super().draw(surface)
