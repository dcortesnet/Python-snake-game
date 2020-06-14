import pygame
import sys
import time
from models.snake import Snake
from models.point import Point
from models.food import Food
from settings import (
    WINDOW_WIDTH, 
    WINDOW_HEIGHT, 
    FRAMES_X_SECONDS, 
    COLOR_RGB_BLUE, 
    COLOR_RGB_ORANGE,
    POINTS_TO_WIN
)

pygame.init()
pygame.display.set_caption('Juego de Serpiente')
pygame.key.set_repeat(30)

class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.point = Point()
        self.food = Food()
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

            self.window.fill(COLOR_RGB_BLUE)
            self.clock.tick(FRAMES_X_SECONDS)
            
            self.point.draw(self.window)
            self.food.draw(self.window)
            self.snake.draw(self.window)

            self.check_collide_snake_border()
            self.check_collide_snake_food()
            self.check_win_game()
            
            self.check_collide_snake_himself()
            pygame.display.flip()
        
    def check_collide_snake_food(self):
        """ Método de verificación si la cabeza del snake colisionó con la comida """
        if self.snake.pos == self.food.pos:
            # Insertamos nuevas coordenadas X e Y
            self.snake.body.insert(0, list(self.food.pos))
            # Agregamos una nueva coordenada para la comida
            self.food.change_pos()
            # Sumamos 10 puntos
            self.point.points += 10
    
    def check_collide_snake_border(self):
        """ Método de verificación si la cabeza del snake colisionó con la frontera """
        snake_pos_x = self.snake.pos[0]
        snake_pos_y = self.snake.pos[1]
        
        if snake_pos_x < 0 or snake_pos_x > WINDOW_WIDTH or snake_pos_y < 0 or snake_pos_y > WINDOW_HEIGHT:
            self.finish_game('loss')

    def check_collide_snake_himself(self):
        """ Método de verificación si la cabeza del snake solisionó con su cuerpo """
        # Se debe comprobar menos la primera pos que es en donde estará la cabeza
        if self.snake.pos in self.snake.body[2:]:
            self.finish_game('loss')


    def check_win_game(self):
        """ Método de verificación si gano el juegó """
        if(self.point.points >= POINTS_TO_WIN):
            self.finish_game('win')

    def finish_game(self, type_of_completion):
        """ Método de visualización de finalización del juego """
        if type_of_completion == "win":
            description = "Juego ganado"
        else:
            description = "Juego perdido"
        font = pygame.font.SysFont('Arial', 72)
        text = font.render(description, True, COLOR_RGB_ORANGE)
        text_rect = text.get_rect()
        text_rect.center = [WINDOW_WIDTH/2, WINDOW_HEIGHT/2]
        self.window.blit(text, text_rect)
        pygame.display.flip()
        time.sleep(3)
        sys.exit()
        
    
            
        
