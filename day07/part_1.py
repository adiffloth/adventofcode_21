import numpy as np

crabs = [int(x) for x in open('day07/0.in').readline().split(',')]

target = int(np.median(crabs))
print(f'Part 1: {sum([abs(target - crab) for crab in crabs])}')

t = int(np.mean(crabs))  # int() vs round()
print(f'Part 2: {sum([abs(t - c) * (abs(t - c) + 1) // 2 for c in crabs])}')  # Gauss
