import time
from game import Game

#main function that initializes the game
def main():
    game = Game()
    game.initialize()

    #main loop
    while not game.is_game_over:
        game.update() #updates game state

        #shows game state
        print(f"Ball: ({game.ball.position.x:.2f}, {game.ball.position.y:.2f}) | Velocity: ({game.ball.velocity.dx:.2f}, {game.ball.velocity.dy:.2f})")
        print(f"P1 Paddle: {game.player1.paddle.position.y:.2f} | P2 Paddle: {game.player2.paddle.position.y:.2f}")
        print(f"Score - P1: {game.scoreManager.player1Score} | P2: {game.scoreManager.player2Score}")
        time.sleep(0.1)

        #finish the if a player hits 2 points
        if game.scoreManager.player1Score >= 2 or game.scoreManager.player2Score >= 2:
            winner = 1 if game.scoreManager.player1Score > game.scoreManager.player2Score else 2
            print(f"Game Over! Player {winner} wins!")
            game.is_game_over = True

def handleInput(self):
    self.player1.paddle.isMovingDown = True
    self.player1.paddle.move()

    if self.collisionManager.checkPaddleCollision(self.ball, self.player1.paddle):
        print("Ball hit Player 1's paddle!")
        self.collisionManager.calculateBounceAngle(self.ball, self.player1.paddle)
        self.ball.accelerate()

def update(self):
    self.ball.move()
    self.player1.paddle.move()
    self.player2.paddle.move()
    self.checkWallCollisions()
    self.handleInput()

    scorer = self.collisionManager.checkScoring(self.ball)
    if scorer > 0:
        self.scoreManager.updateScore(scorer)
        self.ball.reset()
        print(f"Player {scorer} scored!")

if __name__ == "__main__":
    main()