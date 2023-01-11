import random

import pygame
import math

# Initialize pygame
pygame.init()

Width, Height = 400, 300
# Set up the display
screen = pygame.display.set_mode((Width, Height))

# Set up the ball
ball_pos = [Width // 2, Height // 2]
ball_vel = [0, 4]
ball_size = 10
ball_color = (0, 0, 0)
ball_vel = [vel * 0.01 for vel in ball_vel]

# Set up the physical constants
gravity = 0.01
coefficient_of_friction = 0.1
restitution = 0.8

class Block:
    def __init__(self, pos, size, color):
        self.pos = pos
        self.size = size
        self.color = color

def detect_collision(ball_pos, ball_size, block_pos, block_size):
    # Check if the ball is overlapping with the block or paddle
    if ((ball_pos[0] + ball_size > block_pos[0] and ball_pos[0] < block_pos[0] + block_size[0]) and (ball_pos[1] + ball_size > block_pos[1] and ball_pos[1] < block_pos[1] + block_size[1])):
        return True
    return False

class Paddle:
    def __init__(self, pos, size, color):
        self.pos = pos
        self.size = size
        self.color = color

# Set up the blocks
blocks = []
for i in range(6):
    for y in range(3):
        blocks.append(Block([i * Width / 6, y * 40], [60, 20], (0, 0, 255)))

# Set up the paddle
paddle = Paddle([Width // 2 - 50, Height - 20], [100, 20], (0, 0, 0))

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.pos[0] -= 0.02
    if keys[pygame.K_RIGHT]:
        paddle.pos[0] += 0.02

    if detect_collision(ball_pos, ball_size, paddle.pos, paddle.size):
        if abs(ball_vel[0]) < 0.005:
            One_shot = False
            ball_vel[0] = random.uniform(-0.02, 0.02)


    # Update game state
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]



    # Check for wall collisions
    if ball_pos[0] < 0 or ball_pos[0] > Width:
        ball_vel[0] = -ball_vel[0]
    if ball_pos[1] > Height:
        ball_vel = [0, 0.04]
        ball_pos = [Width // 2, Height // 2]
        paddle.pos = [Width // 2 - 50, Height - 20]

    # Check for block or paddle collisions
    for i, block in enumerate(blocks):
        if detect_collision(ball_pos, ball_size, block.pos, block.size):
            ball_vel[1] = -ball_vel[1]
            del blocks[i]
            break
    if detect_collision(ball_pos, ball_size, paddle.pos, paddle.size):
        ball_vel[1] = -ball_vel[1]

    # Draw the screen
    screen.fill((255, 255, 255))
    for block in blocks:
        pygame.draw.rect(screen, block.color, (block.pos[0], block.pos[1], block.size[0], block.size[1]))
    pygame.draw.rect(screen, paddle.color, (paddle.pos[0], paddle.pos[1], paddle.size[0], paddle.size[1]))
    pygame.draw.circle(screen, ball_color, ball_pos, ball_size)
    pygame.display.flip()

# Shut down pygame
pygame.quit()
