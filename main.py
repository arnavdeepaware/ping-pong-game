import pygame
import random
import asyncio

#Dimensions for game window
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

#Colors used in the game: Black & White
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

async def main():

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

    #Clock Object
    clock = pygame.time.Clock()
    started = False

    #GAME LOOP
    while True:
        screen.fill(COLOR_BLACK)
        await asyncio.sleep(0)

        if not started:
            
            font = pygame.font.SysFont('Consolas', 30)

            #Draw some starter text for the game
            text = font.render('Press Space to Start', True, COLOR_WHITE)
            text_rect = text.get_rect()
            text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            screen.blit(text, text_rect)

            pygame.display.flip()
            await asyncio.sleep(0)

            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        started = True
            await asyncio.sleep(0)
            continue

        delta_time = clock.tick(60)

        #checking for events
        for event in pygame.event.get():

            #For every game event checks if the user quit at any instance
            if event.type == pygame.QUIT:
                return

            #User presses a keydown
            if event.type == pygame.KEYDOWN:
                
                #Player 1
                if event.key == pygame.K_w: #Goes Up
                    paddle_1_move = -0.5
                elif event.key == pygame.K_s: #Goes Down
                    paddle_1_move = 0.5

                #Player 2
                if event.key == pygame.K_UP:
                    paddle_2_move = -0.5
                elif event.key == pygame.K_DOWN:
                    paddle_2_move = 0.5
                
            # if the player released a key
            if event.type == pygame.KEYUP:
                # if the key released is w or s, stop the movement of paddle_1
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    paddle_1_move = 0.0

                # if the key released is the up or down arrow, stop the movement of paddle_2
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    paddle_2_move = 0.0
        
        #Paddle Movements            
        paddle_1.top += paddle_1_move * delta_time
        paddle_2.top += paddle_2_move * delta_time

        #Ensuring Paddle Stays Within Bounds
        if paddle_1.top < 0:
            paddle_1.top = 0
        if paddle_1.bottom > SCREEN_HEIGHT:
            paddle_1.bottom = SCREEN_HEIGHT

        if paddle_2.top < 0:
            paddle_2.top = 0
        if paddle_2.bottom > SCREEN_HEIGHT:
            paddle_2.bottom = SCREEN_HEIGHT
        
        #Ball Movements
        if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
            return  #End game if ball touches the sides
        
        #Top / Bottom 
        if ball.top < 0:
            ball_accel_y *= -1
            ball.top = 0
        if ball.bottom > SCREEN_HEIGHT - ball.height:
            ball_accel_y *= -1
            ball.bottom = SCREEN_HEIGHT - ball.height

        #If ball collides with the paddle
        if paddle_1.colliderect(ball) and paddle_1.left < ball.left:
            ball_accel_x *= -1
            ball.left += 5
        if paddle_2.colliderect(ball) and paddle_2.left > ball.left:
            ball_accel_x *= -1
            ball.left -= 5

        # move the ball if game started
        if started:
            ball.left += ball_accel_x * delta_time
            ball.top += ball_accel_y * delta_time    
    
        #Draws player 1 and player 2's paddle and the ball with white color
        pygame.draw.rect(screen, COLOR_WHITE, paddle_1)
        pygame.draw.rect(screen, COLOR_WHITE, paddle_2)
        pygame.draw.rect(screen, COLOR_WHITE, ball)

        #Update display
        pygame.display.update()
        await asyncio.sleep(0)


if __name__ == '__main__':
    asyncio.run(main())