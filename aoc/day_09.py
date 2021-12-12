from collections import Counter
from functools import reduce
from typing import Tuple

import numpy as np
import matplotlib.pyplot as plt


def part_one(file_path: str):
    """
    Returns the sum of the heights of local minimums
    Performs a search of all local neighbours to find local min

    Args:
        file_path (str): 

    Returns:
        int: sum of the heights of local minimums
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()

    # create numpy array
    X = np.array([[int(number) for number in line.strip()] for line in lines])
    n,m = X.shape
    
    # initialise sum
    sum1 = 0
    for i in range(n):
        for j in range(m):
            # get point
            point = X[i,j]
            # get neighbouring values
            neighbours = get_neighbours(X,i,j,n,m)
            # if point is less than all the neighbours then it is local min
            if point < neighbours.min():
                # then add it to the total
                sum1 += point+1
    return sum1


def part_two(file_path: str):
    """
    Calculates the product of the size of the 3 largest basins

    Until converge:
        iterate through each value
        if the value is not 9 then it must be part of the basin
        for each neighbour:
            if any are part of existing basin assign all non-9 neighbours
            to the same basin

    Args:
        file_path (str): 

    Returns:
        int: the product of the size of the 3 largest basins
    """

    with open(file_path) as f:
        lines = f.readlines()
    
    # create numpy array
    X = np.array([[int(number) for number in line.strip()] for line in lines])
    n,m = X.shape

    # initialise nothing in a basin
    basins = np.zeros((n,m))

    # only matters if shape is 0 or 9
    X = X != 9

    n_basins = 1
    changed = True
    
    # until converge
    while changed:
        changed = False
        # for each value
        for i in range(n):
            for j in range(m):
                # if value is not 9
                if X[i,j]:
                    # get all neighbours and included point
                    rows, columns = get_neighbour_indices(i,j,n,m)
                    rows = np.append(rows, i)
                    columns = np.append(columns, j)
                    # if any are non-zero and hence part of a basin
                    if basins[rows, columns].any():
                        # then get the lowest basin it could be part of
                        val = min([x for x in basins[rows, columns].flatten() if x!=0])
                        # then for each neighbour and point
                        for i1,j1 in zip(rows, columns):
                            # if it is not a wall (9)
                            if X[i1,j1]:
                                # change the value (and update convergence)
                                if basins[i1, j1] != val:
                                    changed = True

                                basins[i1,j1] = val
                    # if none of the neighbours are basins
                    else:
                        # then assign a new basin
                        basins[i,j] = n_basins
                        n_basins += 1

    # flatten all values
    flatten_basin = [x for x in basins.flatten() if x!=0]

    # get the sizes of the 3 largest basins
    counts = [size for basin, size in Counter(flatten_basin).most_common(3)]

    return reduce(lambda x, y: x * y, counts)

def get_neighbours(X: np.array, i:int,j:int,n:int,m:int) -> np.array:
    """
    return the values of X that are directly above,
    below, left or right of X[i,j]

    Args:
        X (np.array): array
        i (int): row indice
        j (int): column indice
        n (int): n_rows
        m (int): n_columns

    Returns:
        np.array: neighbourhood values
    """

    rows, columns = get_neighbour_indices(i,j,n,m)
    return X[rows, columns]

def get_neighbour_indices(i:int,j:int,n:int,m:int) -> Tuple[np.array]:
    """
    Returns the neighbouring (excluding diagonals) indices of
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
    rows = np.array([i-1, i, i, i+1])
    columns = np.array([j, j-1, j+1, j])
    # initialise list
    indices = []
    for k in range(4):
        # if values are not out of bound
        if not (rows[k] < 0 or rows[k]==n or columns[k] < 0  or columns[k]==m):
            # keep those values
            indices.append(k)
    return rows[indices], columns[indices]


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_09.txt"))
    print(part_two("aoc/inputs/day_09.txt"))
