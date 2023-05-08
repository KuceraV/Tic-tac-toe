import os

symbols = ["x", "o"]
board = [" ", " ", " "]
game_is_on = True


while game_is_on and " " in board:
    os.system("cls")
    player_o = int(input("Player o | Please enter your move number: ")) - 1
    if board[player_o] not in symbols:
        board[player_o ] = "o"
        print(board)
    else:
        print("Position is already taken!")
else:
    print("Konec hry")

