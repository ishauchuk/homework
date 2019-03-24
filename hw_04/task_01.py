# 1) Дан список целых чисел.
# Создать новый список, каждый элемент которого равен исходному элементу умноженному на -2


list_old = [1, 2, 3, 4, 5]
i = 0
lenght = len(list_old)
while i < lenght:
    list_old[i] = list_old[i] * (-2)
    i += 1
print (list_old)