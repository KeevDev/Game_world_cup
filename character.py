import pygame
gravity = 0.5
class Player:
   
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 0
        self.velocidad_y = 0
        self.tiempo_total = 3000
        self.is_jumping = False


    def jump(self):
        if not self.is_jumping:
            self.velocidad_y = -10  # Ajusta la velocidad inicial del salto según tus necesidades
            self.is_jumping = True

    def movimiento(self,SCREEN_HEIGHT):

        self.x += self.speed

        self.velocidad_y += gravity

        # Actualizar la posición vertical del personaje
        if self.y + self.velocidad_y < 400 // 2 + 20:
            self.y += self.velocidad_y
            self.is_jumping = False


    
        
