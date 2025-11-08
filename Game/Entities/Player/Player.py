"""
A test player square that you can move around.
"""
import pygame

from Game.Entities.IControllable import IControllable
from Game.Entities.Player.PlayerInputTranslator import PlayerInputTranslator


class Player(IControllable):
    def __init__(self) -> None:
        self.player_input_translator = PlayerInputTranslator()
        self.speed = 20
        self.position = [100, 100]
        self.dimension_x = 10
        self.dimension_y = 10
        self.sprite = pygame.Rect(
            self.position[0],
            self.position[1],
            self.dimension_x,
            self.dimension_y
        )

    def update(self, delta_time: float, event_list: list) -> None:
        input_dict = self.player_input_translator.retrieve_input(event_list)
        action_dict = self.player_input_translator.translate_input(input_dict)
        self.handle_input(delta_time, action_dict)

    def handle_input(self, delta_time: float, action_dict: dict) -> None:
        self.position[0] += action_dict["MOVE"][0] * self.speed * delta_time
        self.position[1] += action_dict["MOVE"][1] * self.speed * delta_time
        if action_dict["JUMP"]:
            print("jump")
        if action_dict["ACTION"]:
            print("ACTION")

    def draw(self, window: pygame.Surface) -> None:
        self.sprite.x = self.position[0]
        self.sprite.y = self.position[1]
        pygame.draw.rect(window, (255, 0, 0), self.sprite)
