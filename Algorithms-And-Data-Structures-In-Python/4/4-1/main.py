number = int(input('Введите натуральное число: '))
variable = float(input('Введите x: '))
product = 1
for index in range(number):
    product *= (2 * index + 1 + (index + 1) * variable)
print(f'Произведение (1 + x)(3 + 2x)... равно: {product}')