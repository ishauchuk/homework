# 2. Написать программу, со следующим интерфейсом: пользователю предоставляется на выбор 12 вариантов
# перевода(описанных в первой задаче). Пользователь вводит цифру от одного до двенадцати.
# После программа запрашивает ввести численное значение.
# Затем программа выдает конвертированный результат. Использовать функции из первого задания.
# Программа должна быть в бесконечном цикле. Код выхода из программы - “0”.

import task_01

while True:
    n = int(input("enter number: "))
    while n <= 0:
        n = int(input("Achtung, alarm!!11 Enter number more than zero: "))
    a = int(input("enter number for calculation:\n1 - Дюймы в сантиметры\n2 - Сантиметры в дюймы\n3 - Мили в километры\n4 - Километры в мили\n5 - Фунты в килограммы\n6 - Килограммы в фунты\n7 - Унции в граммы\n8 - Граммы в унции\n9 - Галлон в литры\n10 - Литры в галлоны\n11 - Пинты в литры\n12 - Литры в пинты\n"))

    if a == 0:
        break
    elif a > 12:
        print('Wrong number')
    elif a == 1:
        print(task_01.inch_to_cm(n))
    elif a == 2:
        print(task_01.cm_to_inch(n))
    elif a == 3:
        print(task_01.miles_to_km(n))
    elif a == 4:
        print(task_01.km_to_miles(n))
    elif a == 5:
        print(task_01.lb_to_kg(n))
    elif a == 6:
        print(task_01.kg_to_lb(n))
    elif a == 7:
        print(task_01.oz_to_g(n))
    elif a == 8:
        print(task_01.g_to_oz(n))
    elif a == 9:
        print(task_01.gallon_to_l(n))
    elif a == 10:
        print(task_01.l_to_gallon(n))
    elif a == 11:
        print(task_01.pint_to_l(n))
    elif a == 12:
        print(task_01.l_to_pint(n))