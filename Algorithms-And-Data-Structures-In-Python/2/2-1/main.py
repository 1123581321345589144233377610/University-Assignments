# Введите строку, состоящую из 2 цифр. Преобразуйте ее в целое и вещественное число. 
# Выведите полученные 3 значения (строку, целое число, вещественное число) на экран в одной строке через запятую, 
# затем пропустите строку и вновь выведите значения по одному на строке. 
# Перед каждым значением выведите его тип.

string = str(input("Введите строку, состоящую из 2 цифр: "))
integerNumber = int(string)
floatNumber = float(string)
print(f"{string}, {integerNumber}, {floatNumber}\n")
print(f"{type(string)}: {string}\n{type(integerNumber)}: {integerNumber}\n{type(floatNumber)}: {floatNumber}")