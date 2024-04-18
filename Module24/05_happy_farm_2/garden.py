class Potato:
    states = {0: 'Посажена', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def print_state(self):
        print(f'Картошка {self.index} сейчас {Potato.states[self.state]}')

    def is_ripe(self):
        if self.state == 3:
            return True
        return False


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def garden_grow_all(self):
        print('Картошка прорастает')
        for potato in self.potatoes:
            potato.grow()

    def all_ripe(self):

        if not all(potato.is_ripe() for potato in self.potatoes):
            print('Картошка еще не созрела!')
            return False
        else:
            print('Вся картошка созрела, можно собирать')
            return True

    def print_all_status(self):
        for potato in self.potatoes:
            potato.print_state()

    def count_potato(self):
        return len(self.potatoes)

    def pick_all(self):
        self.potatoes = []
