import numpy as np

def get_most_common(a):  # Banker's rounding
    return 1 if (sum(a) / len(a) == 0.5) else int(sum(a) > len(a) / 2)

def bits_to_int(b):  # Fiddly bits
    return int(''.join([str(bit) for bit in b.T]).replace(' ', '')[1:-1], base=2)

o2_bits = co2_bits = np.array([list(x) for x in open('day03/0.in').read().splitlines()], dtype=int).T

i = 0
while len(o2_bits[0]) > 1:
    mask = o2_bits[i] != get_most_common(o2_bits[i])  # O2 generator
    o2_bits = np.delete(o2_bits, mask, 1)
    i += 1

i = 0
while len(co2_bits[0]) > 1:
    mask = co2_bits[i] == get_most_common(co2_bits[i])  # CO2 scrubber
    co2_bits = np.delete(co2_bits, mask, 1)
    i += 1

print(f'Part 2: {bits_to_int(o2_bits) * bits_to_int(co2_bits)}')
