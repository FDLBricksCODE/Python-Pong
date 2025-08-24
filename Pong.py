import pygame
import sys

# Initialization pygame
pygame.init()

# Screen Size
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Pong")

# Color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
paddle_speed = 6

player1 = pygame.Rect(30, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2 = pygame.Rect(WIDTH-45, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball
BALL_SIZE = 20
ball = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)
ball_speed_x, ball_speed_y = 5, 5

# Score
score1, score2 = 0, 0
font = pygame.font.Font(None, 50)

clock = pygame.time.Clock()

# Loop game
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Control player 1 (W/S)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= paddle_speed
    if keys[pygame.K_s] and player1.bottom < HEIGHT:
        player1.y += paddle_speed

    # Control player 2 (UP/DOWN)
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= paddle_speed
    if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
        player2.y += paddle_speed

    # Move ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Bounce up down
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Bounce paddle
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

    # Score
    if ball.left <= 0:
        score2 += 1
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_speed_x *= -1
    if ball.right >= WIDTH:
        score1 += 1
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_speed_x *= -1

    # Image
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

    # Show score
    score_text = font.render(f"{score1} - {score2}", True, WHITE)
    screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 20))

    # Update screen
    pygame.display.flip()
    clock.tick(60)
