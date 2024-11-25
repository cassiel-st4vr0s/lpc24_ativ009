class ScoreManager:
    def __init__(self, max_score: int):
        self.player1Score = 0
        self.player2Score = 0
        self.maxScore = max_score
    
    def updateScore(self, player: int):
        if player == 1:
            self.player1Score += 1
        else:
            self.player2Score += 1
        print(f"Score - P1: {self.player1Score} | P2: {self.player2Score}")
    
    def checkVictory(self) -> bool:
        return self.player1Score >= self.maxScore or self.player2Score >= self.maxScore
    
    def reset(self):
        self.player1Score = 0
        self.player2Score = 0
    
    def getScore(self, player: int) -> int:
        return self.player1Score if player == 1 else self.player2Score