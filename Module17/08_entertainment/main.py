import random

sticks = int(input('Кол-во палок: '))
throws = int(input('Кол-во бросков: '))
stick_list = [stick for stick in range(1, sticks +1)]
pop_list = []

for throw in range(throws):
    L_i = random.randint(1, sticks - 1)
    R_i = random.randint(L_i, sticks)
    print('Бросок', throw + 1, '. Сбиты палки с номера ', L_i, 'по номер', R_i)
    pop_list.extend([pop for pop in range(L_i, R_i + 1)])

stick_list = ['.' if elem in pop_list else 'I' for elem in stick_list]
print('Результат: ', ''.join(stick_list))