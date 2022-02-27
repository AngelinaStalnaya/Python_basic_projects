text = input('Введите текст: ')
vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']

vowels_in_text = [vow for vow in text if vow in vowels]

print('Cписок гласных букв: ', vowels_in_text)
print('Длина списка: ', len(vowels_in_text))
