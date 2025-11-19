"""
A camera that focuses where the action is.
"""
import Game.Utils.GameConstants as Constants
from Game.Entities.IControllable import IControllable
from Game.Services.Singleton import SingletonMeta


class Camera(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.position = [0, 0]
        self.min_position = [0, 0]
        self.max_position = [0, 0]
        self.entity = None

    # region Getters & Setters
    def get_position(self) -> list:
        return self.position

    def set_entity(self, entity: IControllable):
        self.entity = entity

    def set_minimum_position(self, minimum_position: list):
        self.min_position = [
            minimum_position[0] + int(Constants.X_RESOLUTION / 2),
            minimum_position[1] + int(Constants.Y_RESOLUTION / 2)
        ]

    def set_maximum_position(self, maximum_position: list):
        self.max_position = [
            maximum_position[0] - int(Constants.X_RESOLUTION / 2),
            maximum_position[1] - int(Constants.Y_RESOLUTION / 2)
        ]
    # endregion

    def update(self):
        if self.entity:
            self.move(self.entity.get_position())

    def move(self, position: list):
        self.position = [
            min(max(position[0], self.min_position[0]), self.max_position[0]),
            min(max(position[1], self.min_position[1]), self.max_position[1])
        ]
