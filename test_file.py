def win_conditions(board: list, symbol):
    win = True
    if symbol == board[0] == board[1] == board[2]:
        win = False
        print(f"Player {symbol} wins the game")

    elif symbol == board[3] == board[4] == board[5]:
        win = False
        print(f"Player {symbol} wins the game")

    elif symbol == board[6] == board[7] == board[8]:
        win = False
        print(f"Player {symbol} wins the game")

    elif symbol == board[0] == board[3] == board[6]:
        win = False
        print(f"Player {symbol} wins the game")

    elif symbol == board[1] == board[4] == board[7]:
        win = False
        print(f"Player {symbol} wins the game")

    elif symbol == board[2] == board[5] == board[8]:
        win = False
        print(f"Player {symbol} wins the game")

    elif symbol == board[0] == board[4] == board[8]:
        win = False
        print(f"Player {symbol} wins the game")

    elif symbol == board[2] == board[4] == board[6]:
        win = False
        print(f"Player {symbol} wins the game")

    return win
