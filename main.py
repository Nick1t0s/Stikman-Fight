# Pygame шаблон - скелет для нового проекта Pygame
import pygame
from pygame.locals import *
import random

WIDTH = 1050
HEIGHT = 600
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stikman Party")
clock = pygame.time.Clock()
menu=pygame.image.load('data/Расход/патроны.png')

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type==KEYDOWN:
            if event.key== K_LEFT:
                print(1)
            if event.key == K_RIGHT:
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.blit(menu,(0,0))

    # Обновление

    # Рендеринг
    screen.fill(BLACK)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()