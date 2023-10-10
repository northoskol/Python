"""Задача №67. Решение в группах 1. Создать новый столбец в таблице с пингвинами,
который будет отвечать  за показатель длины клюва пингвина.
high - длинный(от 42) middle - средний(от 35 до 42) low - маленький(до 35)"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

penguins = sns.load_dataset("penguins")

penguins.loc[penguins['bill_length_mm'] < 35, 'height_group'] = 'small'
penguins.loc[(penguins['bill_length_mm'] >= 35) & (
            penguins['bill_length_mm'] < 42), 'height_group'] = 'middle'
penguins.loc[penguins['bill_length_mm'] >= 42, 'height_group'] = 'big'

penguins.to_csv('penguins.csv')

sns.histplot(penguins, x='flipper_length_mm', hue='height_group')
plt.show()