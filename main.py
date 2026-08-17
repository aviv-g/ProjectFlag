import consts
import pygame
import screen
import soldier
import game_field

status = True
keypad = {"pressed": False, "key" : "none"}

game_status = consts.GAME

def user_events_mouse():
    global status
    global keypad
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False
        if event.type == pygame.KEYDOWN:
            keypad["pressed"] = True
            recognize_key(event)


def recognize_key(event):
    global keypad
    if event.key == pygame.K_LEFT:
        keypad["key"] = "left"
    if event.key == pygame.K_RIGHT:
        keypad["key"] = "right"
    if event.key == pygame.K_UP:
        keypad["key"] = "up"
    if event.key == pygame.K_DOWN:
        keypad["key"] = "down"
    if event.key == pygame.K_RETURN:
        keypad["key"] = "enter"


def main():
    pygame.init()
    landmine_list = game_field.search_landmine(game_field.field)
    bush_list = game_field.search_bushes(game_field.bush_field)

    while status:
        user_events_mouse()
        screen.create_green_field(bush_list)

        if keypad["pressed"]:
            if keypad["key"] == "left":
                print(soldier.move_left())

            if keypad["key"] == "right":
                print(soldier.move_right())

            if keypad["key"] == "up":
                print(soldier.move_up())

            if keypad["key"] == "down":
                print(soldier.move_down())

            if keypad["key"] == "enter":
                screen.create_field(landmine_list)
                pygame.time.delay(1000)

            keypad["pressed"] = False

        #screen.create_green_field(bush_list)


main()
