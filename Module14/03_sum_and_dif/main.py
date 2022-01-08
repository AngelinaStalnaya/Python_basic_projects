# Сумма чисел и разность

number = int(input('Введите число: '))

def summ_of_num(number):
    summ_of_num = 0
    while number > 0:
        summ_of_num += number % 10
        number //= 10
    return summ_of_num

def amount_of_num(number):
    amount_of_num = 0
    while number > 0:
        amount_of_num += 1
        number //= 10
    return amount_of_num

distinction = abs(summ_of_num(number) - amount_of_num(number))

print('Сумма чисел: ', summ_of_num(number))
print('Количество чисел: ', amount_of_num(number))
print('Разность суммы и количества цифр: ', distinction)