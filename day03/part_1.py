import numpy as np

bits = np.array([list(x) for x in open('day03/0.in').read().splitlines()], dtype=int).T

gamma_s = ''.join((str(int(sum(bit) > len(bits[0]) // 2)) for bit in bits))  # More 1s thans 0s
epsilon_s = ''.join('1' if x == '0' else '0' for x in gamma_s)  # Signed ints make inverse not work

print(f'Part 1: {int(gamma_s, base=2) * int(epsilon_s, base=2)}')
