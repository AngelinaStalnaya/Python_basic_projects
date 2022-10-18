import random


class Parent:

    def __init__(self, name, age, children=[]):
        self.parent_name = name
        self.parent_age = age
        self.children = children.copy()

    def print_info(self):
        print(f'Имя: {self.parent_name}\n'
              f'Возраст: {self.parent_age}\n'
              f'Дети: {self.children}\n')

    def calm_child(self, child):
        calm_actions = ['поиграл', 'спел', 'обнял', 'включил мультики', 'рассмешил']
        print(f'{self.parent_name} {random.choice(calm_actions)} чтобы успокоить {child.name}')
        child.change_calm()

    def feed_child(self, child):
        print(f'{self.parent_name} покормил ребёнка {child.name}.')
        child.change_hunger()

    def add_child(self, child_name, age):
        if age < self.parent_age - 16:
            self.children.append(child_name)
        else:
            print(f'{child_name} не может быть ребенком {self.parent_name}')


class Child:

    def __init__(self, child_name, child_age, calm=False, hunger=True):
        self.name = child_name
        self.age = child_age
        self.calm = calm
        self.hunger = hunger

    def change_calm(self):
        self.calm = True
        print(f'Ребёнок {self.name} спокоен.\n')

    def change_hunger(self):
        self.hunger = False
        print(f'Ребёнок {self.name} сыт.\n')

    def find_parent(self, parent):
        parent.add_child(self.name, self.age)

    def print_child_info(self):
        print(f'Имя ребенка: {self.name}'
              f'Возраст ребенка: {self.age}'
              f'Ребенок сейчас {"спокоен" if self.calm == True else "неспокоен"} и '
              f'{"сыт" if self.hunger == False else "голоден"}')


parent_1 = Parent('Maria', 36)
parent_2 = Parent('Ivan', 40)

child_1 = Child('Andrey', 10, True)
child_2 = Child('Anna', 15)
child_3 = Child('Vera', 24, True, False)

child_2.find_parent(parent_1)
child_1.find_parent(parent_2)
child_3.find_parent(parent_1)
child_3.find_parent(parent_2)

parent_1.print_info()
parent_2.print_info()


if not child_1.calm:
    parent_1.calm_child(child_1)

if child_2.hunger:
    parent_1.feed_child(child_2)

if child_1.hunger:
    parent_2.feed_child(child_1)

if not child_2.calm:
    parent_1.calm_child(child_2)