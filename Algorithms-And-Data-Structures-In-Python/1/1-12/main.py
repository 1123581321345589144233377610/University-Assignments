# Пусть пользователь вводит 5 чисел: а, b, c, d, e. 
# Реализуйте программу расчета выражения вида res = (a + bc) / (2d - e)+ Ost[be / c] , где Ost – означает остаток от деления. 
# Учесть невозможность деления на 0.

a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))
d = float(input("Введите d: "))
e = float(input("Введите e: "))

if 2 * d - e == 0:
    print("2 * d - e == 0, a на ноль делить нельзя!")
    exit()
elif c == 0:
    print("с == 0, a на ноль делить нельзя!")
    exit()
else:
    result = ((a + b * c) / (2 * d - e)) + (pow(b, e) % c)
    print(f"Результат: {result}!")