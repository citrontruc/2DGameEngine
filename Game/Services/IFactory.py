"""
An interface to create factories who can then build entities.
"""
from abc import ABC
from abc import abstractmethod

from Game.Services.Singleton import SingletonMeta


class IFactory(ABC, metaclass=SingletonMeta):
    @abstractmethod
    def create(self):
        pass
