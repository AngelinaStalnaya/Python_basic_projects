special_symbols = ['@', '№', '$', '%', '^', '&', '*', '()']

file_name = input('Название файла: ')

if file_name[0] in special_symbols and file_name.startswith(file_name[0]):
    print('Ошибка: название начинается на один из специальных симоволов.')
elif not file_name.endswith('.txt') or file_name.endswith('.docx'):
    print('Ошибка: неверное расширение файла.')
else:
    print('Файл назван верно.')
