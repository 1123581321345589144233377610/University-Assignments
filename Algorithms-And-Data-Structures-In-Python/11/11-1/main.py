# Описать функцию BinaryToDecimal, которая преобразует заданное двоичное число в десятичное число.

def binary_to_decimal(number: int) -> int:
    final_number = 0
    index_of_power = 0
    while number:
        final_number += (number % 10) * (2 ** index_of_power)
        index_of_power += 1
        number //= 10
    return final_number

print(binary_to_decimal(int('1011')))