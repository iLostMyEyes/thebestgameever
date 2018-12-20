import pygame
import random

print("Gamers rise up!")

pygame.init()
MAX_HEIGHT = 300
MAX_WIDTH = 480
screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
done = False
is_blue = True
x = MAX_WIDTH / 2
y = MAX_HEIGHT / 2
points = 0
font = pygame.font.SysFont("comicsansms", 14)
clock = pygame.time.Clock()
SPEED = 5

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
    pygame.display.flip()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= SPEED
    if pressed[pygame.K_DOWN]: y += SPEED
    if pressed[pygame.K_LEFT]: x -= SPEED
    if pressed[pygame.K_RIGHT]: x += SPEED
    if (x < 0):
        x += MAX_WIDTH
    if (x > MAX_WIDTH):
        x -= MAX_WIDTH
    if (y < 0):
        y += MAX_HEIGHT
    if (y > MAX_HEIGHT):
        y -= MAX_HEIGHT
    if is_blue:
        color = (0, 128, 255)
    else:
        color = (255, 100, 0)
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
    text = font.render(("Score: " + str(points)), True, (255, 255, 255))
    points += random.randint(1, 420)
    screen.blit(text, (0, 0))
    clock.tick(60)
