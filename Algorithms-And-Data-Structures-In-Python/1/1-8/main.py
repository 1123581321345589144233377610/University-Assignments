# Разработать программу вычисления радиуса круга и его площади по известной длине окружности.

from math import pi

while True:
    circleLength = float(input("Введите длину окружности: "))
    if circleLength < 0:
        print("Длина окружности не может быть отрицательной!")
    else:
        break
print("Радиус круга:", circleLength / (2 * pi))
print("Площадь круга:", (pow(circleLength, 2)) / (4 * pi))