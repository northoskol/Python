"""
Задача №25. Решение в группах
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()
"""
"""
def modify_str(my_str):
    letters = my_str.split()
    print(letters)
    l_count = {}
    new_str = []

    for letter in letters:
        if letter in l_count:
            l_count[letter] += 1
            mod_letter = f"{letter}_{l_count[letter] - 1}"
        else:
            l_count[letter] = 1
            mod_letter = letter

        new_str.append(mod_letter)
    print(l_count)
    return " ".join(new_str)


my_str = "a a a b c a a d c d d"
mod_str = modify_str(my_str)
print(mod_str)"""

lst = "a a a b c a a d c d d".split()
res = {}
for el in lst:
    if el in res:
        print(f"{el}_{res[el]}", end=" ")
    else:
        print(el, end=" ")
    res[el] = res.get(el, 0) + 1
