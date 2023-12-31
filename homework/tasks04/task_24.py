"""Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
Она растёт на круглой грядке, причём кусты высажены только по окружности.
Таким образом, у каждого куста есть ровно два соседних.
Всего на грядке растёт N кустов.Эти кусты обладают разной урожайностью,
поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод,
которое может собрать за один заход собирающий модуль,
находясь перед некоторым кустом заданной во входном файле грядки."""

"""def max_berry_harvest(berry_counts):
    n = len(berry_counts)
    max_harvest = 0

    for i in range(n):
        # Вычисляем количество ягод, которое можно собрать с i-ого куста
        harvest = berry_counts[i] + berry_counts[(i - 1) % n] + berry_counts[(i + 1) % n]
        max_harvest = max(max_harvest, harvest)

    return max_harvest

# Чтение входных данных из файла (предположим, что они хранятся в файле input_1.txt)
with open('input_1.txt', 'r') as file:
    berry_counts = list(map(int, file.readline().split()))

# Вычисление максимального количества ягод
result = max_berry_harvest(berry_counts)

# Вывод результата
print("Максимальное количество ягод, которое можно собрать:", result)"""

def max_berry_harvest(berry_counts):
    n = len(berry_counts)
    max_harvest = 0

    for i in range(n):
        # Вычисляем количество ягод, которое можно собрать с i-ого куста
        harvest = berry_counts[i] + berry_counts[(i - 1) % n] + berry_counts[(i + 1) % n]
        max_harvest = max(max_harvest, harvest)

    return max_harvest

# Ввод данных от пользователя
n = int(input("Введите количество кустов черники: "))
berry_counts = []
for i in range(n):
    berry = int(input(f"Введите количество ягод на {i+1}-ом кусте: "))
    berry_counts.append(berry)

# Вычисление максимального количества ягод
result = max_berry_harvest(berry_counts)

# Вывод результата
print("Максимальное количество ягод, которое можно собрать:", result)