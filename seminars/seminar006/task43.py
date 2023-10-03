"""Задача №43. Решение в группах Дан список чисел.
Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
Вводится список чисел. Все числа списка находятся на разных строках.
Ввод: 1 2 3 2 3 2 Вывод: 2"""

# a = [1, 2, 3, 2, 3, 3, 6, 1, 8, 3, 3]
#
# p = list(set(a))
# res = 0
# print(p)
# for i in range(len(p)):
#     res = res + a.count(p[i]) // 2
#     # print(res)
# print(res)

"""генератор чисел"""

# from random import randint
#
# list_1 = [randint(1, 10) for _ in range(10)]
# print(list_1)
# pair_count = sum(list_1.count(el) // 2 for el in set(list_1))
# print(pair_count)

import random


def count_elements(list_1):
    count = 0
    for i in range(1, len(list_1) - 1):
        if list_1[i - 1] < list_1[i] and list_1[i] > list_1[i + 1]:
            count += 1
    return count


def great_fill_list(numbers, start, finish):
    new_list = [random.randint(start, finish) for i in range(numbers)]
    return new_list


n = int(input("Введите количество элементов массива: "))
start_l = int(input("Введите начало диапазона элементов массива: "))
finish_l = int(input("Введите начало конец элементов массива: "))
my_list = great_fill_list(n, start_l, finish_l)
print("Сгенерирован массив: ")
print(my_list)
print(f"Количество элементов у которых оба соседних меньше = {count_elements(my_list)}")