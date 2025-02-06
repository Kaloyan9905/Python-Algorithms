def print_chess_board(board):
    for row in range(len(board)):
        print(*board[row], sep=' ')
    print()


def set_queen(row, col, board, rows, cols, left_diagonals, right_diagonals):
    board[row][col] = '*'
    rows.add(row)
    cols.add(col)
    left_diagonals.add(row - col)
    right_diagonals.add(row + col)


def remove_queen(row, col, board, rows, cols, left_diagonals, right_diagonals):
    board[row][col] = '-'
    rows.remove(row)
    cols.remove(col)
    left_diagonals.remove(row - col)
    right_diagonals.remove(row + col)


def can_place_queen(row, col, rows, cols, left_diagonals, right_diagonals):
    if row in rows:
        return False

    if col in cols:
        return False

    if (row - col) in left_diagonals:
        return False

    if (row + col) in right_diagonals:
        return False

    return True


def queens_puzzle(row, board, rows, cols, left_diagonals, right_diagonals):
    if row == 8:
        print_chess_board(board)
        return

    for col in range(8):
        if can_place_queen(row, col, rows, cols, left_diagonals, right_diagonals):
            set_queen(row, col, board, rows, cols, left_diagonals, right_diagonals)
            queens_puzzle(row + 1, board, rows, cols, left_diagonals, right_diagonals)
            remove_queen(row, col, board, rows, cols, left_diagonals, right_diagonals)


n = 8
chess_board = []

for _ in range(n):
    chess_board.append(['-'] * n)

queens_puzzle(0, chess_board, set(), set(), set(), set())
