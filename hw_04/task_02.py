# 2) Дан список целых чисел. Подсчитать сколько четных чисел в списке

list_1 = [1, 2, 3, 4, 5]
i = 0
count = 0
lenght = len(list_1)
while i < lenght:
    if list_1[i] % 2 == 0:
        count += 1
    i += 1
print(count)