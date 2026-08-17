import consts
import pygame
import screen
import soldier
import game_field

status = True
keypad = {"pressed": False, "key" : "none"}

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
    location = (0, 0)

    while status:
        game_status = consts.GAME
        while game_status == consts.GAME:
            user_events_mouse()
            #screen.start_message()
            screen.create_green_field(bush_list, location)

            if keypad["pressed"]:
                if keypad["key"] == "left":
                    game_status, location = soldier.left(location)

                if keypad["key"] == "right":
                    game_status, location = soldier.right(location)

                if keypad["key"] == "up":
                    game_status, location = soldier.up(location)

                if keypad["key"] == "down":
                    game_status, location = soldier.down(location)

                if keypad["key"] == "enter":
                    screen.create_field(landmine_list, location)
                    pygame.time.delay(1000)

            keypad["pressed"] = False
            keypad["key"] = "none"


        if game_status == consts.WIN:
            print("Win")
        else:
            print("Lose")

        #screen.create_green_field(bush_list)


main()
