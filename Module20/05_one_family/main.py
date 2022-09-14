family_members = {
    'Сидоров': {
        'Сидоров Никита': 35,
        'Сидорова Алина': 34,
        'Сидоров Павел': 10,
    },
    'Петров': {
        'Петров Александр': 39,
        'Петрова Валентина': 36,
        'Петров Денис': 15,
        'Петрова Анна': 12
    },
    'Козлов': {
        'Козлова Ирина': 65,
        'Козлов Геннадий': 68,
        'Козлов Пётр': 33,
        'Козлов Сергей': 30
    }
}
surname = input('Введите фамилию: ').title()

if surname in family_members:
    print(family_members[surname])
elif surname.endswith('а') or surname.endswith('ы'):
    surname = surname[:-1]
    if surname in family_members:
        for name, age in family_members[surname].items():
            print(name, age)
    else:
        print('Семьи с такой фамилией нет в базе данных')
