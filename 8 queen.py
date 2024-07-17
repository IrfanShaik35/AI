def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].
    This means checking if there's a queen in the same column or diagonals.
    """
    for i in range(row):
        if board[i][col] == 1:
            return False
        
        if col - (row - i) >= 0 and board[i][col - (row - i)] == 1:
            return False
        
        if col + (row - i) < len(board) and board[i][col + (row - i)] == 1:
            return False
        
    return True

def solve_n_queens_util(board, row):
    """
    Utilizes backtracking to place queens on the board.
    """
    if row >= len(board):
        return True

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve_n_queens_util(board, row + 1):
                return True
            board[row][col] = 0  # Backtrack

    return False

def solve_n_queens(n):
    """
    Solves the N-queens problem and prints the board.
    """
    board = [[0 for _ in range(n)] for _ in range(n)]

    if solve_n_queens_util(board, 0):
        print_board(board)
    else:
        print("No solution exists")

def print_board(board):
    """
    Prints the chessboard with queens placed.
    """
    for row in board:
        print(" ".join("Q" if col == 1 else "." for col in row))
    print()

# Solve the 8-queens problem
solve_n_queens(8)
