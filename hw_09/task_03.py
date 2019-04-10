# Создать декоратор для функции, которая принимает список чисел.
# Декоратор должен производить предварительную проверку данных - удалять все четные элементы из списка.


def my_decorator(func):
    def change(lst):
        lst = [i for i in lst if not int(i) % 2 == 0]
        return func(lst)

    return change


@my_decorator
def my_func(lst):
    return lst


print(my_func([1, 2, 3, 4, 5]))