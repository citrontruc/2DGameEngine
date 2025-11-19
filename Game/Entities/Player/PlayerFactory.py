"""
A class to create players and do the setup for players.
"""
from Game.Services.IFactory import IFactory


class PlayerFactory(IFactory):
    def create(self):
        return super().create()
