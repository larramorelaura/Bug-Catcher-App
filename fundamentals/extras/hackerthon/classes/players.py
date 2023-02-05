from . import deck

card_deck=deck.Deck()

class Player:
    def __init__(self):
        self.hand= []
        # self.hand.append(deal_card)

    def hit(self):
        self.hand.append(card_deck.deal_card())

    def stay(self):
        pass
    



