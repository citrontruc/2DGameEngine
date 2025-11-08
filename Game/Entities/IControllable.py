"""
An interface to handle elements that can be controllable.
"""
from abc import ABC
from abc import abstractmethod


class IControllable(ABC):
    @abstractmethod
    def handle_input(self, action_dict: dict) -> None:
        pass

    @abstractmethod
    def update(self, delta_time: float) -> None:
        pass

    @abstractmethod
    def draw(self) -> None:
        pass
