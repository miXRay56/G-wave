import math
import pygame
import matplotlib.pyplot as plt
import numpy as np

running = True

G = float(input('G: '))  # 5000 6000
rc = math.sqrt((1920 / 2) ** 2 + (1080 / 2) ** 2)
rx = float(input('r12 (x): '))  # 200 300
ry = 0 #float(input('r12 (y): '))  # 0
rx1 = 0 #float(input('r12 (x1): '))  # 0
ry1 = float(input('r12 (y1): '))  # 2.5 2.5

r12 = math.sqrt(rx ** 2 + ry ** 2)
m1 = float(input('m1: ')) #5 5
m2 = float(input('m2: ')) #1 2.5
constant = m1 / m2
G = G * m1 * m2 / (m1 + m2)

h = 1 / 200
c = 300000
t = 0

x1 = rc - rx * (1 / (constant + 1))
y1 = rc - ry * (1 / (constant + 1))
x2 = rc + rx * (1 / (1 / constant + 1))
y2 = rc + ry * (1 / (1 / constant + 1))

pygame.init()

WIDTH, HEIGHT = 1920, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Планета")
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
l_min = 1000
l_max = 0
t_max = 0
t_min = 0
TPER = 0
l_prev = 0

y_max1 = 0
y_min1 = 10**5
y_max2 = 0
y_min2 = 10**5

A1 = 0
A2 = 0
a1 = 0
a2 = 0
counter = False
E = 0

while running:
    rx1 = rx1 - h * G * rx / (r12 ** 3)
    rx = rx1 * h + rx
    ry1 = ry1 - h * G * ry / (r12 ** 3)
    ry = ry1 * h + ry

    x1 = rc + rx * (1 / (constant + 1))
    y1 = rc + ry * (1 / (constant + 1))
    x2 = rc - rx * (1 / (1 / constant + 1))
    y2 = rc - ry * (1 / (1 / constant + 1))

    x11 = (1 / (constant + 1)) * rx1
    x21 = -(1 / (1 / constant + 1)) * rx1
    y11 = (1 / (constant + 1)) * ry1
    y21 = -(1 / (1 / constant + 1)) * ry1

    WIN.fill(WHITE)
    pygame.draw.circle(WIN, BLACK, (x1 - 150, y1 - 600), 10)
    pygame.draw.circle(WIN, BLACK, (x2 - 150, y2 - 600), 10)
    pygame.display.update()

    if TPER == 0:
        l_new = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        if l_new > l_prev and l_new > l_max:
            l_max = l_new
            t_max = t
        elif l_new < l_prev and l_new < l_min:
            l_min = l_new
            t_min = t
        elif l_prev < l_new < l_max:
            TPER = (t_min - t_max) * 6
            print('Period:', str(round(TPER / 10, 1)), 'c')
        l_prev = l_new

        if y1 > y_max1:
            y_max1 = y1
        elif y1 < y_min1:
            y_min1 = y1

        if y2 > y_max2:
            y_max2 = y2
        elif y2 < y_min2:
            y_min2 = y2

        E += m1 * (x11 ** 2 + y11 ** 2) / 2 + m2 * (x21 ** 2 + y21 ** 2) / 2 + G * m1 * m2 / r12

    if TPER != 0 and not counter:
        A1 = m2 * (l_min + l_max) / (2 * (m1 + m2))
        A2 = m1 * (l_min + l_max) / (2 * (m1 + m2))
        a1 = (y_max1 - y_min1) / 2
        a2 = (y_max2 - y_min2) / 2
        counter = True
        # print('A1', A1)
        # print('A2', A2)
        # print('a1', a1)
        # print('a2', a2)
        e1 = math.sqrt(1 - a1**2 / A1**2)
        e2 = math.sqrt(1 - a2**2 / A2**2)
        w1 = 32 * (G**4) * (m1**2) * (m2**2) * (m1 + m2) * (1 + 73 * e1**2 / 24 + 37 * e1**4 / 96) / (5 * c**5 * A1**5) * (1 - e1**2)**(7/2)
        w2 = 32 * (G ** 4) * (m1 ** 2) * (m2 ** 2) * (m1 + m2) * (1 + 73 * e2 ** 2 / 24 + 37 * e2 ** 4 / 96) / (
                    5 * c ** 5 * A2 ** 5) * (1 - e2 ** 2) ** (7 / 2)
        print('Энергетические потери составляют:', f'{(100 * (w1 + w2) * TPER / E / 2):.2e}', '%')

    r12 = math.sqrt(rx ** 2 + ry ** 2)
    t += h



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()



