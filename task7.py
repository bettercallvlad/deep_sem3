# Подсчитайте сколько раз встречается каждая буква в строке без
# использования метода count и с ним.
# Результат сохраните в словаре, где ключ - символ,
# а значение - частота встречи символа в строке.
# Обратите внимание на порядок ключей. Объясните
# почему они совпадают или не совпадают в ваших решениях.

letter_string = 'afnjanfjnajfnjanjaaaaaa'

letter_frequency = {}
for letter in letter_string:
    letter_frequency[letter] = letter_frequency.get(letter, 0) + 1
print(letter_frequency)
