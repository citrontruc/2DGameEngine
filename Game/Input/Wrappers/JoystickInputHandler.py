"""
A simple class to retrieve joystick user input.
"""
from enum import auto
from enum import Enum

import pygame
from pygame import joystick


class JOYSTICK(Enum):
    SOUTH_BUTTON = auto()
    WEST_BUTTON = auto()
    LEFT_STICK_DOWN = auto()
    LEFT_STICK_UP = auto()
    LEFT_STICK_RIGHT = auto()
    LEFT_STICK_LEFT = auto()


class JoystickInputHandler:
    def __init__(self) -> None:
        self.joystick = None
        self.joystick_id = None
        self.sensitivity = 0.1

    # region Getters and Setters
    def reset_joystick(self):
        self.joystick = None
        self.joystick_id = None

    def has_joystick(self):
        return self.joystick is not None
    # endregion

    # region Check connection of new joysticks
    def handle_joystick_connection(self, event_list: list):
        if not self.has_joystick():
            self.check_for_existing_joystick()
            self.check_joystick_connect_event(event_list)
        if self.has_joystick():
            self.check_joystick_disconnect_event(event_list)
        return self.has_joystick()

    def connect_joystick(self, joystick_value: joystick.JoystickType) -> None:
        self.joystick = joystick_value
        self.joystick_id = self.joystick.get_instance_id()
        self.joystick.init()

    def check_for_existing_joystick(self) -> None:
        if self.joystick is None:
            joystick_count = joystick.get_count()
            if joystick_count > 0:
                self.connect_joystick(joystick.Joystick(0))

    def check_joystick_connect_event(self, event_list: list) -> None:
        for event in event_list:
            if event.type == pygame.JOYDEVICEADDED and self.joystick is None:
                self.connect_joystick(joystick.Joystick(0))
                print(f"joystick connected {self.joystick_id}")

    def check_joystick_disconnect_event(self, event_list: list) -> None:
        for event in event_list:
            if event.type == pygame.JOYDEVICEREMOVED:
                if self.joystick is not None and event.instance_id == self.joystick.get_instance_id():
                    self.reset_joystick()
                    print(f"joystick disconnected {self.joystick_id}")
    # endregion

    # region Get input
    def get_joystick_input(self) -> dict:
        if not self.joystick:
            raise ValueError("No joystick found")
        joystick_input_dict = {
            "left_axis": (
                self.joystick.get_axis(0) if abs(self.joystick.get_axis(0)) > self.sensitivity else 0,
                self.joystick.get_axis(1) if abs(self.joystick.get_axis(1)) > self.sensitivity else 0
            ),
            "south_button": self.joystick.get_button(0),
            "west_button": self.joystick.get_button(2),
        }
        return joystick_input_dict
    # endregion
