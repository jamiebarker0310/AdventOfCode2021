from aoc.day_13 import part_one, part_two
import pytest


def test_part_one():

    test_file_path = "tests/test_inputs/test_day_13.txt"

    assert part_one(test_file_path) == 17


@pytest.mark.skip(reason="testing graphical output")
def test_part_two():

    test_file_path = "tests/test_inputs/test_day_13.txt"

    assert part_two(test_file_path)
