string = input('Введите строку: ')
h_appearance = []
index = 0

for h_sym in string:
    if h_sym == 'h':
        h_appearance.append(index)
    index += 1
hh_string = [sym for sym in string[(h_appearance[-1]) -1: h_appearance[0]: -1]]


print('Развернутая последовательность между последним и первым h:', ''.join(hh_string))