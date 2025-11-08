"""
A class to create a simple level for the player to move in
"""
from pygame import Surface

from Game.Entities.Player.Player import Player
from Game.Scenes.IScene import IScene


class Level(IScene):
    def __init__(self) -> None:
        self.load()

    def load(self) -> None:
        self.player = Player()

    def unload(self) -> None:
        pass

    def update(self, delta_time: float, event_list: list) -> None:
        self.player.update(delta_time, event_list)

    def draw(self, window: Surface) -> None:
        window.fill("purple")
        self.player.draw(window)
