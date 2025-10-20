# Дан список. Обнулить все четные числа, содержащиеся в списке. 
# Если четные числа в списке отсутствуют, то оставить список без изменений.

list = [number for number in range(101)]
print(f'Начальный список: {list}\n\n{'_' * len(list)}\n\n')
for index in range(len(list)):
    if list[index] % 2 == 0:
        list[index] = 0
print(f'Конечный список: {list}\n\n')