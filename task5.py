# Создайте вручную список с повторяющимися целыми числами.
# Сформируйте список с порядковыми номерами нечётных
# элементов исходного списка. Нумерация начинается с единицы.

elements = [1, 2, 3, 4, 4, 5, 6]
result = []

for number, element in enumerate(elements, start=1):
    if element % 2 != 0:
        result.append(number)
print(result)
