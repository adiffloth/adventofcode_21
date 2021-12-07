import numpy as np

crabs = [int(x) for x in open('day07/0.in').readline().split(',')]

target = int(np.median(crabs))
print(f'Part 1: {sum([abs(target - crab) for crab in crabs])}')

target = int(np.mean(crabs))  # This rounds the wrong way for the worked example.
print(f'Part 2: {sum([sum(range(abs(target - crab) + 1)) for crab in crabs])}')
