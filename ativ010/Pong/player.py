from paddle import Paddle
from keys import Keys
class Player:
    def __init__(self, player_number: int):
        self.score = 0
        self.controls = Keys()
        self.paddle = Paddle(player_number)
    
    def handle_input(self, key_event: str):
        if key_event == self.controls.get_up_key():
            self.paddle.is_moving_up = True
            self.paddle.is_moving_down = False
        elif key_event == self.controls.get_down_key():
            self.paddle.is_moving_down = True
            self.paddle.is_moving_up = False
    
    def update_score(self):
        self.score += 1
    
    def get_score(self) -> int:
        return self.score
    
    def reset(self):
        self.score = 0
        self.paddle.reset()