# 1) Написать программу, в которой вводятся два операнда Х и Y и знак операции
# sign (+, –, /, *). Вычислить результат Z в зависимости от знака. Предусмотреть
# реакции на возможный неверный знак операции, а также на ввод Y=0 при делении.
# Организовать возможность многократных вычислений без перезагрузки программа
# (т.е. построить бесконечный цикл). В качестве символа прекращения вычислений
# принять ‘0’ (т.е. sign='0').
while True:
    x = int(input('X: '))
    y = int(input('Y: '))
    sign = input('+, –, /, * ')

    if sign == '+':
        result = x + y
        print(result)
    elif sign == '-':
        result = x - y
        print(result)
    elif sign == '/':
        if y == 0:
            print('error')
        else:
            result = x / y
            print(result)
    elif sign == '*':
        result = x * y
        print(result)
    elif sign == '0':
        break
    else:
        print('choose another sign')