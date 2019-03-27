# 2)Для каждого натурального числа в промежутке от m до n вывести все делители, кроме единицы и самого числа. m и n вводятся с клавиатуры.
# Пример:m =100, n = 105

n = int(input('N: '))
m = int(input('M: '))

for i in range(n, m + 1):
    row = []
    for f in range(2, i):
        if i % f == 0:
            row.append(str(f))
    string_1 = ' '.join(row)

    print(str(i) + ':', string_1)