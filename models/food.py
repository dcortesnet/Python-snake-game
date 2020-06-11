import random
import pygame
from settings import COLOR_RGB_ORANGE

class Food:
    def __init__(self):
        self.pos = self.random_pos()
    
    def draw(self, window):
        """ Pintar los la comida """
        pygame.draw.rect(window, COLOR_RGB_ORANGE, pygame.Rect(self.pos[0], self.pos[1], 10, 10))

    def change_pos(self):
        """ Método que cambia la posición X e Y de la comida"""
        self.pos = self.random_pos()
    
    def random_pos(self):
        """ Método para cambiar la posición de X e Y aleatorio en la pantalla """
        # x 10 ya que el snake es de 10 px el tamaño
        return [     
            (random.randint(0, 49)) * 10,
            (random.randint(0, 49)) * 10
        ]

