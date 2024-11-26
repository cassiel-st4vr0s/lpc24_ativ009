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
        print(f"Score - P1: {game.score_manager.player1_score} | P2: {game.score_manager.player2_score}")
        time.sleep(0.1)

        #finish the if a player hits 2 points
        if game.score_manager.player1_score >= 2 or game.score_manager.player2_score >= 2:
            winner = 1 if game.score_manager.player1_score > game.score_manager.player2_score else 2
            print(f"Game Over! Player {winner} wins!")
            game.is_game_over = True

def handle_input(self):
    self.player1.paddle.is_moving_down = True
    self.player1.paddle.move()

    if self.collision_manager.check_paddle_collision(self.ball, self.player1.paddle):
        print("Ball hit Player 1's paddle!")
        self.collision_manager.calculate_bounce_angle(self.ball, self.player1.paddle)
        self.ball.accelerate()

def update(self):
    self.ball.move()
    self.player1.paddle.move()
    self.player2.paddle.move()
    self.check_wall_collision()
    self.handle_input()

    scorer = self.collision_manager.check_scoring(self.ball)
    if scorer > 0:
        self.score_manager.update_score(scorer)
        self.ball.reset()
        print(f"Player {scorer} scored!")

if __name__ == "__main__":
    main()