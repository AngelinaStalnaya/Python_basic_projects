class Human:

    def __init__(self, name, house):
        self.name = name
        self.hunger = 50
        self.home = house

    def eat(self):
        self.hunger += 10
        self.home.money -= 10
        print(f'{self.name} поел.')

    def work(self):
        self.hunger -= 10
        self.home.money += 30
        print(f'{self.name} сходил на работу.')
        self.check_hunger()

    def play(self):
        self.hunger -= 10
        print(f'{self.name} поиграл.')
        self.check_hunger()

    def shopping_for_food(self):
        self.home.fridge += 30
        self.home.money -= 30
        print(f'{self.name} сходил в магазин за продуктами.')

    def check_hunger(self):
        if self.hunger < 0:
            print(f'{self.name} умер от голода')
            self.name = 'R.I.P.'

    def print_info(self):
        print(f'\nИмя: {self.name}\n'
              f'Состояние голода: {self.hunger}\n')


class House:

    fridge = 50
    money = 0

    def print_info(self):
        print(f'Количество денег: {self.money}\n'
              f'Заполненность холодильника: {self.fridge}')

