import random

amount = int(input('Кол-во чисел в списке: '))
numbers = [random.randint(0, 2) for i in range(amount)]
print('Список до сжатия: ', numbers)
numbers_pressed = numbers[:]
for i in numbers_pressed:
    if i == 0:
        numbers_pressed.append(i)
        numbers_pressed.remove(0)
new_list = [num for num in numbers_pressed if num > 0]
print('Список после сжатия: ', new_list)