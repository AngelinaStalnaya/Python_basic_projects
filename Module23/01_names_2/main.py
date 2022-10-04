count_sym = 0
count_line = 0
errors = ''

with open('people.txt', 'r', encoding='utf-8') as file_from:
    print('Содержимое файла people.txt: ')
    for i_line in file_from:
        print(i_line.rstrip())
        try:
            count_sym += len(i_line.rstrip())
            count_line += 1
            if len(i_line.rstrip()) < 3:
                raise Exception
        except Exception:
            errors += '\nОшибка: менее трёх символов в строке {}'.format(count_line)

print(errors)
print('Общее количество символов: {}'.format(count_sym))


