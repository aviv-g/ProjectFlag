import consts
import pygame

screen = pygame.display.set_mode((consts.WINDOW_HEIGHT, consts.WINDOW_WIDTH))
screen.fill(consts.BLACK)

def soldier_draw():

    image = pygame.image.load("soldier.png").convert()
    soldier = pygame.transform.scale(image, (consts.SQUARE_X*4, consts.SQUARE_Y*2))
    screen.blit(soldier, (0, 0))
    pygame.display.update()

#pygame.display.flip()
#pygame.time.delay(1000)