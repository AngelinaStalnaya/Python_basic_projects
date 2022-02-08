number_skates = int(input('Кол-во коньков: '))
roller_skates = []
feet_sizes = []
no_roller = []
rental = 0

for size in range(number_skates):
    print('Размер', size + 1, 'пары: ', end='')
    size_roller = input()
    roller_skates.append(size_roller)

print()
people = int(input('Кол-во людей: '))

for person in range(people):
    print('Размер ноги', person + 1, ' человека: ', end='')
    feet = input()
    feet_sizes.append(feet)

for roller in roller_skates:
    if roller in feet_sizes:
        rental += 1
        feet_sizes.remove(roller)
    else:
        no_roller.append(roller)

for rest_roller in feet_sizes:
    for bigger_roller in no_roller:
        if rest_roller < bigger_roller:
            rental += 1
            no_roller.remove(bigger_roller)

print()
print('Наибольшее кол-вo людeй,которые могу взять ролики: ', rental)