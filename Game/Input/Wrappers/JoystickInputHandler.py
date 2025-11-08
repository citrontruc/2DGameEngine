"""
A simple class to retrieve joystick user input.
"""
from enum import Enum

import pygame
from pygame import joystick


class JOYSTICK(Enum):
    SOUTH_BUTTON = 1
    EAST_BUTTON = 2
    DPAD_DOWN = 3
    DPAD_UP = 4
    DPAD_RIGHT = 5
    DPAD_LEFT = 6


class JoystickInputHandler:
    def __init__(self) -> None:
        self.joystick = None
        self.joystick_id = None

    def has_joystick(self):
        return self.joystick is not None

    def connect_joystick(self, joystick_value: joystick.JoystickType) -> None:
        self.joystick = joystick_value
        self.joystick_id = self.joystick.get_instance_id()
        self.joystick.init()

    def check_for_existing_joystick(self) -> None:
        if self.joystick is None:
            joystick_count = joystick.get_count()
            if joystick_count > 0:
                self.connect_joystick(joystick.Joystick(0))

    def check_joystick_connect(self, event_list: list) -> None:
        for event in event_list:
            if event.type == pygame.JOYDEVICEADDED and self.joystick is None:
                self.connect_joystick(joystick.Joystick(0))
                print(f"jooystick connected {self.joystick_id}")

    def check_joystick_disconnect(self, event_list: list) -> None:
        for event in event_list:
            if event.type == pygame.JOYDEVICEREMOVED:
                if self.joystick is not None and event.instance_id == self.joystick.get_instance_id():
                    self.reset_joystick()
                    print(f"jooystick disconnected {self.joystick_id}")

    def reset_joystick(self):
        self.joystick = None
        self.joystick_id = None
