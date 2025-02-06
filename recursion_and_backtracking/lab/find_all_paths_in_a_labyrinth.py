def find_all_paths_in_a_labyrinth(row, col, labyrinth, direction, path):
    if row < 0 or col < 0 or row >= len(labyrinth) or col >= len(labyrinth[0]):
        return

    if labyrinth[row][col] == '*':
        return

    if labyrinth[row][col] == 'v':
        return

    path.append(direction)

    if labyrinth[row][col] == 'e':
        print(*path, sep='')

    else:
        labyrinth[row][col] = 'v'

        find_all_paths_in_a_labyrinth(row - 1, col, labyrinth, 'U', path)  # up
        find_all_paths_in_a_labyrinth(row + 1, col, labyrinth, 'D', path)  # down
        find_all_paths_in_a_labyrinth(row, col - 1, labyrinth, 'L', path)  # left
        find_all_paths_in_a_labyrinth(row, col + 1, labyrinth, 'R', path)  # right

        labyrinth[row][col] = '-'

    path.pop()


rows = int(input())
cols = int(input())

matrix = []

for _ in range(rows):
    matrix.append(list(input()))

find_all_paths_in_a_labyrinth(0, 0, matrix, '', [])
