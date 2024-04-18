text = 'Mama myla ramu.'

my_file = open('text.txt', 'w', encoding='utf-8') #запись файла
my_file.write(text)
my_file.close()

alphabeth = 'abcdefghijklmnopqrstuvwxyz'


file_from = open('text.txt', 'r') #чтение файла
print('Содержимое файла text.txt:')
content = file_from.read()
file_from.close()
print(content)

my_dict_letters = dict()
my_text = sorted(content.lower())
for sym in my_text: #формирование словаря с ключами(буквы) - значение(кол-во букв)
    if sym in alphabeth:
        if sym in my_dict_letters:
            my_dict_letters[sym] += 1
        else:
            my_dict_letters[sym] = 1


all_letters = sum(my_dict_letters.values())
sorted_keys = sorted(my_dict_letters, key=my_dict_letters.get, reverse=True) #сортировка ключей a-z по значению 10-1


new_text = ''
for i in sorted_keys: # формирование строк: буква-соотношение в тексте
    new_text += f'{i} {round(my_dict_letters[i]/all_letters, 3)} \n'

file_to = open('analysis.txt', 'w') #запись нового файла
file_to.write(new_text)
file_to.close()

print('\nСодержимое файла analysis.txt:') #чтение нового файла
file = open('analysis.txt', 'r')
for i_line in file:
    print(i_line.rstrip())
file.close()