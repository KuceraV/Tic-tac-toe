import os

# symbols = ["x", "o"]
# board = [" ", " ", " "]
# game_is_on = True
#
#
# while game_is_on and " " in board:
#     player_o = input("Player o | Please enter your move number: ")
#     if board[int(player_o) - 1] not in symbols:
#         board[int(player_o) - 1] = "o"
#         print(board)
#     else:
#         print("Position is already taken!")
# else:
#     print("Konec hry")

board = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
win = [1, 2, 3]

if "x" in board[:3] or "x" in board[4:7] or "x" in board[6:]:
    print("Player_x wins the game")

elif "x" in board[0] and "x" in board[3] and "x" in board[6]:
    print("Player_x wins the game")

elif "x" in board[1] and "x" in board[4] and "x" in board[7]:
    print("Player_x wins the game")

elif "x" in board[2] and "x" in board[5] and "x" in board[8]:
    print("Player_x wins the game")

elif "x" in board[0] and "x" in board[4] and "x" in board[8]:
    print("Player_x wins the game")

elif "x" in board[2] and "x" in board[4] and "x" in board[6]:
    print("Player_x wins the game")

elif "o" in board[:3] or "o" in board[4:7] or "o" in board[6:]:
    print("Player_o wins the game")

elif "o" in board[0] and "o" in board[3] and "o" in board[6]:
    print("Player_o wins the game")

elif "o" in board[1] and "o" in board[4] and "o" in board[7]:
    print("Player_o wins the game")

elif "o" in board[2] and "o" in board[5] and "o" in board[8]:
    print("Player_o wins the game")

elif "o" in board[0] and "o" in board[4] and "o" in board[8]:
    print("Player_o wins the game")

elif "o" in board[2] and "o" in board[4] and "o" in board[6]:
    print("Player_o wins the game")

else:
    print("lose the game")

