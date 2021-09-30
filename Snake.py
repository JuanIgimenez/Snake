import pygame
import sys
import random

#from pygame import*
def main():
    #inicio de ventana 
    pygame.init()
    #configuraciones de ventana
    ventana=pygame.display.set_mode((1000,600))
    pygame.display.set_caption("Snake")
    #colores
    c_ventana=((80,76,76))
    c_personaje=((126,216,64))
    c_comida=((239,232,22))
    #objetos visibles
    superficie1=pygame.Surface((1001,601))
    sup1=superficie1.get_rect()
    sup1.center=(500,300)
    #comida

    #personaje
    cabeza=pygame.Surface((34,34))
    cabeza_rect=cabeza.get_rect()
    cabeza_rect.center=(500,300)  
    while True:
        pygame.time.Clock().tick(100)
        #controles
        while True:
            tecla=pygame.key.get_pressed()
            if tecla[pygame.K_w]:
                cabeza_rect.y -=2.5
            if tecla[pygame.K_a]:
                cabeza_rect.x -=2.5           
            if tecla[pygame.K_d]:
                cabeza_rect.x +=2.5
            if tecla[pygame.K_s]:
                cabeza_rect.y +=2.5
       
        #salida
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  
        #coliciones borde
        if cabeza_rect.x>=966:
            cabeza_rect.x=5
        if cabeza_rect.x <=1:
            cabeza_rect.x=966
        if cabeza_rect.y <=1:
            cabeza_rect.y=565
        if cabeza_rect.y >=566:
            cabeza_rect.y=5
        #display
        ventana.blit(superficie1,sup1)
        superficie1.fill(c_ventana)
        superficie1.blit(cabeza,cabeza_rect)
        cabeza.fill(c_personaje)        
        pygame.display.update()
if __name__=="__main__":
    main()