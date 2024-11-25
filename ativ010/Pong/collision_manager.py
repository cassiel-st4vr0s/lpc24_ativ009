from ball import Ball
from paddle import Paddle

class CollisionManager:
    def checkPaddleCollision(self, ball: Ball, paddle: Paddle) -> bool:
        ball_x = ball.position.getX()
        ball_y = ball.position.getY()
        paddle_x = paddle.position.getX()
        paddle_y = paddle.position.getY()
        
        return (ball_x >= paddle_x and 
                ball_x <= paddle_x + paddle.width and
                ball_y >= paddle_y and 
                ball_y <= paddle_y + paddle.height)
    
    def checkWallCollision(self, ball: Ball) -> bool:
        return ball.position.getY() <= 0 or ball.position.getY() >= 20
    
    def checkScoring(self, ball: Ball) -> int:
        if ball.position.getX() <= 0:
            return 2  # Player 2 scores
        elif ball.position.getX() >= 40:
            return 1  # Player 1 scores
        return 0  # No scoring
    
    def calculateBounceAngle(self, ball: Ball, paddle: Paddle):
        relative_intersect_y = (paddle.position.getY() + (paddle.height / 2)) - ball.position.getY()
        normalized_intersect = relative_intersect_y / (paddle.height / 2)
        bounce_angle = normalized_intersect * 0.75
        ball.velocity.setDirection(-ball.velocity.dx, -bounce_angle)