class ScoreManager:
    def __init__(self, max_score: int):
        self.player1_score = 0
        self.player2_score = 0
        self.max_score = max_score
    
    def update_score(self, player: int):
        if player == 1:
            self.player1_score += 1
        else:
            self.player2_score += 1
        print(f"Score - P1: {self.player1_score} | P2: {self.player2_score}")
    
    def check_victory(self) -> bool:
        return self.player1_score >= self.max_score or self.player2_score >= self.max_score
    
    def reset(self):
        self.player1_score = 0
        self.player2_score = 0
    
    def get_score(self, player: int) -> int:
        return self.player1_score if player == 1 else self.player2_score