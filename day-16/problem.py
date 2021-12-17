try:
    from math import prod
except ImportError as e:
    from functools import reduce
    prod = lambda values: reduce(lambda a, b: a * b, values, 1)


with open('input') as f:
    hex_value = f.read().strip()
    bin_value = (bin(int(hex_value, 16))[2:]).zfill(len(hex_value) * 4)


def parse_packet(bin_input):
    packet_version, packet_type, content = int(bin_input[:3], 2), bin_input[3:6], bin_input[6:]
    if packet_type == '100':
        bits, idx, terminal = '', 0, False
        while not terminal:
            terminal = content[idx] == '0'
            bits += content[idx + 1:idx + 5]
            idx += 5
        literal = int(bits, 2)
        return (packet_version, packet_type, literal), content[idx:]
    else:
        packets = []
        if content[0] == '0':
            total_bits = int(content[1:16], 2)
            r, remainder = content[16:16 + total_bits], content[16 + total_bits:]
            while r:
                packet, r = parse_packet(r)
                packets.append(packet)
        else:
            total_subpackets = int(content[1:12], 2)
            remainder = content[12:]
            for _ in range(total_subpackets):
                packet, remainder = parse_packet(remainder)
                packets.append(packet)
        return (packet_version, packet_type, tuple(packets)), remainder


# Part 1
def versions(packet):
    packet_version, _, value = packet
    yield packet_version
    if isinstance(value, (tuple, list)):
        for p in value:
            for v in versions(p):
                yield v


packet, _ = parse_packet(bin_value)
print(sum(versions(packet)))
# 871


# Part 2
def operate(packet):
    _, packet_type, value = packet
    if packet_type == '100':
        return value
    else:
        subpackets = [operate(p) for p in value]
        if packet_type == '000':
            return sum(subpackets)
        if packet_type == '001':
            return prod(subpackets)
        if packet_type == '010':
            return min(subpackets)
        if packet_type == '011':
            return max(subpackets)
        if packet_type == '101':
            return 1 if subpackets[0] > subpackets[1] else 0
        if packet_type == '110':
            return 1 if subpackets[0] < subpackets[1] else 0
        if packet_type == '111':
            return 1 if subpackets[0] == subpackets[1] else 0


print(operate(packet))
# 68703010504
