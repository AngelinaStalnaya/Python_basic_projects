
def find_error(my_string):
    my_parts = list(my_string.split())
    try:
        if len(my_parts) == 3:
            pass
        else:
            raise IndexError
        if my_parts[0].isalpha():
            pass
        else:
            raise NameError
        if '@' and '.' in my_parts[1]:
            pass
        else:
            raise SyntaxError
        if 10 <= int(my_parts[2]) <= 99:
            pass
        else:
            raise ValueError
    except IndexError:
        bad_file.write(my_string + '       НЕ присутствуют все три поля\n')
    except NameError:
        bad_file.write(my_string + '       Поле «Имя» содержит НЕ только буквы\n')
    except SyntaxError:
        bad_file.write(my_string + '       Поле «Имейл» НЕ содержит @ и . (точку)\n')
    except ValueError:
        bad_file.write(my_string + '       Поле «Возраст» НЕ является числом от 10 до 99\n')
    else:
        good_file.write(my_string + '\n')


with open('registrations.txt', 'r', encoding='utf-8') as main_file,\
     open('registrations_good.log', 'w', encoding='utf-8') as good_file,\
     open('registrations_bad.log', 'w', encoding='utf-8') as bad_file:

    for i_line in main_file:
        find_error(i_line.rstrip())


with open('registrations_good.log', 'r', encoding='utf-8') as written_good_file,\
     open('registrations_bad.log', 'r', encoding='utf-8') as written_bad_file:

    print('\nСодержимое файла registrations_bad.log:')
    for b_line in written_bad_file:
        print(b_line.rstrip())

    print("+{:-^101}+".format("+"))
    print('Содержимое файла registrations_good.log:')
    for g_line in written_good_file:
        print(g_line.rstrip())
