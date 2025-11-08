"""
An abstract class to create Scenes / levels.
"""
from abc import ABC
from abc import abstractmethod

from pygame import Surface


class IScene(ABC):
    @abstractmethod
    def load(self) -> None:
        pass

    @abstractmethod
    def unload(self) -> None:
        pass

    @abstractmethod
    def update(self, delta_time: float, event_list: list) -> None:
        pass

    @abstractmethod
    def draw(self, window: Surface) -> None:
        pass
