import pygame
import sys
import random
def comida():
    comida_pos = [random.randint(0,19)*20, random.randint(0,23)*20]
    return comida_pos
#from pygame import*
def main():
    #inicio de ventana 
    pygame.init()
    #configuraciones de ventana
    ventana=pygame.display.set_mode((400,480))
    pygame.display.set_caption("Snake")
    #colores variables
    c_ventana=((80,76,76))
    c_personaje=((126,216,64))
    c_comida=((239,232,22))
    #objetos visibles
    superficie1=pygame.Surface((400,480))
    sup1=superficie1.get_rect()
    sup1.center=(200,240)

    cuerpo_pos=[20,20]
    cuerpo=[[20,20]]

    direccion="RIGHT"
    cambio=direccion

    comida_pos=comida()
    while True:
        #velocidad del programa
        pygame.time.Clock().tick(7)
        #salida
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        cambio= "RIGHT"
                    if event.key == pygame.K_a:
                        cambio= "LEFT"
                    if event.key == pygame.K_w:
                        cambio= "UP"
                    if event.key == pygame.K_s:
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
            cuerpo_pos[0] += 20
        if direccion == "LEFT":
            cuerpo_pos[0] -= 20
        if direccion == "UP":
            cuerpo_pos[1] -= 20
        if direccion == "DOWN":
            cuerpo_pos[1] += 20
        cuerpo.insert(0, list(cuerpo_pos))
        if cuerpo_pos == comida_pos:
            comida_pos = comida()
        else:
            cuerpo.pop() 
        #coliciones borde
        if cuerpo_pos[0] <=0:
            cuerpo_pos[0]=380
        if cuerpo_pos[0] >=380:
            cuerpo_pos[0]=0       
        if cuerpo_pos[1] <=0:
            cuerpo_pos[1]=460
        if cuerpo_pos[1] >=460:
            cuerpo_pos[1]=0

        #display
        ventana.blit(superficie1,sup1)
        superficie1.fill(c_ventana)
        for pos in cuerpo:
            pygame.draw.rect(superficie1,c_personaje, pygame.Rect(pos[0], pos[1], 20, 20))
        
        pygame.draw.rect(superficie1, (255,160,60), pygame.Rect(comida_pos[0], comida_pos[1], 20, 20))
        pygame.display.update()

if __name__=="__main__":
    main()