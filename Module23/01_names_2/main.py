count_sym = 0
count_line = 0

with open('people.txt', 'r', encoding='utf-8') as file_from,\
     open('errors.log', 'w', encoding='utf-8') as file_to:
    print('Содержимое файла people.txt: ')
    for i_line in file_from:
        print(i_line.rstrip())
        try:
            count_sym += len(i_line.rstrip())
            count_line += 1
            if len(i_line.rstrip()) < 3:
                file_to.write(f'Ошибка: менее трёх символов в строке {count_line}\n')
        except Exception as exc:
            print(exc)
            file_to.write(f'{exc} \n')

print()

with open('errors.log', 'r', encoding='utf-8') as file:
    for e_line in file:
        print(e_line.rstrip())
print('Общее количество символов: {}'.format(count_sym))


