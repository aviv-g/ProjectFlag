import consts
import pygame
import screen



def user_events_mouse():
    global status
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left")
            if event.key == pygame.K_RIGHT:
                print("right")
            if event.key == pygame.K_UP:
                print("up")
            if event.key == pygame.K_DOWN:
                print("down")
            if event.key == pygame.K_RETURN:
                print("enter")

status = True


def main():
    pygame.init()


    while status:
        user_events_mouse()
        screen.soldier()

main()
