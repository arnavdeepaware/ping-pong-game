import pygame
import random

#Dimensions for game window
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

#Colors used in the game: Black & White
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (255, 255, 255)

def main():

    #Game Set up
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Play Pong!')

    #GAME LOOP
    while True:
        screen.fill(COLOR_BLACK)

        #checking for events
        for event in pygame.event.get():

            #For every game event checks if the user quit at any instance
            if event.type == pygame.QUIT():
                return