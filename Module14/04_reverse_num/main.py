# Задача 4. Число наоборот 3

number1 = float(input('Введите первое число: '))
number2 = float(input('Введите второе число: '))

def reverse_num(number1):
    new_num = ''
    first_part = ''
    second_part = ''
    a_part, b_part = str(number1).split('.')
    for symbol in a_part:
        first_part = symbol + first_part
    for symbol in b_part:
        second_part = symbol + second_part
    new_num = first_part + '.' + second_part
    return float(new_num)

print('Первое число наоборот: ', reverse_num(number1))
print('Второе число наоборот: ', reverse_num(number2))
print('Сумма чисел: ', reverse_num(number1) + reverse_num(number2))