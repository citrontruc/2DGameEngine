import pygame

from Game.Input.InputHandler import InputHandler


class GameManager:
    def __init__(self) -> None:
        self.input_handler = InputHandler()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1280, 720))

    def initialize_game(self):
        pygame.init()
        pygame.joystick.init()

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

            # delta_time = self.get_delta_time()

            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill("purple")

            # RENDER YOUR GAME HERE

            # flip() the display to put your work on screen
            pygame.display.flip()

            self.clock.tick(60)  # limits FPS to 60

        pygame.quit()
