"""
A class to handle user input and update our input component.
"""
import pygame

from Game.Input.Wrappers.MouseInputHandler import MouseInputHandler


class InputHandler:
    def __init__(self):
        self.mouse_input_handler = MouseInputHandler()

    def show_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            print("W is being held down")

    def show_mouse(self):
        mouse_dict = {"position": self.mouse_input_handler.get_position(),
                      "button_press": self.mouse_input_handler.get_button()}
        return mouse_dict
