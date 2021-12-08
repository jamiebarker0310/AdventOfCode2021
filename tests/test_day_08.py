from aoc.day_08 import part_one, part_two, get_mapping


def test_part_one():

    test_file_path = "tests/test_inputs/test_day_08.txt"

    assert part_one(test_file_path) == 26


def test_part_two():

    test_file_path = "tests/test_inputs/test_day_08.txt"

    assert part_two(test_file_path) == 61229


def test_get_mapping():

    expected = {"a": "c", "b": "f", "c": "g", "d": "a", "e": "b", "f": "d", "g": "e"}

    line = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab \
    | cdfeb fcadb cdfeb cdbaf"
    patterns, output = tuple(map(lambda x: x.split(" "), line.strip().split(" | ")))

    # assert get_mapping(patterns) == expected

    assert expected == get_mapping(patterns)
