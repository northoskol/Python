"""
Задача №21. Решение в группах
Напишите программу для печати всех уникальных
значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""
# традиционный итератор
"""lst_obj = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
           {"VII": "S005"}, {"V": "S009"}, {" VIII": "S007"}]
uniq_el = set()
for el in lst_obj:
    for val in el.values():
        uniq_el.add(val)
print(uniq_el)"""

# включение для словаря
lst_obj = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
           {"VII": "S005"}, {"V": "S009"}, {" VIII": "S007"}]
uniq_el = set(val for el in lst_obj for val in el.values())

print(uniq_el)