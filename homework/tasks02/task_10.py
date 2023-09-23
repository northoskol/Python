"""Задача 10: На столе лежат n монеток.
Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть
"""


def min_flips(coins):
    # Инициализируем счетчики для решек и гербов
    heads_count = 0
    tails_count = 0

    # Подсчитываем количество решек и гербов с использованием цикла for
    for coin in coins:
        if coin == 'H':
            heads_count += 1
        else:
            tails_count += 1

    # Инициализируем переменную для хранения минимального количества переворотов
    min_flips_count = min(heads_count, tails_count)

    # Переменные для подсчета текущего количества переворотов
    current_heads_flips = 0
    current_tails_flips = 0

    # Используем цикл while для нахождения минимального количества переворотов
    i = 0
    while i < len(coins):
        if coins[i] == 'H':
            current_heads_flips += 1
        else:
            current_tails_flips += 1

        # Если текущее количество переворотов становится больше минимального,
        # обновляем минимальное количество переворотов
        if current_heads_flips > min_flips_count:
            min_flips_count = current_heads_flips
        elif current_tails_flips > min_flips_count:
            min_flips_count = current_tails_flips
        i += 1

    return min_flips_count

# Пример использования
n = int(input("Введите количество монеток: "))
coins = input("Введите последовательность монеток через пробел (H - решка, T - герб): ").split()
if len(coins) != n:
    print("Ошибка! Количество монеток не соответствует введенному числу.")
else:
    result = min_flips(coins)
    print("Минимальное количество переворотов:", result)