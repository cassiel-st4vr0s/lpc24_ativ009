from collision_manager import CollisionManager
from score_manager import ScoreManager
from player import Player
from ball import Ball

class Game:
    def __init__(self):
        self.size = (40, 20)  # Terminal-friendly size
        self.maxScore = 5
        self.isGameOver = False
        self.gameSpeed = 0.5
        self.ball = Ball()
        self.player1 = Player(1)
        self.player2 = Player(2)
        self.scoreManager = ScoreManager(self.maxScore)
        self.collisionManager = CollisionManager()
    
    def initialize(self):
        print("Game initialized! Use WASD and arrow keys to control paddles.")
        self.reset()
    
    def update(self):
        self.ball.move()
        self.player1.paddle.move()
        self.player2.paddle.move()
        self.checkWallCollisions()
        self.handleInput()
        
        # Check for scoring
        scorer = self.collisionManager.checkScoring(self.ball)
        if scorer > 0:
            self.scoreManager.updateScore(scorer)
            self.ball.reset()
            print(f"Player {scorer} scored!")
        
        # Check paddle collisions
        if self.collisionManager.checkPaddleCollision(self.ball, self.player1.paddle):
            print("Ball hit Player 1's paddle!")
            self.collisionManager.calculateBounceAngle(self.ball, self.player1.paddle)
            self.ball.accelerate()
        
        if self.collisionManager.checkPaddleCollision(self.ball, self.player2.paddle):
            print("Ball hit Player 2's paddle!")
            self.collisionManager.calculateBounceAngle(self.ball, self.player2.paddle)
            self.ball.accelerate()
        
        self.checkVictory()
    
    def handleInput(self):
        # Simulated input handling
        pass
    
    def checkVictory(self):
        if self.scoreManager.checkVictory():
            winner = 1 if self.scoreManager.player1Score > self.scoreManager.player2Score else 2
            print(f"Game Over! Player {winner} wins!")
            self.isGameOver = True
    
    def reset(self):
        self.ball.reset()
        self.player1.reset()
        self.player2.reset()
        self.scoreManager.reset()
        self.isGameOver = False
        print("Game reset!")
    
    def checkWallCollisions(self):
        if self.collisionManager.checkWallCollision(self.ball):
            self.ball.velocity.dy = -self.ball.velocity.dy
            print("Ball bounced off wall!")