# Пользователь вводит данные.
# Сделайте проверку данных и преобразуйте
# если возможно в один из вариантов ниже:
#
# целое положительное число
# вещественное положительное или отрицательное число
# строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
# строку в верхнем регистре в остальных случаях

data = (input())
if data.isdecimal():
    if int(data) > 0:
        print(int(data))
elif '.' in data:
    part1, part2 = data.split('.')
    if part1.isdigit() and part2.isdigit():
        print(float(data))
elif data != data.lower():
    print(data.lower())
else:
    print(data.upper())

# вариант через работу с исключениями
try:
    if float(data) == int(data):
        print(int(data))
    else:
        print(float(data))
except ValueError:
    if data != data.lower():
        print(data.lower())
    else:
        print(data.upper())
