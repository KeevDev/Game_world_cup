import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simulación de Pelota de Fútbol")

# Configuración de la pelota
ball_radius = 10
ball_color = (255, 0, 0)  # Rojo

# Posición y velocidad inicial de la pelota
ball_x, ball_y = width // 2, height - ball_radius
ball_speed_x, ball_speed_y = 0, 0

# Fuerza aplicada cuando se presiona una tecla
force = 10
gravity = 1

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Manejar eventos de teclado
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ball_speed_x = -force
            elif event.key == pygame.K_RIGHT:
                ball_speed_x = force
            elif event.key == pygame.K_UP:
                ball_speed_y = -force

        elif event.type == pygame.KEYUP:
            # Detener la pelota cuando se suelta la tecla
            ball_speed_x, ball_speed_y = 0, 0

    # Actualizar posición de la pelota
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Rebotar en los bordes
    if ball_x - ball_radius < 0:
        ball_x = ball_radius
        ball_speed_x = 0
    elif ball_x + ball_radius > width:
        ball_x = width - ball_radius
        ball_speed_x = 0

    # Simular la gravedad
    if ball_y + ball_radius < height:
        ball_speed_y += gravity
    else:
        ball_y = height - ball_radius
        ball_speed_y = 0

    # Limpiar la pantalla
    window.fill((255, 255, 255))  # Fondo blanco

    # Dibujar la pelota
    pygame.draw.circle(window, ball_color, (int(ball_x), int(ball_y)), ball_radius)

    # Actualizar la ventana
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.Clock().tick(30)
