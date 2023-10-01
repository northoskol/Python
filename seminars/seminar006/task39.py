"""Задача №39. Решение в группах Даны два массива чисел.
Требуется вывести те элементы первого массива
(в том порядке, в каком они идут в первом массиве),
которых нет во втором массиве. Пользователь вводит  число N - количество элементов в первом массиве,
затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве.
Затем элементы второго массива"""

from random import randint

def create_list(n):
    new_list = [randint(0, 9) for _ in range(n)] #LS
    return new_list

def get_diff_elements(list1, list2):
    list3 = [el for el in list1 if el not in list2] #LS

    return list3

n = randint(5, 9)
m = randint(5, 9)
list1 = create_list(n)
list2 = create_list(m)
print(n, ' -> ', list1)
print(m, ' -> ', list2)
print(get_diff_elements(list1, list2))

# традиционный итертаор с функцией append
# list3 = []
# for el in list1:
#    if el in list1:
#        if el not in list2:
#            list3.append(el)
# print(list3)
