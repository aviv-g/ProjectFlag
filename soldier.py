import pygame
import consts
import screen
import game_field


def find_soldier():
    field = game_field.field
    for i in range (len(field)):
        for j in range (len(field[i])):
            if field[i][j]["status"] == consts.SOLDIER:
                game_field.field[i][j]["status"] = consts.EMPTY
                return j,i


def check_move(x, y):
    landmine = check_landmine(x, y)
    flag = check_flag(x, y)

    if landmine:
        game_status = consts.LOSE

    elif flag:
        game_status = consts.WIN

    else:
        move_soldier(x,y)
        game_status = consts.GAME

    return game_status, (x, y)


def in_frame(x, y):
    if (0 <= x <= 50 - 3) and (0 <= y <= 25 - 4):
        return True
    return False

def left(location):
    x = location[0]
    y = location[1]
    x_new = x - 1

    if in_frame(x_new, y):
        return check_move(x_new, y)
    return check_move(x, y)




def right(location):
    x = location[0]
    y = location[1]
    x_new = x + 1

    if in_frame(x_new, y):
        return check_move(x_new, y)
    return check_move(x, y)


def up(location):
    x = location[0]
    y = location[1]
    y_new = y - 1

    if in_frame(x, y_new):
        return check_move(x, y_new)
    return check_move(x, y)


def down(location):
    x = location[0]
    y = location[1]
    y_new = y + 1

    if in_frame(x, y_new):
        return check_move(x, y_new)
    return check_move(x, y)


def check_landmine(x,y):
    legs_index = [(y + 4, x), (y + 4, x + 1)]
    for i in range(len(game_field.field)):
        for j in range(len(game_field.field[i])):
            if game_field.field[i][j]["status"] == consts.LANDMINE:
                if (i, j) in legs_index:
                    return True #The soldier location is the same as the landmine location
    return False


def check_flag(x, y):
    body_index = [(y, x), (y, x + 1), (y + 1, x), (y + 1, x + 1)]
    field = game_field.field
    for i in range(len(field)):
        for j in range(len(field[i])):
            if game_field.field[i][j]["status"] == consts.FLAG:
                if (i, j) in body_index:
                    return True #The soldier location is the same as the flag location
    return False


def move_soldier(x,y):
    for i in range(consts.ROW_NUM):
        for j in range(consts.COLUMN_NUM):
            if (j, i) == (x, y):
                game_field.field[i][j]["status"] = consts.SOLDIER












