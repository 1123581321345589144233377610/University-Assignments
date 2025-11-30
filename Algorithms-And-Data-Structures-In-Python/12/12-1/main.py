# Описать функцию CountSublists, которая принимает список и возвращает количество вложенных 
# списков внутри него.

def count_sublists(current_list) -> int:
    count = 0
    for element in current_list:
        if isinstance(element, list):
            count += 1 + count_sublists(element)
    return count

list_of_lists = [[[1, 2], 10], [2, [2, [4, 12]]]]
print('Функция, которая принимает список и возвращает количество вложенных списков внутри него')
print(f'На примере {list_of_lists}. Должно выдать: 5')
print(f'Результат: {count_sublists(list_of_lists)}')