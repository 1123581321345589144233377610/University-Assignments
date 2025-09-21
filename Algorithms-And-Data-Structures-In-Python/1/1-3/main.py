# Вычислите сумму цифр пятизначного числа.

print("Введите пятизначное число:")
number = int(input())
sumOfDigits = 0
for i in range(5):
    sumOfDigits += (number % 10)
    number //= 10
print("Сумма цифр пятизначного числа:", sumOfDigits)