# Разработать программу по вычислению площади кольца по известным значениям его внешнего и внутреннего радиусов.

from math import pi

outerRadius = float(input("Введите внешний радиус: "))
innerRadius = float(input("Введите внутренний радиус: "))
print("Площадь кольца:", pi * (pow(outerRadius, 2) - pow(innerRadius, 2)))