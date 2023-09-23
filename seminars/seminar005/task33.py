"""
Задача №33. Решение в группах
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
"""
"""from random import randint

def invertMaxMarks(marks):
    max_mark, min_mark = max(marks), min(marks)
    for i in range(len(marks)):
        if marks[i] == max_mark:
            marks[i] = min_mark
    return marks

n = int(input('Введите количество оценок '))
marks = [randint(1, 5) for _ in range(n)]
print(marks)
print(invertMaxMarks(marks))""" #цикл

"""marks = [1, 3, 3, 3, 4]
def invert(marks, max_mark = max(marks), min_mark = min(marks)):
    if not marks:
        return [ ]
    elif marks[0] == max_mark:
        marks[0] = min_mark
    return [marks[0]] + invert(marks[1:])

print(invert(marks)) #рекурсия

def invert2(marks, n, max_mark, min_mark):
    if n == 2*len(marks):
        return ""
    if marks[n - len(marks)] == max_mark:
        marks[n - len(marks)] = min_mark
    print(marks[n - len(marks)], end=' ')
    return invert2(marks, n + 1, max_mark, min_mark)

n = 6
marks = [1, 3, 2, 4, 3, 4]
print(invert2(marks, n, max(marks), min(marks)))""" #рекурсия 2

