import random
import numpy as np

# Constants
ROWS = 6
COLUMNS = 7
EMPTY = 0
PLAYER1 = 1
PLAYER2 = 2

# Create the game board
def create_board():
    return np.zeros((ROWS, COLUMNS), int)

# Drop a piece in the board
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# Check if the column is valid for a drop
def is_valid_location(board, col):
    return board[ROWS-1][col] == EMPTY

# Get the next open row in the column
def get_next_open_row(board, col):
    for r in range(ROWS):
        if board[r][col] == EMPTY:
            return r

# Print the board
def print_board(board):
    print(np.flip(board, 0))

# Check for a win
def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMNS-3):
        for r in range(ROWS):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLUMNS):
        for r in range(ROWS-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(COLUMNS-3):
        for r in range(ROWS-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(COLUMNS-3):
        for r in range(3, ROWS):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

# Main game loop
def main():
    board = create_board()
    print_board(board)
    game_over = False

    # Randomly decide which player goes first
    turn = random.randint(0, 1)
    print(f"Player {turn + 1} goes first!")

    while not game_over:
        # Ask for Player 1 Input
        if turn == 0:
            col = int(input("Player 1 Make your Selection (0-6):"))

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, PLAYER1)

                if winning_move(board, PLAYER1):
                    print_board(board)
                    print("Player 1 wins!")
                    game_over = True

        # Ask for Player 2 Input
        else:
            col = int(input("Player 2 Make your Selection (0-6):"))

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, PLAYER2)

                if winning_move(board, PLAYER2):
                    print_board(board)
                    print("Player 2 wins!")
                    game_over = True

        print_board(board)
        turn += 1
        turn = turn % 2  # Switch turns

if __name__ == "__main__":
    main()