import os

text = input('Введите строку: ')
ending = f'{os.path.sep}'.join(input('\nКуда хотите сохранить документ? Введите последовательность папок (через пробел): ').split())
doc_name = input('Введите имя файла: ')

file_name = f'{doc_name}.txt'
cur_path = os.path.abspath(os.path.sep)


def find_folder(path, file_name):
    try:
        if os.path.isdir(path):
            for i_elem in os.listdir(path):
                new_path = os.path.join(path, i_elem)
                if new_path.endswith(file_name):
                    return new_path
                else:
                    result = find_folder(new_path, file_name)
                    if result:
                         return result
    except PermissionError:
        pass


path = find_folder(cur_path,ending)

def write_file(text, my_path, file_name):
    file = open(my_path, 'w', encoding='utf-8')
    file.write(text)
    file.close()
    print(f'\nCодержимое файла {file_name}:')
    file_from = open(my_path, 'r', encoding='utf-8')
    for i_line in file_from:
        print((i_line.rstrip()))
    file.close()


my_path = os.path.join(path, file_name)

if os.path.exists(my_path):
    answer = input('Вы действительно хотите перезаписать файл? ').lower()
    if answer == 'да':
        print('Файл успешно перезаписан!')
        write_file(text, my_path, file_name)
    else:
        print('Файл не был записан.')
else:
    print('Файл успешно сохранен!')
    write_file(text, my_path, file_name)