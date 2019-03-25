# 5) Составить список чисел Фибоначчи содержащий 15 элементов.

number_1 = 0
number_2 = 1
i = 1
list_fib = []
while i <= 15:
    if i == 1:
        list_fib.append(i)
    else:
        number_sum = number_1 + number_2
        list_fib.append(number_sum)
        number_1 = number_2
        number_2 = number_sum
    i += 1
print(list_fib)