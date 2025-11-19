"""
An interface to create factories who can then build entities.
"""
from abc import ABC
from abc import abstractmethod


class IFactory(ABC):
    @abstractmethod
    def create(self):
        pass
