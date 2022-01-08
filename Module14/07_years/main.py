# Задача 7. Года

start_period = int(input('Введите первый год: '))
stop_period = int(input('Введите второй год: '))

def tripple_num(year):
  symbol1 = year // 1000
  symbol2 = year // 100 % 10
  symbol3 = year // 10 % 10
  symbol4 = year % 10
  if (symbol1 == symbol2 == symbol3) or (symbol1 == symbol3 == symbol4) or (symbol2 == symbol3 == symbol4) or (symbol2 == symbol1 == symbol4):
    print(year)


print('Года от', start_period, 'до', stop_period, 'с тремя одинаковыми цифрами: ')

for year in range(start_period, stop_period + 1):
  tripple_num(year)


