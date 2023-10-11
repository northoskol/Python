"""Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
"""
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

import random
import pandas as pd

# Исходные данные
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Преобразование в one-hot кодировку
one_hot = pd.get_dummies(data['whoAmI'])

# Объединение исходных данных и one-hot кодировки
data = pd.concat([data, one_hot], axis=1)

# Удаление исходного столбца 'whoAmI'
data.drop('whoAmI', axis=1, inplace=True)

# Вывод первых пяти строк данных
print(data.head())