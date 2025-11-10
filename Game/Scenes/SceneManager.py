"""
A class to handle transitions between scenes (menus and levels).
"""
from Game.Scenes.IScene import IScene
from Game.Scenes.Levels.JsonLevelReader import JsonLevelReader
from Game.Scenes.Levels.Level import Level


class SceneManager:
    def __init__(self) -> None:
        self.level_reader = JsonLevelReader()
        self.current_scene = None

    def get_level_from_id(self, level_id: str) -> IScene:
        level = self.level_reader.get_level(level_id)
        return Level(level)

    def transition_to(self, new_scene: IScene):
        if self.current_scene:
            self.current_scene.unload()
        self.current_scene = new_scene
        self.current_scene.load()

    def update(self, delta_time: float, event_list: list):
        if self.current_scene is not None:
            self.current_scene.update(delta_time, event_list)

    def draw(self, window):
        if self.current_scene is not None:
            self.current_scene.draw(window)
