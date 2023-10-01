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

from random import randint

list_1 = [randint(1, 10) for _ in range(10)]
print(list_1)
pair_count = sum(list_1.count(el) // 2 for el in set(list_1))
print(pair_count)
