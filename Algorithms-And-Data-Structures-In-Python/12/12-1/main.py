# Описать функцию CountSublists, которая принимает список и возвращает количество вложенных 
# списков внутри него.

def count_sublists(current_list) -> int:
    count = 0
    for element in current_list:
        if isinstance(element, list):
            count += 1 + count_sublists(element)
    return count

print(count_sublists([[1, 2], [2, [2, [4, 12]]]]))