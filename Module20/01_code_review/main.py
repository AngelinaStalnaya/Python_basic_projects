students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def data_students(students):
    list_of_interests = []
    len_surnames = 0
    for ID in students:
        list_of_interests.extend(students[ID]['interests'])
        len_surnames += len(students[ID]['surname'])
    return set(list_of_interests), len_surnames


pairs = []
for ID in students:
    pairs.append(tuple((ID, students[ID]['age'])))
print('Список пар "ID студента - возраст": ', pairs)

my_lst, total_len_surname = data_students(students)

print('Полный список интересов всех студентов: ', my_lst)
print('Общая длина всех фамилий студентов: ', total_len_surname)


