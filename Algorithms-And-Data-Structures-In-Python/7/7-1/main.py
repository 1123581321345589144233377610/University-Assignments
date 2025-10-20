# Дана матрица размера M × N. Перед столбцом матрицы, 
# содержащим максимальное значение элемента матрицы, вставить столбец из нулей.

import random

ROWS = random.randint(1, 10)
COLS = random.randint(1, 10)

matrix = []
maxElement = None
indexOfMaxElement = 0
subIndexOfMaxElement = 0

for index in range(ROWS):
    matrix.append([])
    for subIndex in range(COLS):
        element = random.randint(-100, 100)
        matrix[index].append(element)
        if index == 0 and subIndex == 0:
            maxElement = matrix[index][subIndex]
        if element > maxElement:
            maxElement = element
            indexOfMaxElement = index
            subIndexOfMaxElement = subIndex

print(matrix)
print(f'\n{'_' * 100}\n')

for index in range(ROWS):
    matrix[index].insert(subIndexOfMaxElement, 0)

print(matrix)