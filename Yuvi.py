# simple_game.py
import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Pygame Game")

# Ball settings
ball_size = 20
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_speed_x = 3
ball_speed_y = 3

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with walls
    if ball_x <= 0 or ball_x >= screen_width - ball_size:
        ball_speed_x *= -1
    if ball_y <= 0 or ball_y >= screen_height - ball_size:
        ball_speed_y *= -1

    # Clear the screen
    screen.fill(black)

    # Draw the ball
    pygame.draw.circle(screen, white, (ball_x, ball_y), ball_size)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
