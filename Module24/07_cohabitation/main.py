from life_of_humans import *
import random


year = 365
house = House()
human_1 = Human(input('Введите имя 1го человека: '), house)
human_2 = Human(input('Введите имя 2го человека: '), house)
house = House()

def play_human(human):
    cube_number = random.randint(1, 6)
    if human.hunger < 20:
        human.eat()
    elif human.home.fridge < 10:
        human.shopping_for_food()
    elif human.home.money < 50:
        human.work()
    elif cube_number == 1:
        human.work()
    elif cube_number == 2:
        human.eat()
    else:
        human.play()


while year > 0:
    choose_human = int(input(f'Выберите человека: 1 - {human_1.name} или 2 - {human_2.name} или любую другую цифру для выхода: '))
    if choose_human == 1:
        play_human(human_1)
        year -= 1
    elif choose_human == 2:
        play_human(human_2)
        year -= 1
    else:
        print(f'+{"+":-^51}+')
        human_1.print_info()
        human_2.print_info()
        house.print_info()
        break









