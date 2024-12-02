import time
from game import Game

def main():
    game = Game()
    game.initialize()
    
    while not game.is_game_over:
        game.update()
        time.sleep(game.game_speed)

        if game.score_manager.check_victory():
            break

if __name__ == "__main__":
    main()