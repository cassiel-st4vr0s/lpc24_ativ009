class Coord:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y
    
    def getX(self) -> float:
        return self.x
    
    def getY(self) -> float:
        return self.y
    
    def setX(self, x: float):
        self.x = x
    
    def setY(self, y: float):
        self.y = y