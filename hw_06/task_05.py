# 5) В массиве целых чисел с количеством элементов 19 определить максимальное число и заменить им все четные по значению элементы.

from random import randint

i = 1
lst = []
while i <= 19:
    lst.append(randint(-9, 9))
    i+=1

print(lst)

max_i = 0
for i in lst:
    if i > max_i:
        max_i = i

lst_new=[]
for number in lst:
    if abs(number) % 2 == 0:
        lst_new.append(max_i)
    else:
        lst_new.append(number)
print(lst_new)