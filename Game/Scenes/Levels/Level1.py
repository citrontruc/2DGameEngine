"""
A class to create a simple level for the player to move in
"""
from Game.Entities.Player.Player import Player
from Game.Scenes.IScene import IScene


class Level(IScene):
    def __init__(self) -> None:
        super().__init__()

    def load(self) -> None:
        self.player = Player()
