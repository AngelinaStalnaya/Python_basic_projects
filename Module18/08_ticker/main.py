string1 = input('Первая строка: ')
string2 = input('Вторая строка: ')
step = 0

while step < len(string2):
    if string1 in string2:
        print('Первая строка получается из второй со сдвигом ', step)
        break
    else:
        step += 1
        string1 = string1[step:] + string1[:step]
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')



