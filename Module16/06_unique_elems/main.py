list_1 = []
list_2 = []

for i in range(3):
    print('Введите', i + 1, 'число для первого списка: ', end='')
    num = input()
    list_1.append(num)
for i in range(7):
    print('Введите', i + 1, 'число для второго списка: ', end='')
    num = input()
    list_2.append(num)

print('Первый список:', (list_1))
print('Второй список:', (list_2))
list_1.extend(list_2)
for i_num in list_1:
    indexes = list_1.count(i_num)
    for _ in range(indexes - 1):
        list_1.remove(i_num)

print('Новый список с уникальными элементами: ', list_1)
