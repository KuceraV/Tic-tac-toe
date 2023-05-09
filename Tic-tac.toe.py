""""
projekt_2.py: druhý projekt do Engeto Online Python Akademie - Tic-tac-toe
author: Vojtech Kucera
email: vojtechkuc@gmail.com
discord: Vojta K.
"""

import os


def main():
    game_is_on = True


def welcome_text() -> str:
    """
    function welcome the user a briefly introduce the rules of the game
    """
    separator = "=" * 40
    print(
        "Welcome to Tic Tac Toe ",
        separator,
        "GAME RULES:",
        """Each player can place one mark (or stone) 
per turn on the 3x3 grid. The WINNER is 
who succeeds in placing three of their
marks in a: """,
        "* horizental,",
        "* vertical or",
        "* diagonal row",
        separator,
        "Let's start the game",
        sep="\n"
    )


welcome_text()


def playground(index=" ") -> list:
    """"
    Function define the playground  with 9 values(position) of Tic-Tac-Toe as a list
    Space is set as default value in playground, and it is replaced by the symbol
    input of the player.

    example: player_x input: 2
    [  ,"x" ,  ,  ,  ,  ,  ,  ,  ]
    """
    board = [index for i in range(10)]
    return board


def write_out_playground(board: list) -> str:
    """"
    function formats the playground to 3 x 3 grid and show current status:

    expamle:
    [  ,"x" ,  ,  ,  ,  ,  ,  ,  ]
    +---+---+---+
    | |x| |
    +---+---+---+
    | | | |
    +---+---+---+
    | | | |
    +---+---+---+
    """
    # os.system("cls") - bad position - delete everything even the introduction

    separator_grid = "+---+---+---+"

    for i in range(3):
        print(
            separator_grid,
            f'|{"|".join(board[(i * 3):(i * 3 + 3)])}|',
            sep="\n"
        )
    print(separator_grid)


def player_move(board: list):
    """
    Function as player to insert number of the move, where to place the symbol.
    If the input is not digit, function warn player to insert only integer
    If the input is out of board range, function warn player
    If the position is already occupied , function warn player
    """

    symbols = ["o", "x"]
    players = {"player_o": "o", "player_x": "x"}

    for move in players:
        index = input(f"{move} | Please enter your move number: ")

        if index.isdigit():
            index = int(index)

            if index not in range(1, 10):
                print("Move number is out of range of the board!")

            elif board[index - 1] not in symbols:
                board[index - 1] = players[move]
                write_out_playground(board)

            else:
                print("Position is already taken!")
        else:
            print("Move number has to be integer!")


def game(game_is_on):
    board = playground()
    write_out_playground(board)

    while game_is_on and " " in board:
        player_move(board)
        win_conditions(board)

    else:
        print("It is a tie.")


game(True)


def win_conditions(board):
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

# def player_o(board):
#     symbols = ["x", "o"]
#
#     player_move = int(input("Player o | Please enter your move number: ")) - 1
#
#     if board[player_move] not in symbols:
#         board[player_move] = "o"
#     else:  # " " not in board[player_o]:
#         print("Position is already taken!")
#     # elif player_o not in range(1, 10):
#     #     print("Please insert number only in range 1 to 9")
#
#
# def player_x(board):
#     symbols = ["x", "o"]
#
#     player_move = int(input("Player x | Please enter your move number: ")) - 1
#
#     if board[player_move] not in symbols:
#         board[player_move] = "x"
#     else:  # " " not in board[player_o]:
#         print("Position is already taken!")
#     # elif player_o not in range(1, 10):
#     #     print("Please insert number only in range 1 to 9")