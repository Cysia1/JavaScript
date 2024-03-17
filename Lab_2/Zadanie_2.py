import pygame
import math

pygame.init()
win = pygame.display.set_mode((600, 600))

pygame.display.set_caption("Litera Z")

# deklarowanie kolorów
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)
CZARNY = (0,0,0)


win.fill(CZARNY)
pygame.display.update()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        
        pygame.draw.rect(win, CZERWONY, (150, 100, 250, 250))
        pygame.draw.polygon(win,CZARNY,[(400,110),(170,330),(410,330)])
        pygame.draw.polygon(win,CZARNY,[(150,115),(360,115),(150,325)])


       





    pygame.display.update()