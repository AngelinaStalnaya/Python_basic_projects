import random

from garden import PotatoGarden


class Gardener:

    def __init__(self, name, garden):
        self.name = name
        self.garden = garden

    def care_garden(self):
        care_steps = ['полил', 'обработал от жуков', 'окучил', 'удобрил']
        print(f'\nСадовник {self.name} {random.choice(care_steps)} грядку картошки')
        self.garden.garden_grow_all()

    def harvest(self):
        count_potatoes = []
        if self.garden.all_ripe():
            count_potatoes.append(self.garden.count_potato())
            self.garden.pick_all()
            print(f'Садовник {self.name} собрал урожай: {sum(count_potatoes)} кустов картошки')
        else:
            print('Урожай еще не созрел!')


garden1 = PotatoGarden(5)
gardener = Gardener('Mike', garden1)
gardener.care_garden()
gardener.care_garden()
gardener.care_garden()
gardener.harvest()
garden2 = PotatoGarden(7)
gardener = Gardener('Mike', garden2)
gardener.care_garden()
gardener.care_garden()
gardener.care_garden()
gardener.harvest()
garden3 = PotatoGarden(9)
gardener = Gardener('Mike', garden3)
gardener.care_garden()
gardener.care_garden()
gardener.care_garden()
gardener.harvest()

