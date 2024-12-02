from collision_manager import CollisionManager
from score_manager import ScoreManager
from player import Player
from ball import Ball
class Game:
    def __init__(self):
        self.size = (40, 20)
        self.max_score = 2  #2 points for winning
        self.game_speed = 0.1  #game speed
        self.is_game_over = False
        self.ball = Ball()
        self.player1 = Player(1)
        self.player2 = Player(2)
        self.players_core = 2 #number of players
        self.score_manager = ScoreManager(self.max_score)
        self.collision_manager = CollisionManager()
    
    def initialize(self):
        print("Game initialized...")
        self.reset()
    
    def update(self):
        self.ball.move()
        self.player1.paddle.move()
        self.player2.paddle.move()
        self.check_wall_collisions()
        self.handle_input()
        
        #check for scoring
        scorer = self.collision_manager.check_scoring(self.ball)
        if scorer > 0:
            self.score_manager.update_score(scorer)
            self.ball.reset()
            print(f"Player {scorer} scored!")
        
        #check paddle collisions
        if self.collision_manager.check_paddle_collision(self.ball, self.player1.paddle):
            print("Ball hit player's 1 paddle!")
            self.collision_manager.calculate_bounce_angle(self.ball, self.player1.paddle)
            self.ball.accelerate()
        
        if self.collision_manager.check_paddle_collision(self.ball, self.player2.paddle):
            print("Ball hit player's 2 paddle!")
            self.collision_manager.calculate_bounce_angle(self.ball, self.player2.paddle)
            self.ball.accelerate()
        
        self.check_victory()
    
    def handle_input(self):
        #simulated input handling
        self.player1.handle_input('s')
        self.player2.handle_input('down')
    
    def check_victory(self):
        if self.score_manager.check_victory():
            winner = 1 if self.score_manager.player1_score > self.score_manager.player2_score else 2
            print(f"Game Over! Player {winner} wins!")
            self.is_game_over = True
    
    def reset(self):
        self.ball.reset()
        self.player1.reset()
        self.player2.reset()
        self.score_manager.reset()
        self.is_game_over = False
        print("Game reset...")
    
    def check_wall_collisions(self):
        if self.collision_manager.check_wall_collision(self.ball):
            self.ball.velocity.dy = -self.ball.velocity.dy
            print("Ball bounced off wall!")