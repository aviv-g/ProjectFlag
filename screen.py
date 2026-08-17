import consts
import pygame

import game_field

screen = pygame.display.set_mode((consts.WINDOW_HEIGHT, consts.WINDOW_WIDTH))
screen.fill(consts.BLACK)


def start_message():
    font = pygame.font.SysFont("Arial", 20)
    text = font.render("Welcome to the flag game. \nHave fun!", True, consts.WHITE)
    screen.blit(text, (100, 100))
    pygame.display.update()


def soldier(x,y):
    image = pygame.image.load("soldier.png").convert_alpha()
    soldier = pygame.transform.scale(image, (consts.SQUARE_SIZE * 4, consts.SQUARE_SIZE * 4))
    screen.blit(soldier, (x * consts.SQUARE_SIZE, y * consts.SQUARE_SIZE))
    pygame.display.update()


def soldier_night(x, y):
    image = pygame.image.load("soldier_nigth.png").convert_alpha()
    soldier = pygame.transform.scale(image, (consts.SQUARE_SIZE * 4, consts.SQUARE_SIZE * 4))
    screen.blit(soldier, (x * consts.SQUARE_SIZE, y * consts.SQUARE_SIZE))


def place_soldier(field):
    for i in range (consts.ROW_NUM):
        for j in range (consts.COLUMN_NUM):
            if field[i][j]["status"] == consts.SOLDIER:
                soldier(i, j)


def place_landmine(landmine_list):
    image = pygame.image.load("mine.png").convert_alpha()
    landmine = pygame.transform.scale(image, (consts.SQUARE_SIZE*3, consts.SQUARE_SIZE))

    for i in range(len(landmine_list)):
        screen.blit(landmine, (landmine_list[i][0] * consts.SQUARE_SIZE, landmine_list[i][1] * consts.SQUARE_SIZE))
    pygame.display.update()



def create_field(landmine_list):
    screen.fill(consts.DARK_GREEN)
    for x in range(consts.SQUARE_SIZE, consts.WINDOW_WIDTH*2, consts.SQUARE_SIZE):
        pygame.draw.line(screen, consts.LINES_GREEN, (x, 0), (x, consts.WINDOW_HEIGHT))

    for y in range(consts.SQUARE_SIZE, consts.WINDOW_HEIGHT, consts.SQUARE_SIZE):
        pygame.draw.line(screen,consts.LINES_GREEN, (0, y), (consts.WINDOW_WIDTH*2, y))

    soldier_night(0, 0)
    place_landmine(landmine_list)

    pygame.display.flip()


def place_bush(bush_list):
    image = pygame.image.load("grass.png").convert_alpha()
    bush = pygame.transform.scale(image, (consts.SQUARE_SIZE * 3, consts.SQUARE_SIZE * 3))

    for i in range(len(bush_list)):
        screen.blit(bush, (bush_list[i][0] * consts.SQUARE_SIZE, bush_list[i][1] * consts.SQUARE_SIZE))


def place_flag():
    image = pygame.image.load("flag.png").convert_alpha()
    flag = pygame.transform.scale(image, (consts.SQUARE_SIZE * 4, consts.SQUARE_SIZE * 4))

    flag_x = game_field.field[consts.FLAG_INDEX[0][0]][consts.FLAG_INDEX[0][1]]["x"]
    flag_y = game_field.field[consts.FLAG_INDEX[0][0]][consts.FLAG_INDEX[0][1]]["y"]

    screen.blit(flag, (flag_x * consts.SQUARE_SIZE, flag_y * consts.SQUARE_SIZE))




def create_green_field(bush_list,x=0, y=0):
    screen.fill(consts.GRASS_GREEN)

    place_bush(bush_list)
    place_flag()
    soldier(x, y)

    pygame.display.flip()






#pygame.display.flip()
#pygame.time.delay(1000)