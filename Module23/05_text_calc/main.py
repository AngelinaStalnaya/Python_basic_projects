result_sum = 0


file = open('calc.txt', 'r')
print('Содержимое файла calc.txt:')
print(file.read())
file.close()
print()


with open('calc.txt', 'r') as ariph_file:
    for i_line in ariph_file:
        i_line = i_line.rstrip()
        my_parts = list(i_line.split())
        try:
            result_sum += eval(i_line)
        except ZeroDivisionError:
            pass
        except SyntaxError:
            print(f'Обнаружена ошибка в строке: {i_line}', end='')
            step_answer = input('    Хотите исправить? ').lower()
            if step_answer == 'да':
                new_line = input('Введите исправленную строку: ')
                result_sum += eval(new_line)
            pass



print(f'\nСумма результатов: {result_sum}')