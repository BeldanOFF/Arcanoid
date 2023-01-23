import random
import pygame
import os
import sys

pygame.init()

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
    last = f1.render(f'RECORD: {max_last}', True,
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

        print(len(serds))

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

        if len(str_last) == 6:
            screen.blit(last, (700, 50))
        elif len(str_last) == 5:
            screen.blit(last, (710, 50))
        elif len(str_last) == 4:
            screen.blit(last, (720, 50))
        elif len(str_last) == 3:
            screen.blit(last, (730, 50))
        elif len(str_last) == 2:
            screen.blit(last, (740, 50))
        elif len(str_last) == 1:
            screen.blit(last, (750, 50))

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
