"""
A class to create and render the basic floor components.
"""
import pygame

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
        self.sprite = None

    def initialize_surface(self):
        """
        We draw once our surface and we then reuse the same surface every time.
        TODO: have the method work with real sprites.
        """
        floor_surface = pygame.Surface((Constants.scale(self.width),
                                       Constants.scale(self.height)))
        for x in range(self.width):
            for y in range(self.height):
                # Add tile image here to list
                pygame.draw.rect(floor_surface, (100, 100, 255), (Constants.scale(x),
                                                                  Constants.scale(y),
                                                                  Constants.scale(self.width),
                                                                  Constants.scale(self.height)))
                # floor_surface.blit(tile[tile_idx], (x * Constants.MEASUREMENT_UNIT * Constants.PIXEL_SIZE, y * Constants.MEASUREMENT_UNIT * Constants.PIXEL_SIZE))
        return floor_surface

    def provides_support(self) -> bool:
        return self.support

    def load(self):
        # TODO
        self.sprite = self.initialize_surface()

    def update(self, delta_time: float):
        """
        Floor platforms don't get any updates.
        """
        pass

    def draw(self, surface):
        """
        When we load the level, we draw our surface with our floor.
        We then blit the surface without redrawing it every frame.
        TODO: check if the surface is on screen or not.
        """
        surface.blit(self.sprite, (self.x, self.y))
