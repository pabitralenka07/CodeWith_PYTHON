def solve_n_queens(N):
    solutions = []

    rows = [-1] * N
    cols = [False] * N
    d1 = [False] * (2 * N)
    d2 = [False] * (2 * N)

    def place_queen(row, col):
        rows[col] = row
        cols[row] = True
        d1[row + col] = True
        d2[row - col + N] = True

    def remove_queen(row, col):
        rows[col] = -1
        cols[row] = False
        d1[row + col] = False
        d2[row - col + N] = False

    def solve(col):
        if col == N:
            solutions.append(rows[:])
            return

        for row in range(N):
            if cols[row] or d1[row + col] or d2[row - col + N]:
                continue

            place_queen(row, col)
            solve(col + 1)
            remove_queen(row, col)

    solve(0)
    return solutions


# Main Program
N = int(input("Enter the value of N: "))
solutions = solve_n_queens(N)

print(f"\nTotal Solutions: {len(solutions)}")

for i, sol in enumerate(solutions, 1):
    print(f"Solution {i}: {sol}")
    