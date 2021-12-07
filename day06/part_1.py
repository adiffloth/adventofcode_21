from collections import defaultdict

line = open('day06/0.in').readline()
counts = {x: line.count(str(x)) for x in range(9)}

for i in range(256):
    next_gen = defaultdict(int)
    next_gen[6] = next_gen[8] = counts[0]
    for j in range(8):
        next_gen[j] += counts[j + 1]
    counts = next_gen
    if i == 79:
        print(f'Part 1: {sum(counts.values())}')

print(f'Part 2: {sum(counts.values())}')
