board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]



player = "O"

for i in range(9):
    print("+---+---+---+")  # prints the empty board starting from line 2 then line 1 and then line 0
    print("| " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
    print("+---+---+---+")
    print("| " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
    print("+---+---+---+")
    print("| " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
    print("+---+---+---+")

    if player == "O": #it plays X and O starting from X
        player = "X"
    else:
        player = "O"
else:
    print("+---+---+---+")
    print("| " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
    print("+---+---+---+")
    print("| " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
    print("+---+---+---+")
    print("| " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
    print("+---+---+---+")
    print("draw")
