contacts_dict = dict()
def add_contact(contacts_dict):
    name = tuple((input('Введите имя и фамилию нового контакта (через пробел): ')).rstrip(' ').title().split(' '))
    print(name)
    if name in contacts_dict:
        print('Такой человек уже есть в контактах.')
    else:
        tel_number = int(input('Введите номер телефона: '))
        contacts_dict[name] = tel_number
    return print('Текущий словарь контактов: ', contacts_dict)

def find_person(contacts_dict):
    surname = input('Введите фамилию для поиска: ').title()
    absent = 0
    for i_person in contacts_dict.keys():
        if surname in i_person:
            print(*i_person, contacts_dict[i_person])
            absent = 1
    if absent == 0:
        print('Такого человека нет в контактах.')
    return contacts_dict



while True:
    new_action = int(input('Введите номер действия: \n1. Добавить контакт \n2. Найти человека \n '))
    if new_action == 1:
        add_contact(contacts_dict)
    elif new_action == 2:
        find_person(contacts_dict)
    else:
        print('Попробуйте снова.')