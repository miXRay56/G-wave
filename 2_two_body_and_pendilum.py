# import math
# import pygame
# import matplotlib.pyplot as plt
# import numpy as np
#
# running = True
#
# m = float(input('G*M: ')) #1500
# rc = math.sqrt((1920 / 2)**2 + (1080 / 2)**2)
# rx = float(input('r12 (x): '))#200
# ry = float(input('r12 (y): '))#200
# rx1 = float(input('r12 (x1): '))#2.5
# ry1 = float(input('r12 (y1): '))#0.5
#
# r12 = math.sqrt(rx**2 + ry**2)
# #constant = float(input('m1/m2: '))#2\
# m1 = float(input('m1: '))
# m2 = float(input('m2: '))
# constant = m1 / m2
#
# h = 1/10
#
# t = 0
#
# x1 = rc - rx * (1 / (constant + 1))
# y1 = rc - ry * (1 / (constant + 1))
# x2 = rc + rx * (1 / (1 / constant + 1))
# y2 = rc + ry * (1 / (1 / constant + 1))
#
# E = []
# L = []
# e1 = []
# e2 = []
# e3 = []
# timer = []
# pygame.init()
#
# WIDTH, HEIGHT = 1920, 1080
# WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Планета")
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# BLACK = (0, 0, 0)
#
# clock = pygame.time.Clock()
# trajectory = []
#
#
# # def draw_trajectory(pos):
# #     trajectory.append(pos)
# #     if len(trajectory) > 200:
# #         trajectory.pop(0)
# #
# #     for i in range(len(trajectory)):
# #         pygame.draw.circle(WIN, BLACK, trajectory[i], 2)
#
#
# while running:
#     rx1 = rx1 - h * m * rx / (r12**3)
#     rx = rx1 * h + rx
#     ry1 = ry1 - h * m * ry / (r12**3)
#     ry = ry1 * h + ry
#
#     x1 = rc - rx * (1 / (constant + 1))
#     y1 = rc - ry * (1 / (constant + 1))
#     x2 = rc + rx * (1 / (1 / constant + 1))
#     y2 = rc + ry * (1 / (1 / constant + 1))
#
#     x11 = constant / (1 + constant) * rx1
#     x21 = -1 / (1 + constant) * rx1
#     y11 = constant / (1 + constant) * ry1
#     y21 = -1 / (1 + constant) * ry1
#
#     WIN.fill(WHITE)
#     pygame.draw.circle(WIN, BLACK, (x1 - 150, y1 - 600), 10)
#     pygame.draw.circle(WIN, BLACK, (x2 - 150, y2 - 600), 10)
#     pygame.display.update()
#
#     r12 = math.sqrt(rx**2 + ry**2)
#     #E.append((rx1 ** 2 + ry1 ** 2) - 2 * m / r12)
#     e = m1 * (x11**2 + y11**2) / 2 + m2 * (x21**2 + y21**2) / 2 - m * m1 * m2 / r12 / (m1*m2 / (m1 + m2))
#     E.append(e)
#     e1.append(m1 * (x11**2 + y11**2) / 2)
#     e2.append(m2 * (x21**2 + y21**2) / 2)
#     e3.append(m * m1 * m2 / r12 / (m1*m2 / (m1 + m2)))
#     L.append(rx * ry1 - ry * rx1)
#     timer.append(t)
#     t += h
#     # print('E:', x, 'Cosh:', A * math.cos(w * t + f))
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
# plt.figure(figsize=(10,5))
# #plt.plot(np.array(timer), np.array(E), color='orange')
# plt.plot(np.array(timer), np.array(e1), color='blue', label='e1')
# plt.plot(np.array(timer), np.array(e2), color='black', label='e2')
# plt.plot(np.array(timer), np.array(e3), color='red', label='e3')
#
# plt.xlabel('t')
# plt.ylabel('E')
# plt.title('Graphics')
# plt.legend()
# plt.grid(True)
# plt.show()
#
# pygame.quit()

import math
import pygame
import matplotlib.pyplot as plt
import numpy as np

running = True

m = float(input('G*M: '))  # 1500
rc = math.sqrt((1920 / 2) ** 2 + (1080 / 2) ** 2)
rx = float(input('r12 (x): '))  # 200
ry = float(input('r12 (y): '))  # 200
rx1 = float(input('r12 (x1): '))  # 2.5
ry1 = float(input('r12 (y1): '))  # 0.5

r12 = math.sqrt(rx ** 2 + ry ** 2)
# constant = float(input('m1/m2: '))#2\
m1 = float(input('m1: '))
m2 = float(input('m2: '))
constant = m1 / m2
mu = m1 * m2 / (m1 + m2)
G = m / (m1 + m2)

h = 1 / 200

t = 0

x1 = rc - rx * (1 / (constant + 1))
y1 = rc - ry * (1 / (constant + 1))
x2 = rc + rx * (1 / (1 / constant + 1))
y2 = rc + ry * (1 / (1 / constant + 1))

E1 = []
E2 = []
E_mean = []
L = []
e1 = []
e2 = []
e3 = []
coef = []
timer = []
e00 = []
u00 = []
t00 = []
pygame.init()

WIDTH, HEIGHT = 1920, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Планета")
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
# l_min = 1000
# l_max = 0
# t_max = 0
# t_min = 0
# TPER = 0
# l_prev = 0


# def draw_trajectory(pos):
#     trajectory.append(pos)
#     if len(trajectory) > 200:
#         trajectory.pop(0)
#
#     for i in range(len(trajectory)):
#         pygame.draw.circle(WIN, BLACK, trajectory[i], 2)


while running:
    rx1 = rx1 - h * m * rx / (r12 ** 3)
    rx = rx1 * h + rx
    ry1 = ry1 - h * m * ry / (r12 ** 3)
    ry = ry1 * h + ry

    x1 = rc + rx * (1 / (constant + 1))
    y1 = rc + ry * (1 / (constant + 1))
    x2 = rc - rx * (1 / (1 / constant + 1))
    y2 = rc - ry * (1 / (1 / constant + 1))

    x11 = (1 / (constant + 1)) * rx1
    x21 = -(1 / (1 / constant + 1)) * rx1
    y11 = (1 / (constant + 1)) * ry1
    y21 = -(1 / (1 / constant + 1)) * ry1

    ee1 = m1 * (x11 ** 2 + y11 ** 2) / 2
    ee2 = m2 * (x21 ** 2 + y21 ** 2) / 2
    ee3 = -  G * m1 * m2 / r12
    e0 = ee1 + ee2 + ee3
    E2.append(e0)
    wer = e0

    WIN.fill(WHITE)
    pygame.draw.circle(WIN, BLACK, (x1 - 150, y1 - 600), 10)
    pygame.draw.circle(WIN, BLACK, (x2 - 150, y2 - 600), 10)
    pygame.display.update()

    # if TPER == 0:
    #     l_new = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    #     if l_new > l_prev and l_new > l_max:
    #         l_max = l_new
    #         t_max = t
    #     elif l_new < l_prev and l_new < l_min:
    #         l_min = l_new
    #         t_min = t
    #     elif l_new > l_prev and l_new < l_max:
    #         TPER = (t_min - t_max) * 4
    #         print('Period:', str(TPER/10), 'c')
    #     l_prev = l_new



    r12 = math.sqrt(rx ** 2 + ry ** 2)
    # E.append((rx1 ** 2 + ry1 ** 2) - 2 * m / r12)
    # e = m1 * (x11**2 + y11**2) / 2 + m2 * (x21**2 + y21**2) / 2 - m * m1 * m2 / r12 / (m1*m2 / (m1 + m2))

    # print(u000,t000,e000,u000/t000)

    ee1 = m1 * (x11 ** 2 + y11 ** 2) / 2
    ee2 = m2 * (x21 ** 2 + y21 ** 2) / 2
    ee3 = -  G * m1 * m2 / r12
    e0 = ee1 + ee2 + ee3
    E1.append(e0)
    wer += e0
    E_mean.append(wer / 2)
    L.append(rx * ry1 - ry * rx1)
    timer.append(t)
    t += h
    # print('E:', x, 'Cosh:', A * math.cos(w * t + f))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

plt.figure(figsize=(10, 5))
#plt.plot(np.array(timer), np.array(E1), color='orange', label='Renewed energy')
#plt.plot(np.array(timer), np.array(E2), color='red', label='Energy')
plt.plot(np.array(timer), np.array(E_mean), color='blue', label='Average energy')
# plt.plot(np.array(timer), np.array(L), color='green', label='coef')
plt.xlabel('t')

plt.ylabel('E')
plt.title('Graphics')
plt.legend()
plt.grid(True)
plt.show()


