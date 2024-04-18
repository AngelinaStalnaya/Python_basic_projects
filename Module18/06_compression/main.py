string = list(input('Введите строку: '))

new_string = []
step = 1

for i in range(len(string)):
    if i + 1 < len(string) and string[i] == string[i + 1]:
        step += 1
    else:
        new_string.append(string[i])
        new_string.append(str(step))
        step = 1
print('Закодированная строка', ''.join(new_string))