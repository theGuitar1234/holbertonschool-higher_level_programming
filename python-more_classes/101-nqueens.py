#!/usr/bin/python3

import sys


def print_usage_and_exit():
    print("Usage: nqueens N")
    sys.exit(1)


def solve_nqueens(n):
    # cols[r] = c means: in row r, queen is placed at column c
    cols = [-1] * n

    used_cols = set()
    used_diag1 = set()  # r - c
    used_diag2 = set()  # r + c

    def backtrack(r):
        if r == n:
            # Build output format: [[row, col], ...]
            solution = [[i, cols[i]] for i in range(n)]
            print(solution)
            return

        for c in range(n):
            d1 = r - c
            d2 = r + c
            if c in used_cols or d1 in used_diag1 or d2 in used_diag2:
                continue

            cols[r] = c
            used_cols.add(c)
            used_diag1.add(d1)
            used_diag2.add(d2)

            backtrack(r + 1)

            used_cols.remove(c)
            used_diag1.remove(d1)
            used_diag2.remove(d2)
            cols[r] = -1

    backtrack(0)


def main():
    if len(sys.argv) != 2:
        print_usage_and_exit()

    n_str = sys.argv[1]
    try:
        n = int(n_str)
    except Exception:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)


if __name__ == "__main__":
    main()
