from random import sample
from sys import argv

if len(argv) == 4:
    width = int(argv[1])
    height = int(argv[2])
    num_mines = int(argv[3])
else:
    width = 20
    height = 17
    num_mines = 20

def contains_mine(x, y):
    return y * height + x in mine_poses


def get_adjacent_cells(x, y):
    output = []

    if x > 0:
        output.append([x - 1, y])
        if y > 0:
            output.append([x - 1, y - 1])

    if x < width - 1:
        output.append([x + 1, y])
        if y < height - 1:
            output.append([x + 1, y + 1])

    if y > 0:
        output.append([x, y - 1])
        if x < width - 1:
            output.append([x + 1, y - 1])

    if y < height - 1:
        output.append([x, y + 1])
        if x > 0:
            output.append([x - 1, y + 1])

    return output


def count_adjacent_mines(x, y):
    output = 0

    for adj_x, adj_y in get_adjacent_cells(x, y):
        if contains_mine(adj_x, adj_y):
            output += 1

    return output


def cell_indicator(x, y):
    if contains_mine(x, y):
        return "*"

    num_adjacent_mines = count_adjacent_mines(x, y)

    if num_adjacent_mines > 0:
        return str(num_adjacent_mines)

    return " "


mine_poses = sample(range(0, width * height), num_mines)

for y in range(height):
    print ' '.join(cell_indicator(x, y) for x in range(width))

