double_words = int(input('Введите кол-вo пар слов: '))
synonims = dict()
original_syn = []


for i in range(double_words):
    original_syn.append((input('{0}-я пара: '.format(i + 1))).split('-'))
    synonims[original_syn[i][0].lower()] = original_syn[i][1]
    synonims[original_syn[i][1].lower()] = original_syn[i][0]

word = input('Введите слово: ').lower()

while word not in synonims:
    print('Такого слова в словаре нет.')
    word = input('Введите слово: ').lower()

print('Синоним: ', synonims[word])
