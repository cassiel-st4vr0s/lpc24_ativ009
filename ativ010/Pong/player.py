from paddle import Paddle
from keys import Keys

class Player:
    def __init__(self, player_number: int):
        self.score = 0
        self.controls = Keys()
        self.paddle = Paddle(player_number)
    
    def handleInput(self, key_event: str):
        if key_event == self.controls.getUpKey():
            self.paddle.isMovingUp = True
        elif key_event == self.controls.getDownKey():
            self.paddle.isMovingDown = False
    
    def updateScore(self):
        self.score += 1
    
    def getScore(self) -> int:
        return self.score
    
    def reset(self):
        self.score = 0
        self.paddle.reset()