"""Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

Пример:"""


list_1 = [1, 2, 3, 4, 5, 6, 7,]
k = 6
closest_element = min(list_1, key=lambda x: abs(x - k))
print(f"Самый близкий элемент к {k} в массиве: {closest_element}")