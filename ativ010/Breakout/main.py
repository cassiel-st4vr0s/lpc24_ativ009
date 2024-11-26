from dataclasses import dataclass
from typing import List, Tuple
import time

@dataclass
class Coord:
    x: float
    y: float

    def getX(self) -> float:
        return self.x

    def getY(self) -> float:
        return self.y

    def setX(self, x: float) -> None:
        self.x = x

    def setY(self, y: float) -> None:
        self.y = y


class SpeedVector:
    def _init_(self, dx: float, dy: float):
        self.dx = dx
        self.dy = dy

    def reverse(self) -> None:
        self.dx = -self.dx
        self.dy = -self.dy

    def setDirection(self, dx: float, dy: float) -> None:
        self.dx = dx
        self.dy = dy


class Ball:
    def _init_(self, position: Coord, size: Tuple[int, int]):
        self.position = position
        self.speed = SpeedVector(2.0, -2.0)
        self.size = size
        self.initialSpeed = 2.0
        self.maxSpeed = 6.0

    def move(self) -> None:
        self.position.x += self.speed.dx
        self.position.y += self.speed.dy
        print(f"Ball moved to position ({self.position.x}, {self.position.y})")

    def increaseSpeed(self) -> None:
        current_speed = abs(self.speed.dx)
        if current_speed < self.maxSpeed:
            self.speed.dx *= 1.1
            self.speed.dy *= 1.1
            print("Ball speed increased!")

    def reverseDirection(self) -> None:
        self.speed.reverse()
        print("Ball direction reversed!")

    def reset(self) -> None:
        self.position.x = 300
        self.position.y = 400
        self.speed = SpeedVector(2.0, -2.0)
        print("Ball reset to initial position")


class Block:
    def _init_(self, position: Coord, width: int, height: int, points: int):
        self.position = position
        self.width = width
        self.height = height
        self.points = points

    def hit(self) -> None:
        print(f"Block hit! Worth {self.points} points")

    def getPoints(self) -> int:
        return self.points


class BlockManager:
    def _init_(self, numColumns: int, spacing: Coord):
        self.blocks: List[Block] = []
        self.numColumns = numColumns
        self.spacing = spacing

    def createBlocks(self) -> None:
        points_per_row = [7, 7, 5, 5, 3, 3, 1,
                          1]  # Points per row from top to bottom
        for row in range(8):
            for col in range(self.numColumns):
                x = col * (40 + self.spacing.x)
                y = row * (20 + self.spacing.y) + 100
                block = Block(Coord(x, y), 40, 20, points_per_row[row])
                self.blocks.append(block)
        print(f"Created {len(self.blocks)} blocks")

    def removeBlock(self, block: Block) -> None:
        self.blocks.remove(block)
        print("Block removed")

    def regenerateBlocks(self) -> None:
        self.blocks.clear()
        self.createBlocks()
        print("Blocks regenerated")


class Paddle:
    def _init_(self, position: Coord, width: int, height: int):
        self.position = position
        self.width = width
        self.height = height
        self.initialWidth = width
        self.isMovingLeft = False
        self.isMovingRight = False

    def move(self) -> None:
        if self.isMovingLeft:
            self.position.x -= 5
            print("Paddle moved left")
        elif self.isMovingRight:
            self.position.x += 5
            print("Paddle moved right")

    def reset(self) -> None:
        self.position.x = 300
        self.width = self.initialWidth
        print("Paddle reset to initial position")

    def expandForSafeMode(self) -> None:
        self.width = 580  # Full width minus borders
        self.position.x = 10  # Left border width
        print("Paddle expanded for safe mode")


class Game:
    def _init_(self, size: Tuple[int, int]):
        self.size = size
        self.score = 0
        self.lives = 3
        self.borderDimensions = (10, 20)  # width, height
        self.inSafeMode = False

        # Initialize game objects
        self.ball = Ball(Coord(300, 400), (10, 10))
        self.paddle = Paddle(Coord(300, 800), 60, 20)
        self.blockManager = BlockManager(14, Coord(3, 3))

    def init(self) -> None:
        self.blockManager.createBlocks()
        print("Game initialized")

    def update(self) -> None:
        self.ball.move()
        self.paddle.move()
        self.checkCollisions()
        print(f"Game state - Score: {self.score}, Lives: {self.lives}")

    def checkCollisions(self) -> None:
        # Check ball-paddle collision
        if (
                self.paddle.position.x <= self.ball.position.x <= self.paddle.position.x + self.paddle.width and
                abs(self.ball.position.y - self.paddle.position.y) < 10):
            self.ball.reverseDirection()
            print("Ball hit paddle!")

        # Check ball-block collisions
        for block in self.blockManager.blocks[:]:
            if (
                    block.position.x <= self.ball.position.x <= block.position.x + block.width and
                    block.position.y <= self.ball.position.y <= block.position.y + block.height):
                self.score += block.getPoints()
                block.hit()
                self.blockManager.removeBlock(block)
                self.ball.reverseDirection()

    def toggleSafeMode(self) -> None:
        self.inSafeMode = not self.inSafeMode
        if self.inSafeMode:
            self.paddle.expandForSafeMode()
        else:
            self.paddle.reset()
        print(f"Safe mode {'enabled' if self.inSafeMode else 'disabled'}")


# Demo usage
def main():
    game = Game((600, 850))
    game.init()

    # Simulate a few game actions
    print("\nSimulating game actions...")
    for _ in range(5):
        game.update()
        time.sleep(1)  # Pause between updates

        # Simulate paddle movement
        game.paddle.isMovingRight = True
        game.paddle.move()
        game.paddle.isMovingRight = False

        # Check if ball is lost
        if game.ball.position.y > game.size[1]:
            game.lives -= 1
            if game.lives <= 0:
                game.toggleSafeMode()
            game.ball.reset()
            print(f"Ball lost! Lives remaining: {game.lives}")


if _name_ == "_main_":
    main()