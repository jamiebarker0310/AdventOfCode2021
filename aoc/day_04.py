from typing import List
import numpy as np


def part_one(file_path: str) -> int:
    """
    returns product of sum of remaining unchecked numbers of first completed
    bingo board and the final number called to complete said board

    Args:
        file_path (str): file path of input file

    Returns:
        int:
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()

    # get called bingo numbers
    called_numbers = [int(x) for x in lines[0].strip().split(",")]

    # get list of bingo boards
    bingo_boards = get_bingo_boards(lines)

    # for each called number
    for number in called_numbers:
        # for each board
        for board in bingo_boards:
            # replace any called number as nan
            board[board == number] = np.nan
            # if any board is complete
            if check_board(board):
                # return product of called number and sum of remaining numbers
                return int(np.nan_to_num(board).sum() * number)


def part_two(file_path: str) -> int:
    """
    returns product of sum of remaining unchecked numbers of last completed
    bingo board and the final number called to complete said board


    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """
    # read file
    with open(file_path) as f:
        lines = f.readlines()

    # get called bingo numbers
    called_numbers = [int(x) for x in lines[0].strip().split(",")]

    # get list of bingo boards
    bingo_boards = get_bingo_boards(lines)

    # for each called number
    for number in called_numbers:
        # for each board
        for board in bingo_boards:
            # replace any called number as nan
            board[board == number] = np.nan
            # if board is complete and is the final board
            if check_board(board) and len(bingo_boards) == 1:
                return int(np.nan_to_num(board).sum() * number)
            # else if board is complete
            elif check_board(board):
                # remove board from list of boards
                bingo_boards = [
                    x
                    for x in bingo_boards
                    if not (np.nan_to_num(x) == np.nan_to_num(board)).all()
                ]


def check_board(board: np.array) -> bool:
    """
    Checks whether a row or column is entirely nan (checked)

    Args:
        board (np.array): bingo board to check

    Returns:
        bool: whether a row or column in entirely nan
    """
    check = np.isnan(board)
    if np.all(check, axis=0).any():
        return True
    elif np.all(check, axis=1).any():
        return True
    else:
        return False


def get_bingo_boards(lines: list) -> List[np.array]:
    """
    Separates list of text into the necessary bingo boards.

    Args:
        lines (list): list of text

    Returns:
        List[np.array]: list of numpy array of bingo boards
    """

    return [
        np.array(
            [line.strip().replace("  ", " ").split(" ") for line in lines[i : i + 5]],
            dtype=np.float32,
        )
        for i in range(2, len(lines), 6)
    ]


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_04.txt"))
    print(part_two("aoc/inputs/day_04.txt"))
