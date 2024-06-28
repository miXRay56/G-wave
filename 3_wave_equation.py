import pygame
import numpy as np
import time

# Параметры экрана
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 1080
FPS = 100
COM = True
# Параметры струны
NUM_POINTS = 100  # количество точек на струне
DAMPING = 0 # коэффициент затухания
TIME_STEP = 0.1 # шаг по времени
C = 10 #light speed
X_STEP = SCREEN_WIDTH // (NUM_POINTS - 1)
SCALE = 50

# Создание экрана Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Wave simulation')

# Инициализация переменных для волнового процесса
u = np.zeros(NUM_POINTS)  # текущее положение струны
u_prev = np.zeros(NUM_POINTS)  # предыдущее положение струны

# Начальное возмущение (просто для примера)
u[NUM_POINTS // 2] = 1
u_prev[NUM_POINTS // 2] = 1

clock = pygame.time.Clock()
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Решение волнового уравнения методом Эйлера
    for i in range(0, NUM_POINTS - 1):
        u_next = 2 * u[i] - u_prev[i] + C**2 * TIME_STEP**2 / X_STEP**2 * (u[i - 1] - 2 * u[i] + u[i + 1]) - DAMPING * (u[i] - u_prev[i])
        u_prev[i] = u[i]
        u[i] = u_next

    u_next = 2 * u[NUM_POINTS - 1] - u_prev[NUM_POINTS - 1] + C ** 2 * TIME_STEP ** 2 / X_STEP ** 2 * (
                u[NUM_POINTS - 2] - 2 * u[NUM_POINTS - 1] + u[0]) - DAMPING * (u[NUM_POINTS - 1] - u_prev[NUM_POINTS - 1])
    u_prev[NUM_POINTS - 1] = u[NUM_POINTS - 1]
    u[NUM_POINTS - 1] = u_next

    # Отрисовка
    screen.fill((0, 0, 0))  # очистка экрана

    # if COM:
    #     time.sleep(5)
    #     COM = False

    # Рисование струны
    for i in range(NUM_POINTS - 1):
        x1 = i * X_STEP
        x2 = (i + 1) * X_STEP
        y1 = int(SCREEN_HEIGHT / 2 - u[i] * SCALE)
        y2 = int(SCREEN_HEIGHT / 2 - u[i + 1] * SCALE)
        pygame.draw.line(screen, (255, 255, 255), (x1, y1), (x2, y2), 2)
    pygame.display.flip()

    # Ограничение частоты кадров
    clock.tick(FPS)


pygame.quit()
