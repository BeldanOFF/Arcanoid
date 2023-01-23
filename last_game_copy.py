import pygame
import random
import os, sys
import math

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
            if event.key == pygame.K_r:
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
        score_surface = ARIAL_FONT_64.render(f'SCORE: {score}', True, (255, 255, 255))
        screen.blit(score_surface, [20, 20])
    else:
        retry_surface = ARIAL_FONT_64.render('GAME OVER. Press R to restart', True, (255, 0, 255))
        screen.blit(retry_surface, [x // 2 - 215, y])
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
