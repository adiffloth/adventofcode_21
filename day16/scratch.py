# import numpy as np
# binary = '01010'  # 10
# binary = '1000100100'  # 20
binary = '101111111000101000'  # 2021

def get_literal_value(start_idx):
    idx = start_idx
    out = []
    is_not_last_group = True
    while is_not_last_group:
        curr_group = binary[idx:idx + 5]
        print(f'{curr_group=}')
        is_not_last_group = int(curr_group[0])
        out.append(curr_group[1:])
        idx += 5
    print(f'{out=}')
    return int(''.join(out), 2), idx

print(get_literal_value(0))

print(bool(0))
vals = [1, 2]
print(min(vals))
