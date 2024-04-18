text = input('Введите сообщение: ')
step = int(input('Введите сдвиг: '))
alphabeth = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
new_text = ''
letter = ''

for symbol in text:
  if symbol in alphabeth:
    if alphabeth.index(symbol) + step > len(alphabeth) - 1:
      letter = alphabeth[alphabeth.index(symbol) + step - len(alphabeth)]
    else:
      letter = alphabeth[alphabeth.index(symbol) + step]
    new_text += letter
  if symbol == ' ':
     new_text += symbol


print('Зашифрованное сообщение: ', new_text)
