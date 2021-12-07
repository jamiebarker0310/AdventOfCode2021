from os import error
import numpy as np

def part_one(file_path: str) -> int:
    """
    returns the absolute error minimiser score
    the median of the data minimises this.

    Args:
        file_path (str): 

    Returns:
        int: [description]
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()

    positions = np.array([int(i) for i in lines[0].split(",")], dtype=np.int32)

    median = np.median(positions)

    return int(np.linalg.norm(positions - median, ord=1))

def part_two(file_path: str) -> int:
    """
    returns the n(n+1)/2 error minimiser score
    the mean of the data approximately minimises the square

    Args:
        file_path (str): [description]

    Returns:
        int: 
    """

    with open(file_path) as f:
        lines = f.readlines()

    positions = np.array([int(i) for i in lines[0].split(",")])

    mean_floor = np.floor(np.mean(positions))
    mean_ceil = np.ceil(np.mean(positions))

    return min(calculate_tri_error(positions, mean_floor), calculate_tri_error(positions, mean_ceil))

def calculate_tri_error(positions: list, pos: int) -> int:
    """
    use arithmentic sum to calculate cost of alignment

    Args:
        positions (list): list of positions to calculate cost function
        pos (int): integer to calculate cost of aligning to

    Returns:
        int: 
    """
    error = np.abs(positions - pos)

    return int(np.linalg.norm(np.multiply(error, error+1)/2, ord=1))


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_07.txt"))
    print(part_two("aoc/inputs/day_07.txt"))
