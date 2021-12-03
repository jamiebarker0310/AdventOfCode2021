def part_one(file_path):

    with open(file_path) as f:
        lines = f.readlines()

    pos = 0
    for row in lines:
        direction, distance = row.strip().split(" ")
        distance = int(distance)

        if direction == "forward":
            pos += distance
        elif direction == "down":
            pos += distance * 1j
        elif direction == "up":
            pos -= distance * 1j

    return int(pos.real * pos.imag)


def part_two(file_path):

    aim = 0
    pos = 0
    with open(file_path) as f:
        lines = f.readlines()

    for row in lines:
        direction, distance = row.strip().split(" ")
        distance = int(distance)

        if direction == "forward":
            pos += distance + (aim * distance) * 1j
        elif direction == "down":
            aim += distance
        elif direction == "up":
            aim -= distance

    return int(pos.real * pos.imag)


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_02.txt"))
    print(part_two("aoc/inputs/day_02.txt"))
