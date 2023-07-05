import pygame
import random
from enum import Enum
from collections import namedtuple

pygame.init()


class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4


Point = namedtuple("Point", "x", "y")


class SnakeGame:
    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h
        # display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Saaaaaaanp🐍")
        self.clock = pygame.time.Clock()

        # initial game state
        self.direction = Direction.RIGHT

        self.head = Point(self.w, self.h)

    def play_step(self):
        pass


if __name__ == "__main__":
    game = SnakeGame()

    while True:
        game.play_step()

    pygame.quit()
