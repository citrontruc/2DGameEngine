"""
A method to retrieve user input and translate them into player actions.
"""
from Game.Input.InputHandler import InputHandler


class PlayerInputTranslator:
    def __init__(self) -> None:
        self.input_handler = InputHandler()
        self.keyboard_translation_dict = {
            "JUMP" : "space_bar",
            "HIT" : "enter",
            "MOVE" : "arrow_keys"
        }

    def retrieve_input(self, event_list: list) -> dict:
        player_input_dict = {
            "mouse" : self.input_handler.get_mouse(),
            "keyboard" : self.input_handler.get_keys(),
            "joystick" : self.input_handler.get_joystick_input()
            if self.input_handler.check_for_joystick(event_list) else None
        }
        return player_input_dict

    def translate_input(self, player_input_dict: dict) -> dict:
        keyboard_control = player_input_dict["keyboard"]
        action_dict = {
            "JUMP" : False,
            "HIT" : False,
            "MOVE" : (0, 0)
        }
        for action in self.keyboard_translation_dict.keys():
            if action == "MOVE":
                action_dict["MOVE"] = (
                    int(keyboard_control["arrow_keys"][1]) - int(keyboard_control["arrow_keys"][0]),
                    int(keyboard_control["arrow_keys"][3]) - int(keyboard_control["arrow_keys"][2])
                )
            else:
                action_dict[action] = keyboard_control[self.keyboard_translation_dict[action]]
        return action_dict
