from collision_manager import CollisionManager
from score_manager import ScoreManager
from player import Player
from ball import Ball

class Game:
    def __init__(self):
        #sets the size of the playing area, maximum score, and other starting parameters
        self.size = (40, 20)
        self.max_score = 5
        self.is_game_over = False
        self.game_speed = 0.5
        self.ball = Ball()  #instancing the ball
        self.player1 = Player(1)  #instancing Player 1
        self.player2 = Player(2)  #instancing Player 2
        self.scoreManager = ScoreManager(self.max_score)  #manages the score
        self.collision_manager = CollisionManager()  #manages collisions
    
    def initialize(self):
        #initializes the game and restarts the parameters
        print("Game initialized! Use WASD and arrow keys to control paddles.")
        self.reset()
    
    def update(self):
        #updates the game state with each iteration
        self.ball.move()
        self.player1.paddle.move()
        self.player2.paddle.move()
        self.checkWallCollision() 
        self.handle_input() #handles command input

       #check if there was a score
        scorer = self.collision_manager.checkScoring(self.ball)
        if scorer > 0:
            self.scoreManager.updateScore(scorer)  #updates the score
            self.ball.reset()
            print(f"Player {scorer} scored!")

        #checks for collisions with the rackets
        if self.collision_manager.checkPaddleCollision(self.ball, self.player1.paddle):
            print("Ball hit Player 1's paddle!")
            self.collision_manager.calculateBounceAngle(self.ball, self.player1.paddle)
            self.ball.accelerate()

        if self.collision_manager.checkPaddleCollision(self.ball, self.player2.paddle):
            print("Ball hit Player 2's paddle!")
            self.collision_manager.calculateBounceAngle(self.ball, self.player2.paddle)
            self.ball.accelerate()

      
        self.check_victory()
    
    def handle_input(self):
        pass
    
    def check_victory(self): 
        if self.scoreManager.checkVictory():
            winner = 1 if self.scoreManager.player1_score > self.scoreManager.player2_score else 2
            print(f"Game Over! Player {winner} wins!")
            self.is_game_over = True
    
    def reset(self):
        #reset game
        self.ball.reset()
        self.player1.reset()
        self.player2.reset()
        self.scoreManager.reset()
        self.is_game_over = False
        print("Game reset!")
    
    def checkWallCollision(self):
        #verify ball collison with walls
        if self.collision_manager.checkWallCollision(self.ball):
            self.ball.velocity.dy = -self.ball.velocity.dy  # Inverte a direção vertical
            print("Ball bounced off wall!")
