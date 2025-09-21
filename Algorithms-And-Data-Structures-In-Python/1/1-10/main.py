# Имеются два n – мерных вектора x и y, которые задают координаты n точек на плоскости (случайные целые числа). 
# Найти наиболее близкие друг другу точки.

import random 
import math

n = int(input("Введите кол-во точек: "))
x = [random.randint(-100, 100) for _ in range(n)]
y = [random.randint(-100, 100) for _ in range(n)]
print("Сгенерированные точки:")
for index in range(n):
    print(f"Точка {index+1}: ({x[index]}, {y[index]})")
minDistance = float('inf')
point1 = None
point2 = None
for index in range(n):
    for subIndex in range(index + 1, n):
        distance = math.sqrt(pow(x[index] - x[subIndex], 2) + pow(y[index] - y[subIndex], 2))
        if distance < minDistance:
            minDistance = distance
            point1 = (x[index], y[index])
            point2 = (x[subIndex], y[subIndex])
            index1 = index + 1
            index2 = subIndex + 1
print(f"\nНаиболее близкие точки: {index1} и {index2}")
print(f"Координаты точки {index1}: {point1}")
print(f"Координаты точки {index2}: {point2}")
print(f"Расстояние между ними: {"%.4f" % minDistance}")