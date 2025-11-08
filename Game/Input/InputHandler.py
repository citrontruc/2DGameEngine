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

    def get_mouse(self):
        mouse_dict = self.mouse_input_handler.get_all_mouse_input()
        return mouse_dict

    def check_for_joystick(self, event_list: list):
        if not self.joystick_input_handler.has_joystick():
            self.joystick_input_handler.check_joystick_connect(event_list)
        if self.joystick_input_handler.has_joystick():
            self.joystick_input_handler.check_joystick_disconnect(event_list)
