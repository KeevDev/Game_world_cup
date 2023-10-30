import pygame
import sys
from menu import menu
from character import Player
from ball import Ball
#---- INICIALIZANDO PYGAME-----
pygame.init()
pygame.mixer.init()
#------------------------------

#----------- Plantillas -------------------------
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
#------------------------------------


#---- Nombre ventana ----------------
pygame.display.set_caption("PRO EVOLUTION SOCCER")
#---------------------------------------------------

#----- configuraciones -----------------
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
reloj = pygame.time.Clock()
font = pygame.font.Font(None, 36)
sonido1 = pygame.mixer.Sound("Sounds/2.wav")
sonido1.set_volume(0.3)
#-------------------------------------------------------------------------

#----inicializando OBJETOS----
player1 = Player(60, SCREEN_HEIGHT // 2 + 10)
player2 = Player(SCREEN_WIDTH-120, SCREEN_HEIGHT // 2 + 10)
ball = Ball(SCREEN_WIDTH,SCREEN_HEIGHT,280,300)
opciones = menu(SCREEN_WIDTH,SCREEN_HEIGHT,screen)
#----------------------------------------------------------------

#-------- variables----------
inicio = False  # Para luego ver que opcion se eligio
instrucciones = False
#---------------------------------------------------------

button_rect1 = pygame.Rect(200, 250, 200, 40) #ubicar el tamaño de los cuadros para los clicks
button_rect2 = pygame.Rect(200, 300, 200, 40)

while True:
    pygame.mixer.Sound.play(sonido1)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                if button_rect1.collidepoint(x, y):
                    inicio = True
                elif button_rect2.collidepoint(x, y):
                    instrucciones = True
                
        if event.type == pygame.KEYDOWN:
            # ----Jugador 1----
            if event.key == pygame.K_a:  
                player1.speed = -4
            if event.key == pygame.K_d:  
                player1.speed = 4
            if event.key == pygame.K_w:
                if player1.y >= SCREEN_HEIGHT // 2 + 10:
                    player1.jump()

            # ----Jugador 2----
            if event.key == pygame.K_LEFT: 
                player2.speed = -4
            if event.key == pygame.K_RIGHT: 
                player2.speed = 4
            if event.key == pygame.K_UP:
                if player2.y >= SCREEN_HEIGHT // 2 + 10:
                    player2.jump()

        if event.type == pygame.KEYUP:
            # Jugador 1
            if event.key == pygame.K_a:
                player1.speed = 0
            if event.key == pygame.K_d:
                player1.speed = 0
            # Jugador 2
            if event.key == pygame.K_LEFT:
                player2.speed = 0
            if event.key == pygame.K_RIGHT:
                player2.speed = 0
                
    opciones.dibujar_fondo_menu() # BACKGROUND

    ''' MENSAJE TITULO DE PANTALLA
    text = 'FUTBOLITO'
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.center = (SCREEN_WIDTH / 2, 50)
    screen.blit(text_surface, text_rect)
    '''


    opciones.dibujar_botones("START", 200, 250, 200, 40, WHITE, BLUE)
    opciones.dibujar_botones("Instrucciones", 200, 300, 200, 40, WHITE, BLUE)



    #---------limites--------------
    player1.movimiento(SCREEN_HEIGHT)
    player2.movimiento(SCREEN_HEIGHT)
    if ball.x < 20 or ball.x > 550: #GOOOOOL
        ball.speed_x = 0
    if player1.x < 40:
        player1.x += 5
    if player2.x > 510:
        player2.x -= 5




    if inicio:
        screen.fill(WHITE)
        #GRAFICOS
        #-----fondo-------
        fondo = pygame.image.load("img/cancha.jpg").convert_alpha()
        fondo = pygame.transform.scale(fondo, (600, 400))
        screen.blit(fondo, (0, 0))
        LineaMitad = pygame.draw.rect(screen, WHITE, (298, 225, 4, 600))
        #-------------------------------------------------------
        
        #----BALON---------
        img_ball = pygame.image.load("img/bola.png")
        img_ball = pygame.transform.scale(img_ball, (30, 30))
        bola = img_ball.get_rect()
        bola.topleft = (ball.x,ball.y)
        screen.blit(img_ball, (ball.x,ball.y))
        #------------------------------------------------------------


        #----ARCOS----
        imgarc_izq = pygame.image.load('img/arco1.png')
        imgarc_der = pygame.image.load('img/arco2.png')
        imgarc_izq = pygame.transform.scale(imgarc_izq, (80, 165))
        imgarc_der = pygame.transform.scale(imgarc_der, (80, 165))
        arco_izq = imgarc_izq.get_rect()
        arco_der = imgarc_der.get_rect()
        screen.blit(imgarc_izq, (0,183))
        screen.blit(imgarc_der, (520,183))
        
        #------jugadores---------
        imagen_jugador1 = pygame.image.load("img/jugador1.png")
        imagen_jugador2 = pygame.image.load("img/jugador2.png")
        imagen_jugador1 = pygame.transform.scale(imagen_jugador1, (51, 113))
        imagen_jugador2 = pygame.transform.scale(imagen_jugador2, (51, 113))

        jugador1 = imagen_jugador1.get_rect()
        jugador2 = imagen_jugador2.get_rect()
        jugador1.topleft = (player1.x,player1.y)
        jugador2.topleft = (player2.x, player2.y)


        screen.blit(imagen_jugador1, (player1.x,player1.y+10))
        screen.blit(imagen_jugador2, (player2.x,player2.y+10))
        #-------------------------------------------------------

        # ------------------------------------------------------------------------------------
        ball.update()
        if jugador1.colliderect(arco_izq):
            player1.x += 5
        if jugador2.colliderect(arco_der):
            player2.x -= 5
        if jugador1.colliderect(bola) or jugador2.colliderect(bola):
            ball.speed_x *= -1
            ball.x += (ball.speed_x)*2

        if ball.speed_x == 0:
            ball.x = 280
            ball.y = 300
            ball.speed_x = 3



        pygame.display.flip()

    elif instrucciones:
        print("estoy mamado")

    pygame.display.flip()
    reloj.tick(60)



