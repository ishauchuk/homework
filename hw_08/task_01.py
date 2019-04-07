# Написать функцию принимающая на вход неопределенным количеством аргументов и именованный аргумент mean_type.
# В зависимости от mean_type вернуть среднеарифметическое либо среднегеометрическое.
# Написать программу в виде трех функций.

def ariphmetic(lst):
    sum = 0
    for n in lst:
        sum += float(n)
    return round(sum / len(lst), 2)


def geometric(lst):
    mult = 1
    for n in lst:
        mult *= float(n)
    return round(pow(mult, 1 / len(lst)), 2)


def check_data(lst):
    for n in lst:
        if isinstance(n, str) or isinstance(n, bool) or isinstance(n,
                                                                   list) or isinstance(
            n, tuple) or isinstance(n, dict) and str(n).isdigit() == False:
            return False
    return True


def mean(*args, **kwargs):
    note = 'Wrong type of data for calculation'
    warning = 'Mean_type is not ariphmetic or geometric.Try again'
    if kwargs['mean_type'] == 'ariphmetic' and check_data(args):
        return ariphmetic(args)
    elif kwargs['mean_type'] == 'geometric' and check_data(args):
        return geometric(args)
    elif check_data(args) == False:
        return note
    else:
        return warning


print(mean(1, 2, 3, mean_type='geometric'))