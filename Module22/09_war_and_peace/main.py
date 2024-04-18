import os
import zipfile


# имеется ошибка в наименовании файла (в задании voina-i-mir.zip, в папке модуля - voyna-i-mir.zip)

all_alphabeths = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяЯЮЭЬЫЪЩШЧЦХФУТСРПОНМЛКЙИЗЖЁЕДГВБА'


my_zip_file_path = zipfile.ZipFile(os.path.abspath(os.path.join(os.getcwd(), 'voyna-i-mir.zip')), 'r') #чтение файла zip
my_zip_file_path.extractall(os.getcwd()) #извлечение содержимого файла в папку по заданной директории
my_zip_file_path.close()

path_to_file = ''
for i_elem in os.listdir(os.getcwd()):
   if i_elem.endswith('.txt'):
      path_to_file = os.path.join(os.getcwd(), i_elem)
print(path_to_file)


my_dict_letters = dict()
file_from = open(path_to_file, 'r', encoding='utf-8') #чтение извлеченного файла
for i_line in file_from:
   for sym in i_line.rstrip(): #формирование словаря с ключами(буквы) - значение(кол-во букв)
      if sym in all_alphabeths:
         if sym in my_dict_letters:
            my_dict_letters[sym] += 1
         else:
            my_dict_letters[sym] = 1
file_from.close()
for i in my_dict_letters:
   print(i, ':', my_dict_letters[i])


all_letters = sum(my_dict_letters.values())
sorted_keys = sorted(my_dict_letters, key=my_dict_letters.get, reverse=True) #сортировка ключей a-z по значению 10-1
print(sorted_keys)

new_text = ''
for i in sorted_keys: # формирование строк: буква-соотношение в тексте
    new_text += f'{i} - {my_dict_letters[i]/all_letters} \n'

file_to = open('war_and_peace_analysis.txt', 'w', encoding='utf-8') #запись нового файла
file_to.write('Частота встречаемости букв кириллицы и латиницы в файле:\n' + new_text)
file_to.close()

print('\nСодержимое файла war_and_peace_analysis.txt:') #чтение нового файла
file = open('war_and_peace_analysis.txt', 'r', encoding='utf-8')
for i_line in file:
    print(i_line.rstrip())
file.close()