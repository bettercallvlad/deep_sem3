# Создайте вручную список с повторяющимися элементами.
# Удалите из него все элементы, которые встречаются дважды.

elements = [1, 2, 3, 3, 4, 5, 5, 5, 5, 6, 6, 6]
COUNT_CRITERIA = 2

for elem in elements:
    elem_in = elements.count(elem)
    if elem_in % COUNT_CRITERIA == 0 or elem_in > 2:
        elements.remove(elem)
        elements.remove(elem)
print(elements)
