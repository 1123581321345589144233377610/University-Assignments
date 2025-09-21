# Для заданного трехзначного числа выведите число, у которого цифры идут в обратном порядке, например, 
# для числа 123 ответ 321.

print("Введите трёхзначное число:")
number = int(input())
reversedNumber = 0
for index in range(3):
    reversedNumber += (number % 10) * pow(10, 2 - index)
    number //= 10
print("Число в обратном порядке:", reversedNumber)