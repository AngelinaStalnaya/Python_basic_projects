import os


path = os.path.abspath(os.path.join('..', '02_zen_of_python', 'zen.txt'))


count_lines = 0
count_letters = 0
words = []
letters = dict()
alphabeth = 'abcdefghijklmnopqrstuvwxyz'

file = open(path, 'r', encoding='utf-8')



for i_line in file:
    count_lines += 1
    for word in i_line.rstrip().split(' '):
        words.append(word.lower())


for word in words:
    for sym in word:
        if sym in letters:
            letters[sym] += 1
        elif sym in alphabeth:
            letters[sym] = 1

count_word = len(words) - 1
count_less_letter = letters['a']

for i_count in letters.values():
    count_letters += i_count
    if i_count < count_less_letter:
        count_less_letter = i_count
for key in letters:
    if letters[key] == count_less_letter:
        count_less_letter = key

print('Количество букв в файле: ', count_letters)
print('Количество слов в файле: ', count_word)
print('Количество строк в файле: ', count_lines)
print('Наиболее редкая буква: ', count_less_letter)

file.close()


