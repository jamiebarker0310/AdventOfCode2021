from typing import Tuple
import numpy as np
import matplotlib.pyplot as plt


def part_one(file_path: str) -> int:
    """
    returns the number of visible dots after 1 fold

    Args:
        file_path (str):

    Returns:
        [type]:
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()

    # get instructions
    instructions = lines[lines.index("\n") + 1 :]

    # initialise dots
    X = initialise_dots(lines)

    # perform single instruction
    X = perform_instructions(X, [instructions[0]])

    return (X > 0).sum()


def part_two(file_path: str):
    """
    Performs all instructions for dots and outputs
    final graph as an image.

    Args:
        file_path (str):

    Returns:
        None
    """
    # read file
    with open(file_path) as f:
        lines = f.readlines()

    # get instructions
    instructions = lines[lines.index("\n") + 1 :]

    # initialise dots
    X = initialise_dots(lines)

    # perform instructions
    X = perform_instructions(X, instructions) > 0

    # flip iamge
    X = np.flipud(X)

    # plot image
    plt.imshow(X)

    # save image
    plt.savefig("aoc/day_13.png")

    # clear image
    plt.clf()


def initialise_dots(lines: list) -> np.array:
    """
    parse input to form a binary np array

    Args:
        lines (list): input text

    Returns:
        np.array: binary np array
    """
    # get relevant lines
    data = lines[: lines.index("\n")]

    # Get co-ordinate pairs of each dot
    X_pair = np.array([[int(x) for x in line.strip().split(",")] for line in data])

    # Create a zero array to fill in
    X = np.zeros(tuple(X_pair.max(axis=0) + 1)[::-1])

    # for each co-ordinate pair
    for pair in X_pair:
        j, i = tuple(pair)
        # set coordinate to 0
        X[i, j] = 1

    # return array
    return X


def perform_instructions(X: np.array, instructions: list) -> np.array:
    """
    perform instruction that involves folding array along a specified
    axis

    Args:
        X (np.array): input array
        instructions (list): list of arrays

    Returns:
        np.array: folded array
    """
    # for each instruction
    for instruction in instructions:

        # parse instructions
        axis, value = parse_instructions(instruction)

        # if folding along x
        if axis == 1:
            # split array
            X1 = X[:, :value]
            X2 = X[:, value + 1 :]
            # flip 2nd array
            X2 = np.fliplr(X2)

        elif axis == 0:
            # split array
            X1 = X[:value, :]
            X2 = X[value + 1 :, :]
            # flip 2nd array
            X1 = np.flipud(X1)
        # add arrays
        X = X1 + X2
    # return array
    return X


def parse_instructions(instruction: str) -> Tuple[int, int]:
    """
    parse instruction to give axis to fold on and position to split on

    Args:
        instruction (str): input instruction

    Raises:
        ValueError: if axis is not x or y

    Returns:
        Tuple[int, int]: axis and line to fold on
    """

    axis, value = instruction.split("=")
    axis = axis[-1]
    value = int(value)

    if axis == "y":
        return 0, value
    elif axis == "x":
        return 1, value
    else:
        raise ValueError


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_13.txt"))
    print(part_two("aoc/inputs/day_13.txt"))
