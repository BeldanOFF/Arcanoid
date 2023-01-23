import pygame
import random

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
            if event.key == pygame.K_r:
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
