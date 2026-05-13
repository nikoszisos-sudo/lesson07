board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

player = "O"

for i in range(9):
    print("  +---+---+---+")  # prints the empty board starting from line 2 then line 1 and then line 0
    print(str(2) + "| " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
    print("  +---+---+---+")
    print(str(1) + "| " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
    print("  +---+---+---+")
    print(str(0) + "| " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
    print("  +---+---+---+")
    print("    0   1   2")

    if player == "O": #it plays X and O starting from X
        player = "X"
    else:
        player = "O"

    while True:
        print("Player " + player + " plays")
        row = int(input("Enter row number: "))
        col = int(input("Enter column number: "))
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid row or column number (0-2)")
            continue
        elif board[row][col] != " ":
            print("Row or column occupied")
            continue
        else:
            board[row][col] = player
            break
    if (board[0][0] == board[0][1] == board[0][2]) and board[0][0] != " ":
        winner = player
    elif (board[1][0] == board[1][1] == board[1][2]) and board[1][0] != " ":
        winner = player
    elif (board[2][0] == board[2][1] == board[2][2]) and board[2][0] != " ":
        winner = player
    elif (board[0][0] == board[1][0] == board[2][0]) and board[0][0] != " ":
        winner = player
    elif (board[0][1] == board[1][1] == board[2][1]) and board[0][1] != " ":
        winner = player
    elif (board[0][2] == board[1][2] == board[2][2]) and board[0][2] != " ":
        winner = player
    elif (board[0][0] == board[1][1] == board[2][2]) and board[0][0] != " ":
        winner = player
    else:
        winner = player
    print("Player " + winner + " wins!")

else:
    print("+---+---+---+")
    print("| " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
    print("+---+---+---+")
    print("| " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
    print("+---+---+---+")
    print("| " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
    print("+---+---+---+")
    print("draw")
