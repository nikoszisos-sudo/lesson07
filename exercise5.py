from random import randrange
kind = {"Heart", "Diamond", "Spade", "Club"}
number = {"Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"}
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

#-------------------kare---------------------------------------

cnt = 0
for card in player1:
    if card[1]=="Ace":
        cnt += 1
if cnt == 4:
    print("Player1 has " + str(cnt) + " Aces. He's got quads!")
else:
    print("Player1 has " + str(cnt) + " Aces.")



cnt = 0
for card in player2:
    if card[1]=="Ace":
        cnt += 1
if cnt == 4:
    print("Player2 has " + str(cnt) + " Aces. He's got quads!")
else:
    print("Player2 has " + str(cnt) + " Aces.")


#---------------------------kenta---------------------------------

player_1_kenta = []
player_2_kenta = []

for card in player1:
    if card[1]=="Ace":
        player_1_kenta.append(1)
    elif card[1]=="Jack":
        player_1_kenta.append(11)
    elif card[1]=="Queen":
        player_1_kenta.append(12)
    elif card[1]=="King":
        player_1_kenta.append(13)
    else:
        player_1_kenta.append(card[1])
print (sorted(player_1_kenta))

for card in player2:
    if card[1]=="Ace":
        player_2_kenta.append(1)
    elif card[1]=="Jack":
        player_2_kenta.append(11)
    elif card[1]=="Queen":
        player_2_kenta.append(12)
    elif card[1]=="King":
        player_2_kenta.append(13)
    else:
        player_2_kenta.append(card[1])
print (sorted(player_2_kenta))




