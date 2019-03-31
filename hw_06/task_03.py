# 3) Два натуральных числа называют дружественными, если каждое из них
# равно сумме всех делителей другого, кроме самого этого числа. Найти все
# пары дружественных чисел, лежащих в диапазоне от 200 до 300.


for i in range(200, 301):
    sum1 = 0
    for number in range(1, i):
        if i % number == 0:
            sum1 += number

    sum2 = 0
    for number in range(1, sum1):
        if sum1 % number == 0:
            sum2 += number

    if i == sum2 and sum1 > i:
        print(i, sum1)