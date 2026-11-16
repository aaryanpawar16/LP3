N = 8
board = [-1] * N  # board[col] = row of queen in that column


def safe(row, col):
    return all(board[c] != row and abs(board[c] - row) != abs(c - col)
               for c in range(N) if board[c] != -1)


def solve(col):
    if col == N:
        return True
    if board[col] != -1:  # column holding the user's first queen
        return solve(col + 1)
    for row in range(N):
        if safe(row, col):
            board[col] = row
            if solve(col + 1):
                return True
            board[col] = -1  # backtrack
    return False


r, c = int(input("First queen row (0-7): ")), int(input("First queen col (0-7): "))
board[c] = r
if solve(0):
    for row in range(N):
        print(" ".join("Q" if board[col] == row else "." for col in range(N)))
else:
    print("No solution")


# ======================= VIVA QUESTIONS =======================
# Q: State the 8-Queens problem.
# A: Place 8 queens on an 8x8 board so that no two attack each other (no common row, column or diagonal).
# Q: What is backtracking?
# A: DFS over a state-space tree: extend a partial solution step by step and undo (backtrack) when a
#    constraint is violated, pruning that whole branch.
# Q: How does your code ensure the constraints?
# A: One queen per column by construction (board[col] = row); safe() checks the same row and
#    diagonals with abs(r1 - r2) == abs(c1 - c2).
# Q: How is the given first queen handled?
# A: It is pre-placed in board[c]; solve() skips that column and fills the rest.
# Q: Brute force vs backtracking?
# A: Brute force tries C(64,8) ~ 4.4 billion placements (or 8^8 ~ 16.7 million with one per column);
#    backtracking prunes invalid partial boards early.
# Q: Time complexity?
# A: Worst case O(N!); space O(N) for the board and recursion stack.
# Q: How many solutions exist for 8 queens?
# A: 92 total, 12 distinct (excluding rotations/reflections).
# Q: Does every first-queen position have a solution for N=8?
# A: Yes. Note N=2 and N=3 have no solution.
# Q: Backtracking vs branch and bound?
# A: Backtracking is DFS with feasibility pruning (enumeration/decision problems); branch and bound uses
#    bounds with BFS/best-first for optimization problems.
# Q: How can safe() be made O(1)?
# A: Keep boolean arrays for rows, diagonals (r+c) and anti-diagonals (r-c), or use bitmasks.
# Q: What is a state-space tree / bounding function?
# A: Tree of all partial solutions; the bounding function (safe) cuts branches that cannot lead to a solution.
# Q: What if no solution exists?
# A: solve() returns False after all options are exhausted and the program prints "No solution".
# Q: Applications of backtracking?
# A: Sudoku, graph colouring, maze solving, subset sum, Hamiltonian cycle, constraint satisfaction.
