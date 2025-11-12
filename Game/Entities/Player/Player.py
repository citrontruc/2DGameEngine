"""
A test player square that you can move around.
"""
import pygame

import Game.Utils.GameConstants as Constants
from Game.Entities.IControllable import IControllable
from Game.Entities.Player.PlayerInputTranslator import PlayerInputTranslator


class Player(IControllable):
    def __init__(self, initial_position: dict) -> None:
        self.player_input_translator = PlayerInputTranslator()

        # region Player Characteristics
        self.speed = 100
        self.position = [int(initial_position["x"]), int(initial_position["y"])]
        self.dimension_x = Constants.MEASUREMENT_UNIT * Constants.PIXEL_SIZE
        self.dimension_y = Constants.MEASUREMENT_UNIT * Constants.PIXEL_SIZE
        self.sprite = pygame.Rect(
            self.position[0],
            self.position[1],
            self.dimension_x,
            self.dimension_y
        )
        # endregion

        # region Status variables
        self.is_grounded = True
        # endregion

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

    def apply_gravity(self, delta_time: float):
        if not self.is_grounded:
            pass
            # Change speed rather than position.
            # self.position[1] += int(delta_time * Constants.GRAVITY_FORCE)

    def check_if_grounded(self):
        self.is_grounded = True

    def draw(self, window: pygame.Surface) -> None:
        self.sprite.x = self.position[0]
        self.sprite.y = self.position[1]
        pygame.draw.rect(window, (255, 0, 0), self.sprite)
