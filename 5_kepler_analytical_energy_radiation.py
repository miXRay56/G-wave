import matplotlib.pyplot as plt
import numpy as np
import array
import math
X = []
Y = []
R= []
F = []
N = 3000000
a = np.pi
k = 2*a/N
m_Sun= 1.98892*1e30
m1= m_Sun
m2= 5.9722*1e24
F = np.arange(a/3, 5*a/3, k)
e=0.016
per=147000000000
ap = 152000000000
b2 = (147.098290+152.098232)*1e9/2
b = math.sqrt(b2**2-((e**2)*(b2**2)))
p=b**2/b2
G = 6.67259e-11
c= 2.99792458*1e8
E = G*m1*m2/(2*b2)
print("Полная энергия системы (по модулю):", E, "Дж")
T = 2 * np.pi * math.sqrt(b2**3/(G*m1))
dE1 = (32*(G**4)*(m1**2)*(m2**2)*(m1+m2))/(5*(c**5)*(b2**5)*((1-e**2)**3.5))*(1+(73/24*e**2)+(37/96)*e**4)
print("Мощность гравитационного излучения:", dE1, "Вт")
print("Потеря энергии за период:", dE1*T, "Дж")
R = p/(1-e*np.cos(F))
param =2
X=R*np.cos(F)
Y=R*np.sin(F)
plt.plot(X, Y,'r')
plt.show()
