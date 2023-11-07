N = 8  # Size of the chessboard

def is_safe(board, row, col):
    # Check if there is a Queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, row):
    if row >= N:
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1  # Place the Queen
            if solve_n_queens(board, row + 1):  # Recur to place rest of the Queens
                return True
            board[row][col] = 0  # If placing Queen doesn't lead to a solution, backtrack
    return False

# Initialize the chessboard with the first Queen already placed
chessboard = [[0 for _ in range(N)] for _ in range(N)]
chessboard[0][0] = 1

# Solve the 8-Queens problem using backtracking
if solve_n_queens(chessboard, 1):
    # Print the solution
    for row in chessboard:
        print(' '.join(['Q' if x else '.' for x in row]))
else:
    print("No solution exists.")
