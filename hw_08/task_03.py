# Рассчитать значение х определив и использовав необходимую функции.

def y(n):
    return 1/2 * (pow(n, 1 / 2) + n)

def calc(*args):
    summ = 0
    for arg in args:
        summ += y(arg)
    return summ

print(calc(5, 12, 19))