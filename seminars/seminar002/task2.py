"""
Задача №11. Решение в группах
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6
"""

"""fib = int(input("Введите число: "))
first_element, second_element, current = 0, 1, 1
count = 2
while current < fib:
    current = first_element + second_element
    first_element = second_element
    second_element = current
    count += 1

if current == fib:
    print(f"Элемент фибоначчи {count}")
else:
    print(-1)"""


number = 5
fib_penultimate, fib_last = 0, 1
count = 2
while number > fib_last:
    fib_penultimate, fib_last = fib_last, fib_penultimate + fib_last
    count += 1
if number == fib_last:
    print(count)
else:
    print("-1")