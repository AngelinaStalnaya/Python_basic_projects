string = input('Введите строку: ')
longest_word = ''

words = string.split()
len_words = [(len(i_word)) for i_word in words]
long_word = len_words.index(max(len_words))
longest_word = words[long_word]

print('Самое длинное слово: ', longest_word)
print('Длина этого слова: ', len(longest_word))
