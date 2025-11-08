# Example file showing a basic pygame "game loop"
import pygame

from Game.Input.InputHandler import InputHandler


def run():
    input_handler = InputHandler()
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.joystick.init()
    clock = pygame.time.Clock()
    running = True

    while running:
        event_list = pygame.event.get()
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in event_list:
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        # RENDER YOUR GAME HERE
        input_handler.check_for_joystick(event_list)

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()
