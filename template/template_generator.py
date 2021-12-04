import sys


def generate_template():

    day = sys.argv[1].zfill(2)

    # create input file
    open(f"aoc/inputs/day_{day}.txt", "w").close()

    # create test input file
    open(f"tests/test_inputs/test_day_{day}.txt", "w").close()

    # create python file
    with open("template/files/template_day.py") as f:
        text = f.read()

    text = text.replace("{day_n}", day)

    with open(f"aoc/day_{day}.py", "w") as f:
        f.write(text)

    # create python test file
    with open("template/files/template_test.py") as f:
        text = f.read()

    text = text.replace("{day_n}", day)

    with open(f"tests/test_day_{day}.py", "w") as f:
        f.write(text)


if __name__ == "__main__":
    generate_template()
