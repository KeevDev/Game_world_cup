import pygame

class Ball():
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT,x, y):
        self.x = x
        self.y = y
        self.speed_x = 3
        self.speed_y = 0
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
  
    def update(self):
        self.x += self.speed_x





    
