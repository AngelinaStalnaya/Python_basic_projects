my_string = 'abcd'
my_tuple = (10, 20, 30, 40)

print('Строка: ', my_string)
print('Кортеж чисел: ', my_tuple)


generator = ((my_string[i], my_tuple[i]) for i in range(len(my_string)))
print('\nPезультат:\n', generator)
for i in generator:
    print(i)