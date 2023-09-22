"""
Задача №31. Решение в группах
Последовательностью Фибоначчи называется
последовательность чисел a0
, a1
, ..., an
, ..., где
a0
 = 0, a1
 = 1,
 ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
"""

"""def fib(n):
    if n < 3:
        return n
    return fib(n-1) + fib(n-2)
num = int(input("Vvedite nomer 4isla fibonnachi N: "))
print(fib(num))"""

def fib(n):
    if n in [0, 1]:
        return 1
    return fib(n-1) + fib(n-2)
num = int(input("Vvedite nomer 4isla fibonnachi N: "))
print(fib(num))