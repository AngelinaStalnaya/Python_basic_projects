class Water:

    name = 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return None


class Air:

    name = 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None


class Fire:

    name = 'Огонь'

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Earth):
            return Lava()
        else:
            return None


class Earth:

    name = 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        else:
            return None


class Storm:
    name = 'Шторм'

    def __init__(self):
        self.components = f'{Water.name} и {Air.name}'

    def __str__(self):
        return f'Сложили  элементы {self.components} - вывели элемент {self.name}\n'

    def __add__(self, other):
        return None


class Steam:
    name = 'Пар'

    def __init__(self):
        self.components = f'{Water.name} и {Fire.name}'

    def __str__(self):
        return f'Сложили  элементы {self.components} - вывели элемент {self.name}\n'

    def __add__(self, other):
        return None


class Dirt:
    name = 'Грязь'

    def __init__(self):
        self.components = f'{Water.name} и {Earth.name}'

    def __str__(self):
        return f'Сложили  элементы {self.components} - вывели элемент {self.name}\n'

    def __add__(self, other):
        return None


class Lightning:
    name = 'Молния'

    def __init__(self):
        self.components = f'{Air.name} и {Fire.name}'

    def __str__(self):
        return f'Сложили  элементы {self.components} - вывели элемент {self.name}\n'

    def __add__(self, other):
        return None


class Dust:
    name = 'Пыль'

    def __init__(self):
        self.components = f'{Air.name} и {Earth.name}'

    def __str__(self):
        return f'Сложили  элементы {self.components} - вывели элемент {self.name}\n'

    def __add__(self, other):
        return None


class Lava:
    name = 'Лава'

    def __init__(self):
        self.components = f'{Fire.name} и {Earth.name}'

    def __str__(self):
        return f'Сложили  элементы {self.components} - вывели элемент {self.name}\n'

    def __add__(self, other):
        return None


class Soul:

    name = 'Душа'

    def __add__(self, other):
        if isinstance(other, Water):
            return Mermaid()
        elif isinstance(other, Fire):
            return Fenix()
        elif isinstance(other, Air):
            return Fairy()
        elif isinstance(other, Earth):
            return Goddess()
        elif isinstance(other, Lightning):
            return Zeus()
        elif isinstance(other, Dust):
            return DustBunny()
        elif isinstance(other, Lava):
            return Volcanus()
        else:
            return None


class Mermaid:

    def __init__(self):
        self.components = f'{Soul.name} и {Water.name}'
        self.name = 'Русалка'

    def __str__(self):
        return f'Сложили  элементы {self.components} - появился союзник {self.name}\n'

    def __add__(self, other):
        return None


class Fenix:

    def __init__(self):
        self.components = f'{Soul.name} и {Fire.name}'
        self.name = 'Феникс'

    def __str__(self):
        return f'Сложили  элементы {self.components} - появился союзник {self.name}\n'

    def __add__(self, other):
        return None


class Fairy:

    def __init__(self):
        self.components = f'{Soul.name} и {Air.name}'
        self.name = 'Фея'

    def __str__(self):
        return f'Сложили  элементы {self.components} - появился союзник {self.name}\n'

    def __add__(self, other):
        return None


class Goddess:

    def __init__(self):
        self.components = f'{Soul.name} и {Earth.name}'
        self.name = 'Богиня Земли'

    def __str__(self):
        return f'Сложили  элементы {self.components} - появился союзник {self.name}\n'

    def __add__(self, other):
        return None


class Zeus:

    def __init__(self):
        self.components = f'{Soul.name} и {Lightning.name}'
        self.name = 'Бог грома Зевс'

    def __str__(self):
        return f'Сложили  элементы {self.components} - появился союзник {self.name}\n'

    def __add__(self, other):
        return None


class DustBunny:

    def __init__(self):
        self.components = f'{Soul.name} и {Dust.name}'
        self.name = 'Пыльный Кролик'

    def __str__(self):
        return f'Сложили  элементы {self.components} - появился союзник {self.name}\n'

    def __add__(self, other):
        return None


class Volcanus:

    def __init__(self):
        self.components = f'{Soul.name} и {Lava.name}'
        self.name = 'Богиня Пеле (покровительница вулканов и магмы)'

    def __str__(self):
        return f'Сложили  элементы {self.components} - появился союзник {self.name}\n'

    def __add__(self, other):
        return None
