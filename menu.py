import pygame
from pygame.math import Vector2
import random
import math
import os
import sys


def main_menu():
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("Game Menu")

    # Load game images
    game1_img = pygame.image.load("game1.png")
    game2_img = pygame.image.load("game2.png")
    game3_img = pygame.image.load("game3.png")
    game4_img = pygame.image.load("game4.png")
    game5_img = pygame.image.load("game5.png")
    game6_img = pygame.image.load("game6.png")
    game7_img = pygame.image.load("game 7.png")

    # Scale images to fit the window
    game1_img = pygame.transform.scale(game1_img, (150, 150))
    game2_img = pygame.transform.scale(game2_img, (150, 150))
    game3_img = pygame.transform.scale(game3_img, (150, 150))
    game4_img = pygame.transform.scale(game4_img, (150, 150))
    game5_img = pygame.transform.scale(game5_img, (150, 150))
    game6_img = pygame.transform.scale(game6_img, (150, 150))
    game7_img = pygame.transform.scale(game7_img, (150, 150))

    # Set coordinates for game images
    game1_rect = game1_img.get_rect(center=(250, 250))
    game2_rect = game2_img.get_rect(center=(500, 250))
    game3_rect = game3_img.get_rect(center=(750, 250))
    game4_rect = game4_img.get_rect(center=(250, 500))
    game5_rect = game5_img.get_rect(center=(500, 500))
    game6_rect = game6_img.get_rect(center=(750, 500))
    game7_rect = game7_img.get_rect(center=(500, 750))

    # Set font for captions
    font = pygame.font.Font(None, 40)

    # Load background image
    background_img = pygame.image.load("backgound.png")

    # Scale background image to fit the window
    background_img = pygame.transform.scale(background_img, (1000, 1000))

    # Set title text
    title_text = "Welcome to the Game Menu"
    title_font = pygame.font.Font(None, 60)
    title_color = (255, 255, 255)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if game1_rect.collidepoint(event.pos):
                    game_1()
                elif game2_rect.collidepoint(event.pos):
                    game_2()
                elif game3_rect.collidepoint(event.pos):
                    game_3()
                elif game4_rect.collidepoint(event.pos):
                    game_4()
                elif game5_rect.collidepoint(event.pos):
                    game_5()
                elif game6_rect.collidepoint(event.pos):
                    game_6()
                elif game7_rect.collidepoint(event.pos):
                    game_7()

        screen.blit(background_img, (0, 0))

        # Blit game images to screen
        screen.blit(game1_img, game1_rect)
        screen.blit(game2_img, game2_rect)
        screen.blit(game3_img, game3_rect)
        screen.blit(game4_img, game4_rect)
        screen.blit(game5_img, game5_rect)
        screen.blit(game6_img, game6_rect)
        screen.blit(game7_img, game7_rect)

        # Render captions
        game1_caption = font.render("Crazy-jump", True, (255, 255, 255))
        screen.blit(game1_caption, (170, 350))
        game2_caption = font.render("People run", True, (255, 255, 255))
        screen.blit(game2_caption, (425, 350))
        game3_caption = font.render("Flappy bird", True, (255, 255, 255))
        screen.blit(game3_caption, (670, 350))
        game4_caption = font.render("Arkanoid", True, (255, 255, 255))
        screen.blit(game4_caption, (185, 600))
        game5_caption = font.render("Galactic defender", True, (255, 255, 255))
        screen.blit(game5_caption, (375, 600))
        game6_caption = font.render("Car driving", True, (255, 255, 255))
        screen.blit(game6_caption, (670, 600))
        game7_caption = font.render("Table tennis", True, (255, 255, 255))
        screen.blit(game7_caption, (415, 850))
        # Render title text
        title_text = title_font.render('Mini Game', True, title_color)
        title_rect = title_text.get_rect(center=(500, 100))
        screen.blit(title_text, title_rect)

        # Add some decorations

        pygame.display.update()


def game_1():
    # Initialize Pygame
    pygame.init()

    # Set the dimensions of the screen (width, height).
    size = (1000, 1000)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Doodle Jump Clone")

    ARIAL_FONT_PATH = pygame.font.match_font('arial')
    ARIAL_FONT_36 = pygame.font.Font(ARIAL_FONT_PATH, 36)

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
        xxx += 150

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
                if event.key == pygame.K_ESCAPE:
                    main_menu()
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

            with open('top_score_game1.txt', 'r') as f:
                first_line = f.read()
            if sumary > int(first_line):
                new_data = first_line.replace(first_line, str(sumary))
                with open('top_score_game1.txt', 'w') as f:
                    f.write(new_data)
            record_surface = ARIAL_FONT_36.render(f'record: {first_line}', True, (255, 255, 255))
            screen.blit(record_surface, [650, 50])
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


def game_2():
    pygame.init()

    ARIAL_FONT_PATH = pygame.font.match_font('arial')
    ARIAL_FONT_36 = pygame.font.Font(ARIAL_FONT_PATH, 36)

    size = (1000, 1000)
    screen = pygame.display.set_mode(size)
    pygame.display.update()
    pygame.display.set_caption('dino')

    def load_image(name, colorkey=None):
        fullname = os.path.join(name)
        # если файл не существует, то выходим
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        return image

    cad1 = load_image('1.png')
    cad2 = load_image('2.png')
    cad3 = load_image('3.png')
    cad4 = load_image('4.png')
    cad5 = load_image('5.png')
    cad6 = load_image('6.png')
    cad7 = load_image('7.png')
    cad8 = load_image('8.png')
    pers = [cad1, cad2, cad3, cad4, cad5, cad6, cad7, cad8]
    pers_ready = pers[0]
    cacts = load_image('cacts.png')
    goose = load_image('gus.png')
    goose = pygame.transform.scale(goose, (35, 25))
    shieled = load_image('shieled.png')

    player_x = 500
    player_y = 600
    player_speed_y = 0
    gravity = 0.25
    player_height = 30
    player_height2 = 30

    birds = []
    cactuss = []
    serds = []
    speed_game_x = -2

    def bird(x, y):
        bird_xy = {
            'x': x,
            'y': y,
        }
        birds.append(bird_xy)

    def cactusi(x, y, height):
        cactus_xy = {
            'x': x,
            'y': y,
            'height': height
        }
        cactuss.append(cactus_xy)

    def serd(x, y):
        serd_xy = {
            'x': x,
            'y': y,
        }
        serds.append(serd_xy)

    max_last = 0

    double_serd = False
    life = False
    time = 0
    timer = 0
    time2 = 0
    kd = 0
    time_animation = 0
    done = False
    speed_animation = 30
    game_over = False

    f1 = pygame.font.Font(None, 50)
    clock = pygame.time.Clock()

    while not done:
        # --- Main event loop
        time_animation += 1

        if time_animation > speed_animation:
            time_animation = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
                if event.key == pygame.K_UP:
                    if player_speed_y <= 0.4 and player_y > 600:
                        player_speed_y += -9
                        if not pers_ready == pers[5]:
                            pers_ready = pers[2]
                if game_over:
                    if event.key != pygame.K_EURO:
                        game_over = False
                        timer = 0
                        cactuss.clear()
                        birds.clear()
                        serds.clear()
                        time2 = 0
                        time = 0
                        player_y = 600
                        double_serd = False
                elif event.key == pygame.K_DOWN:
                    player_height = 0
                    if not pers_ready == pers[5]:
                        pers_ready = pers[1]
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    player_height = 30
                    if not pers_ready == pers[5]:
                        pers_ready = pers[2]

        player_speed_y += gravity
        player_y += player_speed_y

        if player_y > 640:
            player_speed_y = 0
            player_speed_y -= 0.25
            if not life:
                if player_height > 1:
                    if time_animation / 3 <= 1:
                        pers_ready = pers[0]
                    elif time_animation / 3 <= 2:
                        pers_ready = pers[3]
                    else:
                        pers_ready = pers[4]
                        time_animation = 0

        SPEED_0 = ''
        timer += 1
        time += 1
        time2 += 1
        if time >= random.randint(200, 400):
            time = 0
            bird(random.randint(1050, 1150), random.randint(500, 650))
            if len(serds) <= 0:
                if random.randint(1, 10) == 5:
                    serd(random.randint(1050, 1150), random.randint(500, 650))

        lvl1 = 1000
        lvl2 = 2500
        lvl3 = 4500
        lvl4 = 7000
        lvl5 = 15000
        lvl6 = 30000

        SPEED_0 = f1.render('', True,
                            (255, 255, 255))
        SPEED = f1.render('SPEED>>', True,
                          (255, 255, 255))

        if lvl5 < timer < lvl6:
            if time2 >= random.randint(110, 130):
                time2 = 0
                cactus_2 = random.randint(1, 2)
                cactus_3 = random.randint(1, 3)
                cactusi(1100, 608, random.randint(0, 20))
                if cactus_2 == 2:
                    cactusi(1100 + 30, 608, random.randint(0, 20))
                    if cactus_3 == 2:
                        cactusi(1100 + 60, 608, random.randint(0, 20))
                speed_game_x = -7
                speed_animation = 5
        if lvl4 < timer < lvl5:
            if time2 >= random.randint(100, 120):
                time2 = 0
                cactus_2 = random.randint(1, 2)
                cactus_3 = random.randint(1, 3)
                cactusi(1100, 608, random.randint(0, 20))
                if cactus_2 == 2:
                    cactusi(1100 + 30, 608, random.randint(0, 20))
                    if cactus_3 == 2:
                        cactusi(1100 + 60, 608, random.randint(0, 20))
                speed_game_x = -6
                speed_animation = 10
        elif lvl3 < timer < lvl4:
            if time2 >= random.randint(90, 110):
                time2 = 0
                cactus_2 = random.randint(1, 2)
                cactus_3 = random.randint(1, 3)
                cactusi(1100, 608, random.randint(0, 20))
                if cactus_2 == 2:
                    cactusi(1100 + 30, 608, random.randint(0, 20))
                    if cactus_3 == 2:
                        cactusi(1100 + 60, 608, random.randint(0, 20))
                speed_game_x = -5
                speed_animation = 15
        elif lvl2 < timer < lvl3:
            if time2 >= random.randint(85, 105):
                time2 = 0
                cactus_2 = random.randint(1, 2)
                cactus_3 = random.randint(1, 3)
                cactusi(1100, 608, random.randint(0, 20))
                if cactus_2 == 2:
                    cactusi(1100 + 30, 608, random.randint(0, 20))
                    if cactus_3 == 2:
                        cactusi(1100 + 60, 608, random.randint(0, 20))
                speed_game_x = -4
                speed_animation = 20
        elif lvl1 < timer < lvl2:
            if time2 >= random.randint(130, 170):
                time2 = 0
                cactus_2 = random.randint(1, 2)
                cactus_3 = random.randint(1, 3)
                cactusi(1100, 608, random.randint(0, 20))
                if cactus_2 == 2:
                    cactusi(1100 + 30, 608, random.randint(0, 20))
                    if cactus_3 == 2:
                        cactusi(1100 + 60, 608, random.randint(0, 20))
                speed_game_x = -3
                speed_animation = 25
        elif timer < lvl1:
            if time2 >= random.randint(160, 220):
                time2 = 0
                cactus_2 = random.randint(1, 2)
                cactus_3 = random.randint(1, 3)
                cactusi(1100, 608, random.randint(0, 20))
                if cactus_2 == 2:
                    cactusi(1100 + 30, 608, random.randint(0, 20))
                speed_game_x = -2
                speed_animation = 30
        texting = str(timer)
        str_last = str(max_last)
        text1 = f1.render(f'{timer}', True,
                          (255, 255, 255))
        text_over = f1.render(f'Game over PRESS any key to RESTART', True,
                              (255, 255, 255))


        # player

        for s in serds:
            s['x'] += speed_game_x
            ptc = pygame.Rect(s['x'], s['y'], 20, 20)
            plr = pygame.Rect(player_x, player_y, 20, player_height)
            plr2 = pygame.Rect(player_x, player_y + 30, 20, player_height2)
            if ptc.colliderect(plr) or ptc.colliderect(plr2):
                double_serd = True
                serds.remove(s)
            if s['x'] < -20:
                serds.remove(s)

        for bir in birds:
            bir['x'] += speed_game_x - 0.2
            ptc = pygame.Rect(bir['x'], bir['y'], 20, 20)
            plr = pygame.Rect(player_x, player_y, 20, player_height)
            plr2 = pygame.Rect(player_x, player_y + 30, 20, player_height2)
            if ptc.colliderect(plr) or ptc.colliderect(plr2):
                if double_serd:
                    life = True
                    player_height = 0
                    player_height2 = 0
                    pers_ready = pers[5]
                else:
                    game_over = True
            if bir['x'] < -20:
                birds.remove(bir)

        if life:
            kd += 1
            if kd > 100:
                life = False
                kd = 0
                double_serd = False
                player_height2 = 30
                player_height = 30
                pers_ready = pers[5]

        for cact in cactuss:
            for bir in birds:
                if abs(bir['y'] - cact['y']) < 150:
                    if cact['x'] - 60 < bir['x'] < cact['x'] + 60:
                        bir['x'] += speed_game_x - 0.5

        for cact in cactuss:
            cact['x'] += speed_game_x
            ptc = pygame.Rect(cact['x'] + 2, cact['y'] + 15, 16, 100)
            plr = pygame.Rect(player_x, player_y, 20, player_height)
            plr2 = pygame.Rect(player_x, player_y + 30, 20, player_height2)
            if ptc.colliderect(plr) or ptc.colliderect(plr2):
                if double_serd:
                    life = True
                    player_height = 0
                    player_height2 = 0
                    pers_ready = pers[5]
                else:
                    game_over = True

            if cact['x'] < -20:
                cactuss.remove(cact)

            # fill to screen
        if game_over == False:
            screen.fill((146, 225, 218))

            for cact in cactuss:
                screen.blit(cacts, (cact['x'], cact['y'] + cact['height']))

            pygame.draw.rect(screen, (0, 0, 0), (0, 699, 1000, 300))
            pygame.draw.rect(screen, (227, 198, 108), (0, 700, 1000, 300))

            screen.blit(pers_ready, (player_x, player_y))

            if lvl1 - 150 < timer < lvl1 - 125:
                screen.blit(SPEED, (500 - 50, 480 - 100))
            if lvl1 - 125 < timer < lvl1 - 100:
                screen.blit(SPEED_0, (500 - 50, 480 - 100))
            if lvl1 - 100 < timer < lvl1 - 75:
                screen.blit(SPEED, (500 - 50, 480 - 100))
            if lvl1 - 75 < timer < lvl1 - 50:
                screen.blit(SPEED_0, (500 - 50, 480 - 100))
            if lvl1 - 50 < timer < lvl1 - 25:
                screen.blit(SPEED, (500 - 50, 480 - 100))
            if lvl1 - 25 < timer < lvl1:
                screen.blit(SPEED_0, (500 - 50, 480 - 100))

            if lvl2 - 150 < timer < lvl2 - 125:
                screen.blit(SPEED, (500 - 50, 480 - 100))
            if lvl2 - 125 < timer < lvl2 - 100:
                screen.blit(SPEED_0, (500 - 50, 480 - 100))
            if lvl2 - 100 < timer < lvl2 - 75:
                screen.blit(SPEED, (500 - 50, 480 - 100))
            if lvl2 - 75 < timer < lvl2 - 50:
                screen.blit(SPEED_0, (500 - 50, 480 - 100))
            if lvl2 - 50 < timer < lvl2 - 25:
                screen.blit(SPEED, (500 - 50, 480 - 100))
            if lvl2 - 25 < timer < lvl2:
                screen.blit(SPEED_0, (500 - 50, 480 - 100))

            if lvl3 - 150 < timer < lvl3 - 125:
                screen.blit(SPEED, (500 - 50, 480 - 100))
            if lvl3 - 125 < timer < lvl3 - 100:
                screen.blit(SPEED_0, (500 - 50, 480 - 100))
            if lvl3 - 100 < timer < lvl3 - 75:
                screen.blit(SPEED, (500 - 50, 480 - 100))
            if lvl3 - 75 < timer < lvl3 - 50:
                screen.blit(SPEED_0, (500 - 50, 480 - 100))
            if lvl3 - 50 < timer < lvl3 - 25:
                screen.blit(SPEED, (500 - 50, 480 - 100))
            if lvl3 - 25 < timer < lvl3:
                screen.blit(SPEED_0, (500 - 50, 480 - 100))

            if lvl4 - 150 < timer < lvl4 - 125:
                screen.blit(SPEED, (500 - 50, 480 - 100))
            if lvl4 - 125 < timer < lvl4 - 100:
                screen.blit(SPEED_0, (500 - 50, 480 - 100))
            if lvl4 - 100 < timer < lvl4 - 75:
                screen.blit(SPEED, (500 - 50, 480 - 100))
            if lvl4 - 75 < timer < lvl4 - 50:
                screen.blit(SPEED_0, (500 - 50, 480 - 100))
            if lvl4 - 50 < timer < lvl4 - 25:
                screen.blit(SPEED, (500 - 50, 480 - 100))
            if lvl4 - 25 < timer < lvl4:
                screen.blit(SPEED_0, (500 - 50, 480 - 100))

            if lvl5 - 150 < timer < lvl5 - 125:
                screen.blit(SPEED, (500 - 50, 480 - 100))
            if lvl5 - 125 < timer < lvl5 - 100:
                screen.blit(SPEED_0, (500 - 50, 480 - 100))
            if lvl5 - 100 < timer < lvl5 - 75:
                screen.blit(SPEED, (500 - 50, 480 - 100))
            if lvl5 - 75 < timer < lvl5 - 50:
                screen.blit(SPEED_0, (500 - 50, 480 - 100))
            if lvl5 - 50 < timer < lvl5 - 25:
                screen.blit(SPEED, (500 - 50, 480 - 100))
            if lvl5 - 25 < timer < lvl5:
                screen.blit(SPEED_0, (500 - 50, 480 - 100))

            if len(texting) == 6:
                screen.blit(text1, (40, 50))
            elif len(texting) == 5:
                screen.blit(text1, (50, 50))
            elif len(texting) == 4:
                screen.blit(text1, (60, 50))
            elif len(texting) == 3:
                screen.blit(text1, (70, 50))
            elif len(texting) == 2:
                screen.blit(text1, (80, 50))
            elif len(texting) == 1:
                screen.blit(text1, (90, 50))

            with open('top_score_game2.txt', 'r') as f:
                first_line = f.read()
            if max_last > int(first_line):
                new_data = first_line.replace(first_line, str(max_last))
                with open('top_score_game2.txt', 'w') as f:
                    f.write(new_data)
            record_surface = ARIAL_FONT_36.render(f'record: {first_line}', True, (255, 255, 255))
            screen.blit(record_surface, [780, 50])

            for bir in birds:
                screen.blit(goose, (bir['x'], bir['y']))

            for s in serds:
                screen.blit(shieled, (s['x'], s['y']))
        else:
            timer -= 1
            if timer > max_last:
                max_last = timer
            screen.fill((0, 0, 0))
            screen.blit(text_over, (180, 480))

        pygame.display.flip()

        clock.tick(60)
    pygame.quit()
    quit()


def game_3():
    WIDTH = 1000
    HEIGHT = 1000
    FPS = 60
    player_x = 500
    player_y = 500
    player_speed_y = 0
    gravity = 0.25
    game_speed = -1.5
    ARIAL_FONT_PATH = pygame.font.match_font('arial')
    ARIAL_FONT_36 = pygame.font.Font(ARIAL_FONT_PATH, 36)
    game_over = False

    def load_image(name, colorkey=None):
        fullname = os.path.join(name)
        # если файл не существует, то выходим
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        return image

    trubi = load_image('trubi.png')
    trubi2 = pygame.transform.rotate(trubi, 180)
    goose = load_image('gus.png')
    goose = pygame.transform.scale(goose, (40, 40))
    goose = pygame.transform.flip(goose, True, False)

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Flappy goose")
    clock = pygame.time.Clock()
    trubs = []

    def trub(x1, y1, y2):
        new_block_hold = {
            'x': x1,
            'y1': y1,
            'y2': y2,
        }
        trubs.append(new_block_hold)

    summary = 0
    f1 = pygame.font.Font(None, 50)
    clock = pygame.time.Clock()

    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
                if event.key == pygame.K_UP:
                    player_speed_y = -6.5
                if event.key != pygame.K_EURO and game_over == True:
                    game_over = False
                    trubs.clear()
                    player_y = 500
                    player_speed_y = 0
                    summary = 0

        if len(trubs) < 5:
            ty = random.randint(-550, 0)
            if len(trubs) == 0:
                trub(1100, ty, ty + 850)
            tx = list(trubs[-1].values())[0] + 400
            trub(tx, ty, ty + 850)
            timer = 0

        clPlayer = pygame.Rect(player_x, player_y, 40, 40)

        for trb in trubs:
            trb['x'] += game_speed
            cltrb1 = pygame.Rect(trb['x'], trb['y1'], 100, 700)
            cltrb2 = pygame.Rect(trb['x'], trb['y2'], 100, 700)
            trb['x'] += game_speed
            if trb['x'] + 50 < player_x <= trb['x'] + 53:
                summary += 1
            if trb['x'] <= -501:
                trubs.remove(trb)
            if cltrb1.colliderect(clPlayer):
                game_over = True
            elif cltrb2.colliderect(clPlayer):
                game_over = True
        str_last = str(summary)
        last = f1.render(f'{summary}', True,
                         (0, 0, 0))
        text_over = f1.render(f'Game over PRESS any key to RESTART', True,
                              (255, 255, 255))

        if player_y > 1000 or player_y < -40:
            game_over = True

        player_speed_y += gravity
        player_y += player_speed_y
        if not game_over:
            screen.fill((146, 225, 218))
            if len(str_last) == 6:
                screen.blit(last, (460, 50))
            elif len(str_last) == 5:
                screen.blit(last, (470, 50))
            elif len(str_last) == 4:
                screen.blit(last, (480, 50))
            elif len(str_last) == 3:
                screen.blit(last, (490, 50))
            elif len(str_last) == 2:
                screen.blit(last, (500, 50))
            elif len(str_last) == 1:
                screen.blit(last, (510, 50))
            screen.blit(goose, (player_x, player_y))
            for trb in trubs:
                screen.blit(trubi2, (trb['x'], trb['y1']))
                screen.blit(trubi, (trb['x'], trb['y2']))
            with open('top_score_game3.txt', 'r') as f:
                first_line = f.read()
            if summary > int(first_line):
                new_data = first_line.replace(first_line, str(summary))
                with open('top_score_game3.txt', 'w') as f:
                    f.write(new_data)
            record_surface = ARIAL_FONT_36.render(f'record: {first_line}', True, (0, 0, 0))
            screen.blit(record_surface, [10, 30])
        else:
            screen.fill((0, 0, 0))
            screen.blit(text_over, (180, 480))

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


def game_4():
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
        if ((ball_pos[0] + ball_size > block_pos[0] and ball_pos[0] < block_pos[0] + block_size[0]) and (
                ball_pos[1] + ball_size > block_pos[1] and ball_pos[1] < block_pos[1] + block_size[1])):
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
            blocks.append(Block([i * Width / 11, y * 40], [60, 20],
                                (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))))

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
        if keys[pygame.K_ESCAPE]:
            main_menu()
        if keys[pygame.K_LEFT]:
            paddle.pos[0] -= 0.4
        if keys[pygame.K_RIGHT]:
            paddle.pos[0] += 0.4

        if detect_collision(ball_pos, ball_size, paddle.pos, paddle.size):
            ball_vel[0] += random.uniform(-0.3, 0.3)

        if len(blocks) == 0:
            for i in range(11):
                for y in range(8):
                    blocks.append(Block([i * Width / 11, y * 40], [60, 20],
                                        (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))))
            ball_vel = [0, 0.50]
            ball_pos = [Width // 2, Height // 2]
            paddle.pos = [Width // 2 - 75, Height - 80]
        textery = str(summary)
        text1 = f1.render(f'{summary}', True,
                          (50, 50, 50))
        # Update game state
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]

        if paddle.pos[0] > Width - 149:
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


def game_5():
    pygame.init()
    pygame.font.init()
    clock = pygame.time.Clock()

    WIDTH, HEIGHT = 1000, 1000
    SIZE = WIDTH, HEIGHT
    FPS = 60

    ARIAL_FONT_PATH = pygame.font.match_font('arial')
    ARIAL_FONT_64 = pygame.font.Font(ARIAL_FONT_PATH, 64)
    ARIAL_FONT_36 = pygame.font.Font(ARIAL_FONT_PATH, 36)

    LIFES = 10
    bullets = []
    enemys = []

    def load_image(name, colorkey=None):
        fullname = os.path.join(name)
        # если файл не существует, то выходим
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        return image

    def create_bullet(x, y):
        new_bullet = {
            'x': x,
            'y': y,
        }
        bullets.append(new_bullet)

    def create_enemy(x, y):
        new_enemy = {
            'x': x,
            'y': y,
        }
        enemys.append(new_enemy)

    x, y = WIDTH // 2, HEIGHT // 2
    PLAYER_POS_X = x - 100
    PLAYER_POS_Y = HEIGHT - 300

    screen = pygame.display.set_mode(SIZE)
    background = pygame.image.load('space.png').convert()
    background = pygame.transform.scale(background, (1000, 1000))

    player = load_image('space_ship.png')
    player = pygame.transform.scale(player, (200, 200))

    enemy_stone = load_image('stone.png')
    enemy_stone = pygame.transform.scale(enemy_stone, (50, 50))
    enemy_speed = -5

    score = 0
    bullet = load_image('bullet.png')
    bullet = pygame.transform.scale(bullet, (30, 40))
    bullet_speed = -10
    bullet_pos_x = PLAYER_POS_X + 85
    bullet_pos_y = PLAYER_POS_Y
    game_over = False
    running = True
    while running:
        screen.blit(background, (0, 0))
        keys = pygame.key.get_pressed()
        player_rect = pygame.Rect(PLAYER_POS_X, PLAYER_POS_Y, 200, 200)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
                if event.key == pygame.K_r and game_over == True:
                    game_over = False
                    enemys.clear()
                    PLAYER_POS_X = x - 100
                    PLAYER_POS_Y = HEIGHT - 300
                    score = 0
                    LIFES = 10
                if event.key == pygame.K_SPACE:
                    create_bullet(PLAYER_POS_X + 85, PLAYER_POS_Y)

        for blt in bullets:
            blt['y'] += bullet_speed
            if blt['y'] < -40:
                bullets.remove(blt)
            bullet_rect = pygame.Rect(blt['x'], blt['y'], 30, 40)

        for en in enemys:
            en['x'] += enemy_speed
            if en['x'] < -50:
                enemys.remove(en)
                LIFES -= 1
            enemy_rect = pygame.Rect(en['x'], en['y'], 50, 50)
            for blt in bullets:
                bullet_rect = pygame.Rect(blt['x'], blt['y'], 30, 40)
                if bullet_rect.colliderect(enemy_rect):
                    score += 1
                    enemys.remove(en)
                    bullets.remove(blt)

        if len(enemys) < 10:
            random_y = random.randint(0, y)
            if len(enemys) == 0:
                create_enemy(1000, random_y)
            create_enemy(list(enemys[-1].values())[0] + 200, random_y)

        if keys[pygame.K_w]:
            if PLAYER_POS_Y >= 0:
                PLAYER_POS_Y -= 5
        elif keys[pygame.K_s]:
            if PLAYER_POS_Y + 200 <= HEIGHT:
                PLAYER_POS_Y += 5
        if keys[pygame.K_d]:
            if PLAYER_POS_X + 200 <= WIDTH:
                PLAYER_POS_X += 5
        if keys[pygame.K_a]:
            if PLAYER_POS_X >= 0:
                PLAYER_POS_X -= 5
        if LIFES == 0:
            game_over = True
        if not game_over:
            screen.blit(player, (PLAYER_POS_X, PLAYER_POS_Y))
            for blt in bullets:
                screen.blit(bullet, (blt['x'], blt['y']))
            for en in enemys:
                screen.blit(enemy_stone, (en['x'], en['y']))
            with open('top_score_game5.txt', 'r') as f:
                first_line = f.read()
            if score > int(first_line):
                new_data = first_line.replace(first_line, str(score))
                with open('top_score_game5.txt', 'w') as f:
                    f.write(new_data)
            record_surface = ARIAL_FONT_64.render(f'record: {first_line}', True, (255, 255, 255))
            score_surface = ARIAL_FONT_64.render(f'score: {score}', True, (255, 255, 255))
            screen.blit(record_surface, [700, 40])
            screen.blit(score_surface, [20, 20])
        else:
            retry_surface = ARIAL_FONT_64.render(f'Game Over. Your score: {score}', True, (255, 255, 255))
            screen.blit(retry_surface, [100, y])
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


def game_6():
    WIDTH, HEIGHT = 1000, 1000
    SIZE = WIDTH, HEIGHT
    FPS = 60

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    def load_image(name, colorkey=None):
        fullname = os.path.join(name)
        # если файл не существует, то выходим
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        return image

    x, y = WIDTH // 2, HEIGHT // 2

    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode(SIZE)
    background = pygame.image.load('fon.png').convert()
    background = pygame.transform.scale(background, (1000, 1024))
    tiles = math.ceil(WIDTH / background.get_width()) + 1

    ARIAL_FONT_PATH = pygame.font.match_font('arial')
    ARIAL_FONT_64 = pygame.font.Font(ARIAL_FONT_PATH, 64)
    ARIAL_FONT_36 = pygame.font.Font(ARIAL_FONT_PATH, 36)

    enemy_car = load_image('enemy_car.png')
    enemy_car = pygame.transform.scale(enemy_car, (200, 150))
    enemy_car = pygame.transform.rotate(enemy_car, -90)

    player = load_image('car.png')
    player = pygame.transform.scale(player, (200, 150))
    player = pygame.transform.rotate(player, 90)
    PLAYER_X = WIDTH // 2 - 100
    PLAYER_Y = HEIGHT - 300
    PLAYER_SPEED_X = 0
    PLAYER_SPEED_Y = 0
    map_x = 0
    map_y = 0
    speed_game = 4
    maps = []
    Y = 0
    player_rect = pygame.Rect(PLAYER_X, PLAYER_Y, 200, 150)
    ls_enemy = []
    enemys = []
    score = 0

    def maps_create(x, y):
        maps_XY = {
            'x': x,
            'y': y
        }
        maps.append(maps_XY)

    def enemy(x, y):
        enemy_xy = {
            'x': x,
            'y': y,
        }
        enemys.append(enemy_xy)

    timer = 0
    enemy(random.randint(0, 900), -100)
    maps_create(0, 0)

    clock = pygame.time.Clock()
    game_over = False
    running = True
    while running:
        PLAYER_X += PLAYER_SPEED_X
        PLAYER_Y += PLAYER_SPEED_Y
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
                if event.key == pygame.K_r and game_over == True:
                    pygame.display.update()
                    PLAYER_SPEED_X = 0
                    PLAYER_SPEED_Y = 0
                    PLAYER_X = WIDTH // 2 - 100
                    PLAYER_Y = HEIGHT - 300
                    enemys.clear()
                    score = 0
                    game_over = False

        if not game_over:
            timer += 1
            if timer >= 60:
                if len(enemys) <= 5:
                    random_x = random.randint(0, 750)
                    enemy(random_x, -200)
                    if random.randint(1, 3) == 3:
                        random_x1 = random.randint(0, 1000)
                        if abs(random_x1 - random_x) <= 200:
                            if random_x + 200 >= 1000 - 190:
                                random_x1 = 1000 - random_x1
                                enemy(
                                    random_x1,
                                    -200)
                    timer = 0

            for en in enemys:
                en['y'] += speed_game + 2
                if en['y'] > 1001:
                    enemys.remove(en)
                    score += 1

            # CHECKING BORDERS

            if PLAYER_Y >= 0:
                if keys[pygame.K_w]:
                    PLAYER_SPEED_Y -= 0.2
            else:
                PLAYER_SPEED_Y = 0
                PLAYER_Y += 1
            if PLAYER_Y + 200 <= HEIGHT:
                if keys[pygame.K_s]:
                    PLAYER_SPEED_Y += 0.2
            else:
                PLAYER_SPEED_Y = 0
                PLAYER_Y -= 1
            if PLAYER_X > 0:
                if keys[pygame.K_a]:
                    PLAYER_SPEED_X -= 0.2
            else:
                PLAYER_SPEED_X = 0
                PLAYER_X += 1
            if PLAYER_X + 150 < WIDTH:
                if keys[pygame.K_d]:
                    PLAYER_SPEED_X += 0.2
            else:
                PLAYER_SPEED_X = 0
                PLAYER_X -= 1

            if len(maps) <= 3:
                Y = list(maps[-1].values())[1]
                maps_create(0, Y - 1000)

            for mp in maps:
                mp['y'] += speed_game
                if mp['y'] >= 1001:
                    maps.remove(mp)

            for mp in maps:
                screen.blit(background, (mp['x'], mp['y']))

            player_rect = pygame.Rect(PLAYER_X, PLAYER_Y, 130, 200)

            for en in enemys:
                rect_enemy = pygame.Rect(en['x'], en['y'], 130, 190)
                if rect_enemy.colliderect(player_rect):
                    game_over = True

            screen.blit(player, (PLAYER_X, PLAYER_Y))

            for en in enemys:
                screen.blit(enemy_car, (en['x'], en['y']))
            with open('top_score_game6.txt', 'r') as f:
                first_line = f.read()
            if score > int(first_line):
                new_data = first_line.replace(first_line, str(score))
                with open('top_score_game6.txt', 'w') as f:
                    f.write(new_data)
            record_surface = ARIAL_FONT_64.render(f'record: {first_line}', True, (255, 255, 255))
            score_surface = ARIAL_FONT_64.render(f'SCORE: {score}', True, (255, 255, 255))
            screen.blit(record_surface, [700, 20])
            screen.blit(score_surface, [20, 20])
        else:
            retry_surface = ARIAL_FONT_64.render('GAME OVER. Press R to restart', True, (255, 0, 255))
            screen.blit(retry_surface, [x // 2 - 215, y])
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


def game_7():
    # SCREEN
    WIDTH, HEIGHT = 1000, 1000
    SIZE = WIDTH, HEIGHT
    FPS = 60

    # COLORS
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    # PLATFORMS CONSTANT
    X1, Y1 = 10, HEIGHT // 2 - 50
    X2, Y2 = WIDTH - 20, HEIGHT // 2 - 50
    x, y = WIDTH // 2, HEIGHT // 2
    SPEED = 7

    # CIRCLE CONSTANT
    circle_speed = 5
    circle_x_speed = circle_speed
    circle_y_speed = 0
    circle_first_collade = False
    RADIUS = 25

    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()

    score_1 = 0
    score_2 = 0
    platform_1 = pygame.rect.Rect(X1, Y1, 10, 100)
    platform_2 = pygame.rect.Rect(X2, Y2, 10, 100)
    field_separation = pygame.draw.line(screen, (255, 255, 255), [x, 0], [x, HEIGHT], 1)
    ball = pygame.rect.Rect(x - RADIUS, y - RADIUS, RADIUS * 2, RADIUS * 2)
    ARIAL_FONT_PATH = pygame.font.match_font('arial')
    ARIAL_FONT_48 = pygame.font.Font(ARIAL_FONT_PATH, 48)
    ARIAL_FONT_36 = pygame.font.Font(ARIAL_FONT_PATH, 36)
    pygame.display.flip()
    game_over = False
    running = True
    while running:
        screen.fill(BLACK)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
                if event.key == pygame.K_r and game_over == True:
                    game_over = False
                    platform_1 = pygame.rect.Rect(X1, Y1, 10, 100)
                    platform_2 = pygame.rect.Rect(X2, Y2, 10, 100)
                    field_separation = pygame.draw.line(screen, (255, 255, 255), [x, 0], [x, HEIGHT], 1)
                    ball = pygame.rect.Rect(x - RADIUS, y - RADIUS, RADIUS * 2, RADIUS * 2)

        # Checking boundaries

        if keys[pygame.K_w]:
            platform_1.y -= SPEED

        if keys[pygame.K_s]:
            platform_1.y += SPEED

        if keys[pygame.K_UP]:
            platform_2.y -= SPEED

        if keys[pygame.K_DOWN]:
            platform_2.y += SPEED

        if not game_over:
            if platform_1.y >= 0:
                platform_1.y -= SPEED
            if platform_1.y + 100 <= HEIGHT:
                platform_1.y += SPEED
            if platform_2.y >= 0:
                platform_2.y -= SPEED
            if platform_2.y + 100 <= HEIGHT:
                platform_2.y += SPEED

            ball.x += circle_x_speed
            ball.y += circle_y_speed
            if platform_1.colliderect(ball):
                if not circle_first_collade:
                    if random.randint(0, 1) == 0:
                        circle_y_speed = circle_speed
                    else:
                        circle_y_speed = -circle_speed
                    circle_first_collade = True

                circle_x_speed = circle_speed

            if platform_2.colliderect(ball):
                if not circle_first_collade:
                    if random.randint(0, 1) == 0:
                        circle_y_speed = circle_speed
                    else:
                        circle_y_speed = -circle_speed
                    circle_first_collade = True

                circle_x_speed = -circle_speed

            pygame.draw.rect(screen, (255, 255, 255), platform_1)
            pygame.draw.rect(screen, (255, 255, 255), platform_2)
            field_separation = pygame.draw.line(screen, (255, 255, 255), [x, 0], [x, HEIGHT], 1)

            # checking the game
            if ball.bottom == HEIGHT:
                circle_y_speed = -circle_speed
            elif ball.top == 0:
                circle_y_speed = circle_speed
            elif ball.right < 0:
                game_over = True
                score_2 += 1
            elif ball.left > WIDTH:
                game_over = True
                score_1 += 1

            pygame.draw.circle(screen, (255, 0, 0), ball.center, RADIUS)
        score_surface_1 = ARIAL_FONT_48.render(str(score_1), True, WHITE)
        score_surface_2 = ARIAL_FONT_48.render(str(score_2), True, WHITE)
        if not game_over:
            screen.blit(score_surface_1, [x // 2 - score_surface_1.get_width() / 2, y])
            screen.blit(score_surface_2, [x + x // 2 - score_surface_2.get_width() / 2, y])
        else:
            if ball.left > WIDTH:
                retry_surface = ARIAL_FONT_36.render('Player 1 WIN. Press R to restart', True, WHITE)
                screen.blit(retry_surface, [x // 2, y])
            elif ball.right < 0:
                retry_surface = ARIAL_FONT_36.render('Player 2 WIN. Press R to restart', True, WHITE)
                screen.blit(retry_surface, [x // 2, y])
        clock.tick(FPS)
        pygame.display.flip()


if __name__ == "__main__":
    main_menu()
