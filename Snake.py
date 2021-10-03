import pygame
import sys
import random
def comida():
    comida_pos = [random.randint(0,32)*30, random.randint(0,19)*30]
    return comida_pos
#from pygame import*
def main():
    #inicio de ventana 
    pygame.init()
    #configuraciones de ventana
    ventana=pygame.display.set_mode((1000,600))
    pygame.display.set_caption("Snake")
    #colores variables
    c_ventana=((80,76,76))
    c_personaje=((126,216,64))
    c_comida=((239,232,22))
    #objetos visibles
    superficie1=pygame.Surface((1001,601))
    sup1=superficie1.get_rect()
    sup1.center=(500,300)

    cuerpo_pos=[100,50]
    cuerpo=[[100,50]]

    direccion="RIGHT"
    cambio=direccion

    comida_pos=comida()
    while True:
        #velocidad del programa
        pygame.time.Clock().tick(30)
        #salida
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        cambio= "RIGHT"
                    if event.key == pygame.K_LEFT:
                        cambio= "LEFT"
                    if event.key == pygame.K_UP:
                        cambio= "UP"
                    if event.key == pygame.K_DOWN:
                        cambio= "DOWN"

        if cambio == "RIGHT" and direccion != "LEFT":
            direccion = "RIGHT"
        if cambio == "LEFT" and direccion != "RIGHT":
            direccion = "LEFT"
        if cambio == "UP" and direccion != "DOWN":
            direccion = "UP"
        if cambio == "DOWN" and direccion != "UP":
            direccion = "DOWN"

        if direccion == "RIGHT":
            cuerpo_pos[0] += 10
        if direccion == "LEFT":
            cuerpo_pos[0] -= 10
        if direccion == "UP":
            cuerpo_pos[1] -= 10
        if direccion == "DOWN":
            cuerpo_pos[1] += 10
        cuerpo.insert(0, list(cuerpo_pos))
        if cuerpo_pos == comida_pos:
            comida_pos = comida()
        #else:
            #cuerpo.pop() 
        #coliciones borde
        if cuerpo_pos[0] <=1:
            cuerpo_pos[0]=965
        if cuerpo_pos[0] >=966:
            cuerpo_pos[0]=3       
        if cuerpo_pos[1] <=1:
            cuerpo_pos[1]=565
        if cuerpo_pos[1] >=566:
            cuerpo_pos[1]=5

        #display
        ventana.blit(superficie1,sup1)
        superficie1.fill(c_ventana)
        for pos in cuerpo:
            pygame.draw.rect(superficie1,c_personaje, pygame.Rect(pos[0], pos[1], 30, 30))
        
        pygame.draw.rect(superficie1, (255,160,60), pygame.Rect(comida_pos[0], comida_pos[1], 30, 30))
        pygame.display.update()

if __name__=="__main__":
    main()