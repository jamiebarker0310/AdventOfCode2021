from aoc.day_04 import part_one, part_two, get_bingo_boards


def test_part_one():

    test_file_path = "tests/test_inputs/test_day_04.txt"

    assert part_one(test_file_path) == 4512


def test_part_two():

    test_file_path = "tests/test_inputs/test_day_04.txt"

    assert part_two(test_file_path)


def test_get_bingo_boards():

    test_file_path = "tests/test_inputs/test_day_04.txt"

    with open(test_file_path) as f:
        lines = f.readlines()

    assert len(get_bingo_boards(lines)) == 3
