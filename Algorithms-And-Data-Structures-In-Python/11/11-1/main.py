# Описать функцию BinaryToDecimal, которая преобразует заданное двоичное число в десятичное число.

def binary_to_decimal(number: int) -> int:
    copy_number = number
    while copy_number:
        if copy_number % 10 == 0 or copy_number % 10 == 1:
            copy_number //= 10
            continue
        else:
            raise ValueError
    final_number = 0
    index_of_power = 0
    while number:
        final_number += (number % 10) * (2 ** index_of_power)
        index_of_power += 1
        number //= 10
    return final_number

number = int(input('Введите число: '))
print(f'Проверим преобразование заданного двоичного числа в десятичное число')
try:
    print(f'Результат: {binary_to_decimal(number)}')
except ValueError:
    print('Ошибка! Число не в двоичном виде!')