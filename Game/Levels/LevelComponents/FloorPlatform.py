"""
A class to create and render the basic floor components.
"""
import Game.Utils.GameConstants as Constants
from Game.Levels.ILevelComponent import ILevelComponent


class FloorPlatform(ILevelComponent):
    def __init__(self, component_characteristics: dict) -> None:
        self.type = component_characteristics["type"]
        self.x = component_characteristics["x"]
        self.y = component_characteristics["y"]
        self.width = component_characteristics["width"]
        self.height = component_characteristics["height"]
        self.support = True
        self.check_dimensions()

    def check_dimensions(self):
        if self.width // Constants.MEASUREMENT_UNIT != 0:
            raise ValueError("Invalid dimensions for a component: width is invalid.")
        if self.height // Constants.MEASUREMENT_UNIT != 0:
            raise ValueError("Invalid dimensions for a component: height is invalid.")

    def provides_support(self) -> bool:
        return self.support

    def load(self):
        # TODO
        return super().load()

    def update(self, delta_time: float):
        """
        Floor platforms don't get any updates.
        """
        pass

    def draw(self, surface):
        return super().draw(surface)
