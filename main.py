import random

import pygame
import math

# Initialize pygame
pygame.init()

Width, Height = 1000, 1000
# Set up the display
screen = pygame.display.set_mode((Width, Height))

# Set up the ball
ball_pos = [Width // 2, Height // 2]
ball_vel = [0, 50]
ball_size = 10
ball_color = (0, 0, 0)
ball_vel = [vel * 0.01 for vel in ball_vel]

# Set up the physical constants
gravity = 0.25
coefficient_of_friction = 0.1
restitution = 0.8
summary = 0
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
for i in range(11):
    for y in range(8):
        blocks.append(Block([i * Width / 11, y * 40], [60, 20], (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))))

f1 = pygame.font.Font(None, 50)
# Set up the paddle
paddle = Paddle([Width // 2 - 75, Height - 80], [150, 20], (0, 0, 0))

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
        paddle.pos[0] -= 0.4
    if keys[pygame.K_RIGHT]:
        paddle.pos[0] += 0.4

    if detect_collision(ball_pos, ball_size, paddle.pos, paddle.size):
        ball_vel[0] += random.uniform(-0.3, 0.3)

    if len(blocks) == 0:
        for i in range(11):
            for y in range(8):
                blocks.append(Block([i * Width / 11, y * 40], [60, 20], (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))))
        ball_vel = [0, 0.50]
        ball_pos = [Width // 2, Height // 2]
        paddle.pos = [Width // 2 - 75, Height - 80]
    textery = str(summary)
    text1 = f1.render(f'{summary}', True,
                      (50, 50, 50))
    # Update game state
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    if paddle.pos[0] > Width-149:
        paddle.pos[0] -= 1
    if paddle.pos[0] < 0:
        paddle.pos[0] += 1

    # Check for wall collisions
    if ball_pos[0] < 0 or ball_pos[0] > Width:
        ball_vel[0] = -ball_vel[0]
    if ball_pos[1] < 0:
        ball_vel[1] = -ball_vel[1]
    if ball_pos[1] > Height:
        ball_vel = [0, 0.50]
        ball_pos = [Width // 2, Height // 2]
        paddle.pos = [Width // 2 - 75, Height - 80]

    # Check for block or paddle collisions
    for i, block in enumerate(blocks):
        if detect_collision(ball_pos, ball_size, block.pos, block.size):
            ball_vel[1] = -ball_vel[1]
            del blocks[i]
            summary += 1
            break
    if detect_collision(ball_pos, ball_size, paddle.pos, paddle.size):
        ball_vel[1] = -ball_vel[1]


    # Draw the screen
    screen.fill((255, 255, 255))
    for block in blocks:
        pygame.draw.rect(screen, block.color, (block.pos[0], block.pos[1], block.size[0], block.size[1]))
    pygame.draw.rect(screen, paddle.color, (paddle.pos[0], paddle.pos[1], paddle.size[0], paddle.size[1]))
    pygame.draw.circle(screen, ball_color, ball_pos, ball_size)

    if len(textery) == 4:
        screen.blit(text1, (460, 550))
    elif len(textery) == 3:
        screen.blit(text1, (470, 550))
    elif len(textery) == 2:
        screen.blit(text1, (480, 550))
    elif len(textery) == 1:
        screen.blit(text1, (490, 550))

    pygame.display.flip()



# Shut down pygame
pygame.quit()
