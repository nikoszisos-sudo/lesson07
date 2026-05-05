from random import randrange
kind = {"heart", "diamond", "spade", "club"}
number = {"ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"}
deck = {(k,n) for k in kind for n in number } #(k,n) is tuple (immutable) inside a set (deck)
print(len(deck))
print(deck)

player1 = set()
player2 = set()

my_deck = list(deck)
for i in range(5):
    pos1 = randrange(0, len(my_deck)) #random item from my_deck
    player1.add(my_deck.pop(pos1))  # pop this item from my_deck and add it to player1 set
    pos2 = randrange(0, len(my_deck))
    player2.add(my_deck.pop(pos2))
print(player1)
print(player2)







