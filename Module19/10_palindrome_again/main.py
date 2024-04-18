string = input('Введите строку: ')
string_dict = dict()
step = 0

for i in string:
    if i not in string_dict:
        string_dict[i] = 1
    else:
        string_dict[i] += 1


for value in string_dict.values():
    if value % 2 != 0:
        step += 1

if step <= 1:
    print('Можно сделать палиндром')
else:
    print('Нельзя сделать палиндром ')