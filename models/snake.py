import pygame
from settings import COLOR_RGB_GRAY
class Snake:
    def __init__(self):
        self.pos = [310, 0]
        self.body = [
            [310, 0], 
            [310,10], 
            [310, 20]
        ] # Coordenadas en donde pintaremos un rectangulo
        self.size = 10
        self.direction = "DOWN" # Dirección inicial

    def draw(self, window):
        """ Pintar los rectangulos """

        # Se suma o resta según la coordenada
        if self.direction == "UP":
            self.pos[1] -= self.size
        elif self.direction == "DOWN":
            self.pos[1] += self.size
        elif self.direction == "LEFT":
            self.pos[0] -= self.size
        elif self.direction == "RIGHT":
            self.pos[0] += self.size

        # Agregamos cuerpo a la serpiente en la pos 0, agregamos una lista con la posción
        self.body.insert(0, list(self.pos))
        # Eliminanos las últimas coordenadas [x,y] para eliminar su cola si no ha colisionado
        self.body.pop()

        for coord in self.body:
            # Le indicamos que lo pintara en nuestra ventana
            # Se pintara un rectángulo por las pos del body
            # Se le indicará en donde se pintará, el color, el rectangulo como tal en que coordenadas se pintara, el tamaño
            pygame.draw.rect(window, COLOR_RGB_GRAY, pygame.Rect(coord[0], coord[1], self.size, self.size))

    def move(self, event):
        """ Se mueve en la posición dependiendo del evento del teclado
            Se escuchan las teclas izquierda, derecha, arriba, abajo
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.move_up()
            elif event.key == pygame.K_DOWN:
                self.move_down()
            elif event.key == pygame.K_LEFT:
                self.move_left()
            elif event.key == pygame.K_RIGHT:
                self.move_right()
        
    def move_up(self):
        self.direction = "UP"

    def move_down(self):
        self.direction = "DOWN"

    def move_left(self):
        self.direction = "LEFT"

    def move_right(self):
        self.direction = "RIGHT"
            