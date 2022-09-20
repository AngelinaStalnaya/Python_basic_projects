def new_site(number_of_sites):
    if number_of_sites >= 1:
        my_structure()
        new_site(number_of_sites - 1)

def my_structure():
    product = input('Введите название продукта для нового сайта: ')
    print("site = {")
    print("            'html': {")
    print("                'head': {")
    print(f"                    'title': 'Куплю/продам {product} недорого'")
    print("                },")
    print("                'body': {")
    print(f"                    'h2': 'У нас самая низкая цена на {product}',")
    print("                    'div': 'Купить',")
    print("                    'p': 'Продать'")
    print("                }")
    print("            }")
    print("}")



number_of_sites = int(input('Сколько сайтов: '))
new_site(number_of_sites)
