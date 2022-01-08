# Задача 5. Наименьший делитель

def least_divisor(number):
    divisor_middle = 0
    divisor_least = 0
    for divisor in range(number, 1, -1):
        if number % divisor == 0:
           divisor_middle = divisor
           if divisor_middle > 1:
               divisor_least = divisor_middle
    return divisor_least

if number <= 1:
    print('Некорректный ввод, попробуйте снова.')
else:
    number = int(input('Введите число: '))
print('Наименьший общий делитель, оличный от единицы : ', least_divisor(number))
