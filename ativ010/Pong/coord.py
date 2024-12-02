class Coord:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y
    
    def get_x(self) -> float:
        return self.x
    
    def get_y(self) -> float:
        return self.y
    
    def set_x(self, x: float):
        self.x = x
    
    def set_y(self, y: float):
        self.y = y