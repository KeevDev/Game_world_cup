import pygame
import os

class Player:
   
    def __init__(self, x, y, jugador):
        self.x = x
        self.y = y
        self.jugador = jugador
        if self.jugador == 1 :
            self.sprite_files = ["jugador1.png","p1.png", "p2.png", "p3.png", "p4.png","p5.png","p6.png","p7.png","p8.png","p9.png"]
            self.figura = [pygame.image.load(os.path.join("img/jugador1_sprites", file)).convert_alpha() for file in self.sprite_files]
        else:
            self.sprite_files = ["jugador2.png","p1.png", "p2.png", "p3.png", "p4.png","p5.png","p6.png","p7.png","p8.png","p9.png"]
            self.figura = [pygame.image.load(os.path.join("img/jugador2_sprites", file)).convert_alpha() for file in self.sprite_files]

        self.speed_x = 0
        self.speed_Y = 0
        self.is_jumping = False
        self.gravity = 0.5
        self.marcador = 0

    def draw(self, screen, posicion):
        self.figura[posicion] = pygame.transform.scale(self.figura[posicion], (90, 153))
        screen.blit(self.figura[posicion],(self.x,self.y))

    def jump(self):
        if not self.is_jumping:
            self.speed_Y = -8  # Ajusta la velocidad inicial del salto según tus necesidades
            self.is_jumping = True

    def update(self,SCREEN_HEIGHT):
        self.jugador = self.figura[0].get_rect() # PARA COLISIONES
        self.jugador.topleft = (self.x,self.y)

        self.x += self.speed_x
        self.speed_Y += self.gravity

        # Actualizar y no dejar que pase del limite del suelo
        if self.y + self.speed_Y <= SCREEN_HEIGHT // 2 + 60 :
            self.y += self.speed_Y
            self.is_jumping = False

    def kick(self,screen,index):

        if index < len(self.figura):
            self.draw(screen,index)
            
        
        
