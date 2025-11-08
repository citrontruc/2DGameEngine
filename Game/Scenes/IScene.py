"""
An abstract class to create Scenes / levels.
"""
from abc import ABC
from abc import abstractmethod


class IScene(ABC):
    @abstractmethod
    def load(self) -> None:
        pass

    @abstractmethod
    def unload(self) -> None:
        pass

    @abstractmethod
    def update(self, delta_time: float) -> None:
        pass

    @abstractmethod
    def draw(self) -> None:
        pass
