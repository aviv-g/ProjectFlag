import consts
import pygame


screen = pygame.display.set_mode((consts.WINDOW_HEIGHT, consts.WINDOW_WIDTH))
screen.fill(consts.BLACK)


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

def place_landmine(x,y):
    image = pygame.image.load("mine.png").convert()
    landmine = pygame.transform.scale(image, (consts.SQUARE_SIZE*3, consts.SQUARE_SIZE))
    screen.blit(landmine, (x, y))
    pygame.display.update()

def create_field():
    for x in range(consts.SQUARE_SIZE, consts.WINDOW_WIDTH*2, consts.SQUARE_SIZE):
        pygame.draw.line(screen, consts.GREEN, (x, 0), (x, consts.WINDOW_HEIGHT))

    for y in range(consts.SQUARE_SIZE, consts.WINDOW_HEIGHT, consts.SQUARE_SIZE):
        pygame.draw.line(screen,consts.GREEN, (0, y), (consts.WINDOW_WIDTH*2, y))




#pygame.display.flip()
#pygame.time.delay(1000)