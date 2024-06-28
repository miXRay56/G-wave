import math
import pygame
import matplotlib.pyplot as plt
import numpy as np

fps = 60
running = True
m = 1

timer = []
e = []
c = []
E = []
delta = []
x00 = 1000
x = float(input('Значение x в нулевой момент времени: '))
x1 = float(input('Значение первой производной x в нулевой момент времени: '))
w = float(input('w (частота): '))
h = float(input('Шаг по времени: '))
l = float(input('Коэффициент затухания: '))
#x = x0
A = math.sqrt(x**2 + (x1 / w)**2)
f = math.atan(-x1/(x * w))
t = 0

pygame.init()

WIDTH, HEIGHT = 1920, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Сравнение")
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

while running:
    x1 = x1 - h * (w**2) * x #- h * l * x1
    x = x1 * h + x

    #dt = clock.tick(fps) / 1000  # время между кадрами

    WIN.fill(WHITE)
    pygame.draw.circle(WIN, BLACK, (x + x00, HEIGHT//3), 10)
    # pygame.draw.circle(WIN, BLACK, (A * math.cos(w * t + f) * math.e**(-l/2*t) + x00, 2 * (HEIGHT // 3)), 10)
    pygame.draw.circle(WIN, BLACK, (A * math.cos(w * t + f) + x00, 2 * (HEIGHT // 3)), 10)

    pygame.display.update()


    e.append(x)
    c.append(-(A * math.cos(w * t + f) ))
    delta.append(abs(x - A * math.cos(w * t + f)))
    timer.append(t)
    E.append(m * x1**2 / 2 + m / w**2 * (A - abs(x)))
    t += h

    # print('E:', x, 'Cosh:', A * math.cos(w * t + f))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

plt.plot(np.array(timer), np.array(e), label='Eyler method', color='orange')
plt.plot(np.array(timer), np.array(c), label='Oscillator equation', color='green')
plt.xlabel('t')
plt.ylabel('x')
plt.title('Comparison')
plt.legend()
plt.grid(True)
plt.show()

plt.plot(np.array(timer), np.array(delta), color='orange')
plt.xlabel('t')
plt.ylabel('delta_x')
plt.title('Mismatch')
plt.legend()
plt.grid(True)
plt.show()
