from ball import Ball
from paddle import Paddle
class CollisionManager:
    def check_paddle_collision(self, ball: Ball, paddle: Paddle) -> bool:
        ball_x = ball.position.get_x()
        ball_y = ball.position.get_y()
        paddle_x = paddle.position.get_x()
        paddle_y = paddle.position.get_y()
        
        return (ball_x >= paddle_x and 
                ball_x <= paddle_x + paddle.width and
                ball_y >= paddle_y and 
                ball_y <= paddle_y + paddle.height)
    
    def check_wall_collision(self, ball: Ball) -> bool:
        return ball.position.get_y() <= 0 or ball.position.get_y() >= 20
    
    def check_scoring(self, ball: Ball) -> int:
        if ball.position.get_x() <= 0:
            return 2  # Player 2 scores
        elif ball.position.get_x() >= 40:
            return 1  # Player 1 scores
        return 0  # No scoring
    
    def calculate_bounce_angle(self, ball: Ball, paddle: Paddle):
        relative_intersect_y = (paddle.position.get_y() + (paddle.height / 2)) - ball.position.get_y()
        normalized_intersect = relative_intersect_y / (paddle.height / 2)
        bounce_angle = normalized_intersect * 0.75
        ball.velocity.set_direction(-ball.velocity.dx, -bounce_angle)