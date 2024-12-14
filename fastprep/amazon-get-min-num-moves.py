#!/usr/bin/env python3

# case 1 (answer = 3)
# blocks = [2, 4, 3, 1, 6]

# case 1a (answer = 5)
# blocks = [2, 6, 4, 1, 3]

# case 2 (answer = 0)
# blocks = [4, 11, 9, 10, 12]

# case 3 (answer = 3)
blocks = [3, 2, 1]


def getMinNumMoves() -> int:
    """Find min num moves"""
    n_blocks = len(blocks)
    min_ind = blocks.index(min(blocks))
    max_ind = blocks.index(max(blocks))
    print(f"min_ind = {min_ind}, max_ind = {max_ind}, len = {n_blocks}")

    n_moves = min_ind + (n_blocks - max_ind - 1)
    if max_ind < min_ind:
        n_moves -= 1
    return n_moves


print(getMinNumMoves())
