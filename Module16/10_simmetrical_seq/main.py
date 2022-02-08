my_list = []
add_list = []

amount = int(input('Кол-во чисел:'))

for i in range(amount):
    num = int(input('Число: '))
    my_list.append(num)
print('Последовательность: ', my_list)

while my_list[-1] == my_list[-2]:
    my_list.pop(-1)
else:
    my_list.pop(-1)


for i in range(len(my_list)):
    indexes = my_list[-i-1]
    add_list.append(indexes)


print('Нужно приписать чисел: ', len(add_list))
print('Сами числа: ', add_list)

