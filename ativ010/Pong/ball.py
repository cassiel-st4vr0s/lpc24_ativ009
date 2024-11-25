from coord import Coord
from vector import Vector

class Ball:
    def __init__(self):
        self.position = Coord(20, 10)  # Center of the field
        self.velocity = Vector(1, 0)
        self.size = (1, 1)
        self.maxSpeedX = 2.0
        self.maxSpeedY = 2.0
    
    def move(self):
        self.position.setX(self.position.getX() + self.velocity.dx)
        self.position.setY(self.position.getY() + self.velocity.dy)
    
    def reverseDirection(self):
        self.velocity.reverse()
    
    def reset(self):
        self.position = Coord(20, 10)
        self.velocity = Vector(1, 0)
    
    def limitSpeed(self):
        if abs(self.velocity.dx) > self.maxSpeedX:
            self.velocity.dx = self.maxSpeedX * (1 if self.velocity.dx > 0 else -1)
        if abs(self.velocity.dy) > self.maxSpeedY:
            self.velocity.dy = self.maxSpeedY * (1 if self.velocity.dy > 0 else -1)
    
    def accelerate(self):
        self.velocity.scale(1.1)
        self.limitSpeed()