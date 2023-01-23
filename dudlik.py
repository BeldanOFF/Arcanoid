import pygame
import random
from pygame.math import Vector2
import os
import sys

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen (width, height).
size = (1000, 1000)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Doodle Jump Clone")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def load_image(name, colorkey=None):
    fullname = os.path.join(name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

image_fon1 = pygame.image.load("fost.png").convert()
image_fon1 = pygame.transform.scale(image_fon1, (200, 1000))
image_fon2 = pygame.image.load("fost.png").convert()
image_fon2 = pygame.transform.scale(image_fon2, (200, 1000))
platform = load_image('platform.png')
platform = pygame.transform.scale(platform, (100, 25))
start_platform = load_image('start_platform.png')
start_platform = pygame.transform.scale(start_platform, (100, 60))
platform_dvij = load_image('platform_dvij.png')
platform_dvij = pygame.transform.scale(platform_dvij, (100, 25))
shipi = load_image('shipi.png')
shipi = pygame.transform.scale(shipi, (25, 15))
ball = load_image('ball.png')
ball = pygame.transform.scale(ball, (25, 25))

# Starting position of the player
player_x = 250 + random.randint(0, size[0] - 500)
player_y = size[1] - 200

start_block_x = player_x
start_block_y = size[1] - 100

player = Vector2(start_block_x, start_block_y)

# Starting speed of the player
player_speed = 0
player_speed_x = 0

# Gravity
gravity = 0.25

# Initialize camera position
block_speed = 0
block_speed_x = 0
camera = pygame.math.Vector2(0, 0)

# Create an empty list to store the blocks
blocks = []
blocks_hold = []
block_hold_speed_x = 1
shufle = []
shufle_speed = 0
# Initialize block spawning timer
block_spawn_timer = 0

# Initialize block spawning rate
block_spawn_rate = 100

sumary = 0
game_over = False

def create_block(x, y, width, height):
    new_block = {
        'x': x,
        'y': y,
        'width': width,
        'height': height,
        'double': False
    }
    blocks.append(new_block)


def create_block_hold(x, y, width, height):
    new_block_hold = {
        'x': x,
        'y': y,
        'width': width,
        'height': height,
        'double': False
    }
    blocks_hold.append(new_block_hold)


def create_shufle(x, y, width, height, false):
    new_shufle = {
        'x': x,
        'y': y,
        'width': width,
        'height': height,
        'dvij': false
    }
    shufle.append(new_shufle)



f1 = pygame.font.Font(None, 50)

xxx = random.randint(start_block_x - 200, start_block_x + 200)
if xxx > 500:
    xxx -= 150
elif 200 >= xxx:
    xxx + 150

create_block(xxx, start_block_y - 150, 100, 20)

time = 0
# Main game loop
# Main game loop
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_speed_x = -5
            elif event.key == pygame.K_RIGHT:
                player_speed_x = 5
            if event.key != pygame.K_EURO and game_over == True:
                player_x = 250 + random.randint(0, size[0] - 500)
                player_y = size[1] - 200
                start_block_x = player_x
                start_block_y = size[1] - 100
                blocks.clear()
                shufle.clear()
                blocks_hold.clear()
                create_block(200 + random.randint(0, 500), start_block_y - 150, 100, 20)
                game_over = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_speed_x = 0


    # --- Game logic should go here
    player_draw = pygame.Rect(player_x, player_y, 40, 40)
    # Apply gravity to the player's speed
    player_speed += gravity
    # Move the player based on their current speed
    player_y += player_speed
    player_x += player_speed_x
    camera_y = player_y - (size[1] / 2)  # move the camera up with the player

    if player_y < 250:
        block_speed = 6.5
        player_speed += 0.8
    elif player_y < 450:
        block_speed = 4.5
        player_speed += 0.5
    elif player_y < 550:
        block_speed = 3.5
        player_speed += 0.3
    elif player_y < 650:
        block_speed = 2.5
        player_speed += 0.1
    else:
        block_speed = 0

    for block in blocks:
        block['y'] += block_speed
    # Update block spawning timer
    block_spawn_timer += clock.get_time()
    # Spawn new block if spawning timer has reached the spawning rate
    if len(blocks) < 10:
        random_x = 200 + random.randint(0, 500)
        random_y = list(blocks[-1].values())[1] - 150
        if random.randint(0, 10) == 10:
            create_block_hold(
                random_x,
                random_y, 100, 20)
            create_block(
                random_x,
                random_y - 150, 100, 20)

        else:
            create_block(
                random_x,
                random_y, 100, 20)
            if random.randint(0, 2) == 2:
                create_shufle(
                    random_x + random.randint(0, 65),
                    random_y - 11, 25, 15, False)

    shufle_speed = block_speed
    block_hold_speed_y = block_speed
    shufle_speed_x = block_hold_speed_x

    for shuf in shufle:
        if shuf['dvij'] == True:
            shuf['x'] += shufle_speed_x

    if len(shufle) > 0:
        for shuf in shufle:
            shuf['y'] += shufle_speed
            shuf_r = list(shufle[0].values())
            xx, yy, ww, hh, dvij = shuf_r
            shufs = pygame.Rect(shuf['x'], shuf['y'], 20, 15)
            # Check for collision between the player and the start_block
            if player_draw.colliderect(shufs):
                game_over = True
                # reverse player's speed to make it "bounce" off the block
            if shuf['y'] < 0:
                shufle.remove(shuf)
    ss = []
    for block in blocks_hold:
        block['x'] += block_hold_speed_x
        block['y'] += block_hold_speed_y
        tet = block['x']
        if block['x'] >= 650:
            block_hold_speed_x = random.randint(-4, -2)
        elif block['x'] <= 250:
            block_hold_speed_x = random.randint(2, 4)

    # Check for collision between the player and the blocks
    for i, block in enumerate(blocks):
        if block['y'] >= 1001:
            blocks.remove(block)
        if (player_x + 20 > block['x'] and player_x - 20 < block['x'] + block['width']) and (
                player_y + 20 > block['y'] and player_y - 20 < block['y'] + block['height']) and player_speed > 0:
            player_speed = -10  # reverse player's speed to make it "bounce" off the block
            camera -= block['x'], block['y']
            tt = time
            start_block_y += 200
            if block['double'] == False:
                block['double'] = True
                sumary += 1

        # Check for collision between the player and the blocks_hold
    for block in blocks_hold:
        if block['y'] >= 1000:
            blocks_hold.remove(block)
        if (player_x + 20 > block['x'] and player_x - 20 < block['x'] + block['width']) and (
                player_y + 20 > block['y'] and player_y - 20 < block['y'] + block['height']) and player_speed > 0:
            player_speed = -10  # reverse player's speed to make it "bounce" off the block
            camera -= block['x'], block['y']
            tt = time
            start_block_y += 200

            if block['double'] == False:
                block['double'] = True
                sumary += 1

    # Check for collision between the player and the start_block
    strt_blck = pygame.Rect(start_block_x - 50, start_block_y, 100, 10)
    if strt_blck.colliderect(player_draw):
        player_speed = -10

    texting = str(sumary)
    text1 = f1.render(f'{sumary}', True,
                      (255, 255, 255))

    if player_y > size[1]:
        game_over = True

    text_over = f1.render(f'Game over PRESS any key to RESTART', True,
                          (255, 255, 255))
    if player_x < 200:
        player_x = size[0] - player_x - 1
    elif player_x >= size[0] - 200:
        player_x = size[0] - player_x
    # --- Drawing code should go here

    if player_y >= size[1] / 2:
        camera_y = camera_y + 50

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    if not game_over:
        screen.fill((24, 21, 33))

        # Draw the player


        screen.blit(start_platform, (start_block_x - 50, start_block_y - 20))


        # Draw the blocks
        for block in blocks:
            screen.blit(platform, (block['x'], block['y']))

        for block in blocks_hold:
            screen.blit(platform_dvij, (block['x'], block['y']))

        for shuf in shufle:
            screen.blit(shipi, (shuf['x'] - 10, shuf['y']))

        screen.blit(ball, (player_x, player_y))



        pygame.draw.rect(screen, (30, 30, 30), (0, 0, 200, 1000))
        pygame.draw.rect(screen, (30, 30, 30), (size[0] - 200, 0, 200, 1000))
        screen.blit(image_fon1, (0, 0))
        screen.blit(image_fon2, (size[0] - 200, 0))

        if len(texting) == 4:
            screen.blit(text1, (470, 50))
        elif len(texting) == 3:
            screen.blit(text1, (480, 50))
        elif len(texting) == 2:
            screen.blit(text1, (490, 50))
        elif len(texting) == 1:
            screen.blit(text1, (500, 50))
    else:
        sumary = 0
        screen.fill((0, 0, 0))
        screen.blit(text_over, (180, 480))

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
