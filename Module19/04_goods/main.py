goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

all_goods = dict()

for key in goods:
    for value in store:
        if goods[key] == value:
            all_goods[key] = store[value]

for good in all_goods:
    total_items = 0
    total_price = 0
    for i in range(len(all_goods[good])):
        total_items += int(all_goods[good][i]['quantity'])
        total_price += int(all_goods[good][i]['price'] * all_goods[good][i]['quantity'])
    print(good, '-', total_items, 'шт., стоимость ', total_price, ' руб.')
