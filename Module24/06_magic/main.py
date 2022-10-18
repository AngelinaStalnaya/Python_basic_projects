from natural_elements import *


water = Water()
air = Air()
fire = Fire()
earth = Earth()


def new_element(elem_1, elem_2):
    return elem_1 + elem_2


element_1 = new_element(water, air)
element_2 = new_element(water, fire)
element_3 = new_element(water, earth)
element_4 = new_element(air, fire)
element_5 = new_element(air, earth)
element_6 = new_element(fire, earth)


print(element_1, element_2, element_3, element_4, element_5, element_6)
elem = new_element(fire, element_6)
print(elem)


soul = Soul()

my_elem_1 = new_element(soul, water)
my_elem_2 = new_element(soul, air)
my_elem_3 = new_element(soul, fire)
my_elem_4 = new_element(soul, earth)

print(my_elem_1, my_elem_2, my_elem_3, my_elem_4)

ally_1 = soul + element_4
ally_2 = soul + element_5
ally_3 = soul + element_6
print(ally_1, ally_2, ally_3)