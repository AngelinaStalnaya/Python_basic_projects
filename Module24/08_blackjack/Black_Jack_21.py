import random


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def card_value(self):
        if isinstance(self.rank, int):
            return self.rank
        else:
            if self.rank == 'Jack' or 'King' or 'Queen':
                return 10
            else:
                return 1

    def card_rank(self):
        return self.rank

    def print_card_info(self):
        print(f'{self.rank} - {self.suit}')


class Deck:

    def __init__(self):
        card_suits = ['clubs', 'diamonds', 'hearts', 'spades']
        card_ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'King', 'Queen', 'Ace']
        self.deck = [Card(suit, rank) for suit in card_suits for rank in card_ranks]
        random.shuffle(self.deck)

    def pass_card(self):
        return self.deck.pop()


class Player:

    def __init__(self, name):
        self.name = name
        self.cards = []

    def hand(self, card):
        self.cards.append(card)

    def get_cards_value(self):
        aces = 0
        total_hand = 0
        for card in self.cards:
            total_hand += card.card_value()
            if card.card_rank() == 'Aces':
                aces += 1
        if total_hand + aces * 10 <= 21: # до 21 - по 11 очков (уже 1 + 10 по кол-ву)
            total_hand += aces * 10
        return total_hand

    def print_player_info(self):
        print(f'Имя игрока: {self.name}\n'
              f'Очки карт: {self.get_cards_value()}\n')

