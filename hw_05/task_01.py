# 1) Дана целочисленная матрица размера 5х5. Получить новую матрицу
# путем деления всех элементов данной матрицы на ее наибольший по
# модулю элемент

matrix = [
    [0, 1, 2, 3, 4],
    [5, 6, -2, 9, 4],
    [-2, 1, -1, 2, 3],
    [4, -5, 3, -1, -5],
    [1, -2, 8, 2, -3],
    [5, 1, 4, -3, -8]
]

max_i = []
for i in matrix:
    max_i.append(max(i))
    max_i.append(abs(min(i)))
c = max(max_i)
# print(c)

new_matrix = []
for horizontal in matrix:
    row = []
    for vertical in horizontal:
        row.append((vertical / c))
    new_matrix.append(row)

print(new_matrix)