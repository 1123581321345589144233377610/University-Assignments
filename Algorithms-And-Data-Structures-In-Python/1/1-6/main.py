# Разработать программу вычисления по известному радиусу площади круга и длины окружности.

from math import pi

while True:
    radius = float(input("Введите радиус: "))
    if radius < 0:
        print("Радиус должен быть неотрицательным!")
    else:
        break
print("Площадь круга:", pi * pow(radius, 2))
print("Длина окружности:", 2 * pi * radius)