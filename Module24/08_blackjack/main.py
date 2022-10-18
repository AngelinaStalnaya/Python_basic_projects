from Black_Jack_21 import *


def game():
    deck = Deck()
    player = Player(input('Введите имя игрока: '))
    dealer = Player('Дилер')

    for i in range(2):
        player.hand(deck.pass_card())
        dealer.hand(deck.pass_card())

    while player.get_cards_value() < 21:
        player.print_player_info()
        answer = input('Хотите набрать карту? да/нет: ').lower()
        if answer == 'да':
            player.hand(deck.pass_card())
        else:
            break
    if player.get_cards_value() == 21 or dealer.get_cards_value() < player.get_cards_value() < 21:
        player.print_player_info()
        dealer.print_player_info()
        print('Вы выиграли!')
    elif player.get_cards_value() == dealer.get_cards_value() < 21:
        player.print_player_info()
        print('У Вас ничья')
    else:
        dealer.print_player_info()
        player.print_player_info()
        print('Вы проиграли!')

game()