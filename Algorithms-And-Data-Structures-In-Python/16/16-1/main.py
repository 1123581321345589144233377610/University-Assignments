# В первом файле хранятся данные о транзакциях на банковском счете в формате «дата: сумма: описание». 
# Найти суммарную сумму всех транзакций и записать ее в новый файл.

print('Это программа, которая считает сумму всех транзакций на банковском счёте, заданных в файле.')

try:
    total_sum = 0
    with open('transactions.txt') as file:
        for line in file:
            date, amount, description = line.strip().split(':')
            total_sum += float(amount)
    with open('total_sum.txt', 'w') as file:
        file.write(str(total_sum))
except FileNotFoundError as error:
    print(f'Error with finding file: {error}')