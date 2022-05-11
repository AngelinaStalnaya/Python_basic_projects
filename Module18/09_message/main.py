message = input('Сообщение: ')
new_message = ''
word = ''


def reversed_word(word):
    new_word = ''
    for i in range(1, len(word) + 1):
        new_word += word[-i]
    return new_word


for i in message:
    if i.isalpha():
        word += i
    else:
        new_message += reversed_word(word) + i
        word = ''


print('Новое сообщение: ', ''.join(new_message))