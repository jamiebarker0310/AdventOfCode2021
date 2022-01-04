from aoc.day_15 import part_one, part_two, get_big_map

import numpy as np


def test_part_one():

    test_file_path = "tests/test_inputs/test_day_15.txt"

    assert part_one(test_file_path) == 40


def test_part_two():

    test_file_path = "tests/test_inputs/test_day_15.txt"

    assert part_two(test_file_path) == 315


def test_get_big_map():

    excected_test_file_path = "tests/test_inputs/test_day_15_big_map.txt"

    with open(excected_test_file_path) as f:
        lines = f.readlines()

    X_expected = np.array([[int(x) for x in list(row.strip())] for row in lines])

    test_file_path = "tests/test_inputs/test_day_15.txt"

    with open(test_file_path) as f:
        lines = f.readlines()

    X = np.array([[int(x) for x in list(row.strip())] for row in lines])

    np.testing.assert_array_equal(get_big_map(X), X_expected)
