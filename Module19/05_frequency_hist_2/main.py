text = input('Введите текст: ')
original_dict = dict()
invert_dict = dict()


for i in text:
    if i not in original_dict:
       original_dict[i]= 1
    else:
        original_dict[i] += 1

print('Оригинальный словарь частот: ')
for i in sorted(original_dict):
    print(i, ' : ', original_dict[i])



for key in set(original_dict.values()):
    invert_dict[key] = [i for i in original_dict.keys() if original_dict[i] == key]


print('Инвертированный словарь: ')
for i in invert_dict:
    print(i, ':', invert_dict[i])

