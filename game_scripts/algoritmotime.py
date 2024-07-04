import pygame
pygame.init() 
    
n = False
tiemponuevo=0
while True:
    tiempoaqui= pygame.time.get_ticks()//1000
    if tiempoaqui == 5:
        n = True

    if n == True:
        tiempoafuera = pygame.time.get_ticks()//1000
        time = tiempoaqui-tiempoafuera
        if tiempoafuera:
            tiemponuevo +=1
        print(f'{tiempoaqui} == {tiempoafuera} --- {tiemponuevo//1000}')
    
        