# Дан список. Используя множества, определить, есть ли дублирующиеся элементы в этом списке.

size = int(input('Введите длину списка: '))
list = [int(input()) for _ in range(size)]
print(list)
if len(set(list)) == len(list):
    print('Нет дубликатов!')
else:
    print('Есть дублирующиеся элементы!')