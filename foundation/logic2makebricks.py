def makeBricks(small, big, goal):
    big_brick_size = 5

    best_num_big_bricks = (goal - goal % big_brick_size) / big_brick_size

    # If we have enough big bricks to make up to the remainder, use those
    # Otherwise use as many as we have
    if best_num_big_bricks > big:
        use_num_big_bricks = big
    else:
        use_num_big_bricks = best_num_big_bricks

    return goal - use_num_big_bricks * big_brick_size <= small


tests = [
    [3, 1, 8, True],
    [3, 1, 9, False],
    [3, 2, 10, True],
    [3, 2, 8, True],
    [3, 2, 9, False],
    [6, 1, 11, True],
    [6, 0, 11, False],
    [1, 4, 11, True],
    [0, 3, 10, True],
    [1, 4, 12, False],
    [3, 1, 7, True],
    [1, 1, 7, False],
    [2, 1, 7, True],
    [7, 1, 11, True],
    [7, 1, 8, True],
    [7, 1, 13, False],
    [43, 1, 46, True],
    [40, 1, 46, False],
    [40, 2, 47, True],
    [40, 2, 50, True],
    [40, 2, 52, False],
    [22, 2, 33, False],
    [0, 2, 10, True],
    [1000000, 1000, 1000100, True],
    [2, 1000000, 100003, False],
    [20, 0, 19, True],
    [20, 0, 21, False],
    [20, 4, 51, False],
    [20, 4, 39, True]
]

for small, big, goal, output in tests:
    if makeBricks(small, big, goal) is not output:
        print small, big, goal, "failed"
