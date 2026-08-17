import pygame
import consts
import screen
import game_field
from main import game_status


def find_soldier():
    field = game_field.field
    for i in range (consts.ROW_NUM):
        for j in range (consts.COLUMN_NUM):
            if field[i][j]["status"] == consts.SOLDIER:
                x,y = j, i
                game_field.field[i][j]["status"] = consts.EMPTY
                return x,y


def move_left():
    x,y = find_soldier()
    x -= 1
    print(x,y)
    return(x, y)



def move_right():
    x,y = find_soldier()
    x += 1
    print(x, y)
    return (x, y)


def move_up():
    x,y = find_soldier()
    y -= 1
    print(x, y)
    return (x, y)


def move_down():
    x,y = find_soldier()
    y += 1
    print(x, y)
    return (x, y)


def check_landmine(x,y):
    for i in range(consts.ROW_NUM):
        for j in range(consts.COLUMN_NUM):
            if game_field.field[i][j]["status"] == consts.LANDMINE:
                if x ==j and y == i:
                    return True #The soldier location is the same as the landmine location
    return False


def check_flag(x, y):
    for i in range(consts.ROW_NUM):
        for j in range(consts.COLUMN_NUM):
            if game_field.field[i][j]["status"] == consts.FLAG:
                if x ==j and y == i:
                    return True #The soldier location is the same as the flag location
    return False


def move_soldier(x,y):
    for i in range(consts.ROW_NUM):
        for j in range(consts.COLUMN_NUM):
            if (j, i) == (x, y):
                game_field.field[i][j]["status"] = consts.SOLDIER


def check_move(x, y):
    landmine = check_landmine(x, y)
    flag = check_flag(x, y)

    if landmine:
        return "LOSE"

    elif flag:
        return "WIN"

    else:
        #move_soldier(x,y)
        return "next"







