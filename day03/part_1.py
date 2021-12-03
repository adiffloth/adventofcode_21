import numpy as np

bits = np.array([list(x) for x in open('day03/0.in').read().splitlines()], dtype=int).T
num_bits = len(bits[0])

gamma_s = ''.join([str(int(sum(bit) > num_bits // 2)) for bit in bits])
epsilon_s = ''.join('1' if x == '0' else '0' for x in gamma_s)
gamma = int(gamma_s, base=2)
epsilon = int(epsilon_s, base=2)
print(f'Part 1: {gamma * epsilon}')
