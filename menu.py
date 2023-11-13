import pygame
pygame.init()
#---- Fuente de texto ----
font = pygame.font.Font(None, 36)
#----------------------------------
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class menu:
    def __init__(self, SCREEN_HEIGHT, SCREEN_WIDTH, screen) -> None:
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.SCREEN_WIDTH =  SCREEN_WIDTH
        self.screen = screen
        self.fondo = pygame.image.load("img/pes.jpg").convert_alpha()
    def dibujar_fondo_menu(self):
        self.fondo = pygame.transform.scale(self.fondo, (1280, 720))
        self.screen.blit(self.fondo, (0, 0)) 

    def dibujar_botones(self, text, x, y, width, height, inactive_color, active_color):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(self.screen, active_color, (x, y, width, height))
            text_surface = font.render(text, True, BLACK)
            text_rect = text_surface.get_rect()
            text_rect.center = (x + width / 2, y + height / 2)
            self.screen.blit(text_surface, text_rect)
            if click[0] == 1:
                return True
        else:
            pygame.draw.rect(self.screen, inactive_color, (x, y, width, height))
            text_surface = font.render(text, True, BLACK)
            text_rect = text_surface.get_rect()
            text_rect.center = (x + width / 2, y + height / 2)
            self.screen.blit(text_surface, text_rect)
            return False
    
   
