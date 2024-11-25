from game import Game

def main():
    game = Game()
    game.initialize()
    
    # Simulate a few game events
    print("\nSimulating game events...")
    for _ in range(5):
        game.update()
        if game.isGameOver:
            break

if __name__ == "__main__":
    main()