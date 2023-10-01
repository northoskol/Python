"""Задача №45.
Решение в группах Два различных натуральных числа n и m называются дружественными,
если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот.
Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел,
каждое из которых не превосходит k. Программа получает на вход одно натуральное число k,
не превосходящее 105. Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k.
Пары необходимо выводить по одной в строке, разделяя пробелами.
Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
Ввод: 300
Вывод:  220 284"""


def divisor_sum(number):
    div_sum = 1
    i = 2
    while i * i <= number:
        if number % i == 0:
            if i == number // i:
                div_sum += i
            else:
                div_sum += i
                div_sum += number // i
        i += 1
    return div_sum


def friendly_num(number):
    lst = list()
    for i in range(1, number + 1):
        divisor_sum1 = divisor_sum(i)
        if divisor_sum1 <= number:
            divisor_sum2 = divisor_sum(divisor_sum1)
            if i == divisor_sum2 and i != divisor_sum1 and divisor_sum1 not in lst:
                print(f"{i} {divisor_sum1}")
                lst.append(i)


k = int(input("Введите число: "))
friendly_num(k)