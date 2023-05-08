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


def playground(index=" "):
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


def player_move(board):
    symbols = ["o", "x"]
    players = {"player_o": "o", "player_x": "x"}

    for move in players:
        index = int(input(f"{move} | Please enter your move number: ")) - 1

        if board[index] not in symbols:
            board[index] = players[move]
            write_out_playground(board)

        else:
            print("Position is already taken!")


def game(game_is_on):
    board = playground()
    write_out_playground(board)

    while game_is_on and " " in board:
        player_move(board)


game(True)


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