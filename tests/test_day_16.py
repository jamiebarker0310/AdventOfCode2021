from aoc.day_16 import hex_to_bin, Packet


def test_hex_to_bin():

    assert hex_to_bin("D2FE28") == "110100101111111000101000"


def test_packet_1():

    bin_str = hex_to_bin("D2FE28")

    packet = Packet(bin_str)

    assert packet.version == 6
    assert packet.type_id == 4
    assert packet.literal
    assert packet.literal_value == 2021


def test_packet_2():

    bin_str = hex_to_bin("38006F45291200")

    packet = Packet(bin_str)

    assert packet.version == 1
    assert packet.type_id == 6
    assert not packet.literal
    assert packet.length_type_id == 0
    assert packet.total_bit_length == 27
    assert len(packet.subpackets) == 2
    assert packet.subpackets[0].literal
    assert packet.subpackets[0].literal_value == 10
    assert packet.subpackets[1].literal
    assert packet.subpackets[1].literal_value == 20


def test_calculate_version_sum():

    bin_str = hex_to_bin("8A004A801A8002F478")
    packet = Packet(bin_str)
    assert packet.calculate_version_sum() == 16

    bin_str = hex_to_bin("620080001611562C8802118E34")
    packet = Packet(bin_str)
    assert packet.calculate_version_sum() == 12

    bin_str = hex_to_bin("C0015000016115A2E0802F182340")
    packet = Packet(bin_str)
    assert packet.calculate_version_sum() == 23

    bin_str = hex_to_bin("A0016C880162017C3686B18A3D4780")
    packet = Packet(bin_str)
    assert packet.calculate_version_sum() == 31


def test_calculate_value():

    bin_str = hex_to_bin("C200B40A82")
    packet = Packet(bin_str)
    assert packet.calculate_value() == 3

    bin_str = hex_to_bin("04005AC33890")
    packet = Packet(bin_str)
    assert packet.calculate_value() == 54

    bin_str = hex_to_bin("880086C3E88112")
    packet = Packet(bin_str)
    assert packet.calculate_value() == 7

    bin_str = hex_to_bin("CE00C43D881120")
    packet = Packet(bin_str)
    assert packet.calculate_value() == 9

    bin_str = hex_to_bin("D8005AC2A8F0")
    packet = Packet(bin_str)
    assert packet.calculate_value() == 1

    bin_str = hex_to_bin("F600BC2D8F")
    packet = Packet(bin_str)
    assert packet.calculate_value() == 0

    bin_str = hex_to_bin("9C005AC2F8F0")
    packet = Packet(bin_str)
    assert packet.calculate_value() == 0

    bin_str = hex_to_bin("9C0141080250320F1802104A08")
    packet = Packet(bin_str)
    assert packet.calculate_value() == 1
