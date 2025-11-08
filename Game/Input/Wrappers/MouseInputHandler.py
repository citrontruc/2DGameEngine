"""
A simple class to retrieve user keyboard input.
"""
from enum import Enum

from pygame import mouse


class MouseControl(Enum):
    RIGHT_BUTTON = 1
    LEFT_BUTTON = 2
    SCROLL_BUTTON = 3


class MouseInputHandler:
    def __init__(self):
        pass

    def get_all_mouse_input(self) -> dict:
        mouse_dict = {"position": self.get_position(),
                      "button_press": self.get_button()}
        return mouse_dict

    def get_position(self) -> tuple:
        return mouse.get_pos()

    def get_button(self) -> tuple:
        return (self.is_button_down(MouseControl.LEFT_BUTTON), self.is_button_down(MouseControl.RIGHT_BUTTON))

    def is_button_down(self, mouse_button: MouseControl) -> bool:
        mouse_button_press = mouse.get_pressed(num_buttons=3)
        match mouse_button:
            case MouseControl.RIGHT_BUTTON:
                return mouse_button_press[2]
            case MouseControl.LEFT_BUTTON:
                return mouse_button_press[0]
            case MouseControl.SCROLL_BUTTON:
                return mouse_button_press[1]
            case _:
                raise ValueError("Incorrect value provided for a mouse button input.")
