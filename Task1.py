# Вычислить результат деления двух чисел c заданной точностью d
a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
d = float(input('Задайте точность деления: '))


def okrug(x, y, z):
    if z <= 10**(-1) and z >= 10**(-10):
        res = x/y
        osn = 1
        while z < 0.1:
            z *= 10
            osn += 1
        res = round(res, osn)
        return res
    else:
        return 'd должно быть 0,1 >= d >= 0.0000000001'


print(okrug(a, b, d))
