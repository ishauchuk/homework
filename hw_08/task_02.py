# Дан список чисел. Посчитать сколько раз встречается каждое число.
# Подсказка: для хранения данных использовать словарь.
# Для проверки нахождения элемента в словаре использовать метод get()

def count(*args):
    dct = {}
    for arg in args:
        if isinstance(arg, int) or isinstance(arg, float):
            if dct.get(arg):
                dct[arg] += 1
            else:
                dct[arg] = 1
    return dct


print(count(1, 2, 1, 3, 3, 3, 3.5, 'a'))