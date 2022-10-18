
class Unit:

    def __init__(self, name='Воин', health=100):
        self.name = name
        self.health = health

    def kick(self):
        self.health -= 20


warrior_1 = Unit('Воин_1')
warrior_2 = Unit('Воин_2')


while min(warrior_1.health, warrior_2.health) > 0:
    whose_turn = input('Кто наносит удар: 1- Воин_1 или 2-Воин_2. Выбор: ')
    if whose_turn == '1':
        print('Воин_1 наносит удар Воину_2')
        warrior_2.kick()
        print(f'У Воина_2 осталось {warrior_2.health} очков здоровья\n')
    elif whose_turn == '2':
        print('Воин_2 наносит удар Воину_1')
        warrior_1.kick()
        print(f'У Воина_1 осталось {warrior_1.health} очков здоровья\n')
    else:
        print('\nОшибка ввода команды, попробуйте снова.\n')


print(f'Бой завершен! Победу одержал {warrior_1.name if warrior_1.health > 0 else warrior_2.name}')