from coord import Coord

class Paddle:
    def __init__(self, player_number: int):
        self.position = Coord(0, 10)  # Starting position
        self.width = 2
        self.height = 6
        self.speed = 1.0
        self.isMovingUp = False
        self.isMovingDown = False
        self.playerNumber = player_number
    
    def move(self):
        if self.isMovingUp:
            self.position.setY(self.position.getY() - self.speed)
        if self.isMovingDown:
            self.position.setY(self.position.getY() + self.speed)
    
    def checkWallCollision(self) -> bool:
        # Check if paddle hits top or bottom walls
        return self.position.getY() <= 0 or self.position.getY() + self.height >= 20
    
    def reset(self):
        self.position = Coord(0 if self.playerNumber == 1 else 38, 10)
        self.isMovingUp = False
        self.isMovingDown = False
    
    def handleCollision(self, ball):
        if self.checkWallCollision():
            if self.position.getY() <= 0:
                self.position.setY(0)
            else:
                self.position.setY(20 - self.height)