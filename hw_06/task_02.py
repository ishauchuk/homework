# 2) Дано число. Найти сумму и произведение его цифр.

n = input('write the number ')
length = len(n)
i = 0
sum = 0
mult = 1
while i < length:
    sum += int(n[i])
    mult *= int(n[i])
    i += 1
print(sum, mult)