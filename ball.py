import pygame

class Ball():
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT,x, y):
        self.x = x
        self.y = y
        self.speed_x = 4
        self.speed_y = 0
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.air = False
        self.gravity = 0.5
    
    def ball_air(self,n):
        if not self.air:
            self.speed_y = -18  # Ajusta la velocidad inicial del salto según tus necesidades
            self.air = True
            if n == 1:
                self.speed_x = +15
            else:
                self.speed_x = -15

    def update(self):
        self.x += self.speed_x
        self.speed_y += self.gravity
        if self.y + self.speed_y <= self.SCREEN_HEIGHT // 2 + 170 :
            self.y += self.speed_y
            self.air = False

    def desaceleration(self):
        self.speed_x -= 0.1 * self.speed_x



    
