# Напишите программу, которая удаляет все элементы из словаря, у которых ключи не начинаются с заданной буквы.

dictionary = {'milk': 50, 'banana': 100, 'bread': 30, 'chocolate': 120, 'water': 20, 'watermelon': 300}
print(dictionary, end = '\n\n')
character = input('Введите букву на которую должны начинаться ключи от a-z: ')
print()
list_of_items_to_delete = []
for item in dictionary:
    if item[0] != character:
        list_of_items_to_delete.append(item)

for item_to_delete in list_of_items_to_delete:
    del dictionary[item_to_delete]

print(dictionary)