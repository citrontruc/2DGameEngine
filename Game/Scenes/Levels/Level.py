"""
A class to create a simple level for the player to move in
"""
from pygame import Surface

from Game.Entities.Player.Player import Player
from Game.Scenes.IScene import IScene


class Level(IScene):
    def __init__(self, level_information: dict) -> None:
        self.level_id: str = level_information["level_id"]
        self.name: str = level_information["name"]
        self.background: dict = level_information["background"]
        self.player_start: dict = level_information["player_start"]
        self.tileset: dict = level_information["tileset"]
        self.platforms: list = level_information["platforms"]
        self.enemies: list = level_information["enemies"]
        self.collectibles: list = level_information["collectibles"]
        self.goal: list = level_information["goal"]
        self.player = self.create_player()
        self.list_components = []

    def create_player(self) -> Player:
        return Player(self.player_start)

    def load(self) -> None:
        """
        Loads textures and sounds for the level.
        Creates the elements of the level.
        """

    def unload(self) -> None:
        pass

    def update(self, delta_time: float, event_list: list) -> None:
        if self.player:
            self.player.update(delta_time, event_list)

    def draw(self, window: Surface) -> None:
        window.fill("purple")
        if self.player:
            self.player.draw(window)
