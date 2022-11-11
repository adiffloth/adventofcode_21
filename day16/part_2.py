import numpy as np

hex_input = open('day16/1.in').read()
binary = f'{int(hex_input, 16):b}'.rjust(len(hex_input) * 4, '0')

def get_literal_value(idx):
    group_vals = []
    is_last_group = False
    while not is_last_group:
        curr_group = binary[idx:idx + 5]
        idx += 5
        is_last_group = not bool(int(curr_group[0]))
        group_vals.append(curr_group[1:])
    return int(''.join(group_vals), 2), idx


def operate(values, type_id):
    if type_id == 0:
        return sum(values)
    if type_id == 1:
        return np.prod(values)
    if type_id == 2:
        return min(values)
    if type_id == 3:
        return max(values)
    if type_id == 5:
        return int(values[0] > values[1])
    if type_id == 6:
        return int(values[0] < values[1])
    if type_id == 7:
        return int(values[0] == values[1])

def process_packet(idx):
    idx += 3
    packet_type_id = int(binary[idx:idx + 3], 2)
    idx += 3

    if packet_type_id == 4:  # Literal value packet
        val, idx = get_literal_value(idx)
        return val, idx

    else:  # Operator packet
        values = []
        length_type_id = int(binary[idx:idx + 1])
        idx += 1
        if length_type_id == 0:  # Total length in bits is specified
            sub_packet_bits = int(binary[idx:idx + 15], 2)
            idx += 15
            end_idx = idx + sub_packet_bits
            while idx < end_idx:
                val, idx = process_packet(idx)
                values.append(val)
        elif length_type_id == 1:  # Number of sub-packets is specified
            sub_packet_cnt = int(binary[idx:idx + 11], 2)
            idx += 11
            sub_packets_processed = 0
            while sub_packets_processed < sub_packet_cnt:
                val, idx = process_packet(idx)
                values.append(val)
                sub_packets_processed += 1
        else:
            raise ValueError(f'Invalid length_type_id: {length_type_id}')
        return operate(values, packet_type_id), idx


print(process_packet(0)[0])
