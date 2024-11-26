from coord import Coord
class Paddle:
    def __init__(self, player_number: int):
        self.position = Coord(0, 10)  #starting position
        self.width = 2
        self.height = 6
        self.speed = 1.0
        self.is_moving_up = False
        self.is_moving_down = False
        self.player_number = player_number
    
    def move(self):
        if self.is_moving_up:
            self.position.setY(self.position.getY() - self.speed)
        if self.is_moving_down:
            self.position.setY(self.position.getY() + self.speed)
    
    def check_wall_collision(self) -> bool:
        #check if paddle hits top or bottom walls
        return self.position.getY() <= 0 or self.position.getY() + self.height >= 20
    
    def reset(self):
        self.position = Coord(0 if self.player_number == 1 else 38, 10)
        self.is_moving_up = False
        self.is_moving_down = False
    
    def handle_collision(self, ball):
        if self.check_wall_collision():
            if self.position.getY() <= 0:
                self.position.setY(0)
            else:
                self.position.setY(20 - self.height)