import pygame
from settings import COLOR_RGB_WHITE, POINTS_TO_WIN

class Point:
    def __init__(self):
        self.points =  0
        self.color = COLOR_RGB_WHITE
        self.font = pygame.font.SysFont('Consolas', 20)
    
    def draw(self, window):
        """ Pintar los puntos """
        text = 'Puntos (win: {0}): {1}'.format(POINTS_TO_WIN, str(self.points).zfill(5))

        self.text_points = self.font.render(text, True, self.color)
        self.text_points_rect = self.text_points.get_rect()
        self.text_points_rect.topleft = [0,0]
        window.blit(self.text_points, self.text_points_rect)