# 3) Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}). Чтобы получить список ключей - использовать метод .keys()

dct = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
list = list(dct.keys())
length = len(list)
i = 0
while i < length:
    a = len(list[i])
    b = list[i] + str(a)
    dct[b] = dct.pop(list[i])
    i += 1
print(dct)