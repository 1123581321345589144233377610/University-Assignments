# Описать рекурсивную функцию CountUppercase, находящую количество прописных букв в строке S без использования оператора цикла.
# С помощью этой функции найти количество прописных букв в заданной строке.

def count_uppercase(string: str) -> int:
    if not string:
        return 0
    return (1 if string[0].isupper() else 0) + count_uppercase(string[1:])

example = input('Введите строку у которой хотите вычеслить количество прописных букв: ')
print(f'Кол-во прописных букв равно: {count_uppercase(example)}')