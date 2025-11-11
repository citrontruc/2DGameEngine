"""
A class to define button components.
"""
from Game.Menus.IMenuComponent import IMenuComponent


class Button(IMenuComponent):
    def __init__(self, button_characteristics: dict) -> None:
        super().__init__()

    def on_hover(self):
        pass

    def on_click(self):
        pass

    def update(self, delta_time: float):
        pass

    def draw(self, surface):
        pass
