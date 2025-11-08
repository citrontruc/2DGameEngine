from Game.GameManager import GameManager


if __name__ == "__main__":
    game_manager = GameManager()
    game_manager.initialize_game()
    game_manager.run_game_loop()
