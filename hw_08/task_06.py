# Дан массив целых чисел A. Найти суммы положительных и
# отрицательных элементов массива, используя функцию определения суммы.

def sum(a, b):
    return a + b


def A(lst):
    sum1 = 0
    sum2 = 0
    for i in lst:
        if i > 0:
            sum1 = sum(sum1, i)
        else:
            sum2 = sum(sum2, i)
    return sum1, sum2


print(A([1, 2, -1, -2, 3]))