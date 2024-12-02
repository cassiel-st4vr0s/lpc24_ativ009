from coord import Coord
from vector import Vector
class Ball:
    def __init__(self):
        self.position = Coord(20, 10)  #center of the field
        self.velocity = Vector(1, 0)
        self.size = (1, 1)
        self.max_speed_x = 2.0
        self.max_speed_y = 2.0
    
    def move(self):
        self.position.set_x(self.position.get_x() + self.velocity.dx)
        self.position.set_y(self.position.get_y() + self.velocity.dy)
    
    def reverse_direction(self):
        self.velocity.reverse()
    
    def reset(self):
        self.position = Coord(20, 10)
        self.velocity = Vector(1, 0)
    
    def limit_speed(self):
        if abs(self.velocity.dx) > self.max_speed_x:
            self.velocity.dx = self.max_speed_x * (1 if self.velocity.dx > 0 else -1)
        if abs(self.velocity.dy) > self.max_speed_y:
            self.velocity.dy = self.max_speed_y * (1 if self.velocity.dy > 0 else -1)
    
    def accelerate(self):
        self.velocity.scale(1.1)
        self.limit_speed()