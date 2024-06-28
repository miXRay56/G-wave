import math
import pygame
import matplotlib.pyplot as plt
import numpy as np

running = True

G = 1500
rc = math.sqrt((1920 // 2)**2 + (1080 // 2)**2)
rx = 200
ry = 200
rx1 = 2.5
ry1 = 0.5

r12 = math.sqrt(rx**2 + ry**2)
m1 = 2
m2 = 1
m3 = 1
constant = m1 / m2

h = 0.05

t = 0

x1 = rc - rx * (1 / (constant + 1))
y1 = rc - ry * (1 / (constant + 1))
x2 = rc + rx * (1 / (1 / constant + 1))
y2 = rc + ry * (1 / (1 / constant + 1))

WIDTH, HEIGHT = 1920, 1080

x_occ = 0
y_occ = HEIGHT // 2
x1_occ = 0
w = 0.1
l = 0.00001
ft = 0
c = 1000

timer = []
pygame.init()
xxx = []
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Планета")
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
trajectory = []
E = []
e_k = []
e_p = []

# def draw_trajectory(pos):
#     trajectory.append(pos)
#     if len(trajectory) > 200:
#         trajectory.pop(0)
#
#     for i in range(len(trajectory)):
#         pygame.draw.circle(WIN, BLACK, trajectory[i], 2)
r1_occ = math.sqrt((x_occ - x1 - 1450)**2 + (y_occ - y1 - 560)**2)
r2_occ = math.sqrt((x_occ - x2 - 1450)**2 + (y_occ - y2 - 560)**2)
f1 = G * m1 * m3 / r1_occ**2
f2 = G * m2 * m3 / r2_occ**2
f1x = G * m1 * m3 * (x_occ - x1 - 1450) / r1_occ**3
f2x = G * m2 * m3 * (x_occ - x2 - 1450) / r2_occ**3
f0 = f1x + f2x

f_res = 0

K = 1
while running:
    rx1 = rx1 - h * (c * f_res + G * (m1 + m2) * rx / (r12**3))
    rx = rx1 * h + rx
    ry1 = ry1 - h * G * (m1 + m2) * ry / (r12**3)
    ry = ry1 * h + ry

    x1 = rc - rx * (1 / (constant + 1))
    y1 = rc - ry * (1 / (constant + 1))
    x2 = rc + rx * (1 / (1 / constant + 1))
    y2 = rc + ry * (1 / (1 / constant + 1))

    x11 = constant / (1 + constant) * rx1
    x21 = -1 / (1 + constant) * rx1
    y11 = constant / (1 + constant) * ry1
    y21 = -1 / (1 + constant) * ry1

    r1_occ = math.sqrt((x_occ - x1 - 1450) ** 2 + (y_occ - y1 - 560) ** 2)
    r2_occ = math.sqrt((x_occ - x2 - 1450) ** 2 + (y_occ - y2 - 560) ** 2)
    f1 = G * m1 * m3 / r1_occ ** 2
    f2 = G * m2 * m3 / r2_occ ** 2
    f1x = G * m1 * m3 * (x_occ - x1 - 1450) / r1_occ ** 3
    f2x = G * m2 * m3 * (x_occ - x2 - 1450) / r2_occ ** 3
    ft = f1x + f2x - f0

    f_res = ft

    x1_occ = x1_occ - h * (w ** 2) * x_occ - h * l * x1_occ - c * ft * h / m3
    x_occ = x1_occ * h + x_occ
    WIN.fill(WHITE)

    f1 = pygame.font.Font(None, 54)
    text = f1.render('x = ' + str(round(x_occ + 1300, 3)), True, BLACK)
    place = text.get_rect(center=(x_occ + 1250, y_occ - 80))
    WIN.blit(text, place)

    pygame.draw.line(WIN, BLACK, (1300, y_occ - 40), (x_occ*100 + 1200, y_occ - 40))
    pygame.draw.circle(WIN, BLACK, (x1 - 150, y1 - 600), 10)
    pygame.draw.circle(WIN, BLACK, (x2 - 150, y2 - 600), 10)
    pygame.draw.circle(WIN, BLACK, (x_occ*100 + 1200, y_occ - 40), 10)
    #print(x_occ, y_occ)
    pygame.display.update()

    r12 = math.sqrt(rx**2 + ry**2)
    a = m3 * x1_occ**2 / 2 + m3 * w**2 * x_occ**2 / 2
    E.append(a)
    e_k.append(m3 * x1_occ**2 / 2)
    e_p.append(m3 * w**2 * x_occ**2 / 2)
    xxx.append(x_occ)
    timer.append(t)
    t += h

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

plt.plot(np.array(timer), np.array(E), color='blue', label='E')
plt.plot(np.array(timer), np.array(e_k), color='red', label='e_k')
plt.plot(np.array(timer), np.array(e_p), color='orange', label='e_p')
# plt.plot(np.array(timer), np.array(xxx), color='blue', label='x(t)')

plt.xlabel('t')
plt.ylabel('E')
plt.title('Graphics')
plt.legend()
plt.grid(True)
plt.show()

pygame.quit()


plt.plot(np.array(timer), np.array(xxx), color='blue', label='x(t)')

plt.xlabel('t')
plt.ylabel('x')
plt.title('Graphics')
plt.legend()
plt.grid(True)
plt.show()

pygame.quit()
