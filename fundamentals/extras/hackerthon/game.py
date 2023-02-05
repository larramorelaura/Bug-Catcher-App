
from classes import deck, players


bicycle = deck.Deck()

# bicycle.show_cards()
# print(f"{bicycle}")

player1=players.Player()

player1.hit()

print(f"{player1.hand}")
