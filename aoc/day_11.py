import itertools
from typing import Tuple

import numpy as np


def part_one(file_path: str, n: int = 100) -> int:
    """
    Calculates how many flashes there are in n runs of the simulation

    Args:
        file_path (str):
        n (int, optional): Number of simulations. Defaults to 100.

    Returns:
        int: Number of flashes
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()

    # initialise array
    X = np.array([[int(number) for number in line.strip()] for line in lines])

    # initialise n_flashes
    n_flashes = 0
    for _ in range(n):
        # run simulation
        X = run_simulation(X)
        # add number of flashes
        n_flashes += len(np.argwhere(X == 0))

    return n_flashes


def part_two(file_path: str) -> int:
    """
    Runs simulation until all elements flash

    Args:
        file_path (str):

    Returns:
        int: number of steps until the elements flash
    """
    # read file
    with open(file_path) as f:
        lines = f.readlines()
    # initialise array
    X = np.array([[int(number) for number in line.strip()] for line in lines])
    # set n
    n = 0
    # while any are not 0
    while (X != 0).any():
        # run simulation
        X = run_simulation(X)

        n += 1

    return n


def run_simulation(X: np.array) -> np.array:
    """Runs simulation on array

    Args:
        X (np.array): input array

    Returns:
        np.array: output array after simulation
    """

    n, m = X.shape
    # increase all by one
    X += 1
    # get initial list of flashers
    flashers = [tuple(x) for x in np.argwhere(X > 9)]
    # get initial list of flashed
    flashed = []
    # while having to still run a simulation on a flasher
    while len(flashers) > 0:
        # remove a flasher
        i, j = flashers.pop()
        # add 1 to all neighbours
        X[get_neighbour_indices(i, j, n, m)] += 1
        # move flasher to flashed
        flashed.append((i, j))
        # recalculate flashers
        flashers = [tuple(x) for x in np.argwhere(X > 9) if tuple(x) not in flashed]
    # return any that flashed to 0
    X = np.where(X > 9, 0, X)
    return X


def get_neighbour_indices(i: int, j: int, n: int, m: int) -> Tuple[np.array]:
    """
    Returns the neighbouring (including diagonals) indices of
    i,j of a n x m array.

    Args:
        i (int): row indice
        j (int): column indice
        n (int): n rows
        m (int): m columns

    Returns:
        Tuple[np.array]: array of rows, array of columns
    """
    # get neighbouring rows
    rows = [i - 1, i, i + 1]
    columns = [j - 1, j, j + 1]

    # get all pairs
    pairs = itertools.product(rows, columns)

    # initialise list
    rows = []
    columns = []

    # for each pair
    for i, j in pairs:
        # if values are not out of bound
        if not (i < 0 or i == n or j < 0 or j == m):
            # keep those values
            rows.append(i)
            columns.append(j)
    return np.array(rows), np.array(columns)


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_11.txt"))
    print(part_two("aoc/inputs/day_11.txt"))
