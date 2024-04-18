import os


path = os.path.abspath('numbers.txt')
file_form = open(path, 'r', encoding='utf-8')

num_list = []
print('Содержимое файла numbers.txt: ')
for i_line in file_form:
    print(i_line)
    for i_elem in i_line.rstrip():
        if i_elem != ' ':
            num_list.append(i_elem)


summa = sum(map(int, num_list))

file_to = open('answer.txt', 'w')
file_to.write(str(summa))
file_to.close()

print('Содержимое файла answer.txt: ')
file = open('answer.txt', 'r')
print(file.read())
file.close()