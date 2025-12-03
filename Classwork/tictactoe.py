def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]


def print_board(board):
    print("\n")
    print("-" * 9)
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")


def is_valid(board, r, c):
    return 0 <= r < 3 and 0 <= c < 3 and board[r][c] == ' '


def make_move(board, r, c, player):
    if is_valid(board, r, c):
        board[r][c] = player
        return True
    return False


def check_winner(board, player):
    # Check rows
    for row in board:
        if row == [player, player, player]:
            return True

    # Check columns
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] == player:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def is_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True


def tic_tac_toe():
    board = create_board()
    current_player = 'X'

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")

        try:
            r = int(input("Enter row (0,1,2): "))
            c = int(input("Enter col (0,1,2): "))
        except:
            print("Invalid input. Try again.")
            continue

        if not make_move(board, r, c, current_player):
            print("Invalid move, try again.")
            continue

        # Check for win
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} WINS!")
            break

        # Check for draw
        if is_draw(board):
            print_board(board)
            print("It's a DRAW!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'


# Run the game
tic_tac_toe()
