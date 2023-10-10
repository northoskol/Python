import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")


# 1
# plt.scatter(penguins['bill_length_mm'], penguins['bill_depth_mm'])
# plt.show()
#
# 2
# plt.scatter(penguins['flipper_length_mm'], penguins['body_mass_g'])
# plt.show()


def func_1():
    # 1
    plt.scatter(penguins['bill_length_mm'], penguins['bill_depth_mm'])
    plt.show()

    # 2
    plt.scatter(penguins['flipper_length_mm'], penguins['body_mass_g'])
    plt.show()


def func_2():
    sns.scatterplot(data=penguins, x='flipper_length_mm', y='body_mass_g', hue='sex', size=10, style='island')
    plt.show()


def func_3():
    x_vars = ["body_mass_g", "bill_length_mm", "bill_depth_mm", "flipper_length_mm"]
    y_vars = ["body_mass_g"]
    g = sns.PairGrid(penguins, hue='sex', x_vars=x_vars, y_vars=y_vars)
    g.map_diag(sns.histplot, color=".3")
    g.map_offdiag(sns.scatterplot)
    g.add_legend()
    plt.show()


def func_4():
    sns.displot(penguins, x="bill_length_mm", y="bill_depth_mm", hue='species')
    plt.show()


def func_5():
    penguins["bill_depth_mm"].hist(bins=30)
    plt.show()


func_5()