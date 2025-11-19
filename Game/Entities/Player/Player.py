"""
A test player square that you can move around.
"""
import pygame

import Game.Utils.GameConstants as Constants
import Game.Utils.MathSupplement as MathSupplement
from Game.Camera.Camera import Camera
from Game.Entities.IControllable import IControllable
from Game.Entities.Player.PlayerInputTranslator import PlayerInputTranslator


class Player(IControllable):
    def __init__(self, initial_position: dict) -> None:
        self.player_input_translator = PlayerInputTranslator()

        # region Player Characteristics
        self.speed = 100
        self.velocity = [0., 0.]  # In our case velocity is a float to suport small increments
        self.max_velocity = [10, 10]
        self.grift = 10
        self.position = [int(initial_position["x"]), int(initial_position["y"])]
        self.dimension_x = Constants.scale(1)
        self.dimension_y = Constants.scale(1)
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

    # region Getters & Setters
    def get_position(self) -> list:
        return self.position
    # endregion

    def update(self, delta_time: float, event_list: list) -> None:
        input_dict = self.player_input_translator.retrieve_input(event_list)
        action_dict = self.player_input_translator.translate_input(input_dict)
        self.handle_input(delta_time, action_dict)
        self.move_player()

    def handle_input(self, delta_time: float, action_dict: dict) -> None:
        self.velocity[0] += action_dict["MOVE"][0] * self.speed * delta_time
        self.velocity[1] += action_dict["MOVE"][1] * self.speed * delta_time
        self.velocity[0] = MathSupplement.sign(self.velocity[0]) * min(abs(self.velocity[0]), self.max_velocity[0])
        self.velocity[1] = MathSupplement.sign(self.velocity[1]) * min(abs(self.velocity[1]), self.max_velocity[1])
        self.velocity[0] -= MathSupplement.sign(self.velocity[0]) * self.grift * delta_time
        self.velocity[1] -= MathSupplement.sign(self.velocity[1]) * self.grift * delta_time
        if action_dict["JUMP"]:
            print("jump")
        if action_dict["ACTION"]:
            print("ACTION")

    def move_player(self):
        self.position[0] += int(self.velocity[0])
        self.position[1] += int(self.velocity[1])

    def apply_gravity(self, delta_time: float):
        if not self.is_grounded:
            pass
            # Change speed rather than position.
            # self.position[1] += int(delta_time * Constants.GRAVITY_FORCE)

    def check_if_grounded(self):
        self.is_grounded = True

    def draw(self, surface: pygame.Surface) -> None:
        self.sprite.x = self.position[0]
        self.sprite.y = self.position[1]
        pygame.draw.rect(surface, (255, 0, 0), self.sprite)
