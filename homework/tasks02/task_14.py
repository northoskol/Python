"""Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N."""

def powers_of_two(N):
    power_of_two = 1

    while power_of_two <= N:
        print(power_of_two)
        power_of_two *= 2

N = int(input("Введите значение N: "))
powers_of_two(N)