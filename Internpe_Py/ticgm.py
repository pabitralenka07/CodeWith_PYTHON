def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    
    while True:
        for player in players:
            valid_move = False
            while not valid_move:
                try:
                    move = int(input(f"Player {player}, enter a position (1-9): ")) - 1
                    row, col = divmod(move, 3)
                    if board[row][col] == " ":
                        board[row][col] = player
                        valid_move = True
                    else:
                        print("Cell already taken, choose another.")
                except (ValueError, IndexError):
                    print("Invalid input, please enter a number between 1 and 9.")
            
            print_board(board)
            
            if check_winner(board, player):
                print(f"Player {player} wins!")
                return
            
            if is_full(board):
                print("It's a draw!")
                return

tic_tac_toe()
