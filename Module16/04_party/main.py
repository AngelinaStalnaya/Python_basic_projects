guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
guests_max = 6


def party(action):
  name = input('Имя гостя: ')
  if action == 'пришел':
    if len(guests) < guests_max:
      print('Привет,', name, '!')
      guests.append(name)
    else:
      print('Прости,', name, ', но мест нет.')
  elif action == 'ушел':
    print('Пока,', name, '!')
    remove_index = guests.index(name)
    guests.pop(remove_index)
  else:
    print('Неверное действие')
  print()
  print('Сейчас на вечеринке', len(guests), 'человек:', guests)
  action = input('Гость пришел или ушел? ')
  choice(action)

def choice(action):
  if action == 'ушел' or action == 'пришел':
    party(action)
  elif action == 'Пора спать':
    print('Вечеринка закончилась, все легли спать.')
  else:
    print('Неверное действие')
    choice(action)


print('Сейчас на вечеринке', len(guests), 'человек:', guests)
action = input('Гость пришел или ушел? ')

choice(action)