lines = [int(x) for x in open('day01/0.in').read().splitlines()]

print(f'Part 1: {sum([1 for x in range(len(lines) - 1) if lines[x + 1] > lines[x]])}')

depths = []
for i in range(len(lines) - 2):
    depths.append(sum(lines[i:i + 3]))

print(f'Part 2: {sum([1 for x in range(len(depths) - 1) if depths[x + 1] > depths[x]])}')
