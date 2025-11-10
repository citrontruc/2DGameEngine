"""
A class to read the content of the json level folder and load all the levels.
"""
import json
import os


class JsonLevelReader:
    def __init__(self) -> None:
        self.level_folder = "Game/Assets"
        self.level_dict = {}
        level_directory_list = os.listdir(self.level_folder)
        for level_json in level_directory_list:
            with open(f"{self.level_folder}/{level_json}") as f:
                document = json.load(f)
                self.level_dict[document["level_id"]] = document

    def get_level(self, level_id: str) -> dict:
        if level_id in self.level_dict.keys():
            return self.level_dict[level_id]
        raise IndexError(f"ID of level you asked for is incorrect{level_id}")
