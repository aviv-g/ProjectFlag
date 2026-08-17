import consts
import pygame
import screen
import soldier
import game_field


def user_events_mouse(soldier_location):
    global status
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                soldier.move_left(soldier_location)
            if event.key == pygame.K_RIGHT:
                soldier.move_right(soldier_location)
            if event.key == pygame.K_UP:
                soldier.move_up(soldier_location)
            if event.key == pygame.K_DOWN:
                soldier.move_down(soldier_location)
            if event.key == pygame.K_RETURN:
                print("enter")

status = True


def main():
    pygame.init()


    while status:


        soldier_location = soldier.find_soldier(game_field.field)
        new_soldier_location = user_events_mouse()

        print(new_soldier_location)
        if soldier.check_landmine(new_soldier_location) == False and soldier.check_flag(soldier_location) == False:
            soldier.move_soldier(new_soldier_location)

        screen.create_field()
        game_field.clear_field()
        #screen.place_soldier(game_field.field)
        #screen.place_landmine(20, 30)



main()
