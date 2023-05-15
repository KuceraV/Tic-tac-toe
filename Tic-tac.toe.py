""""
projekt_2.py: druhý projekt do Engeto Online Python Akademie - Tic-tac-toe
author: Vojtech Kucera
email: vojtechkuc@gmail.com
discord: Vojta K.
"""


def main():
    board = playground()
    welcome_text()
    write_out_playground(board)
    game(board)


def welcome_text():
    """
    function welcome the users a briefly introduce the rules of the game
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


def playground() -> list:
    """
    Function defines the playground  with 9 values(position) of Tic-Tac-Toe as a list.
    Space is set as default value in playground.

    example:
    [" " , " " ," "  ," "  ," "  ," "  ," "  ," "  , " " ]
    """
    board = [" " for i in range(9)]
    return board


def write_out_playground(board: list):
    """
    function formats the playground to 3 x 3 grid:

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

    separator_grid = "+---+---+---+"

    for i in range(3):
        print(
            separator_grid,
            f'|{"|".join(board[(i * 3):(i * 3 + 3)])}|',
            sep="\n"
        )
    print(separator_grid)


def game(board: list):
    """
    Function activates the player's moves. If the winning condition is not met and all moves are taken,
    it is ended the game as a tie.
    """
    separator = "=" * 40
    players = {"player_o": "o", "player_x": "x"}
    while " " in board:
        player_move(board, players)

    else:
        print(
            separator,
            "Tie, Game over!",
            separator,
            sep="\n"
        )


def player_move(board: list, players: dict):
    """
    Function ask player to insert number of the move, where to place the symbol.
    If the input is not digit, function warn player to insert only integer
    If the input is out of board range, function warn player
    If the position is already occupied , function warn player
    If the winning conditions are fulfilled, it ends the game
    If the winning condition is not met and all moves are taken, it breaks the cycle with players input.
    """
    separator = "=" * 40
    for move in players:
        player_input = True
        while player_input and " " in board:

            print(separator)
            index = input(f"{move} | Please enter your move number: ")
            print(separator)

            if index.isdigit():
                index = int(index)

                if index not in range(1, 10):
                    print("Move number is out of range of the board!")

                elif board[index - 1] == " ":
                    player_input = False
                    board[index - 1] = players[move]
                    write_out_playground(board)

                    if not win_conditions(board, players[move]):
                        game_over(players[move])

                else:
                    print("Position is already taken!")

            else:
                print("Move number has to be integer!")


def win_conditions(board: list, symbol: str) -> bool:
    """
    function control the winning condition. The winning condition is when one of the symbols fill
    one of the rows or columns or diagonals.

    +---+---+---+
    | |x| |
    +---+---+---+
    | |x| |
    +---+---+---+
    | |x| |
    +---+---+---+
    game_on = False
    """

    game_on = True
    if symbol == board[0] == board[1] == board[2]:
        game_on = False

    elif symbol == board[3] == board[4] == board[5]:
        game_on = False

    elif symbol == board[6] == board[7] == board[8]:
        game_on = False

    elif symbol == board[0] == board[3] == board[6]:
        game_on = False

    elif symbol == board[1] == board[4] == board[7]:
        game_on = False

    elif symbol == board[2] == board[5] == board[8]:
        game_on = False

    elif symbol == board[0] == board[4] == board[8]:
        game_on = False

    elif symbol == board[2] == board[4] == board[6]:
        game_on = False

    return game_on


def game_over(players_move: str):
    """
    function ended the game when winning conditions are fulfilled and print the winner.
    """
    separator = "=" * 40
    print(
        separator,
        f"Congratulations, the player {players_move} WON!",
        separator,
        sep="\n"
    )
    quit()


if __name__ == "__main__":
    main()