import pygame

from Game.Scenes.SceneManager import SceneManager


class GameManager:
    def __init__(self) -> None:
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1280, 720))
        self.scene_manager = SceneManager()

    def initialize_game(self):
        pygame.init()
        pygame.joystick.init()
        level = self.scene_manager.get_level_from_id("1")
        self.scene_manager.transition_to(level)

    def get_delta_time(self) -> float:
        delta_time = self.clock.get_time() / 1000  # Convert to milliseconds
        return delta_time

    def run_game_loop(self):
        running = True

        while running:
            event_list = pygame.event.get()
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in event_list:
                if event.type == pygame.QUIT:
                    running = False

            delta_time = self.get_delta_time()
            self.scene_manager.update(delta_time, event_list)

            # fill the screen with a color to wipe away anything from last frame
            self.scene_manager.draw(self.screen)

            # flip() the display to put your work on screen
            pygame.display.flip()

            self.clock.tick(60)  # limits FPS to 60

        pygame.quit()
