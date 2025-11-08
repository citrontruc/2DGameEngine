"""
A simple class to retrieve user keyboard input.
"""
from enum import Enum

import pygame
from pygame import key


class KEYBOARD(Enum):
    SPACE_BAR = 1
    ENTER_BUTTON = 2
    ARROW_DOWN = 3
    ARROW_UP = 4
    ARROW_RIGHT = 5
    ARROW_LEFT = 6


class KeyboardInput:
    def __init__(self) -> None:
        self.input = {
            KEYBOARD.SPACE_BAR : False,
            KEYBOARD.ENTER_BUTTON : False,
            KEYBOARD.ARROW_DOWN : False,
            KEYBOARD.ARROW_UP : False,
            KEYBOARD.ARROW_RIGHT : False,
            KEYBOARD.ARROW_LEFT : False,
        }


class KeyboardInputHandler:
    def __init__(self):
        self.keyboard = KeyboardInput()

    def get_all_keyboard_input(self) -> dict:
        keyboard_key = key.get_pressed()
        key_dict = {
            "arrow_keys" : [keyboard_key[pygame.K_LEFT],
                            keyboard_key[pygame.K_RIGHT],
                            keyboard_key[pygame.K_UP],
                            keyboard_key[pygame.K_DOWN]],
            "space_bar" : keyboard_key[pygame.K_SPACE],
            "enter" : keyboard_key[pygame.K_RETURN],
        }
        return key_dict
