import random

sum_count = 0
step = 0
hell_number = random.randint(1, 13)


file_to_write = open('out_file.txt', 'w')

try:
   while sum_count < 777:
        my_num = int(input('Введите число: '))
        step += 1
        if step != hell_number:
            sum_count += my_num
            file_to_write.write(f'{my_num}\n')
        else:
            raise Exception
except Exception:
    print('Вас постигла неудача!')
else:
    print('Вы успешно выполнили условие для выхода из порочного цикла!')
finally:
    file_to_write.close()
    print('\nСодeржание файла out_file.txt: ')
    with open('out_file.txt', 'r') as final_file:
        for i_line in final_file:
            print(i_line.rstrip())