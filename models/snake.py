class Snake:
    def __init__(self, initial_pos_x: int=100, initial_pos_y: int=50):
        self.pos_x = initial_pos_x
        self.pos_y = initial_pos_y
        self.body = [[100, 50], [90,50], [80, 50]] # Coordenadas en donde pintaremos un rectangulo

    def draw(self, window):
        """ Pintar los rectangulos """
        for coord in self.body:
            # Le indicamos que lo pintara en nuestra ventana
            pass
            
            