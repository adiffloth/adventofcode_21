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
    values.append(int(''.join(group_vals), 2))
    return idx


def process_packet(idx):
    version = int(binary[idx:idx + 3], 2)
    idx += 3
    versions.append(version)

    packet_type_id = int(binary[idx:idx + 3], 2)
    idx += 3

    if packet_type_id == 4:  # Literal value packet
        idx = get_literal_value(idx)
        return idx

    else:  # Operator packet
        length_type_id = int(binary[idx:idx + 1])
        idx += 1
        if length_type_id == 0:  # Total length in bits is specified
            sub_packet_bits = int(binary[idx:idx + 15], 2)
            idx += 15
            end_idx = idx + sub_packet_bits
            while idx < end_idx:
                idx = process_packet(idx)
            return idx
        elif length_type_id == 1:  # Number of sub-packets is specified
            sub_packet_cnt = int(binary[idx:idx + 11], 2)
            idx += 11
            sub_packets_processed = 0
            while sub_packets_processed < sub_packet_cnt:
                idx = process_packet(idx)
                sub_packets_processed += 1
            return idx
        else:
            raise ValueError(f'Invalid length_type_id: {length_type_id}')


versions = []
values = []
process_packet(0)

print(f'Sum of versions: {sum(versions)}')
