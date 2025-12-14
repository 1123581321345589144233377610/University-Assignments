# Дан файл f, содержащий список городов и их население. Найти город с наибольшим населением и 
# записать его название в новый файл g.

print('Это программа, которая из файла с городами с их населением, находит город с наибольшим населением и записывает \
его название в новый файл.')

biggest_city = ''
biggest_population = 0

try:
    with open('cities.txt', 'r') as file:
        for line in file:
            city, population = line.strip().split()
            if int(population) > biggest_population:
                biggest_city = city
                biggest_population = int(population)
    with open('biggest_city.txt', 'w') as file:
        file.write(biggest_city)
except FileNotFoundError as error:
    print(f'Error with finding file: {error}')