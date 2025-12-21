# Написать функцию, которая принимает словарь и ключ, и возвращает значение по данному ключу. 
# Обработать исключение KeyError если ключа нет в словаре.

def get(dictionary: dict, key):
    try:
        return dictionary[key]
    except KeyError as error:
        print(f'There is no such key in the dictionary. Error: {error}')

dictionary = {
    'Дима': 18,
    'Олег': 25,
    'Анна': 39,
    'Ольга': 16,
    'Андрей': 19
}

print('Применим функцию, которая принимает словарь и ключ, и возвращает значение по данному ключу.')
key = input('Введите ключ: ')
print(f'Значение по данному ключу: {get(dictionary, key)}')