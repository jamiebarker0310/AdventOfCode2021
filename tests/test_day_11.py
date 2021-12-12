import numpy as np
from aoc.day_11 import part_one, part_two, run_simulation


def test_part_one():

    test_file_path = "tests/test_inputs/test_day_11.txt"

    assert part_one(test_file_path) == 1656


def test_part_two():

    test_file_path = "tests/test_inputs/test_day_11.txt"

    assert part_two(test_file_path) == 195


def test_steps():

    test_file_path = "tests/test_inputs/test_day_11.txt"

    with open(test_file_path) as f:
        lines = f.readlines()

    X = np.array([[int(number) for number in line.strip()] for line in lines])

    for i in range(1, 11):
        print(i)

        test_file_path = f"tests/test_inputs/day_11/step_{str(i).zfill(2)}.txt"
        with open(test_file_path) as f:
            lines = f.readlines()

        X_expected = np.array(
            [[int(number) for number in line.strip()] for line in lines]
        )
        X = run_simulation(X)
        print(X)

        np.testing.assert_array_equal(X, X_expected)
