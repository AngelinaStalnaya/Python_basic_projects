site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
             'h2': 'Здесь будет мой заголовок',
             'div': 'Тут, наверное, какой-то блок',
             'p': 'А вот здесь новый абзац'
        }
    }
}

def find_value(structure, key, steps = 0, level=0):
    result = None
    if steps > 0 and level >= steps:
        return result
    if key in structure:
        return structure[key]
    else:
        for i_value in structure.values():
            if isinstance(i_value, dict):
                result = find_value(i_value, key, steps, level+1)
        return result



my_key = input('Введите искомый ключ: ')
max_depth_option = input('Хотите ввести максимальную глубину? Y/N: ').lower()

if max_depth_option == 'y':
    max_depth = int(input('Введите максимальную глубину: '))
    print('Значение ключа: ', find_value(site, my_key, max_depth))
else:
    print('Значение ключа: ', find_value(site, my_key))

