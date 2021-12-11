import numpy as np

lines = np.array([list(x) for x in open('day11/0.in').read().splitlines()], dtype=int)

def neighbors_8(y, x):
    deltas = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    neighbs = []
    for d in deltas:
        if 0 <= y + d[0] < lines.shape[0] and 0 <= x + d[1] < lines.shape[1]:
            neighbs.append((y + d[0], x + d[1]))
    return neighbs

def visit_pt(y, x):
    if lines[y][x] <= 9 or (y, x) in flashed:  # I'm not going to flash
        return

    flashed.add((y, x))  # I've flashed, so increment neighbors and cascade
    stack = [(y, x)]
    while stack:
        curr_y, curr_x = stack.pop()
        neighbs = neighbors_8(curr_y, curr_x)
        for neighb_y, neighb_x in neighbs:
            lines[neighb_y][neighb_x] += 1
            if lines[neighb_y][neighb_x] > 9 and (neighb_y, neighb_x) not in flashed:
                flashed.add((neighb_y, neighb_x))
                stack.append((neighb_y, neighb_x))

step = 0
flashed = set()
while len(flashed) < 100:
    step += 1
    flashed = set()
    lines += 1  # All octopus energies increase by 1

    for j in range(lines.shape[0]):
        for i in range(lines.shape[1]):
            visit_pt(j, i)

    lines[lines > 9] = 0

print(f'Part 2: {step}')
