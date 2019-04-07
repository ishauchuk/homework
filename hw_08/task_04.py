# Написать функцию по решению квадратных уравнений.

def discriminant(dct):
    return float(pow(dct['b'], 2) - 4 * dct['a'] * dct['c'])


def result(**kwargs):
    warning = 'There is no solution'
    if kwargs.get('a'):
        if kwargs.get('b') is None and kwargs.get('c') is None:
            n1 = 0
            return n1
        else:
            if kwargs.get('b') is None:
                kwargs['b'] = 0
            if kwargs.get('c') is None:
                kwargs['c'] = 0
            if discriminant(kwargs) > 0:
                n1 = float(
                    (-kwargs.get('b') + pow(discriminant(kwargs), 1 / 2)) / (
                            2 * kwargs.get('a')))
                n2 = float(
                    (-kwargs.get('b') - pow(discriminant(kwargs), 1 / 2)) / (
                            2 * kwargs.get('a')))
                return n1, n2
            elif discriminant(kwargs) == 0:
                return float(-kwargs.get('b') / (2 * kwargs.get('a')))
            else:
                return warning
    else:
        return 'It is not quadratic equation'


print(result(a=3, b=-14, c=-5))