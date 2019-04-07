# Описать функцию is_power_n( k , n ) логического типа, возвращающую True,
# если целый параметр k (> 0) является степенью числа n (> 1), и False в противном случае.
# Дано число n (> 1) и набор из 10 целых положительных чисел.
# С помощью функции is_power_n найти количество степеней числа N в данном наборе.


def is_power_n(k, n):
    while k > 1:
        k = k / n
    if k == 1:
        return True
    else:
        return False


def check(N, lst):
    if N < 1:
        return 'N is less than 1'
    if len(lst) != 10:
        return 'List is less than 10 elements'
    count = 0
    for i in lst:
        if is_power_n(i, N):
            count += 1
    return count


print(check(3, [10, 25, 9, 32, 64, 121, 144, 169, 81, 27]))