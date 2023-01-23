import pygame
import random
import os
import sys

WIDTH = 1000
HEIGHT = 1000
FPS = 60
player_x = 500
player_y = 500
player_speed_y = 0
gravity = 0.25
game_speed = -1.5
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
    else:
        screen.fill((0, 0, 0))
        screen.blit(text_over, (180, 480))


    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
