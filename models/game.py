import pygame
import sys
import time
from models.snake import Snake

pygame.init()
pygame.key.set_repeat(30)

class Game:
    def __init__(self, window_width: int, window_height: int, frames_x_seconds:int):
        self.window_width = window_width
        self.window_height = window_height
        self.frames_x_seconds = frames_x_seconds
        self.points = 0
        self.window = pygame.display.set_mode(
            (self.window_width, self.window_height)
        )
        self.clock = pygame.time.Clock()
        self.snake = Snake()

    def run(self):
        """ Loop princial del juego """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

        self.updateGame()

    def updateGame(self):
        """ Actualiza el juego por segundo"""
        pygame.display.flip()


        
