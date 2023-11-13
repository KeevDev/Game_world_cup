import pygame
import sys

# Inicializa Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animación del Jugador")

# Color de fondo
background_color = (255, 255, 255)

class PlayerAnimation:
    def __init__(self, idle_image_path, kick_images_path, x, y):
        self.idle_image = pygame.image.load(idle_image_path)
        self.kick_images = [pygame.image.load(path) for path in kick_images_path]
        self.current_frame = 0
        self.rect = self.idle_image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        # Actualizar la animación
        self.current_frame += 1
        if self.current_frame >= len(self.kick_images):
            self.current_frame = 0

    def draw(self, surface):
        # Limpiar el área ocupada por el jugador
        surface.fill(background_color, self.rect)

        # Dibujar la animación actual
        surface.blit(self.kick_images[self.current_frame], self.rect.topleft)

# Crear una instancia de PlayerAnimation
player = PlayerAnimation('img/idle.png', ['img/kick1.png', 'img/kick2.png', 'img/kick3.png'], 100, 100)

# Bucle principal
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar la pantalla
    screen.fill(background_color)

    # Actualizar y dibujar la animación del jugador
    player.update()
    player.draw(screen)

    pygame.display.flip()
    clock.tick(10)  # Ajusta la velocidad de la animación según sea necesario

pygame.quit()
sys.exit()
