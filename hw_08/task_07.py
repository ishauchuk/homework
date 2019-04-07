# Описать функцию fact2( n ) вещественного типа, вычисляющую двойной факториал :n!! = 1·3·5·...·n, если n — нечетное;
# n!! = 2·4·6·...·n, если n — четное (n > 0 — параметр целого типа.
# С помощью этой функции найти двойные факториалы пяти данных целых чисел

def fact2(n):
    if n < 0:
        return 'Wrong number'
    i = n
    result = 1
    while i > 0:
        result *= i
        i -= 2
    return result


def result(*args):
    dct = {}
    for arg in args:
        dct[arg] = fact2(arg)
    return dct


print(result(1, 2, 3, 4, 6))
