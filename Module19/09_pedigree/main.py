people = int(input('Введите количество человек: '))
tree_couples = dict()
height_person = dict()


for i in range(1, people):
    couple = (input('{0} пара: '.format(i))).split()
    tree_couples[couple[0]] = couple[1]

print(tree_couples)


for person in tree_couples:
    height = 1
    parent = tree_couples[person]
    while parent in tree_couples:
        parent = tree_couples[parent]
        height += 1
    height_person[person] = height


for parent in tree_couples.values():
    if parent not in height_person:
        height_person[parent] = 0


print('"Высота" каждого члена семьи: ')


for person in height_person:
    print(person, height_person[person])