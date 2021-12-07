import numpy as np

def part_one(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()

    positions = [int(i) for i in lines[0].split(",")]

    proposed_positions = np.array([[i for _ in range(len(positions))] for i in range(min(positions), max(positions))])

    positions_array = np.array([positions for _ in range(proposed_positions.shape[0])])

    return int(np.linalg.norm(proposed_positions - positions_array, ord=1, axis=1).min())

def part_two(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    with open(file_path) as f:
        lines = f.readlines()

    positions = [int(i) for i in lines[0].split(",")]

    proposed_positions = np.array([[i for _ in range(len(positions))] for i in range(min(positions), max(positions))])

    positions_array = np.array([positions for _ in range(proposed_positions.shape[0])])

    difference_array = np.abs(proposed_positions - positions_array)

    cost = np.multiply(difference_array, (difference_array + 1))/2

    return int(cost.sum(axis=1).min())

if __name__ == "__main__":
    print(part_one("aoc/inputs/day_07.txt"))
    print(part_two("aoc/inputs/day_07.txt"))
