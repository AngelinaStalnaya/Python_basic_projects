orders = int(input('Введите количество заказов: '))
orders_dict = dict()
pizzas = []

for i in range(orders):
    pizzas.append(input('{}-й заказ: '.format(i+1)).split())


for i in range(len(pizzas)):
    if pizzas[i][0] not in orders_dict:
        orders_dict[pizzas[i][0]] = ({pizzas[i][1] : int(pizzas[i][2])})
    else: # иванов есть
        if pizzas[i][1] in orders_dict[pizzas[i][0]]:
            orders_dict[pizzas[i][0]][pizzas[i][1]] += int(pizzas[i][2])
        else:
            orders_dict[pizzas[i][0]][pizzas[i][1]] = int(pizzas[i][2])


for person in orders_dict:
    print(person, ':')
    for pizza_name in orders_dict[person]:
        print('\t', pizza_name, ':', orders_dict[person][pizza_name])
