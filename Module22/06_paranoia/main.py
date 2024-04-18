
my_text = 'Hello\nHello\nHello\nHello'
my_file = open('text.txt', 'w', encoding='utf-8')
my_file.write(my_text)
my_file.close()

ciphered_text = ''
step = 1


def chipher(text, step):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    new_line = ''
    for sym in text.lower():
        index = alpha.index(sym)
        new_index = index + step
        if new_index < len(alpha):
            new_line += alpha[new_index]
        else:
            new_index - len(alpha)
            new_line += alpha[new_index]
    return new_line.title()


file_from = open('text.txt', 'r', encoding='utf-8')
print('Содержимое файла text.txt: ')
for i_line in file_from:
    print(i_line.rstrip())
    ciphered_text += chipher(i_line.rstrip(), step) + '\n'
    step += 1

file_to = open('cipher_text.txt', 'w', encoding='utf-8')
file_to.write(ciphered_text)
file_to.close()

new_file = open('cipher_text.txt', 'r', encoding='utf-8')
print('\nСодержимое файла cipher_text.txt: ')
for i_line in new_file:
    print(i_line.rstrip())


file_from.close()
file_to.close()