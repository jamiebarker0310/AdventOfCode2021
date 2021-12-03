from aoc.day_{day_n} import part_one, part_two

def test_part_one():

    test_file_path = "tests/test_inputs/test_day_{day_n}.txt"

    assert part_one(test_file_path)

def test_part_two():

    test_file_path = "tests/test_inputs/test_day_{day_n}.txt"

    assert part_two(test_file_path)