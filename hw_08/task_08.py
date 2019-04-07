# Даны три слова. Выяснить, является ли хоть одно из них палиндромом ("перевертышем"), т. е. таким,
# которое читается одинаково слева направо и справа налево.
# (Определить функцию, позволяющую распознавать слова палиндромы.)

def palindrom(string):
    if string == string[::-1]:
        return True
    return False


def check(*args):
    count = 0
    result = True
    for arg in args:
        if palindrom(arg):
            count += 1
            result = True
        else:
            result = False
    return result, f'amount palindroms is: {count}'


print(check('abba', 'apple', 'blabla', 'madam'))