from aoc.day_14 import part_one, part_two


def test_part_one():

    test_file_path = "tests/test_inputs/test_day_14.txt"

    assert part_one(test_file_path) == 1588


def test_part_two():

    test_file_path = "tests/test_inputs/test_day_14.txt"

    assert part_two(test_file_path) == 2188189693529
