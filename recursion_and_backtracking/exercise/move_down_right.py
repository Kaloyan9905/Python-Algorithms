def solution(row, col, matrix, paths):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return

    if matrix[row][col] == 'v':
        return

    if row == len(matrix) - 1 or col == len(matrix[0]) - 1:
        paths.append((row, col))
        return
    else:
        matrix[row][col] = 'v'
        solution(row + 1, col, matrix, paths)
        solution(row, col + 1, matrix, paths)
        matrix[row][col] = '-'


rows_size = int(input())
cols_size = int(input())

mtrx = [['-'] * cols_size for _ in range(rows_size)]
paths = []

solution(0, 0, mtrx, paths)
print(len(paths))
