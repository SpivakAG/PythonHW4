# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа
n = int(input('Введите число: '))

print('Простые делители:')

for i in range(n - 1, 1, -1):
    prost = 0
    if (n % i == 0):
        for j in range(i - 1, 1, -1):
            if (i % j == 0):
                prost = prost + 1
        if (prost == 0):
            print(i, end=' ')