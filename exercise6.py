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

    print ("Player " + player + " plays")

    while True:
        row = int(input("Enter row number: "))
        col = int(input("Enter column number: "))
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid row or column number")
            continue
        elif board[row][col] != " ":
            print("Row or column occupied")
            continue
        else:
            break

else:
    print("+---+---+---+")
    print("| " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
    print("+---+---+---+")
    print("| " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
    print("+---+---+---+")
    print("| " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
    print("+---+---+---+")
    print("draw")
