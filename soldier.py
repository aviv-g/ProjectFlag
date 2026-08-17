import pygame
import consts
import screen
import game_field

"""def soldier(x,y):
    image = pygame.image.load("soldier.png").convert_alpha()
    soldier = pygame.transform.scale(image, (100, 40))
    screen.blit(soldier, (x*consts.SQUARE_SIZE, y*consts.SQUARE_SIZE))
    pygame.display.update()

def soldier_night():
    image = pygame.image.load("soldier_nigth.png").convert_alpha()
    soldier = pygame.transform.scale(image, (100, 40))
    screen.blit(soldier, (0, 0))
    pygame.display.update()



def place_soldier(field):
    for i in range (consts.ROW_NUM):
        for j in range (consts.COLUMN_NUM):
            if field[i][j]["status"] == consts.SOLDIER:
                soldier(i, j)"""


def find_soldier():
    field = game_field.field
    for i in range (consts.ROW_NUM):
        for j in range (consts.COLUMN_NUM):
            if field[i][j]["status"] == consts.SOLDIER:
                x,y = j, i
                return x,y


def move_left():
    x,y = find_soldier()
    x -= 1
    print(x,y)
    return x,y


def move_right():
    x,y = find_soldier()
    x += 1
    print(x, y)
    return x,y


def move_up():
    x,y = find_soldier()
    y -= 1
    print(x, y)
    return x,y


def move_down():
    x,y = find_soldier()
    y += 1
    print(x, y)
    return x,y


def check_landmine(x,y):
    for i in range(consts.ROW_NUM):
        for j in range(consts.COLUMN_NUM):
            if game_field.field[i][j]["status"] == consts.LANDMINE:
                if x ==j and y == i:
                    return True #The soldier location is the same as the landmine location
    return False


def check_flag(soldier_location):
    for i in range(consts.ROW_NUM):
        for j in range(consts.COLUMN_NUM):
            if game_field.field[i][j]["status"] == consts.FLAG:
                if x ==j and y == i:
                    return True #The soldier location is the same as the flag location
    return False


def move_soldier(x,y):

    for i in range(consts.ROW_NUM):
        for j in range(consts.COLUMN_NUM):
            if (j, i) == soldier_location:
                game_field.field[i][j]["status"] = consts.SOLDIER
                soldier(j,i)







