import pygame
import consts
import screen

def soldier(x,y):
    image = pygame.image.load("soldier.png").convert_alpha()
    soldier = pygame.transform.scale(image, (100, 40))
    screen.blit(soldier, (x*consts.SQUARE_SIZE, y*consts.SQUARE_SIZE))
    pygame.display.update()

def soldier_night():
    image = pygame.image.load("soldier_night.png").convert_alpha()
    soldier = pygame.transform.scale(image, (100, 40))
    screen.blit(soldier, (0, 0))
    pygame.display.update()



def place_soldier(field):
    for i in range (consts.ROW_NUM):
        for j in range (consts.COLUMN_NUM):
            if field[i][j]["status"] == consts.SOLDIER:
                soldier(i, j)

