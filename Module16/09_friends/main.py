friends = int(input('Кол-во друзей: '))
debts = int(input('Долговых расписок: '))
balance = []

for personal_debt in range(friends):
    num = 0
    balance.append(num)

for i in range(1, debts + 1):
    print(i, 'расписка')
    debtor = int(input('Кому: '))
    lender = int(input('От кого: '))
    if debtor != lender:
        money = int(input('Сколько: '))
        id_debtor = debtor - 1
        balance[id_debtor] -= money
        id_lender = lender - 1
        balance[id_lender] += money
        print()
    else:
        print('Ошибка ввода')

print('Баланс друзей: ')
for person in range(friends):
    print(person + 1, ':', balance[person])
