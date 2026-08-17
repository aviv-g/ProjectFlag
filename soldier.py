import pygame
import consts
import screen
import game_field

def soldier(x,y):
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
                soldier(i, j)

def find_soldier(field):
    for i in range (consts.ROW_NUM):
        for j in range (consts.COLUMN_NUM):
            if field[i][j]["status"] == consts.SOLDIER:
                soldier_location = (j, i)
    return soldier_location

def move_left(soldier_location):
    soldier_location[0] -= 1
    return soldier_location

def move_right(soldier_location):
    soldier_location[0] += 1
    return soldier_location

def move_up(soldier_location):
    soldier_location[1] -= 1
    return soldier_location

def move_down(soldier_location):
    soldier_location[1] += 1
    return soldier_location

def check_landmine(soldier_location):
    for i in range(consts.ROW_NUM):
        for j in range(consts.COLUMN_NUM):
            if game_field.field[i][j]["status"] == consts.LANDMINE:
                if soldier_location == (j, i):
                    return True #The soldier location is the same as the landmine location
    return False

def check_flag(soldier_location):
    for i in range(consts.ROW_NUM):
        for j in range(consts.COLUMN_NUM):
            if game_field.field[i][j]["status"] == consts.FLAG:
                if soldier_location == (j, i):
                    return True #The soldier location is the same as the flag location
    return False

def move_soldier(soldier_location):
    for i in range(consts.ROW_NUM):
        for j in range(consts.COLUMN_NUM):
            if (j, i) == soldier_location:
                game_field.field[i][j]["status"] = consts.SOLDIER
                soldier(j,i)







