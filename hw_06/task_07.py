# 7) Дана целочисленная квадратная матрица. Найти в каждой строке наи-
# больший элемент и поменять его местами с элементом главной диагонали.

from random import randint

n = int(input('n: '))
matrix = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(randint(-9, 9))
    matrix.append(row)

print(matrix)

matrix_new = []
i = 0
for row in matrix:
    maxi = 0
    for number in row:
        if number > maxi:
            maxi = number
    row_new = row
    row_new[row.index(maxi)] = row[i]
    row_new[i] = maxi
    matrix_new.append(row_new)
    i += 1

print(matrix_new)
