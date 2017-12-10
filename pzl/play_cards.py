from itertools import product
from random import shuffle, sample

class Card(object):

    def __init__(self):
        self.shape = ['Diamond', 'Hearts', 'Spear', 'Clubs']
        self.num = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.all_cards = list(product(self.shape, self.num))
        self.dict_cards = {ids: val for ids, val in enumerate(self.all_cards)}

    def display_cards(self):
        return self.dict_cards

    def shuffle_cards(self):
        card_keys = list(self.dict_cards.keys())
        shuffle(card_keys)
        return {card_key: self.dict_cards[card_key] for card_key in card_keys}

    def sort_cards(self, shuffle_card):
        card_keys = sorted(list(shuffle_card.keys()))
        return {card_key: self.dict_cards[card_key] for card_key in card_keys}

    def random_card(self, card_deck):
        deck = card_deck
        card_keys = list(deck.keys())
        card = sample(card_keys, 1)[0]
        random_pick = deck[card]
        return random_pick

if __name__ == '__main__':
    cd = Card()
    print('\n Before shuffling .... \n')
    for card in cd.display_cards().values():
        print(card)

    print('\n After shuffling .... \n')
    shuffle_cards_deck = cd.shuffle_cards()
    for card in shuffle_cards_deck.values():
        print(card)

    print('\n After ordering .... \n')

    sorted_cards = cd.sort_cards(shuffle_cards_deck)
    for card in sorted_cards.values():
        print(card)

    print('\n Random pick a card ...\n ')
    pick = cd.random_card(shuffle_cards_deck)
    print(pick)








