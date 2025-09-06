import math

# Function to print the board
def print_board(board, n):
    """
    Prints the N-Queens board in a readable format.
    """
    for i in range(n):
        for j in range(n):
            if board[i] == j:
                print("[Q] ", end="")
            else:
                print("[] ", end="")
        print()
    print()

# Function to check if a queen can be safely placed at a given row and column.
def is_safe(board, row, col):
    """
    Checks for diagonal attacks from previously placed queens.
    This is simpler because row and column safety are handled by the 1D list.
    """
    for i in range(row):
        # Check if queens are on the same diagonal
        if board[i] == col or math.fabs(board[i] - col) == math.fabs(i - row):
            return False
    return True

# Recursive function to solve the N-Queens problem using backtracking.
def n_queen(board, row, n, first_queen_row, first_queen_col):
    """
    Recursive backtracking function to find all solutions.
    """
    # Base case: If all queens are placed, we've found a solution.
    if row == n:
        print_board(board, n)
        return

    # Check if this is the row with the pre-placed queen
    if row == first_queen_row:
        # If the pre-placed queen's position is safe, continue to the next row
        if is_safe(board, row, first_queen_col):
            board[row] = first_queen_col
            n_queen(board, row + 1, n, first_queen_row, first_queen_col)
        # We don't try other columns in this row
        return

    # Try placing a queen in each column of the current row.
    for col in range(n):
        if is_safe(board, row, col):
            # Place the queen
            board[row] = col
            # Recur to place the next queen in the next row
            n_queen(board, row + 1, n, first_queen_row, first_queen_col)
            # Backtracking happens implicitly as the loop continues
            # and overwrites the board[row] value in the next iteration.

def main():
    n = 8
    
    first_queen_row = int(input("Enter the row (0-7) for the first queen: "))
    first_queen_col = int(input("Enter the column (0-7) for the first queen: "))
    print()

    # Use a 1D list where board[row] stores the column of the queen.
    board = [-1] * n  # Use -1 to indicate an empty row
    
    # Check if the initial placement is valid
    if not (0 <= first_queen_row < n and 0 <= first_queen_col < n):
        print("Invalid initial position. Please enter values between 0 and 7.")
        return 1
    
    print(f"Finding solutions with the first queen at ({first_queen_row}, {first_queen_col})...")
    
    # Start backtracking from the first row.
    # The recursive function will handle the pre-placed queen's row.
    n_queen(board, 0, n, first_queen_row, first_queen_col)

if __name__ == "__main__":
    main()
