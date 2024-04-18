def fibonacci_num(number):
    if number <= 1:
        return number
    else:
        return fibonacci_num(number - 1) + fibonacci_num(number - 2)



number = int(input('Введите позицию в ряде Фибоначчи: '))
print('Число: ', fibonacci_num(number))