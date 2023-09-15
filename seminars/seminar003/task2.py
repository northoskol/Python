"""
Задача №19. Решение в группах
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
"""

"""
list1 = []
for i in range(10):
    list.append(i)
k = int(input("enter k: "))
print(list1)
list1 = list[-k:] + list[k]"""


"""функция pop"""
k = 3
lst = [1, 2, 3, 4, 5]
for i in range(k-1):
    last_el = lst.pop()
    lst.insert(0, last_el)
print(lst)


