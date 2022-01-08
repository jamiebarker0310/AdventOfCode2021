from aoc.day_17 import part_one, part_two, get_x_position, get_y_position, get_pairs
import unittest


def test_part_one():

    test_file_path = "tests/test_inputs/test_day_17.txt"

    assert part_one(test_file_path) == 45


def test_part_two():

    test_file_path = "tests/test_inputs/test_day_17.txt"

    assert part_two(test_file_path) == 112


def test_get_x_position():

    assert get_x_position(3, 1) == 3

    assert get_x_position(5, 2) == 9

    assert get_x_position(6, 10) == 21


def test_get_y_position():

    assert get_y_position(3, 1) == 3

    assert get_y_position(5, 2) == 9

    assert get_y_position(3, 9) == -9


def test_get_pairs():

    test_file_path_pairs = "tests/test_inputs/test_day_17_pairs.txt"

    test_file_path = "tests/test_inputs/test_day_17.txt"

    with open(test_file_path_pairs) as f:
        lines = f.readlines()

    expected_pairs = []
    for line in lines:

        for pair in line.strip().split():
            expected_pairs.append(tuple([int(x.strip()) for x in pair.split(",")]))

    pairs = get_pairs(test_file_path)

    case = unittest.TestCase()

    case.maxDiff = None

    case.assertCountEqual(pairs, expected_pairs)
