import random
from crazy_life import *


# husband = Husband(input('Введите имя мужа: '))
# wife = Wife(input('Введите имя жены: '))
# cat1 = Cat(input('Введите кличку кота: '))
# child = Child(input('Введите имя ребёнка: '))
# cat2 = Cat(input('Введите кличку кота: '))
# cat3 = Cat(input('Введите кличку кота: '))
husband = Husband('Victor')
wife = Wife('Anya')
cat1 = Cat('Puffy')
child = Child('Lisa')
cat2 = Cat('Leon')
cat3 = Cat('Molly')
family = [husband, wife, cat1, child, cat2, cat3]
my_house = House()

print(f'+{"+":-^51}+')


def new_day_life(house, family):
    for i_member in family:
        if isinstance(i_member, Cat) and i_member.satiety < 30 and house.cat_food > 0:
            i_member.eat(house)
        elif isinstance(i_member, Person) and i_member.satiety < 50 and house.food > 30:
            i_member.eat(house)
        elif isinstance(i_member, Cat):
            if random.randint(1, 2) == 1:
                i_member.scrap_off_wallpapers(house)
            else:
                i_member.sleep()
        elif isinstance(i_member, Husband):
            if house.money < 600:
                husband.go_to_work(house)
            elif husband.happiness < 60:
                if random.randint(1, 2) == 1:
                    husband.play()
                else:
                    husband.pet_cat()
        elif isinstance(i_member, Wife):
            if house.money > 300 and house.food < 150:
                wife.buy_products(house)
            elif house.money > 250 and house.cat_food < 90:
                wife.buy_cat_food(house)
            elif house.dirt > 50:
                wife.clean_house(house)
            elif house.money > 350:
                wife.buy_coat(house)
            elif wife.happiness < 40:
                wife.pet_cat()
        elif isinstance(i_member, Child):
            if child.happiness < 30:
                child.play()
            elif random.randint(1, 2) == 1:
                child.pet_cat()
            else:
                child.cry()


for day in range(365):
    print(f'День: {day + 1}\n')
    my_house.add_pollution(family)
    new_day_life(my_house, family)
    if my_house.set_dead_status(family):
        print('Эксперимент провалился.')
        break


print(f'+{"+":-^51}+')
print('Итоги прожитого года:\n')
my_house.__str__()
