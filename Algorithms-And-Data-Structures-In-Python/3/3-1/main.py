# Определить, является ли число n простым.

def IsPrime(number):
    if number == 1:
        return False
    index = 2
    while index <= pow(number, 0.5):
        if number % index == 0:
            return False
        index += 1
    return True

number = int(input('Введите число, которое хотите проверить на простоту: '))
if IsPrime(number):
    print(f'Число {number} простое!')
else:
    print(f'Число {number} составное!')
