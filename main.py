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


def user_events_keyboard():
    global status
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print("here")
            if event.key == pygame.K_LEFT:
                x, y = soldier.move_left()
                print(x, y)
            elif event.key == pygame.K_RIGHT:
                x, y = soldier.move_right()
                print(x, y)
            elif event.key == pygame.K_UP:
                x, y = soldier.move_up()
                print(x, y)
            elif event.key == pygame.K_DOWN:
                x, y = soldier.move_down()
                print(x, y)
            elif event.key == pygame.K_RETURN:
                print("enter")


status = True


def main():
    pygame.init()
    landmine_list = game_field.search_landmine(game_field.field)
    print(landmine_list)


    while status:
        user_events_mouse()
        user_events_keyboard()



        screen.create_field(landmine_list)
        #soldier.move_soldier()


main()
