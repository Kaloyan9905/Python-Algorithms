class Area:
    def __init__(self, _row, _col, _size):
        self.row = _row
        self.col = _col
        self.size = _size


def connected_areas(row, col, matrix):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return 0

    if matrix[row][col] == '*':
        return 0

    if matrix[row][col] == 'v':
        return 0

    matrix[row][col] = 'v'

    size = 1
    size += connected_areas(row + 1, col, matrix)
    size += connected_areas(row - 1, col, matrix)
    size += connected_areas(row, col + 1, matrix)
    size += connected_areas(row, col - 1, matrix)

    return size


rows_size = int(input())
cols_size = int(input())

mtrx = []
areas = []

for _ in range(rows_size):
    mtrx.append([x for x in input()])

for row in range(rows_size):
    for col in range(cols_size):
        area_size = connected_areas(row, col, mtrx)

        if not area_size == 0:
            areas.append(Area(row, col, area_size))

print(f'Total areas found: {len(areas)}')

for index, area in enumerate(sorted(areas, key=lambda x: x.size, reverse=True)):
    print(f'Area #{index + 1} at ({area.row}, {area.col}), size: {area.size}')
