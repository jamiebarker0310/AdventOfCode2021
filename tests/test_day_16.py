from aoc.day_16 import (
    part_one,
    part_two,
    parse_packets_1,
    convert_to_binary,
    parse_packets_2,
)


def test_part_one():

    test_file_path = "tests/test_inputs/test_day_16.txt"

    assert part_one(test_file_path) == 82


# def test_part_two():

#     test_hex_str = ["D2FE28"]

#     assert part_two(test_hex_str) == "110100101111111000101000"


def test_convert_to_binary_1():

    test_hex_str = "D2FE28"

    assert convert_to_binary(test_hex_str) == "110100101111111000101000"


def test_convert_to_binary_2():

    test_hex_str = "38006F45291200"

    assert (
        convert_to_binary(test_hex_str)
        == "00111000000000000110111101000101001010010001001000000000"
    )


def test_convert_to_binary_3():

    test_hex_str = "EE00D40C823060"

    assert (
        convert_to_binary(test_hex_str)
        == "11101110000000001101010000001100100000100011000001100000"
    )


def test_parse_packets_1_1():

    test_hex_str = "8A004A801A8002F478"

    test_bin_str = convert_to_binary(test_hex_str)

    assert parse_packets_1(test_bin_str) == 16


def test_parse_packets_1_2():

    test_hex_str = "620080001611562C8802118E34"

    test_bin_str = convert_to_binary(test_hex_str)

    assert parse_packets_1(test_bin_str) == 12


def test_parse_packets_1_3():

    test_hex_str = "C0015000016115A2E0802F182340"

    test_bin_str = convert_to_binary(test_hex_str)

    assert parse_packets_1(test_bin_str) == 23


def test_parse_packets_2_1():

    test_hex_str = "C200B40A82"

    test_bin_str = convert_to_binary(test_hex_str)

    assert parse_packets_2(test_bin_str) == 3


def test_parse_packets_2_2():

    test_hex_str = "04005AC33890"

    test_bin_str = convert_to_binary(test_hex_str)

    assert parse_packets_2(test_bin_str) == 54


def test_parse_packets_2_3():

    test_hex_str = "880086C3E88112"

    test_bin_str = convert_to_binary(test_hex_str)

    assert parse_packets_2(test_bin_str) == 7


def test_parse_packets_2_4():

    test_hex_str = "CE00C43D881120"

    test_bin_str = convert_to_binary(test_hex_str)

    assert parse_packets_2(test_bin_str) == 9


def test_parse_packets_2_5():

    test_hex_str = "D8005AC2A8F0"

    test_bin_str = convert_to_binary(test_hex_str)

    assert parse_packets_2(test_bin_str) == 1


def test_parse_packets_2_6():

    test_hex_str = "F600BC2D8F"

    test_bin_str = convert_to_binary(test_hex_str)

    assert parse_packets_2(test_bin_str) == 0


def test_parse_packets_2_7():

    test_hex_str = "9C005AC2F8F0"

    test_bin_str = convert_to_binary(test_hex_str)

    assert parse_packets_2(test_bin_str) == 0


def test_parse_packets_2_8():

    test_hex_str = "9C0141080250320F1802104A08"

    test_bin_str = convert_to_binary(test_hex_str)

    assert parse_packets_2(test_bin_str) == 1
