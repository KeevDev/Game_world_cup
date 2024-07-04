import pygame

class Player:
   
    def __init__(self, x, y, figura):
        self.x = x
        self.y = y
        self.figura = pygame.image.load(figura).convert_alpha
        self.figura = pygame.transform.scale(self.figura, (58, 113))
        jugador = self.figura.get_rect()
        jugador.topleft = (self.x,self.y)
        self.speed_x = 0
        self.speed_Y = 0
        self.is_jumping = False
        self.gravity = 0.5

    def jump(self):
        if not self.is_jumping: #si no es false entra
            self.velocidad_y = -10  
            self.is_jumping = True

    def update(self,SCREEN_HEIGHT):

        self.x += self.speed

        self.velocidad_y += self.gravity

        # Actualizar la posición vertical del personaje
        if self.y + self.velocidad_y < 400 // 2 + 20:
            self.y += self.velocidad_y
            self.is_jumping = False


    