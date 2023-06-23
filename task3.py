# Создайте вручную кортеж содержащий элементы разных типов.
# Получите из него словарь списков,
# где ключ - тип элемента, а значение - список элементов данного типа.
# {str: ['srt', 'vlad'], float: [21.11], int: [111]}

data = ('srt', 'vlad', 21.11, 111, True, ['list'])
type_dict = {}
for i in data:
    key = type_dict.setdefault(type(i), list())
    key.append(i)
print(type_dict)
