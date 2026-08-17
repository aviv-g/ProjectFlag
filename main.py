import consts
import pygame
import screen
import soldier
import game_field


def user_events_mouse():
    global status
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move = "left"
                return move
            if event.key == pygame.K_RIGHT:
                move = "right"
                return move
            if event.key == pygame.K_UP:
                move = "up"
                return move
            if event.key == pygame.K_DOWN:
                move = "down"
                return move
            if event.key == pygame.K_RETURN:
                move = "enter"
                return move

status = True
game_status = consts.GAME

def main():
    pygame.init()
    landmine_list = game_field.search_landmine(game_field.field)
    bush_list = game_field.search_bushes(game_field.bush_field)

    while status:
        user_events_mouse()
        screen.create_green_field(bush_list)
        if  user_events_mouse() == "left":
            print(soldier.move_left())


        if user_events_mouse() == "right":
            print(soldier.move_right())

        if user_events_mouse() == "up":
            print(soldier.move_up())

        if user_events_mouse() == "down":
            print(soldier.move_down())

        if user_events_mouse() == "enter":
            screen.create_field(landmine_list)
            pygame.time.delay(1000)



main()
