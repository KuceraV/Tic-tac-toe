board = [" " for i in range(10)]
players = {"player_o": "o", "player_x": "x"}

for move in players:
    index = input(f"{move} | Please enter your move number: ")

    if index.isdigit():
        index = int(index)

        if index not in range(1, 10):
            print("Move number is out of range of the board!")

        elif board[index - 1] == " ":
            board[index - 1] = players[move]
            write_out_playground(board)
            if not win_conditions(board, players[move]):
                print(f"Congratulations, the player {players[move]} WON!")
                break

        else:
            print("Position is already taken!")

    else:
        print("Move number has to be integer!")
        continue


def write_out_playground(board: list):
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