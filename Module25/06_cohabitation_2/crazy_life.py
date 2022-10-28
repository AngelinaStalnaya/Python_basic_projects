
class House:
    total_food = 0
    total_cat_food = 0
    total_money_earned = 0
    total_coats = 0

    def __init__(self):
        self.money = 100
        self.food = 50
        self.cat_food = 30
        self.dirt = 0

    def add_pollution(self, family):
        self.dirt += 5
        if self.dirt > 90:
            for i_member in family:
                if isinstance(i_member, Person):
                    i_member.happiness -= 10

    def food_minus(self, food_amount):
        self.food -= food_amount
        self.total_food += food_amount

    def cat_food_minus(self, cat_food_amount):
        self.cat_food -= cat_food_amount
        self.total_cat_food += cat_food_amount

    def fridge_food(self, food_amount):
        self.food += food_amount

    def fridge_cat_food(self, cat_food_amount):
        self.cat_food += cat_food_amount

    def set_dead_status(self, family):
        for i_member in family:
            if i_member.satiety < 0:
                print(f'{i_member.get_name()} умер от голода')
                return True
            elif i_member.happiness < 10 and isinstance(i_member.get_name(), Person):
                print(f'{i_member.get_name()} умер от депрессии.')
                return True
            else:
                return False

    def __str__(self):
        print(f'Все члены семьи живы и здоровы!\n\n'
              f'Съедено еды: {self.total_food} ед.\n'
              f'Съедено еды котами: {self.total_cat_food} ед.\n'
              f'Куплено шуб женой: {self.total_coats} шт.\n'
              f'Заработано денег мужем: {self.total_money_earned} у.е.\n'
              f'Осталось денег в тумбочке: {self.money} у.е.\n'
              f'Осталось еды в холодильнике: {self.food} ед.\n'
              f'Осталось кошачьей еды: {self.cat_food} ед.\n'
              f'Уровень загрязнённости дома: {self.dirt}%')


class Creature:

    def __init__(self, name):
        self.__name = name
        self.satiety = 30

    def get_name(self):
        return self.__name


class Person(Creature):

    def __init__(self, name):
        super().__init__(name)
        self.happiness = 100

    def pet_cat(self):
        self.happiness += 5
        self.satiety -= 10
        print(f'{self.get_name()} погладил(а) кота.\n')

    def eat(self, house, food_amount=30):
        self.satiety += food_amount
        house.food_minus(food_amount)
        print(f'{self.get_name()} поел(a).\n')

    def __str__(self):
        print(f'Имя: {self.get_name()}\n'
              f'Уровень счастья: {self.happiness}\n'
              f'Уровень сытости: {self.satiety}\n')

    def check_happiness(self, family):
        for i_member in family:
            if isinstance(i_member, Person) and self.happiness > 90:
                return True


class Husband(Person):

    def play(self):
        self.satiety -= 10
        self.happiness += 20
        print(f'Муж {self.get_name()} поиграл в компьютер.\n')

    def go_to_work(self, house):
        self.satiety -= 10
        house.money += 150
        house.total_money_earned += 150
        print(f'Муж {self.get_name()} сходил на работу.\n')


class Wife(Person):

    def buy_products(self, house, food_amount=100):
        self.satiety -= 10
        house.fridge_food(food_amount)
        house.money -= food_amount
        print(f'Жена {self.get_name()} купила продукты.\n')

    def buy_cat_food(self, house, cat_food_amount=60):
        self.satiety -= 10
        house.fridge_cat_food(cat_food_amount)
        house.money -= cat_food_amount
        print(f'Жена {self.get_name()} купила кошачью еду.\n')

    def buy_coat(self, house):
        self.satiety -= 10
        house.money -= 350
        self.happiness += 60
        house.total_coats += 1
        print(f'Жена {self.get_name()} купила шубу.Несмотря на то, что шуба была очень дорогая, она счастлива!\n')

    def clean_house(self, house):
        self.satiety -= 10
        house.dirt -= 100
        if house.dirt < 0:
            house.dirt = 0
        print(f'Жена {self.get_name()} убралась дома.\n')


class Cat(Creature):

    def sleep(self):
        self.satiety -= 10
        print(f'Кот {self.get_name()} поспал.\n')

    def scrap_off_wallpapers(self, house):
        self.satiety -= 10
        house.dirt += 5
        print(f'Кот {self.get_name()} подрал обои.\n')

    def eat(self, house, cat_food_amount=10):
        self.satiety += cat_food_amount * 2
        house.cat_food_minus(cat_food_amount)
        print(f'Кот {self.get_name()} поел.\n')

    def __str__(self):
        print(f'Имя: {self.get_name()}\n'
              f'Уровень сытости: {self.satiety}\n')


class Child(Person):

    def play(self):
        self.satiety -= 10
        self.happiness += 10
        print(f'Ребёнок {self.get_name()} поиграл.\n')

    def cry(self):
        self.happiness -= 20
        self.satiety -= 10
        print(f'Ребёнок {self.get_name()} плачет.\n')

    def laugh(self):
        self.happiness += 10
        self.satiety -= 10
        print(f'Ребёнок {self.get_name()} смеётся.\n')


