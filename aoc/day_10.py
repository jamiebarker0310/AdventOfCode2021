import numpy as np


def part_one(file_path: str) -> int:
    """
    calculates the sum of the scores of the corrupted lines

    Args:
        file_path (str):

    Returns:
        int:
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()

    # return sum of all lines
    return sum([corrupted(line.strip()) for line in lines])


def part_two(file_path: str) -> int:
    """
    removes all corrupted lines
    then calculates the cost of completing the incompleted lines

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    with open(file_path) as f:
        lines = f.readlines()

    # initialise scores
    scores = []
    # for each line
    for line in lines:
        # if it's not corrupted
        if not corrupted(line.strip()):
            # add score to list
            scores.append(incomplete(line.strip()))

    # return median score
    return int(np.median(scores))


def corrupted(line: str) -> int:
    """
    calculates if line is corrupted using a stack technique

    Args:
        line (str):

    Returns:
        int: score of corrupt character
    """

    stack = []
    pair_dict = {"(": ")", "{": "}", "[": "]", "<": ">"}
    score_dict = {")": 3, "]": 57, "}": 1197, ">": 25137}
    for character in line:
        if character in ("(", "{", "[", "<"):
            stack.append(character)
        else:
            if pair_dict[stack.pop()] != character:
                return score_dict[character]
    return 0


def incomplete(line: str) -> int:
    """
    looks at remaining stack to calculate score

    Args:
        line (str): [description]

    Returns:
        int:  score of incomplete line
    """

    score_dict = {"(": 1, "[": 2, "{": 3, "<": 4}
    # initialise stack
    stack = []
    # for each character
    for character in line:
        # add to stack
        if character in ("(", "{", "[", "<"):
            stack.append(character)
        # remove from stack
        else:
            stack.pop()
    # calculate score
    total = 0
    # score reverse stack
    for s in stack[::-1]:
        # multiply score by 5
        total *= 5
        # add correspondind score
        total += score_dict[s]
    return total


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_10.txt"))
    print(part_two("aoc/inputs/day_10.txt"))
