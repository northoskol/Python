"""
Задача №23. Решение в группах
Дан массив, состоящий из целых чисел. Напишите
программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента
с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)
"""
"""
lst = [0, -1, 5, 2, 3]
count = 0
for i in range(len(lst) -1):
    if lst[i+1] > lst[i]:
        count +=1
print(lst)
print(count)
"""

lst = [0, -1, 5, 2, 3]
count = 0
for i in range(1, len(lst)):
    if lst[i] > lst[i - 1]:
        count += 1
print(lst)
print(count)