"""
Задача №35. Решение в группах
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes
"""

"""def is_prime_rec(n, den):
    if n <= 1:
        return "no"
    elif n==2:
        return "yes"
    elif den * den > n:
        return "yes"
    elif n % den == 0:
        return "no"
    else:
        return is_prime_rec(n, den + 1)

num = int(input("vvedite 4islo dlya proverki: "))
den = 2
print(is_prime_rec(num, den))""" #рекурсия

def is_prime_number(n, start):
    if start == n:
        print('yes')
        return
    if n % start == 0:
        print('no')
        return
    is_prime_number(n, start + 1)

n = int(input('Введите число: '))
start = 2
is_prime_number(n, start)


# def is_prime_number(n):
#     for i in range(2, n):
#         if n % i == 0:
#             print('no')
#             return;
#     print('yes')
#     return;
#
# n = int(input('Введите число: '))
# is_prime_number(n)