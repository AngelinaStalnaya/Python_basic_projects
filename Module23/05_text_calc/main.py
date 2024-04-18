import operator

result_sum = 0


file = open('calc.txt', 'r')
print('Содержимое файла calc.txt:')
print(file.read())
file.close()
print()


def is_expression(line, result=None):
    all_operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '//': operator.floordiv,
        '%': operator.mod,
        '**': operator.xor}
    my_parts = list(line.split())
    num_1 = int(my_parts[0])
    num_2 = int(my_parts[2])
    in_line_operation = my_parts[1]
    result = all_operations[in_line_operation](num_1, num_2)
    return result


with open('calc.txt', 'r') as ariph_file:
    for i_line in ariph_file:
        i_line = i_line.rstrip()
        try:
            result_sum += is_expression(i_line)
        except ZeroDivisionError:
            pass
        except (KeyError, ValueError):
            print(f'Обнаружена ошибка в строке: {i_line}', end='')
            step_answer = input('    Хотите исправить? ').lower()
            if step_answer == 'да':
                new_line = input('Введите исправленную строку: ')
                result_sum += is_expression(new_line)
            pass



print(f'\nСумма результатов: {result_sum}')