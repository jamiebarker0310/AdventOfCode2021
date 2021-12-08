from aoc.day_08 import part_one, part_two,get_mapping

def test_part_one():

    test_file_path = "tests/test_inputs/test_day_08.txt"

    assert part_one(test_file_path) == 26

def test_part_two():

    test_file_path = "tests/test_inputs/test_day_08.txt"

    assert part_two(test_file_path) == 61229

def test_get_mapping():

    test_file_path = "tests/test_inputs/test_day_08.txt"

    with open(test_file_path) as f:
        lines = f.readlines()

    expected = {
        "a":"d",
        "b":"e",
        "c":"a",
        "d":"f",
        "e":"g",
        "f":"b",
        "g":"c"
    }

    line = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
    patterns, output = tuple(map(lambda x: x.split(" ") ,line.strip().split(" | ")))

    assert get_mapping(patterns) == expected
