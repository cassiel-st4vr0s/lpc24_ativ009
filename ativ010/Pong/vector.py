class Vector:
    def __init__(self, dx: float = 0, dy: float = 0):
        self.dx = dx
        self.dy = dy
    
    def reverse(self):
        self.dx = -self.dx
        self.dy = -self.dy
    
    def set_direction(self, dx: float, dy: float):
        self.dx = dx
        self.dy = dy
    
    def scale(self, factor: float):
        self.dx *= factor
        self.dy *= factor