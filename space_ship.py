import pygame
import random
import os, sys
import math

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
            if event.key == pygame.K_r:
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
        score_surface = ARIAL_FONT_64.render(f'score: {score}', True, (255, 255, 255))
        screen.blit(score_surface, [20, 20])
    else:
        retry_surface = ARIAL_FONT_64.render(f'Game Over. Your score: {score}', True, (255, 255, 255))
        screen.blit(retry_surface, [100, y])
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
