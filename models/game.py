import pygame
import sys
import time
from models.snake import Snake
from models.point import Point
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, FRAMES_X_SECONDS, COLOR_RGB_BLUE

pygame.init()
pygame.display.set_caption('Juego de Serpiente')
pygame.key.set_repeat(30)

class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.point = Point()
        self.window = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT)
        )

    def run(self):
        """ Loop princial del juego """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
                self.snake.move(event)

            self.clock.tick(FRAMES_X_SECONDS)
            self.window.fill(COLOR_RGB_BLUE)
            self.point.draw(self.window)
            self.snake.draw(self.window)
            
            pygame.display.flip()
        


        
