import pygame
import sys
from game_scripts.menu import menu
from game_scripts.character import Player
from game_scripts.ball import Ball
#---- INICIALIZANDO PYGAME-----

pygame.init()
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=40)

#------------------------------

#----------- Plantillas -------------------------
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
#------------------------------------


#---- Nombre ventana ----------------
pygame.display.set_caption("Human Vs Zombie Cup")
#---------------------------------------------------

#----- configuraciones -----------------
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
reloj = pygame.time.Clock()
font = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None, 42)
gol_text = pygame.font.Font(None, 60)
sonido1 = pygame.mixer.Sound("Sources/Sounds/2.wav")
sonido1.set_volume(0.3)
sonido2 = pygame.mixer.Sound("Sources/Sounds/estadio.wav")
sonido2.set_volume(0.3)
sonido3 = pygame.mixer.Sound("Sources/Sounds/gol.wav")
#-------------------------------------------------------------------------

#----inicializando OBJETOS----
player1 = Player(125, SCREEN_HEIGHT // 2 + 60,1)
player2 = Player(SCREEN_WIDTH-210, SCREEN_HEIGHT // 2 + 60,2)
ball = Ball(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_WIDTH//2-20,SCREEN_HEIGHT // 2 + 170)
opciones = menu(SCREEN_WIDTH,SCREEN_HEIGHT,screen)

#----------------------------------------------------------------

#-------- variables----------
inicio = False  # Para luego ver que opcion se eligio
instrucciones = False
button_rect1 = pygame.Rect(500, 400, 300, 60) #ubicar el tamaño de los cuadros para los clicks
button_rect2 = pygame.Rect(500, 400, 300, 60)
gol = False
marcador1 =0
marcador2 =0
minutos =0
segundos=0
milisegundos=0
pateo, pateo2 = False, False

index, index2 = 0, 0
espera = 0
#---------------------------------------------------------

while True:
    #pygame.mixer.Sound.play(sonido1)
    keys = pygame.key.get_pressed()
    time_inicio = pygame.time.get_ticks()//1000
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
                player1.speed_x = -4
            if event.key == pygame.K_d:
                player1.speed_x = 4
            if event.key == pygame.K_w:
                if player1.y >= SCREEN_HEIGHT // 2 +40:
                    player1.jump()
            if event.key == pygame.K_SPACE:
                pateo = True
                '''Aqui va cuando se aprete para la patada
                    debe contener aqui los sprites y las colisiones
                    con la pelota para poder hacer el efecto del
                    movimiento
                '''

            # ----Jugador 2----
            if event.key == pygame.K_LEFT:
                player2.speed_x = -4
            if event.key == pygame.K_RIGHT:
                player2.speed_x = 4
            if event.key == pygame.K_UP:
                if player2.y >= SCREEN_HEIGHT // 2+40: #LIMITE DEL SALTO
                    player2.jump()
            if event.key == pygame.K_RETURN:
                pateo2 = True

        if event.type == pygame.KEYUP:
            # Jugador 1
            if event.key == pygame.K_a:
                player1.speed_x = 0
            if event.key == pygame.K_d:
                player1.speed_x = 0
            # Jugador 2
            if event.key == pygame.K_LEFT:
                player2.speed_x = 0
            if event.key == pygame.K_RIGHT:
                player2.speed_x = 0

    opciones.dibujar_fondo_menu() # BACKGROUND
    opciones.dibujar_botones("START", 500, 400, 300, 60, WHITE, BLUE)
    opciones.dibujar_botones("Instrucciones", 500, 490, 300, 60, WHITE, BLUE)

    if inicio:
        screen.fill(WHITE)
        #sonido1.stop()
        #sonido2.play()

        #GRAFICOS
        #-----fondo-------
        fondo = pygame.image.load("Sources/img/cancha.jpg").convert_alpha()
        fondo = pygame.transform.scale(fondo, (1280, 720))
        screen.blit(fondo, (0, 0))
        LineaMitad = pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2+45, 4, 600))
        #-------------------------------------------------------

        #----BALON---------
        ball.update()
        img_ball = pygame.image.load("Sources/img/bola.png")
        img_ball = pygame.transform.scale(img_ball, (40, 40))
        bola = img_ball.get_rect()
        bola.topleft = (ball.x,ball.y)
        screen.blit(img_ball, (ball.x,ball.y))

        #------------------------------------------------------------

        #----ARCOS----
        imgarc_izq = pygame.image.load('Sources/img/arco1.png')
        imgarc_der = pygame.image.load('Sources/img/arco2.png')
        imgarc_izq = pygame.transform.scale(imgarc_izq, (160, 265))
        imgarc_der = pygame.transform.scale(imgarc_der, (160, 265))
        arco_izq = imgarc_izq.get_rect()
        arco_der = imgarc_der.get_rect()
        screen.blit(imgarc_izq, (0,320))
        screen.blit(imgarc_der, (SCREEN_WIDTH-160,320))



        #-------------marcador------------
        marcador_img = pygame.image.load('Sources/img/marcador.png')
        marcador_img = pygame.transform.scale(marcador_img, (600, 120))
        screen.blit(marcador_img, (SCREEN_WIDTH//2-310,0))

        text_marcador = f'{player1.marcador} - {player2.marcador}'
        text_surface_marcador = font2.render(text_marcador, True, WHITE)
        text_rect_marcador = text_surface_marcador.get_rect()
        text_rect_marcador.center = (SCREEN_WIDTH / 2, 50)
        screen.blit(text_surface_marcador, ((SCREEN_WIDTH//2)-35,40))

        #-----------time------------------

        if time_inicio:
            milisegundos +=1
        if milisegundos % 60 == 0:
            segundos+=1
            milisegundos = 0
            
        if segundos == 60:
            minutos+=1
            segundos = 0
        if segundos < 10:
            cero = 0
        else:
            cero = ""
        # CONTADOR TIME
        text_time = f'TIME   {minutos}: {cero}{segundos}'
        text_surface_time = font2.render(text_time, True, WHITE)
        text_rect_time = text_surface_time.get_rect()
        text_rect_time.center = (SCREEN_WIDTH / 2, 50)
        screen.blit(text_surface_time, ((SCREEN_WIDTH//2-25)-54,92))

        # MENSAJE DE GOL
        if gol is True:
            #sonido3.play()
            if segundos:
                espera +=1
                if espera !=50:
                    text = 'GOOOL'
                    text_surface = gol_text.render(text, True, WHITE)
                    text_rect = text_surface.get_rect()
                    text_rect.center = (SCREEN_WIDTH / 2, 50)
                    screen.blit(text_surface, ((SCREEN_WIDTH//2)-70,150))
                else:
                    #sonido3.stop()
                    espera =0
                    gol = False
            

        #------jugadores---------
        if pateo == False:
            player1.draw(screen,0)
        if pateo2 == False:
            player2.draw(screen,0)
        #-------------------------------------------------------


        #---------actualizaciones_movimientos & limites--------------

        player1.update(SCREEN_HEIGHT)
        player2.update(SCREEN_HEIGHT)

        #LIMITE SI EL BALON ENTRA EN EL PRIMER ARCO
        if ball.x < 130 and bola.y >= 320: #GOOOOOL
            ball.speed_x = 0
            gol = True
            player2.marcador +=1
        #LIMITE SI EL BALON ENTRA EN EL SEGUNDO ARCO
        if ball.x > 1220 and bola.y >= 320:
            ball.speed_x = 0
            gol = True
            player1.marcador +=1
        #LIMITES CON LOS ARCOS
        if player1.x < 100:
            player1.x += 5
        if player2.x > 1100:
            player2.x -= 5
       
        if ball.x < 128 and bola.y < 320 or bola.x > SCREEN_WIDTH: 
            ball.speed_x *= -1
            ball.x += 15
            ball.y -= 15

        if ball.x > 1222 and bola.y < 320 or bola.x < 0: 
            ball.speed_x *= -1
            ball.x -= 15
            ball.y -= 15

        if player1.jugador.colliderect(bola) or player2.jugador.colliderect(bola):
            ball.speed_x *= -1
            ball.x += ball.speed_x* 2
            ball.desaceleration()
            #Si colisiona que la velocidad sea 0 para pararlo
            #y ya dentro de la patada si pueda mandarlo

        if player1.jugador.colliderect(bola) and pateo == True:
            ball.ball_air(1) 
            ball.desaceleration()
        if player2.jugador.colliderect(bola) and pateo2 == True:
            ball.ball_air(2) 
            ball.desaceleration()  

        if gol == True:
            ball.x = SCREEN_WIDTH//2-20
            ball.y = SCREEN_HEIGHT // 2 + 170
            player1.x = 125
            player1.y = SCREEN_HEIGHT // 2 + 60
            player2.x = SCREEN_WIDTH-210
            player2.y = SCREEN_HEIGHT // 2 + 60
            ball.speed_x = 5

        if index>4:
            index=0
            pateo = False
        if pateo == True:
            if milisegundos:
                index += 1
                player1.kick(screen,index)
                pygame.display.flip()
                
        if index2>4:
            index2=0
            pateo2 = False
        if pateo2 == True:
            if milisegundos:
                index2 += 1
                player2.kick(screen,index2)     
                pygame.display.flip()
                


        pygame.display.flip()

    elif instrucciones:
        instrucciones = pygame.image.load("img/instrucciones.jpg")
        screen.blit(instrucciones, (0, 0))

    pygame.display.flip()
    reloj.tick(60)
 



