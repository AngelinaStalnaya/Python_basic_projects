import os


path = os.path.abspath('zen.txt')

file = open('zen.txt', 'r')
len_line = ''

for i_line in file:
    line = i_line.rstrip()
    len_line = line + '\n' + len_line

file.close()

print(len_line)
