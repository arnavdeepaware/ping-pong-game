import pygame
import random

#Dimensions for game window
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

#Colors used in the game: Black & White
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

def main():

    #Game Set up
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Play Pong!')

    #Player Paddles
    paddle_1 = pygame.Rect(30, 0, 7, 100)
    paddle_2 = pygame.Rect(SCREEN_WIDTH - 50, 0, 7, 100)

    #Player moves per frame
    paddle_1_move = 0
    paddle_2_move = 0

    #Game Ball
    ball = pygame.Rect(SCREEN_WIDTH/ 2, SCREEN_HEIGHT / 2, 25, 25)
    ball_accel_x = random.randint(2, 4) * 0.1
    ball_accel_y = random.randint(2, 4) * 0.1

    #Randomize Direction of the ball
    if random.randint(1, 2) == 1:
        ball_accel_x *= -1
    if random.randint(1, 2) == 1:
        ball_accel_y *= -1

    #GAME LOOP
    while True:
        screen.fill(COLOR_BLACK)

        #checking for events
        for event in pygame.event.get():

            #For every game event checks if the user quit at any instance
            if event.type == pygame.QUIT:
                return
    
        #Draws player 1 and player 2's paddle and the ball with white color
        pygame.draw.rect(screen, COLOR_WHITE, paddle_1)
        pygame.draw.rect(screen, COLOR_WHITE, paddle_2)
        pygame.draw.rect(screen, COLOR_WHITE, ball)

        #Update display
        pygame.display.update()


if __name__ == '__main__':
    main()