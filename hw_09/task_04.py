# Создать универсальны декоратор, который меняет порядок аргументов в функции на противоположный.

def my_decorator(func):
    def change(*args):
        args = args[::-1]
        return func(*args)

    return change


@my_decorator
def my_func(*args):
    return args


print(my_func(1, 3, 5))