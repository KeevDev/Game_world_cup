import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simulación de Movimiento Rectilíneo Uniforme con Gravedad")

# Configuración del objeto
object_width, object_height = 50, 50
object_color = (0, 0, 255)  # Azul

# Posición y velocidad inicial del objeto
object_x, object_y = width // 2 - object_width // 2, height // 2 - object_height // 2
object_speed_x, object_speed_y = 5, 0
gravity = 0.5

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualizar posición del objeto
    object_x += object_speed_x
    object_speed_y += gravity
    object_y += object_speed_y

    # Si el objeto sale de la ventana, reiniciar su posición
    if object_x > width or object_y > height:
        object_x = -object_width
        object_speed_y = 0
        object_y = height // 2 - object_height // 2

    # Limpiar la pantalla
    window.fill((255, 255, 255))  # Fondo blanco

    # Dibujar el objeto
    pygame.draw.rect(window, object_color, (object_x, int(object_y), object_width, object_height))

    # Actualizar la ventana
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.Clock().tick(30)
