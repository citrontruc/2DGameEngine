"""
A class to handle user input and update our input component.
TODO: allow keybinding by using an intermediate class to translate keys to controls
"""
import pygame

from Game.Input.Wrappers.JoystickInputHandler import JoystickInputHandler
from Game.Input.Wrappers.KeyboardInputHandler import KeyboardInputHandler
from Game.Input.Wrappers.MouseInputHandler import MouseInputHandler


class InputHandler:
    def __init__(self):
        self.keyboard_input_handler = KeyboardInputHandler()
        self.mouse_input_handler = MouseInputHandler()
        self.joystick_input_handler = JoystickInputHandler()

    def get_keys(self) -> dict:
        keys = self.keyboard_input_handler.get_all_keyboard_input()
        return keys

    def get_mouse(self) -> dict:
        mouse_dict = self.mouse_input_handler.get_all_mouse_input()
        return mouse_dict

    def check_for_joystick(self, event_list: list) -> bool:
        return self.joystick_input_handler.handle_joystick_connection(event_list)

    def get_joystick_input(self) -> dict:
        joystick_input_dict = self.joystick_input_handler.get_joystick_input()
        return joystick_input_dict
