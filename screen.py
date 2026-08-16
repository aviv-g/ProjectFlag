import consts
import pygame

screen = pygame.display.set_mode((consts.WINDOW_HEIGHT, consts.WINDOW_WIDTH))
screen.fill(consts.BLACK)

def soldier():
    image = pygame.image.load("soldier.png").convert()
    soldier = pygame.transform.scale(image, (100, 40))
    screen.blit(soldier, (100, 100))
    pygame.display.update()


#pygame.display.flip()
#pygame.time.delay(1000)